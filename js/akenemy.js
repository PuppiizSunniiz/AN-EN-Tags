    $.holdReady(true);

    //console.log = function () { }

    var db = {}
    var tlracedict={};
    var enemyforfilter=[]
    const allimmunity=["stunImmune","silenceImmune","sleepImmune","frozenImmune","levitateImmune","disarmedCombatImmune","fearedImmune"]

    var d0 = $.getJSON("json/gamedata/zh_CN/gamedata/excel/gamedata_const.json",function(data){
        db["dataconst"] = data;
    });
    var d1 = $.getJSON("json/gamedata/zh_CN/gamedata/excel/enemy_handbook_table.json",function(data){
        db["enemy"] = data;
    });
    var d2 = $.getJSON("json/gamedata/zh_CN/gamedata/levels/enemydata/enemy_database.json",function(data){
        let enemydic = {}
        data.enemies.forEach(enemy =>{
            enemydic[enemy.Key]=enemy.Value
        })
        db["enemyDetail"] = enemydic;
    });
    var d3 = $.getJSON("json/gamedata/en_US/gamedata/excel/enemy_handbook_table.json",function(data){
        db["enemyEN"] = data;
    });
    var d4 = $.getJSON("json/named_effects.json",function(data){
        db["named_effects"] = data;
    });
    var d5 = $.getJSON("json/akenemy.json",function(data){
        db["akenemy"] = data;
    });
    $.when(d0,d1,d2,d3,d4,d5).then(function(){
        Object.keys(db.enemy.raceData).forEach(race => {
            tlracedict[race]=db.enemyEN.raceData[race]?db.enemyEN.raceData[race].raceName:db.enemyEN.raceData[race].raceName
        })
        Object.values(db.enemy.enemyData).forEach(enemy => {
            if(!enemy.hideInHandbook){
                var immunitylist = []
                var enemydatadetail=db.enemyDetail[enemy.enemyId][0].enemyData
                var silenceable=false
                
                allimmunity.forEach(immunity => {if (enemydatadetail.attributes[immunity].m_value) immunitylist.push(immunity)})
                if (enemy.abilityList){
                    enemy.abilityList.forEach(ability => {
                        if(ability.textFormat=="SILENCE") {
                            silenceable=true
                            return
                    }})
                }

                var linkEnemies = []
                if (enemy.linkEnemies.length){
                    enemy.linkEnemies.forEach(linkenemy=>{
                        if (db.enemy.enemyData[linkenemy]){
                            var linkdata=db.enemy.enemyData[linkenemy]
                            if (!linkdata.hideInHandbook) 
                                linkEnemies.push({
                                                    "enemyId"           :linkdata.enemyId,
                                                    "name"              :linkdata.name,
                                                    "nameEN"            :db.enemyEN.enemyData[linkdata.enemyId]?db.enemyEN.enemyData[linkdata.enemyId].name:"",
                                                    "enemyIndex"        :linkdata.enemyIndex,})
                        }
                    })
                }

                enemyforfilter.push({
                                        "enemyId"           :enemy.enemyId,
                                        "name"              :enemy.name,
                                        "nameEN"            :db.enemyEN.enemyData[enemy.enemyId]?db.enemyEN.enemyData[enemy.enemyId].name:"",
                                        "sortId"            :enemy.sortId,
                                        "enemyIndex"        :enemy.enemyIndex,
                                        "enemyLevel"        :enemy.enemyLevel,
                                        "enemyTags"         :enemydatadetail.enemyTags.m_value,
                                        "applyWay"          :enemydatadetail.applyWay.m_value,
                                        "motion"            :enemydatadetail.motion.m_value,
                                        "damageType"        :enemy.damageType,
                                        "immunity"          :immunitylist,
                                        "silenceable"       :silenceable,
                                        "linkEnemies"       :linkEnemies,
                                        "filterappearance"  :db.akenemy.enemies[enemy.enemyId]
                                    })
            }
        })
        console.log(enemyforfilter)
        $.holdReady(false);
    });
    
    var lang;
    var reg;
    var selectedEnemy;
    var selectedLevel=0;
    
    var skeletonType = "skel"
    var chibitype = 'enemy'
    var charName = 'enemy_1510_frstar2';
    var chibipers = 'front'
    var chibiName = 'enemy_1510_frstar2'
    var folder = `https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/spineassets/${chibitype}/`
    var spinewidget 
    var loadchibi = true;
    var defaultAnimationName = "Default";
    var animationqueue
    var chibiscaleweb = 0
    var chibiscaleweblist = [[0.5,-775],[0.6,-800],[0.7,-825],[0.8,-850],[0.9,-875],[1,-900]]
    var savenum = 0

    $(document).ready(function(){
        FilterType("BOSS")
        $('#to-tag').click(function() {      // When arrow is clicked
            $('body,html').animate({
                scrollTop : 0                       // Scroll to top of body
            }, 500);
        });

        $('.dropdown-trigger').dropdown();
        $('[data-toggle="tooltip"]').tooltip();


        if(!localStorage.getItem('gameRegion') || !localStorage.getItem('webLang')){
            console.log("game region undefined");
            localStorage.setItem("gameRegion", 'cn');
            localStorage.setItem("webLang", 'en');
            reg = "cn";
            lang = "en";
        } else {
            console.log(localStorage.getItem('webLang'));
            reg = localStorage.getItem('gameRegion');
            lang = localStorage.getItem('webLang');
        }
        if(!localStorage.getItem('selectedEnemy')){
            localStorage.removeItem("selectedEnemy");
        } else {
            selectedEnemy = localStorage.getItem('selectedEnemy');
        }
        $('.reg[value='+reg+']').addClass('selected');
        $('.lang[value='+lang+']').addClass('selected');
        changeUILanguage();
        populateEnemy(true)
    });

    $.getScript("js/arrive.min.js", function(){
        $(document).arrive("#regionDropdown", function(){
            $("#navitemRegion").addClass('ak-disable2');
            $("#navitemLanguage").addClass('ak-disable2');
        });
    });
    $('#Chibi-download').click(function(event){
        // var canvas = spinewidget.canvas
        
        var checkdiv = $("#spine-widget").children()[0]
        console.log(checkdiv)
        var img = checkdiv.toDataURL("image/png");
        var link = document.createElement("a");
        link.download = `${chibiName}-${savenum}.png`;
        savenum++
        link.href = img;
        link.click();
    });
    function regDropdown(el){
        localStorage.setItem('gameRegion', el.attr("value"));
        $(".dropdown-item.reg").removeClass("selected");
        el.addClass("selected");   
        changeUILanguage();
    }
    
    function langDropdown(el){
        localStorage.setItem('webLang', el.attr("value"));
        console.log(localStorage.getItem('webLang'))
        $(".dropdown-item.lang").removeClass("selected");
        el.addClass("selected");
        changeUILanguage();
    }
    

    function FilterType(type){
        charaFilter=[]
        let currHtml = []
        $("#tbody-list").empty()
        
        // currHtml.push(`</div></div> `)
        // console.log(currHtml)
        $("#tbody-list").html(currHtml.join(""))
    }
    function clickBtnTag(el){
        let section = $(el).attr("section");

        if ((section!="immunity" && section!="other") && $(el).hasClass("btn-secondary")) $(`.enemy-${section}`).removeClass("btn-primary").addClass("btn-secondary");
        $(el).toggleClass("btn-secondary btn-primary");

        populateEnemy();
    }
    function clickImmunity(el){
        $(`.enemy-immunity`).removeClass("btn-primary").addClass("btn-secondary");
        $(el).toggleClass("filter-tag-red filter-tag-blue");
        if ($(el).hasClass("filter-tag-red")) $(el).html("Immunity")
        else $(el).html("Appliable")

        populateEnemy();
    }
    function clickBtnClear(){
        $(".button-tag").removeClass("btn-primary").addClass("btn-secondary");
        $("#GamemodeDropdown").removeClass("btn-primary").addClass("btn-secondary");
        $("#GamemodeDropdown").html("Select Gamemode")
        $("#GamemodeDropdown").attr("data-id","")

        $("#GameeventDropdown").removeClass("btn-primary").addClass("btn-secondary ak-disable");
        $("#GameeventDropdown").html("&lt;&lt;&lt; Select Gamemode first")
        $("#GameeventDropdown").attr("data-id","")

        $("#GameeventList").empty()

        $("#opname").val("")
        populateEnemy(true);
    }

    function selectGamemode(el){
        var gameeventtext
        $("#GamemodeDropdown").html(el.html())
        $("#GamemodeDropdown").attr("data-id",el.attr("data-id"))
        $("#GamemodeDropdown").removeClass("btn-secondary").addClass("btn-primary");

        function gameeventtext(gamemode){
        switch (gamemode){
            case "main":
                return "Episode"
            case "sidestory" :
                return "Side Story"
            case "supply":
                return "Operation"
            case "campaign":
                return "Mission"
            case "coop":
                return "Event"
            case "cc":
            case "is":
            case "tn":
            case "ra":
                return "Season"
            case "sss":
                return "Tower"
            }
        }

        $("#GameeventDropdown").removeClass("btn-primary ak-disable").addClass("btn-secondary");
        $("#GameeventDropdown").html(`Select ${gameeventtext(el.attr("data-id"))}`)

        $("#GamemodeList .dropdown-item").removeClass("selected")
        el.addClass("selected")

        $("#GameeventList").empty()
        eventlisting(el.attr("data-id"))
        populateEnemy()
    }

    function eventlisting(gamemode){    // old
        gameeventhtml=""
        db.akenemy.gamemode[gamemode].forEach(event =>{
            gameeventhtml+=`<a class="dropdown-item unselectable" onclick="selectGameevent($(this))" data-id="${event}">${db.akenemy.events[event]}</a>`
        })

        $("#GameeventList").append(gameeventhtml)
    }

    /*
    function event_listing(gamemode){    // new
        gameeventhtml = ""
        activity_dict = db.akenemy.gamemode[gamemode]["activity"]
        Object.keys(activity_dict).forEach(event =>{
            gameeventhtml += `<a class="dropdown-item unselectable" onclick="selectGameevent($(this))" data-id="${event}">${activity_dict[event].name}</a>`
        })

        $("#GameeventList").append(gameeventhtml)
    }*/

    function selectGameevent(el){
        $("#GameeventDropdown").html(el.html())
        $("#GameeventDropdown").attr("data-id",el.attr("data-id"))
        $("#GameeventDropdown").removeClass("btn-secondary").addClass("btn-primary");

        $("#GameeventList .dropdown-item").removeClass("selected")
        el.addClass("selected")

        populateEnemy()
    }

    function populateEnemy(allenemies=false){
        let enemy_class = $(".enemy-class.btn-primary").map((_, btn) => $(btn).attr("data-id")).get();
        let enemy_race = $(".enemy-race.btn-primary").map((_, btn) => $(btn).attr("data-id")).get();
        let enemy_attack = $(".enemy-attack.btn-primary").map((_, btn) => $(btn).attr("data-id")).get();
        let enemy_movement = $(".enemy-movement.btn-primary").map((_, btn) => $(btn).attr("data-id")).get();
        let enemy_damage = $(".enemy-damage.btn-primary").map((_, btn) => $(btn).attr("data-id")).get();
        let enemy_immunity = $(".enemy-immunity.btn-primary").map((_, btn) => $(btn).attr("data-id")).get();
        let enemy_silenceable = $("#silenceable").hasClass("btn-primary")
        let enemy_name = $("#opname").val().search("头像_敌人_")!=-1?$("#opname").val().split("头像_敌人_")[1]:$("#opname").val()
        let Notappliable=$(`#filter-enemy-immunity`).html()=="Immunity"

        let enemy_gamemode = $("#GamemodeDropdown.btn-primary").attr("data-id")
        let enemy_gameevent = $("#GameeventDropdown.btn-primary").attr("data-id")

        var enemiesfiltered = enemyforfilter

        if(enemy_class.length == 0 &&
            enemy_race.length == 0 &&
            enemy_attack.length == 0 &&
            enemy_movement.length == 0 &&
            enemy_damage.length == 0 &&
            enemy_immunity.length == 0 &&
            !enemy_silenceable &&
            !enemy_name &&
            !enemy_gamemode &&
            !enemy_gameevent) allenemies=true
        
        console.log(enemy_class.length,enemy_race.length,enemy_attack.length,enemy_movement.length,enemy_damage.length,enemy_immunity.length,!enemy_silenceable,!enemy_name,!enemy_gamemode,!enemy_gameevent,"allenemies =",allenemies)
        if(!allenemies){
            if (enemy_class.length) enemiesfiltered=enemiesfiltered.filter(enemy => enemy_class[0]==enemy.enemyLevel)
            if (enemy_race.length) enemiesfiltered=enemiesfiltered.filter(enemy => enemy.enemyTags?enemy.enemyTags.includes(enemy_race[0]):false)
            if (enemy_attack.length) enemiesfiltered=enemiesfiltered.filter(enemy => enemy_attack[0]==enemy.applyWay)
            if (enemy_movement.length) enemiesfiltered=enemiesfiltered.filter(enemy => enemy_movement[0]==enemy.motion)
            if (enemy_damage.length) enemiesfiltered=enemiesfiltered.filter(enemy => enemy.damageType.includes(enemy_damage[0]))
            if (enemy_immunity.length) enemiesfiltered=enemiesfiltered.filter(enemy => enemy_immunity.every(immunity => enemy.immunity.length?enemy.immunity.includes(immunity)+Notappliable-1:!Notappliable))
            if (enemy_silenceable) enemiesfiltered=enemiesfiltered.filter(enemy => enemy.silenceable==true)
            if (enemy_name.length) enemiesfiltered=enemiesfiltered.filter(enemy => (enemy.name.toUpperCase().search(enemy_name.toUpperCase())!=-1) || (enemy.nameEN.length?enemy.nameEN.toUpperCase().search(enemy_name.toUpperCase())!=-1:false) || (enemy.enemyId.toUpperCase().search(enemy_name.toUpperCase())!=-1) || (enemy.enemyIndex.toUpperCase().search(enemy_name.toUpperCase())!=-1))
            if (enemy_gamemode) {
                console.log(enemy_gamemode,enemy_gameevent)
                if(enemy_gameevent) enemiesfiltered=enemiesfiltered.filter(enemy => enemy.filterappearance.includes(enemy_gameevent))
                else enemiesfiltered=enemiesfiltered.filter(enemy => {
                    return enemy.filterappearance.some(item => {
                        return db.akenemy.gamemode[enemy_gamemode].includes(item)
                    })
                })
            }
        }
        console.log(enemiesfiltered)
        let currHtml = []
        enemiesfiltered.sort((a,b)=> a.sortId-b.sortId)
        if(enemiesfiltered.length > 0){
            $('#enemyResult').empty();
            $('#enemyResult').show();
            for (var i = 0; i < enemiesfiltered.length; i++) {
                let image = `<img style="height:80px;padding:1px" src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/enemy/${enemiesfiltered[i].enemyId}.png" title="${enemiesfiltered[i].nameEN?enemiesfiltered[i].nameEN:""} [${enemiesfiltered[i].name}]">  `

                currHtml.push(`
                                <li class="ak-btn ak-enemy" style="display:inline-block;cursor: pointer;width:90px;margin:2px;margin-bottom:2px;padding:1px;border-radius:2px" data-toggle="modal" data-target="#enemysd" onclick="selectEnemy('${enemiesfiltered[i].enemyId}')"> 
                                    <div class="col-12"style="white-space: nowrap;padding:0px;text-align:center;margin:0px ">
                                        <div style="position:absolute;top:-2px;left:2px;white-space: nowrap;padding:3px;padding-top:1px;padding-bottom:0px;margin:0px;background:#222">${enemiesfiltered[i].enemyIndex}</div>
                                        ${image}
                                    </div>
                                </li>`)
            }
        } else {
            $('#enemyResult').empty();
            $('#enemyResult').hide();
        }
        $("#enemyResult").append(currHtml.join(""));

    }

    function selectEnemy(el){
        let currEnemy = query(db.enemy.enemyData,"enemyId",el)
        let currFromfilter = query(enemyforfilter,"enemyId",el)
        let currEnemyEN = db.enemyEN.enemyData[el]
        let currEnemyDetail = db.enemyDetail[el]
        let currHtml = []    
        let tlname = query(db.enemytl,"name_cn",currEnemy.name).name_en 
        let tldesc = currEnemy.description
        let tlrace = []
        let tlability
        if (currEnemyEN) {
            tlname = currEnemyEN.name
            tldesc = currEnemyEN.description
            tlability = currEnemyEN.abilityList
        }else{
            tlability = currEnemy.abilityList
        }
        let firstEnemyData = currEnemyDetail[0].enemyData
        console.log(currEnemy)

        let atktype =[]
        let atkrange = ""
        let enemiesabilities=[]
        let linkEnemieslist=[]

        //Enemies Attack Type
        if(firstEnemyData){
            switch(firstEnemyData.applyWay.m_value){
                case "MELEE"    : atkrange = `<span style="color:red">Melee</span>` ;break;
                case "RANGED"   : atkrange = `<span style="color:dodgerblue">Ranged</span>` ;break;
                case "ALL"      : atkrange = `<span style="color:red">Melee</span> & <span style="color:dodgerblue">Ranged</span>` ;break;
                default         : atkrange = `<span style="color:grey">Does Not Attack</span>` ;break;
            }
        }
        //Enemies Race
        if(firstEnemyData.enemyTags.m_value){
            firstEnemyData.enemyTags.m_value.forEach(element => {
                tlrace.push(tlracedict[element])
            })
        }
        //Enemies Damage Type
        currEnemy.damageType.forEach(element => {
            switch (element) {
                case "PHYSIC"       : atktype.push(`<span style="color:orange">Physical</span>`) ;break;
                case "MAGIC"        : atktype.push(`<span style="color:cyan">Arts</span>`) ;break;
                case "NO_DAMAGE"    : atktype.push(`<span style="color:grey">Does Not Attack</span>`) ;break;
                case "HEAL"         : atktype.push(`<span style="color:lightgreen">Heal</span>`) ;break;
                default: atktype.push(element) ;break;
            }
        });
        //Abilities
        if(tlability.length >0){
            tlability.forEach(ability => {
                if      (ability.textFormat == "TITLE")     enemiesabilities.push(`<span style="font-size:larger;color: mediumspringgreen;">${ChangeDescriptionColor(ability.text)}</span>`)
                else if (ability.textFormat == "NORMAL")    enemiesabilities.push("&mdash; "+ChangeDescriptionColor(ability.text))
                else if (ability.textFormat == "SILENCE")   enemiesabilities.push(`<img style="width:16px" src="extra/40px-Silence_effect.webp" title="Silenceable"> `+ChangeDescriptionColor(ability.text))
            })
        }
        
        //Related Enemis
        if (currFromfilter.linkEnemies.length){
            linkEnemieslist.push(`  
                                        <div style="display:inline-block;vertical-align:top">   
                                            <u>Related Enemies</u>
                                        </div>
                                        <div style="/*! display:inline-block */height: 10px;"></div>`)

            currFromfilter.linkEnemies.forEach(linkenemy => {
                linkEnemieslist.push(   `<li class="ak-btn ak-enemy" style="display:inline-block;cursor: pointer;width:90px;margin:2px;margin-bottom:2px;padding:1px;border-radius:2px" /*data-toggle="modal"*/ data-target="#enemysd" onclick="selectEnemy('${linkenemy.enemyId}')"> 
                                            <div class="col-12"style="white-space: nowrap;padding:0px;text-align:center;margin:0px ">
                                                <div style="position:absolute;top:-2px;left:2px;white-space: nowrap;padding:3px;padding-top:1px;padding-bottom:0px;margin:0px;background:#222">${linkenemy.enemyIndex}</div>
                                                <img style="height:80px;padding:1px" src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/enemy/${linkenemy.enemyId}.png" title="${linkenemy.nameEN?linkenemy.nameEN:""} [${linkenemy.name}]">
                                            </div>
                                        </li>`
                )
            })
        }

        currHtml.push(`
        <div class="ak-c-black col">
            <div style="text-align:right;color:#999">${el}</div>
            <div style="display:inline-flex;flex-direction: row;min-width: 100%;">
                <div style="margin-bottom:8px;padding:5px;padding-top:10px;background:#444;margin-top:2px;display:inline-block;padding-left:10px;padding-right:30px">
                    <div style="display:inline-flex">
                        <img style="height:80px;padding:1px" src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/enemy/${currEnemy.enemyId}.png" title="${tlname?tlname:""} [${currEnemy.name}]">
                        <div style="border:3px solid #FFF;text-align:center;margin:5px;padding:0px;height:50px;width:50px;display:inline-block;${currEnemy.enemyIndex.length==2?"font-size:30px":"font-size:15px;padding-top:10px"}">${currEnemy.enemyIndex}</div>
                        <div style="display:inline-block;vertical-align:top">   
                            <div style="width: max-content;">${tlname?tlname:""} [${currEnemy.name}] </div>
                            <div>${tlrace.length?tlrace.join(", "):"-"}</div>
                            <div>${firstEnemyData.motion.m_value=="FLY"?"Flying Path":"Ground Path"}</div>
                        </div>
                    </div>

                    <div>Enemy Type : ${currEnemy.enemyLevel.charAt(0) + currEnemy.enemyLevel.slice(1).toLowerCase()}</div>
                    <div>Attack type : ${atkrange?atkrange:""}</div>
                    <div>Damage type : ${atktype.join(" & ")}</div>
                </div>
                <div style="margin-bottom:8px;background:#444;margin-top:2px;flex-grow:1"></div>
                <div style="margin-bottom:8px;padding:5px;padding-top:10px;background:#444;margin-top:2px;/*! display:inline-block; */padding-left:10px;padding-right:30px;/*! align-content: flex-end; *//*! height: 100%; *//*! flex-shrink: inherit; *//*! flex-wrap: nowrap; */">
                ${linkEnemieslist.join("")}
                </div>
            </div>

            <div class="ak-shadow" style="margin-bottom:8px;padding-top:10px;padding:5px;background:#444">
                <div style="color:#BBB;font-size:17px;background:#222;padding:5px;border-radius:2px">Description</div>
                <div style="padding:6px"> ${tldesc}</div>
            </div>

            ${tlability.length >0 ?
            `<div class="ak-shadow" style="margin-bottom:8px;padding-top:10px;padding:5px;background:#444">
                <div style="color:#BBB;font-size:17px;background:#222;padding:5px;border-radius:2px">Traits</div>
                <div style="padding:6px"> ${enemiesabilities.join("</br>")}</div>
            </div>`:""}

        </div>`)
        //<div>
            //<button type="button" class="btn ak-button  browse-btn" style="width:90px" data-toggle="modal" data-target="#enemysd"">
            //    Check SD
            //</button>
        //</div>

        //<div  class="ak-shadow" style="margin-bottom:8px;padding:5px;padding-top:10px;background:#444;margin-top:2px;display:inline-block;padding-left:10px;padding-right:30px;display:none">
        //            <div class="modal-body" style="display: inline-flex;padding:0px;margin:0px;max-height: 183px;justify-content: center;align-items:flex-end;">
        //                <div id="spine-frame" style="width: 150px; height: 150px;transform: scale(0.75);z-index:2;pointer-events: none;">
        //                    <div id="spine-frameheader" class='btn btn-sm ak-sm-btn' style="display:inline-block;cursor: move;pointer-events:all;transform: scale(2);margin:0px;position: absolute;left:140px;top:90px;opacity: 0;"><i class="fas fa-arrows-alt"></i></div>
        //                    <button class='btn btn-sm ak-sm-btn ak-disable' style='display:none;position:absolute;top:75px;left:75px;font-size:30px'  type='button' id='loading-spine'>Loading ...</button>
        //                    <div id="spine-widget" class="top-layer" style="position:absolute;width: 4000px; height: 4000px;top:-2200px;left:-1850px;pointer-events: none;z-index: 20;transform: scale(0.5);"></div> <!-- scaling 0.5 for "supersampling" chibi -->   
        //                </div>
        //            </div>
        //
        //           <div style="display:inline-flex;width:100%;bottom:0px;background: #444;padding:10px;border-radius: 2px;justify-content: center;">
        //                <div id="spine-toolbar" style="width: 400px; height: 50px;z-index:1;">
        //                    <button class="btn btn-sm ak-chibi-btn" id="Chibi-download" title='Experimental Saving'><i class="far fa-save"></i></button>
        //                    <button class='btn btn-sm ak-chibi-btn ak-disable' style='min-width:30px;height:30px'  type='button' >C</button>
        //                    <button class='btn btn-sm ak-chibi-btn' style='min-width:31px;height:30px' onclick='PlayPause("widget")' type='button' id='Chibi-Play'><b>l l </b></button>
        //                    <button class='btn btn-sm ak-chibi-btn' style='min-width:30px;height:30px' onclick='ChangeAnimation("widget","#spine-text",-1)' type='button' id='Chibi-Prev'><i class="fas fa-step-backward"></i></button>
        //                    <button id="spine-text" class="btn ak-chibi-btn" style="width:140px;height:30px; "onclick='ChangeAnimation("widget","#spine-text",0)'></button>
        //                    <button class='btn btn-sm ak-chibi-btn' style='min-width:30px;height:30px' onclick='ChangeAnimation("widget","#spine-text",1)' type='button' id='Chibi-Next'><i class="fas fa-step-forward"></i></button>
        //                    <button type="button" class="btn btn-danger spine-danger" data-dismiss="modal">Close</button>
        //                </div>
        //            </div>
        //        </div>


        
        // <div style="max-width:100%;margin-bottom:15px;margin-top:15px" >
        //         <div class="col" style="border:3px solid #FFF;text-align:center;margin:5px;padding:0px;height:80px;width:100px;display:inline-block">
        //         <div style="padding:0px;font-size:12px">
        //             <img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/enemy/hp.png" style="margin-top:-5px;position:absolute;top:5px;left:0px">
        //             Health</div><div style="font-size:40px;margin-top:-5px">${currEnemy.endure}</div>
        //         </div>
        //         <div class="col" style="border:3px solid #FFF;text-align:center;margin:5px;padding:0px;height:80px;width:100px;display:inline-block">
                
        //         <div style="padding:0px;font-size:12px">
        //             <img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/enemy/atk.png" style="margin-top:-5px;position:absolute;top:5px;left:0px">
        //             Attack</div><div style="font-size:40px;margin-top:-5px">${currEnemy.attack}</div>
        //         </div>
        //         <div class="col" style="border:3px solid #FFF;text-align:center;margin:5px;padding:0px;height:80px;width:100px;display:inline-block">
        //         <div style="padding:0px;font-size:12px">
        //             <img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/enemy/defense.png" style="margin-top:-5px;position:absolute;top:5px;left:0px">
        //             Defense</div><div style="font-size:40px;margin-top:-5px">${currEnemy.defence}</div>
        //         </div>
        //         <div class="col" style="border:3px solid #FFF;text-align:center;margin:5px;padding:0px;height:80px;width:100px;display:inline-block">
        //         <div style="padding:0px;font-size:12px;text-align:right;margin-right:5px">
        //             <img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/enemy/resistance.png" style="margin-top:-5px;position:absolute;top:5px;left:0px">
        //             Spell Resist</div><div style="font-size:40px;margin-top:-5px">${currEnemy.resistance}</div>
        //         </div>
        //     </div>
        if(currEnemyDetail){
            currHtml.push(`<div class="ak-c-black" style="text-align:center;margin-top:5px;background:#222"> Stat & Immunity Detail </div> <div class="ak-c-black" style="background:#2f2f2f;padding-left:15px">`)
            currEnemyDetail.forEach(element => {
                currHtml.push(`<div id="Level${element.level}" class="btn btn-sm ak-btn ak-mid"style="display:inline;border: 1px #222;background:#111;color:white" onclick='enemyDetail(\"${el}\",${element.level})'> Level ${element.level}</div>`)
            });
            enemyDetail(el,0)
        }else{
            $('#enemyDetail2').hide();
        }
        currHtml.push(`</div>`)
        
        $('#enemyDetail').html(currHtml.join(""))
        $("#Level0").css("background", "#09d")
        $('[data-toggle="tooltip"]').tooltip()
    }

    function enemyDetail(el,level){
        $('#enemyDetail2').empty();
        $('#enemyDetail2').hide();
        let currEnemyDetail = db.enemyDetail[el]
        let firstEnemyData = currEnemyDetail[0].enemyData
        let currEnemyData = currEnemyDetail[level].enemyData
        let currHtml = []
        console.log(currEnemyDetail)
        
        var currattr = currEnemyData.attributes
        var firstattr = firstEnemyData.attributes

        var EnemyImmune=[]
        $(["stun","silence","sleep","frozen","levitate","disarmedCombat","feared"].forEach(immune =>{
            if (currattr[immune+"Immune"].m_value!=0?currattr[immune+"Immune"].m_value:firstattr[immune+"Immune"].m_value)
                EnemyImmune.push(`<td><span style="color:crimson;font-weight: bold;">Immune</span></td>`)
            else
                EnemyImmune.push(`<td><span style="color:Lime;font-weight: bold;">Appliable</span></td>`)
        }))

        currHtml.push(`
        <div class="ak-c-black col">    
            <table class="table table-sm table-bordered" style="text-align: center; table-layout: fixed;">
                <thead class="thead-light">
                    <tr style="background-color: #dbdbdb;">
                        <th scope="col" style="text-overflow: ellipsis; overflow: hidden;">HP</th>
                        <th scope="col" style="text-overflow: ellipsis; overflow: hidden;">Attack</th>
                        <th scope="col" style="text-overflow: ellipsis; overflow: hidden;">Defense</th>
                        <th scope="col" style="text-overflow: ellipsis; overflow: hidden;">Resistance</th>
                        <th scope="col" style="text-overflow: ellipsis; overflow: hidden;">Element Resistance</th>
                        <th scope="col" style="text-overflow: ellipsis; overflow: hidden;">Elemental Resistance</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>${currattr.maxHp.m_value!=0?currattr.maxHp.m_value:firstattr.maxHp.m_value}</td>
                        <td>${currattr.atk.m_value!=0?currattr.atk.m_value:firstattr.atk.m_value}</td>
                        <td>${currattr.def.m_value!=0?currattr.def.m_value:firstattr.def.m_value}</td>
                        <td>${currattr.magicResistance.m_value!=0?currattr.magicResistance.m_value:firstattr.magicResistance.m_value}</td>
                        <td>${currattr.epDamageResistance.m_value!=0?currattr.epDamageResistance.m_value:firstattr.epDamageResistance.m_value}</td>
                        <td>${currattr.epResistance.m_value!=0?currattr.epResistance.m_value:firstattr.epResistance.m_value}</td>
                    </tr>
                </tbody>
                <thead class="thead-light">
                    <tr style="background-color: #dbdbdb;">
                        <th scope="col" style="text-overflow: ellipsis; overflow: hidden;">ATK Interval</th>
                        <th scope="col" style="text-overflow: ellipsis; overflow: hidden;">ATK Radius</th>
                        <th scope="col" style="text-overflow: ellipsis; overflow: hidden;">Speed</th>
                        <th scope="col" style="text-overflow: ellipsis; overflow: hidden;">Weight</th>
                        <th scope="col" style="text-overflow: ellipsis; overflow: hidden;">HP Seals</th>
                        <th scope="col" style="text-overflow: ellipsis; overflow: hidden;">HP Regen</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>${currattr.baseAttackTime.m_value!=0?currattr.baseAttackTime.m_value:firstattr.baseAttackTime.m_value}</td>
                        <td>${currEnemyData.rangeRadius.m_value>0?currEnemyData.rangeRadius.m_value:firstEnemyData.rangeRadius.m_value==-1?"-":firstEnemyData.rangeRadius.m_value}</td>
                        <td>${currattr.moveSpeed.m_value!=0?currattr.moveSpeed.m_value:firstattr.moveSpeed.m_value}</td>
                        <td>${currattr.massLevel.m_value!=0?currattr.massLevel.m_value:firstattr.massLevel.m_value}</td>
                        <td>${currEnemyData.lifePointReduce.m_value!=0?currEnemyData.lifePointReduce.m_value:firstEnemyData.lifePointReduce.m_value}</td>
                        <td>${currattr.hpRecoveryPerSec.m_value!=0?currattr.hpRecoveryPerSec.m_value:firstattr.hpRecoveryPerSec.m_value}</td>
                    </tr>
                </tbody>
            </table>
            <table class="table table-sm table-bordered" style="text-align: center; vertical-align: middle; table-layout: fixed;margin-bottom: 0;">
                <thead class="thead-light">
                    <tr style="background-color: #dbdbdb; text-decoration: underline;">
                        <th scope="col" class="hovertooltip" data-tooltip="Unable to move, block, attack, or use skills.">Stun</th>
                        <th scope="col" class="hovertooltip" data-tooltip="Disables the target's special ability.">Silence</th>
                        <th scope="col" class="hovertooltip" data-tooltip="Invulnerable and unable to take any actions.">Sleep</th>
                        <th scope="col" class="hovertooltip" data-tooltip="Unable to move, attack, or use skills, RES -15.">Freeze</th>
                        <th scope="col" class="hovertooltip" data-tooltip="Target becomes aerial and cannot move, attack, or use skills. Duration halved if Weight is greater than 3.">Levitate</th>
                        <th scope="col" class="hovertooltip" data-tooltip="Cannot perform normal attacks when blocked.">Frighten</th>
                        <th scope="col" class="hovertooltip" data-tooltip="Cannot be blocked, run away in panic.">Fear</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        ${EnemyImmune.join("")}
                    </tr>
                </tbody>
            </table>
        
            `) // 
        currHtml.push(`</div>`)
        if(firstEnemyData.talentBlackboard){
            enemytalentBlackboard = currEnemyData.talentBlackboard?currEnemyData.talentBlackboard:firstEnemyData.talentBlackboard
            currHtml.push(`<div class="ak-c-black" style="text-align:center;background:#222">Trait Details<div class="ak-c-black" style="text-align:left;padding-left: 15px;">`)
            firstEnemyData.talentBlackboard.forEach(element=>{
                if (enemytalentBlackboard!=firstEnemyData.talentBlackboard){
                    enemytalentBlackboard.forEach(currelement=>{
                        if (element.key==currelement.key) element=currelement
                    })
                }
                currHtml.push(`<div>${element.key} : ${element.valueStr?element.valueStr:element.value}</div>`)
            })
            currHtml.push(`</div></div> `)
        }
        
        $('#enemyDetail2').html(currHtml.join(""))
        $("[id^='Level']").css("background", "#111")
        $("#Level"+level.toString()).css("background", "#09d")
        $('#enemyDetail2').show();
    }    

    function ChangeDescriptionColor(desc){
        if(!desc) return desc

        desc = desc.replace(/\<([A-z\"\'].+?)\>/g,`<span style="color:deeppink">$1</span>`) // Summon/Related enemy
        desc = desc.replace(/([\[【].+?[\]】])/g,`<span style="color:yellow">$1</span>`)  // Ability name
        desc = ChangeDesc1(desc)
        desc = ChangeDesc2(desc)

        return desc
    }

    function ChangeDesc1(desc,addbackgroundcolor = false){
        desc = desc.replace(/<[@](.+?)>(.+?)<\/>/g, function(m, rtf, text) {
            let rich = db.dataconst.richTextStyles[rtf];
            let rich2 = db.named_effects.termDescriptionDict[rtf];
            if (!rich2){
                rich2 = db.dataconst.termDescriptionDict[rtf]
            }
            if (rich) {
                let colorRTF = /<color=(#[0-9A-F]+)>\{0\}<\/color>/;
                if (colorRTF.test(rich)) {
                    let color = colorRTF.exec(rich)[1]
                    return `<span class="${addbackgroundcolor?`stat-important2`:""}" style="color:${color}">${text}</span>`
                } else {
                    return rich.replace('{0}', text)
                }
            } else if (rich2) {
                return `<span class="stathover" data-toggle="tooltip" data-html="true" data-delay='{ "show": 0, "hide": 500 }' data-placement="bottom"
                title='
                <span class="tooltiptext" style="display:inline-block">
                    <div class="tooltipHeader">${rich2.termName.replace(/\'/g,"&apos;")}</div>
                    <div class="tooltipcontent">${CreateTooltip(rich2.description.replace(/\'/g,"&apos;"))}</div>
                </span>'
                style="color:#0098DC">${text}</span>`
            }else{
                return text
            }
        })
        return desc
    }

    function ChangeDesc2(desc){
        desc = desc.replace(/<[$](.+?)>(.+?)<\/>/g, function(m, rtf, text) {
            let rich2 = db.named_effects.termDescriptionDict[rtf];
            if (!rich2){
                rich2 = db.dataconst.termDescriptionDict[rtf]
            }
            if (rich2) {
                return `<span class="stathover" data-toggle="tooltip" data-html="true" data-delay='{ "show": 0, "hide": 500 }' data-placement="bottom"
                title='
                <span class="tooltiptext" style="display:inline-block">
                    <div class="tooltipHeader">${rich2.termName.replace(/\'/g,"&apos;")}</div>
                    <div class="tooltipcontent">${CreateTooltip(rich2.description.replace(/\'/g,"&apos;"))}</div>
                </span>'
                style="color:#0098DC">${text}</span>`
            }
        })
        return desc
    }

    function CreateTooltip(desc,addbackgroundcolor = false){
        desc = desc.replace(/<[$](.+?)>(.+?)<\/>/g, function(m, rtf, text) {
            let rich2 = db.named_effects.termDescriptionDict[rtf];
            console.log(m)
            if (!rich2){
                rich2 = db.dataconst.termDescriptionDict[rtf]
            }
            if (rich2) {
                return `<span class="stat-important tooltip3" style="color:#0098DC">${text}<span class="tooltiptext2" style="display:inline-block"><div class="tooltipHeader">${rich2.termName}</div>${CreateTooltip2(rich2.description.replace(/\'/g,"&apos;"))}</span></span>`
            }
        })
        return desc
    }

    function CreateTooltip2(desc,addbackgroundcolor = false){
        desc = desc.replace(/<[$](.+?)>(.+?)<\/>/g, function(m, rtf, text) {
            let rich2 = db.named_effects.termDescriptionDict[rtf];
            console.log(m)
            if (!rich2){
                rich2 = db.dataconst.termDescriptionDict[rtf]
            }
            if (rich2) {
                return `<span class="stat-important" style="color:#0098DC">${text}</span>`
            }
        })
        return desc
    }

    function query(db,key,val,single=true,returnKey=false){
        if(single){
            var result = {};
        } else {
            var result = [];
        }
        var found = false;
        $.each(db,function(key2,v){
            if(v[key].toLowerCase() == val.toLowerCase()){
                found = true;
                if(single){
                    if(returnKey){
                        result[key2] = v;
                    } else {
                        result = v;
                    }
                    return false;
                } else {
                    if(returnKey){
                        var obj = {};
                        obj[key2] = v; 
                        result.push(obj);
                    } else {
                        result.push(v);
                    }
                }
            }
        });
        if(found){
            return result;
        } else {
            return false;
        }
    }

    function changeUILanguage(){
        reg = localStorage.getItem('gameRegion');
        lang = localStorage.getItem('webLang');

        $('#display-reg').text(reg.toUpperCase())
        
        switch (lang) {
            case "en":$('#display-lang').text("English");break;
            case "cn":$('#display-lang').text("Chinese");break;
            case "jp":$('#display-lang').text("Japanese");break;
        }
        
        localStorage.setItem("gameRegion", reg);
        localStorage.setItem("webLang", lang);
        getJSONdata("ui",function(data){
            if(data.length != 0){
                $.each(data, function(i,text){
                    $("[translate-id="+text.id).html(text['ui_'+lang]);
                });
            }
        });
    }

    function getJSONdata(type, callback){
        var x = 0;
        var req = $.getJSON("json/tl-"+type+".json");
        req.done(function(response){
            callback(response);
        });
        req.fail(function(response){
            console.log("type: "+type+" fail: ");
            console.log(response);
        });
    }

    function ChangeSkillAnim(skillnum,skillmax,token){
        // console.log(skillnum)
        // console.log(token)
        // console.log(skillmax)
        console.log(token)
        tokenname = token
        if(spinewidgettoken&&token&&spinewidgettoken.loaded){
            
            LoadAnimationToken(token)
        }else if(spinewidget&&spinewidget.loaded){
            var animlist = Object.keys(spinewidget.customanimation).filter(search=>search.includes("Skill"))

            animlist=animlist.sort((a,b)=>{
                if(a<b)return 1
                if(a>b)return -1
                return 0
            })
            
            if(animlist&&animlist.length>0){
                // console.log(animlist)
                // console.log(skillmax-skillnum-1)
                
                if(animlist[skillmax-skillnum-1]){
                    $("#spine-text").text(`Skill ${skillnum+1}`)
                    // console.log()
                    CreateAnimation(spinewidget,spinewidget.customanimation[animlist[skillmax-skillnum-1]],true)
                }
            }
            // console.log(currselectedanim)
            // CreateAnimation(spinewidget)
            
        }
    }

    function ConvertAtlas(atlas){
        var combined = []
        var eachpart = atlas.split(/\n\n/g)
        // console.log(eachpart)
        eachpart.forEach(part => {
            combined.push(ParseAtlas(part))
        });
        return combined
    }
    function ParseAtlas(texts){
        var json = {parts:[]}
        var eachlines = texts.split(/\n/g)
        var isheaderfinished=false
        var isheader = false
        var currheader
        var num = -1
        eachlines.forEach(line => {
            // console.log(line)
            if(line=="\r"){
                
            }
            else if(line!=""){
                if(!isheaderfinished){
                    if(!json.image){
                            json.image=line;
                        }else{
                            var currvalue = GetAtlasValue(line)
                            json[currvalue.key] = currvalue.value
                            if(currvalue.key=="repeat"){
                                isheaderfinished=true
                            }
                    }
                }else{
                    if((/(  )/g).test(line)&&currheader){
                        isheader = false
                        var currvalue = GetAtlasValue(line.replace("  ",""))
                        json.parts[currheader][currvalue.key] = currvalue.value
                    }else{
                        isheader = true
                        num =+1
                        currheader = line
                        json.parts[line]={}
                    }
                }
            }
        });
        return json
    }
    function GetAtlasValue(value){
        var content = value.split(":")
        var splitvalue = [content[1]]
        if(content[1]&&content[1].includes(",")){
          splitvalue = content[1].split(",")
        }
        return {key:content[0],value:splitvalue}
      }
    
    function LoadAnimation(chibiname = chibiName){
        // console.log(spinewidget)
        $("#loading-spine").text("Loading...")
        if(spinewidget){
            // spinewidget.loadWidgets()
            // spinewidget.loadTexture()
            spinewidget.pause()
            spinewidget = undefined
            $("#spine-widget").remove()
            currscale = chibiscaleweblist[chibiscaleweb]
            $("#spine-frame").append(`<div id="spine-widget" class="top-layer" style="position:absolute;width: 4000px; height: 4000px;top:-2200px;left:-1850px;pointer-events: none;z-index: 20;transform: scale(0.5);"></div>`)
            // console.log(loadchibi)
            // if(loadchibi)$("#spine-frame").fadeIn(100);
        }else{
            if(loadchibi)$("#spine-frame").fadeIn(100);
        }
        if (chibiname != null && defaultAnimationName != null) {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', folder + chibiname + "." +skeletonType, true);
            xhr.responseType = 'arraybuffer';
            var array;
            $("#spine-widget").hide()
            var defaultskin ='default'
            
            $("#loading-spine").fadeIn(200)
            console.log(chibiname)
            chibiName = chibiname
            
            xhr.onloadend = function (e) {
                if (xhr.status != 404) {
                    buffer = xhr.response;
                    array = new Uint8Array(buffer);
                    // console.log(array);
                    skelBin = new SkeletonBinary();
                    var jsonskel
                    if(array.length==0){
                        $("#loading-spine").text("Load Failed")
                    }
                    if (skeletonType== "skel"){
                        skelBin.data = array
                        skelBin.initJson()
                        jsonskel = JSON.stringify(skelBin.json)
                        var parsedskeljson = JSON.parse(jsonskel)
                        console.log(JSON.parse(jsonskel))
                        if(!Object.keys(parsedskeljson.animations).find(search=>search==defaultAnimationName)){
                            defaultAnimationName = Object.keys(parsedskeljson.animations)[0]
                        }
                        if(!Object.keys(parsedskeljson.skins).find(search=>search==defaultskin)){
                            defaultskin = Object.keys(parsedskeljson.skins)[0]
                        }
                    }else if (skeletonType== "json"){
                        jsonskel = JSON.parse(new TextDecoder("utf-8").decode(array))
                        var parsedskeljson = jsonskel
                        console.log(JSON.parse(jsonskel))
                        if(!Object.keys(parsedskeljson.animations).find(search=>search==defaultAnimationName)){
                            defaultAnimationName = Object.keys(parsedskeljson.animations)[0]
                        }
                        if(!Object.keys(parsedskeljson.skins).find(search=>search==defaultskin)){
                            defaultskin = Object.keys(parsedskeljson.skins)[0]
                        }
                    }
                    
                    
                    
                    // var test = new TextDecoder("utf-8").decode(array);
                    // console.log(JSON.parse(test))
                    // console.log(JSON.stringify(skelBin.json, null, "\t"));
                    var spineX = parseFloat(4000)/2
                    var spineY = parseFloat(4000)/2 -900
                    var xhratlas = new XMLHttpRequest();
                    xhratlas.open('GET', folder + chibiname + ".atlas", true);
                    xhratlas.onloadend = function (e) {
                        if (xhratlas.status != 404) {
                            var loadedatlas = xhratlas.response;
                            var imagename = ConvertAtlas(loadedatlas)
                            var atlaslist = []
                            imagename.forEach(image => {
                                atlaslist.push(image.image)
                            });
                            console.log(atlaslist)
                            new spine.SpineWidget("spine-widget", {
                                jsonContent: jsonskel,
                                atlas: folder + chibiname + ".atlas",
                                atlasPages: atlaslist,
                                animation: defaultAnimationName,
                                backgroundColor: "#00000000",
                                skin : defaultskin,
                                // debug: true,
                                // imagesPath: chibiName + ".png", 
                                premultipliedAlpha: true,
                                fitToCanvas : false,
                                loop:true,
                                x:spineX,
                                y:spineY,
                                //0.5 for normal i guess
                                scale:1,
                                success: function (widget) {
                                    
                                    animIndex=0
                                    spinewidget = widget
                                    $("#spine-text").text(widget.skeleton.data.animations[0].name)
                                    $("#loading-spine").fadeOut(200)
                                    animations = widget.skeleton.data.animations;
                                    // console.log(animations)
                                    // console.log(widget)
                                    $("#spine-widget").show()
                                    if(animations.find(search=>search.name=="Start")){
                                        CreateAnimation(spinewidget,["Start","Idle"])
                                        $("#spine-text").text("Idle")
                                    }else if(animations.find(search=>search.name=="Relax")){
                                        CreateAnimation(spinewidget,"Relax")
                                        $("#spine-text").text("Relax")
                                    }

                                    // CreateAnimation(["Skill_Begin",["Skill_Loop",5],"Skill_End","Idle"],true)
                                    // CreateAnimation(["Skill_2_Begin",["Skill_2_Loop",5],"Skill_2_Loop_End","Idle"],true)

                                    widget.customanimation = CheckAnimationSet(animations)
                                    // console.log(widget)


                                    //ange skill 2
                                    // CreateAnimation(["Skill1_Begin",["Skill1_Loop",15],"Skill1_End",["Idle_Charge",2]],true)

                                    //ange skill 3 (is weird)
                                    // CreateAnimation(["Skill2_Begin",["Skill2_Loop",15],"Skill2_End",["Idle_Charge",2]],true)

                                    // Normal skill loop with begin and idle i guess (nian skill 2)
                                    // CreateAnimation(["Skill_2_Begin",["Skill_2_Loop",5],"Skill_2_Idle"],true,true)


                                    // console.log(widget.state)
                                    // console.log(widget.state.trackEntry)
                                    $("#spine-toolbar-next").onclick = function () {
                                        widget.state.clearTracks()
                                        if(animationqueue!=undefined)clearInterval(animationqueue)
                                        animIndex++;
                                        // console.log(animations)
                                        if (animIndex >= animations.length) animIndex = 0;
                                        widget.setAnimation(animations[animIndex].name)
                                        $("#spine-text").text(animations[animIndex].name)
                                    }
                                }
                            })
                        }
                        
                    }
                    xhratlas.send()
                }else{
                    $("#loading-spine").text("Load Failed")
                    // $("#spine-frame").fadeOut()
                }
            };
            xhr.send()
        }
    }


    function LoadAnimationToken(tokenkey=opdataFull.tokenKey){
        // console.log(spinewidgettoken)
        // console.log(opdataFull)
        // var tokenName =
        var tokenname = tokenkey
        var tokenfolder = `https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/spineassets/token/${opdataFull.id}/${tokenkey}`
        console.log(tokenfolder)
        // $("#loading-spine").text("Loading...")
        if(spinewidgettoken){
            // spinewidget.loadWidgets()
            // spinewidget.loadTexture()
            spinewidgettoken.pause()
            spinewidgettoken = undefined
            $("#spine-widget-token").remove()
            currscale = chibiscaleweblist[chibiscaleweb]
            $("#spine-frame-token").append(`<div id="spine-widget-token" class="top-layer" style="position:absolute;width: 1800px; height: 1800px;top:${currscale[1]}px;left:-750px;pointer-events: none;z-index: 20;transform: scale(${currscale[0]});"></div>`)
            // console.log(loadchibi)
            // if(loadchibi)$("#spine-frame").fadeIn(100);
        }else{
            if(loadchibi)$("#spine-frame-token").fadeIn(100);
        }
        if (chibiName != null && defaultAnimationName != null) {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', tokenfolder +"."+skeletonType, true);
            xhr.responseType = 'arraybuffer';
            var array;
            $("#spine-widget-token").hide()

            
            // $("#loading-spine").fadeIn(200)
            // console.log(chibiName)
            xhr.onloadend = function (e) {
                if (xhr.status != 404) {
                    buffer = xhr.response;
                    array = new Uint8Array(buffer);
                    // console.log(array);
                    skelBin = new SkeletonBinary();
                    var jsonskel
                    if(array.length==0){
                        // $("#loading-spine").text("Load Failed")
                    }
                    if (skeletonType== "skel"){
                        skelBin.data = array
                        skelBin.initJson()
                        jsonskel = JSON.stringify(skelBin.json)
                    }else if (skeletonType== "json"){
                        jsonskel = JSON.parse(new TextDecoder("utf-8").decode(array))

                    }
                    
                    
                    
                    // var test = new TextDecoder("utf-8").decode(array);
                    // console.log(JSON.parse(test))
                    // console.log(JSON.stringify(skelBin.json, null, "\t"));
                    new spine.SpineWidget("spine-widget-token", {
                        jsonContent: jsonskel,
                        atlas: tokenfolder + ".atlas",
                        animation: defaultAnimationName,
                        backgroundColor: "#00000000",
                        // debug: true,
                        // imagesPath: chibiName + ".png", 
                        premultipliedAlpha: true,
                        fitToCanvas : false,
                        loop:true,
                        x:900,
                        y:650,
                        //0.5 for normal i guess
                        scale:1,
                        success: function (widget) {
                            
                            // animIndex=0
                            spinewidgettoken = widget
                            // $("#spine-text").text(widget.skeleton.data.animations[0].name)
                            // $("#loading-spine").fadeOut(200)
                            tokenanimations = widget.skeleton.data.animations;
                            // console.log(animations)
                            // console.log(widget)
                            $("#spine-widget-token").show()
                            if(tokenanimations.find(search=>search.name=="Start")){
                                CreateAnimation(spinewidgettoken,["Start","Idle"])
                                // $("#spine-text").text("Idle")
                            }else if(tokenanimations.find(search=>search.name=="Relax")){
                                CreateAnimation(spinewidgettoken,"Relax")
                                // $("#spine-text").text("Relax")
                            }else if(tokenanimations.find(search=>search.name=="Idle")){
                                CreateAnimation(spinewidgettoken,"Idle")
                                // $("#spine-text").text("Relax")
                            }

                            widget.customanimation = CheckAnimationSet(tokenanimations)
                            console.log(widget)
                        }
                    })
                }else{
                }
            };
            xhr.send()
        }
    }
    function ChangeAnimation2(widget,widgettext,num){
        if(widget=="token") widget=spinewidgettoken
        else widget=spinewidget

        var curranimation = Object.keys(widget.customanimation)
        widget.state.clearTracks()
        if(animationqueue!=undefined)clearInterval(animationqueue)
        animIndex += num;
        // console.log(animIndex)
        // console.log(curranimation)
        
        if (animIndex >= curranimation.length) animIndex = 0;
        else if (animIndex < 0) animIndex = curranimation.length-1;
        // spinewidget.state.setDefaultMix(0.1);
        // spinewidget.config.scale = 2
        // console.log(widget)
        // console.log(animIndex)
        // widget.setAnimation(curranimation[animIndex].name)
        // console.log(widget.customanimation[Object.keys(widget.customanimation)[animIndex]])

        CreateAnimation(widget,widget.customanimation[Object.keys(widget.customanimation)[animIndex]],true)
        // console.log(widgettext)
        $(widgettext).text(Object.keys(widget.customanimation)[animIndex])
    }

    function ChangeAnimation(widget,widgettext,num){
        if(widget=="token") widget=spinewidgettoken
        else widget=spinewidget

        var curranimation = widget.skeleton.data.animations
        widget.state.clearTracks()
        if(animationqueue!=undefined)clearInterval(animationqueue)
        animIndex += num;
        // console.log(animIndex)
        // console.log(curranimation)
        
        if (animIndex >= curranimation.length) animIndex = 0;
        else if (animIndex < 0) animIndex = curranimation.length-1;
        // spinewidget.state.setDefaultMix(0.1);
        // spinewidget.config.scale = 2
        // console.log(widget)
        // console.log(animIndex)
        // widget.setAnimation(curranimation[animIndex].name)
        // console.log(widget.customanimation[Object.keys(widget.customanimation)[animIndex]])
        // console.log(curranimation[index])
        CreateAnimation(widget,curranimation[animIndex].name)
        // widget.setAnimation(curranimation[animIndex].name)
        // console.log(widgettext)
        $(widgettext).text(curranimation[animIndex].name)
    }

    function ChangeSkin(name="",pers=""){
        currskin = name
        var skinname = currskin.split(opdataFull.id)[1]?name.split(opdataFull.id)[1]:""
        console.log(opdataFull.id)
        console.log(skinname)
        if(spinewidgettoken){
            console.log("      waaa "+tokenname)
            LoadAnimationToken(tokenname+skinname)
        }
        if(name!="")chibiName=name
        if(pers!="")chibipers=pers
        if(chibipers=='build') {chibiName.includes("build")?chibiName=chibiName:chibiName= "build_"+chibiName}
        else chibiName.includes("build")?chibiName=chibiName.split("_").slice(1).join("_"):chibiName=chibiName
        folder = `https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/spineassets/${chibitype}/${charName}/${chibipers}/`
        if(spinewidget)LoadAnimation()

        
    }


    function PlayPause(widget){
        if(widget=="token") widget=spinewidgettoken
        else widget=spinewidget
        if(widget.isPlaying()){
            console.log("Playing")
            widget.pause()
        }else{
            console.log("Paused")
            widget.play()
        }
    }


    function CreateAnimation(chibiwidget,animArray,endloop = false,skipStart = false){
        // console.log(animArray)
        
        // console.log(Array.isArray(animArray))
        // console.log(animArray.length>1)
        // console.log(Array.isArray(animArray[0]))
        
        if((Array.isArray(animArray)&&animArray.length>1)){
            // console.log("ayyyyyy")
            var delay = 0
            var animNum = 0
            if(animationqueue!=undefined)clearInterval(animationqueue)
            var curranimplay = Array.isArray(animArray[0])?animArray[0][0]:animArray[0]
            if(chibiwidget.loaded)chibiwidget.setAnimation(curranimplay)
            chibiwidget.state.clearTracks()
            var curranimations = chibiwidget.skeleton.data.animations
            animArray.forEach(element => {
                var curranim = element
                var animTimes = 1
                var isloop = animNum==animArray.length-1
                
                if(Array.isArray(element)){
                    curranim = element[0]
                    animTimes = element[1]
                    isloop = true
                }
                if(animNum==0)chibiwidget.state.setAnimation(0,curranim,Array.isArray(animArray[0])&&animArray[0].length>1?true:false)
                else chibiwidget.state.addAnimation(animNum,curranim,isloop,delay)
                delay +=curranimations[GetAnimationIndex(curranimations,curranim)].duration*animTimes
                animNum++
                // console.log(element)
            });
            if(endloop){
                if(skipStart)animArray.shift()

                console.log(animArray)
                animationqueue = setInterval(function(){
                    var delay = 0
                    var animNum = 0
                    
                    chibiwidget.state.clearTracks()
                    animArray.forEach(element => {
                        var curranim = element
                        var animTimes = 1
                        var isloop = animNum==animArray.length-1
                        if(Array.isArray(element)){
                            curranim = element[0]
                            animTimes = element[1]
                            isloop = true
                        }
                        if(animNum==0)chibiwidget.state.setAnimation(0,curranim,Array.isArray(animArray[0])&&animArray[0].length>1?true:false)
                        else chibiwidget.state.addAnimation(animNum,curranim,isloop,delay)
                        delay +=curranimations[GetAnimationIndex(curranimations,curranim)].duration*animTimes
                        animNum++
                        console.log(element)
                    });
                },delay*1000)
            }
        }else{
            // chibiwidget.state.setAnimation(animArray)
            // console.log("WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            
            if(animationqueue!=undefined)clearInterval(animationqueue)
            // console.log(animArray)

            var curranimplay = Array.isArray(animArray[0])?animArray[0][0]:animArray
            if(chibiwidget.loaded)chibiwidget.setAnimation(curranimplay)
            chibiwidget.state.clearTracks()
            
            chibiwidget.state.setAnimation(0,curranimplay,true)
        }
    }
    
    function CheckAnimationSet(anim){
        // console.log(anim)
        var curranimlist = {}
        if(anim.find(search=>search.name=="Interact")){
            //Build Mode
            // console.log("Is Build")

        }else if(anim.find(search=>search.name=="Idle")){
            //Battle Mode
            // console.log("Is Battle")
            anim.forEach(curranim => {
                var numberregx = /(\d)/
                var currsplit = curranim.name.split("_")[0]
                
                if(currsplit)
                var splitnum = numberregx.exec(curranim.name)
                if(splitnum){
                    var nameregex = /(.*)(?=\d)/g
                    var checkname = nameregex.exec(currsplit)
                    // console.log(checkname[0])
                    if(checkname)currsplit = checkname[0]
                    // console.log(checkname[0])
                    splitnum=splitnum[0]
                }
                else if (!splitnum) splitnum=""

                if(!curranimlist[`${currsplit}${splitnum}`]){
                    curranimlist[`${currsplit}${splitnum}`] = []
                }
                if(!curranim.name.includes("Down")){
                    curranimlist[`${currsplit}${splitnum}`].push(curranim.name)
                }
                
            });
            Object.keys(curranimlist).forEach(keys => {
                curranimlist[keys]= curranimlist[keys].sort((a,b)=>{
                    var sortarray = [
                        "Pre",
                        "Begin",
                        "Start",
                        "Idle",
                        "",
                        "Loop",
                        "End",
                        "Die"
                    ]
                    var anum = 0
                    var bnum = 0
                    for(i=0;i<sortarray.length;i++){
                        // console.log(sortarray[i])
                        if(sortarray[i]==""){
                            var isAfree = true
                            var isBfree = true
                            for(j=0;j<sortarray.length;j++){
                                if(sortarray[j]!=""){
                                    if(a.includes(sortarray[j]))isAfree=false
                                    if(b.includes(sortarray[j]))isBfree=false
                                }
                            }
                            if (isAfree) anum += 4
                            if (isBfree) bnum += 4
                        }else{
                            if(a.includes(sortarray[i]))anum+=i+1
                            if(b.includes(sortarray[i]))bnum+=i+1
                        }
                    }
                    return anum - bnum
                    
                })
                // curranimlist[keys].forEach(element => {
                //     if(curranimlist[keys].length>=2&&(element.includes("Loop")||element.includes("Idle"))){
                //         console.log(element)
                //         element = [element,5]
                //     }
                // });
                if(curranimlist[keys].find(search=>search.includes("End"))){
                    if(anim.find(search=>search.name.includes("Idle_Charge"))) curranimlist[keys].push("Idle_Charge")
                    else curranimlist[keys].push("Idle")
                }
                if(curranimlist[keys].find(search=>search.includes("Die"))){
                    if(anim.find(search=>search.name.includes("Start"))) curranimlist[keys].push("Start")
                }
                for(i=0;i<curranimlist[keys].length;i++){
                    var filterarray = [
                        "Pre",
                        "Begin",
                        "Start",
                        "Idle",
                        "Loop",
                        "End",
                        "Die"
                    ]
                    var iscomp = true
                    if (curranimlist[keys].length>=2&&(curranimlist[keys][i].includes("Loop")||curranimlist[keys][i].includes("Idle"))&&!curranimlist[keys][i].includes("End")) iscomp = false
                    else{
                        iscomp = false
                        filterarray.forEach(element => {
                            if(curranimlist[keys][i].includes(element)) iscomp = true
                        });
                    }
                    if(!iscomp){
                        // console.log(curranimlist[keys][i])
                        var currvariable = anim.find(search=> search.name == curranimlist[keys][i])
                        // console.log(currvariable)
                        // console.log("Got "+ Math.round(8/currvariable.duration))
                        if(curranimlist[keys][i].includes("Idle")){
                            if(Math.round(3/currvariable.duration)>3)curranimlist[keys][i] = [curranimlist[keys][i],Math.round(3/currvariable.duration)]
                        }else{
                            curranimlist[keys][i] = [curranimlist[keys][i],Math.round(8/currvariable.duration)]
                        }
                        
                    }
                }
            });

            
        }
        console.log(curranimlist)
        return curranimlist
    }

    function GetAnimationIndex(anim,name){
        
        return anim.map(function(e) { return e.name; }).indexOf(name)
    }