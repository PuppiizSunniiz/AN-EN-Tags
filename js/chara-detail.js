    $.holdReady(true);

    console.log = function () { }

    const jsonList = {

        //CN
        chars           :"./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/character_table.json",
        charpatch       :"./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/char_patch_table.json",
        handbookInfo    :"./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/handbook_info_table.json",
        handbookTeam    :"./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/handbook_team_table.json",
        range           :"./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/range_table.json",
        skills          :"./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/skill_table.json",
        skintable       :"./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/skin_table.json",
        dataconst       :"./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/gamedata_const.json",
        audio_data      :"./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/audio_data.json",
        uniequip        :"./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/uniequip_table.json",
        battle_equip    :"./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/battle_equip_table.json",
        favor           :"./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/favor_table.json",

        //EN
        charsEN         :"./json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/character_table.json",
        charpatchEN     :"./json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/char_patch_table.json",
        handbookInfoEN  :"./json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/handbook_info_table.json",
        handbookTeamEN  :"./json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/handbook_team_table.json",
        skillsEN        :"./json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/skill_table.json",
        uniequipEN      :"./json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/uniequip_table.json",
        battle_equipEN  :"./json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/battle_equip_table.json",

        //Utilities
        attacktype      :"./json/tl-attacktype.json",
        effect          :"./json/tl-effect.json",
        subclass        :"./json/subclass.json",

        //Sliced
        enemy           :"./json/puppiiz/enemy_name.json",
        stage           :"./json/puppiiz/stage_code.json",
        potential_token :"./json/puppiiz/potential_token.json",
        build           :"./json/puppiiz/riic_data.json",
        special_operator:"./json/puppiiz/special_operator.json",
        charword        :"./json/puppiiz/charword_table.json",

        //TL
        voicelineTL     :"./json/tl-voiceline.json",
        campdata        :"./json/tl-campdata.json",
        charastoryTL    :"./json/tl-charastory.json",
        storytextTL     :"./json/tl-storytext.json",
        vaTL            :"./json/tl-va.json",
        potentialTL     :"./json/tl-potential.json",
        unreadNameTL    :"./json/tl-unreadablename.json",
        itemsTL         :"./json/tl-item.json",
        tags            :"./json/tl-tags.json",
        classes         :"./json/tl-type.json",
        chars2          :"./json/tl-akhr.json",
        gender          :"./json/tl-gender.json",
        tlsubclass      :"./json/tl-subclass.json",
        ktags           :"./json/tl-tags-key.json",
        ModuleTL        :"./json/tl-module.json",
        artistTL        :"./json/tl-artist.json",

        //jet TL
        talentsTL       :"./json/ace/tl-talents.json",
        skillsTL        :"./json/ace/tl-skills.json",
        named_effects   :"./json/named_effects.json",

        //extra
        extra_range       :"./json/ace/extra_range.json",
        voiceold          :"./json/ace/oldvoice.json"

    };
    const d = new Date()
    const sus = (d.getDate() == 1) && (d.getMonth() + 1 == 4) //April 1st

    var db = {}
    LoadAllJsonObjects(jsonList).then(function(result) {
        db = result
        $.holdReady(false);
    });

    var lang;
    var reg;
    var lefthand;
    var opdataFull = {};
    var curpath;
    var opapp;
    var gmapp;
    var classfilter;
    var sort;
    var opSType;
    var skeletonType = "skel"
    var chibitype = 'character'
    var charName = 'char_180_amgoat';
    var chibipers = 'front'
    var chibiName = 'char_180_amgoat'
    var folder = `https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/spineassets/${chibitype}/${charName}/${chibipers}/`
    var spinewidget
    var spinewidgetcg
    var opid;
    var curropid
    var defaulttoken
    var globaltoken
    var globalelite = 0
    var globallevel =[1,1,1]
    var globalskill = 0
    var skillValue
    const TRUE_INFINITY = ['skchr_lolxh_1', 'skchr_strong_1', 'skchr_strong_2', 'skchr_nothin_2', 'skchr_talr_1', 'skchr_flameb_2', 'skchr_whitew_1', 'skchr_platnm_2', 'skchr_absin_1', 'skchr_folivo_1', 'skchr_tuye_2', 'skchr_whispr_2', 'skchr_vodfox_1', 'skchr_quercu_1', 'skchr_ash_1', 'skchr_acnipe_2', 'skchr_bgsnow_1', 'skchr_phenxi_3', 'skchr_ray_2', 'skchr_narant_1', 'skchr_marcil_2', 'skchr_logos_1', 'skchr_lin_1', 'skchr_gdglow_2', 'skchr_whitw2_1', 'skchr_lisa_2', 'skchr_skadi2_2', 'skchr_cetsyr_1', 'skchr_lmlee_1', 'skchr_lmlee_3', 'skchr_swire2_1', 'skchr_swire2_2', 'skchr_swire2_3', 'skchr_weedy_2', 'skchr_agoat2_1', 'skchr_jesca2_1', 'skchr_nearl2_1', 'skchr_f12yin_2', 'skchr_svrash_2', 'skchr_hodrer_2', 'skchr_ulpia_2', 'skchr_huang_2', 'skchr_surtr_3', 'skchr_siege2_2', 'skchr_phatm2_2']
    var israritygrouped
    var talentValue = [0,0,0]
    var talentLimit = []
    var ModuletalentValue

    var Amiyacurrclass  =   "caster"
    const AmiyaCaster   =   "char_002_amiya"
    const AmiyaGuard    =   "char_1001_amiya2"
    const AmiyaMedic    =   "char_1037_amiya3"
    const AmiyaPatchID  =   [AmiyaGuard,AmiyaMedic]
    const AmiyaAllID    =   [AmiyaCaster, ...AmiyaPatchID]

    var teamHTML = [[],[],[]]
    var currskin
    var skinsuffix
    var currVoiceID
    const VAlanglist = ["LINKAGE", "JP", "CN_MANDARIN", "CN_TOPOLECT", "EN", "KR", "FRE", "GER", "ITA", "RUS"]
    var attempt = 0;
    var SpineVersion
    var spinewidgettoken
    var animIndex = 0;
    var animations
    var tokenname
    var tokenanimations
    var animationqueue
    var defaultAnimationName = "Default";
    var loadchibi = false;
    // var chibiscaleweb = 0
    // var chibiscaleweblist = [[0.5,-775],[0.6,-800],[0.7,-825],[0.8,-850],[0.9,-875],[1,-900]]
    var chibiscale = [0.5,0]
    var chibiperscurr = 0
    var chibiperslist = ["front","back","build"]
    var chibipersextralist = ["front","back"]
    var bgnum = 0
    var bgmax = 5
    var scrollcheck = 0
    var savenum = 0

    var canvasNum = 0
    var canvasSize = [[1800,1800],[1200,800],[800,800],[600,600],[500,500]]
    var wid = 1800
    var hei = 1800

    const validparam = ["opname", "gamemode", "story", "voice", "sfx"]

    $(document).ready(function(){
        console.log("Function Starto !!!")
        refreshurl()

        Object.keys(db.chars).forEach(id =>{
            var currentop = db.chars[id]
            currentop.rarity = RarityConvert(currentop.rarity)
        })

        Object.keys(db.charpatch.patchChars).forEach(id =>{
            var currentop = db.charpatch.patchChars[id]
            currentop.rarity = RarityConvert(currentop.rarity)
        })

        Object.keys(db.handbookTeam).forEach(id =>{
            if(id != "none"){
                teamHTML[db.handbookTeam[id].powerLevel].push(
                    `<div class="op-faction btn-secondary tooltip2 adv-filter" data-id="${id}" onclick="toggleBtn(this)" section="faction">
                        <img loading='lazy' class='filter-img faction-img' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/factions/logo_${id}.png'>
                        <span class="tooltiptext tooltiptop tooltipstyle1 nohover">
                            ${Object.keys(db.handbookTeamEN).includes(id)?db.handbookTeamEN[id].powerName:db.handbookTeam[id].powerCode}
                        </span>
                    </div>`)
            }
        })

        $("#nation").html(teamHTML[0])
        $("#group").html(teamHTML[1])
        $("#team").html(teamHTML[2])

        tooltip_activate()
        $('#to-tag').click(function(){              // When arrow is clicked
            $('body, html, .modal-body').animate({
                scrollTop : 0                       // Scroll to top of body
            }, 500);
        });
        $(window).scroll(function(){
            var sticky = $('#ak-bottom-allnav'),
                scroll = $(window).scrollTop();
                isScrollUp = scroll<scrollcheck
            scrollcheck = scroll

            if(loadchibi){
                if (scroll >= 500) {
                    sticky.removeClass('fixedNav');
                    sticky.removeClass('fixedNav1');
                    sticky.addClass('fixedNav2')
                }
                else if(scroll >= 400 && !isScrollUp){
                    sticky.addClass('fixedNav');
                    sticky.removeClass('fixedNav2');
                } else if(scroll >= 400 && isScrollUp){
                    sticky.addClass('fixedNav1');
                    sticky.removeClass('fixedNav2');
                }else{
                    sticky.removeClass('fixedNav');
                    sticky.removeClass('fixedNav1');
                    sticky.removeClass('fixedNav2');
                }
            }
        });

        dragElement2(document.getElementById("charazoom"),document.getElementById("charazoom"))

        // Add listener to class tabs
        $("#classlist .nav-item").children().each(function(i){
            $(this).click(function(){
                selOpClass($(this).attr("data-opclass"));
            })
        });
        $("#all-op").each(function(i){
            $(this).click(function(){
                selOpClass($(this).attr("data-opclass"));
            })
        });

        $("#spine-frame-tokenheader").contextmenu(function(){
            $('#spine-frame-token').toggleClass('spine-frame-token-above')
            return false;
        })

        $(window).click(function(event) {
            if (!$(event.target).is('#to-tag')){
                $('#operatorsResult').empty();
                $('#operatorsResult').hide();
            }
        });

        $("#Chibi-Show").click(function(){
            var isvisible = $("#spine-frame").is(":visible")
            $("#spine-frame").fadeToggle(100);

            if(!loadchibi){
                loadchibi=true
                if(bgnum == 0 && $("#spine-bg").is(":hidden")){
                    bgnum = 1
                    $('#spine-bg').attr("src", "https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/spine/bg" + bgnum +".png");
                    $('#spine-bg').fadeIn('fast');
                }
                if(!spinewidget){
                    LoadAnimation()
                }
                if(!spinewidgettoken){
                    if(globaltoken){
                        LoadAnimationToken()
                    }
                }
            }

            if(spinewidget){
                if(isvisible){
                    spinewidget.pause()
                    loadchibi = false
                    $('#spine-bg').fadeOut('fast')
                }
                else {
                    spinewidget.play()
                    loadchibi = true

                    if($("#spine-bg").is(":hidden")){
                        if (bgnum == 0) bgnum = 1
                        $('#spine-bg').attr("src", "https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/spine/bg" + bgnum + ".png");
                        $('#spine-bg').fadeIn('fast');
                    }
                }
            }

            if(spinewidgettoken){
                if(isvisible){
                    spinewidgettoken.pause()
                    $("#spine-frame-token").fadeOut(100);
                }
                else {
                    spinewidgettoken.play()
                    $("#spine-frame-token").fadeIn(100);

                }
            }
            var sticky = $('#ak-bottom-allnav')
            console.log(scrollcheck)
            if(scrollcheck >= 500 && sticky.hasClass("fixedNav2")){
                sticky.addClass('fixedNav1')
                sticky.removeClass('fixedNav2');

                window.setTimeout(function(){
                    sticky.removeClass('fixedNav1')
                }, 100);
            }
        });
        dragElement(document.getElementById("spine-frame"));
        dragElement(document.getElementById("spine-frame-token"));
        dragElement(document.getElementById("spine-frame-op"));
        $("#Chibi-Bg").click(function(){
            bgnum ++
            if(bgnum > bgmax) bgnum = 0
            else if(bgnum < 0) bgnum = bgmax

            if(bgnum == 0) $('#spine-bg').fadeOut('fast')
            else {
                $('#spine-bg').fadeOut('fast', function () {
                    $('#spine-bg').attr("src", "https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/spine/bg" + bgnum + ".png");
                    $('#spine-bg').fadeIn('fast');
                });
                console.log( $('#spine-bg').attr("src") )
            }


        });
        $("#Chibi-Perspective").click(function(){
            chibiperscurr++

            newpers = Chibi_per()
            ChangeSkin(currskin, newpers, "", "", true)
        });
        $("#Chibi-Show-menu").click(function(){
            $('#Chibi-menu').toggleClass("chibi-menu-closed")

        });
        $("#Chibi-frameSize").click(function(){
            // $('#Chibi-menu').toggleClass("chibi-menu-closed")
            canvasNum++

            if(canvasNum >= canvasSize.length) canvasNum = 0
            else if(canvasNum < 0)canvasNum = canvasSize.length

            wid = canvasSize[canvasNum][0]
            hei = canvasSize[canvasNum][1]
            if(spinewidget){
                LoadAnimation()
            }
            if(spinewidgettoken){
                if(globaltoken){
                    LoadAnimationToken()
                }
            }
        });

        $("#Chibi-Scale").click(function(){

            // chibiscaleweb++


            // if(chibiscaleweb>=chibiscaleweblist.length)chibiscaleweb=0
            // else if(chibiscaleweb<0)chibiscaleweb=chibiscaleweblist.length
            // console.log(chibiscaleweb)
            // console.log(chibiscaleweblist)


            // var currscale = chibiscaleweblist[chibiscaleweb]
            // console.log(currscale)
            $('#chibizoomslider').val(0)
            ZoomChibi(0)
            // $('#chibizoomslider').click();
            // $("#spine-widget").css("transform",`scale(0.5)`)
            // $("#spine-widget").css("top",`-775px`)
            // $("#spine-widget-token").css("transform",`scale(0.5)`)
            // $("#spine-widget-token").css("top",`-775px`)



        });

        $('#Chibi-download').click(function(event){
            // var canvas = spinewidget.canvas

            var checkdiv = $("#spine-widget").children()[0]
            // console.log($("#spine-widget").children())
            // console.log(canvas)
            // console.log(checkdiv)
            var img = checkdiv.toDataURL("image/png");
            // $('#Chibi-download').attr("href",img)
            // $('#Chibi-download').attr("download","a.png")
            // console.log(img)
            // $("#spine-widget-2").html('<img src="'+img+'"/>');
            console.log(currskin)
            var link = document.createElement("a");
            link.download = `${currskin}-${savenum}.png`;
            savenum++
            link.href = img;
            link.click();

            // CreateAnimation(spinewidget,["Skill_2_Begin",["Skill_2_Loop",20],"Skill_2_Loop_End"],false,false,true)
            // console.log(spinewidget)
            // var dataURL = $("#spine-widget")[0].toDataURL('image/png');
            // var w = window.open('about:blank', 'image from canvas');
            // w.document.write("<img src='" + img + "' alt='from canvas'/>");

        });

        $('#operatorsResult').click(function(event){
            event.stopPropagation();
        });
        $('#opBrowseButton').click(function(event){
            $("#opchoosemodal").modal('show');
        });
        $('#opBrowseButton2').click(function(event){
            event.stopPropagation();
        });
        $('#opBrowseButton3').click(function(event){
            event.stopPropagation();
        });
        $('#opname').click(function(event){
            event.stopPropagation();
        });
        $(".fa-sort-amount-up").click(event => event.stopPropagation());
        $(".fa-sort-amount-down").click(event => event.stopPropagation());
        $('#lefthandtoggle').click(function(event){
            lefthand = !lefthand
            localStorage.setItem("lefthand", JSON.stringify(lefthand))
            location.reload()
        })
        if(!localStorage.getItem('lefthand')){
            lefthand = false
            localStorage.setItem("leftHand", JSON.stringify(lefthand))

        }else{
            lefthand = JSON.parse(localStorage.getItem('lefthand'))
        }

        if(!localStorage.getItem('israritygrouped')){
            israritygrouped = true
            localStorage.setItem("israritygrouped", JSON.stringify(israritygrouped))
            $(`#group-rarity`).addClass("btn-primary");
        }else{
            israritygrouped = JSON.parse(localStorage.getItem('israritygrouped'))
            if(israritygrouped){
                $(`#group-rarity`).addClass("btn-primary");
            }else{
                $(`#group-rarity`).addClass("btn-secondary");
            }
        }

        if(lefthand)
        $('#lefthandtoggle').css("background-color", "#0077AA")
        else
        $('#lefthandtoggle').css("background-color", "#222")

        $('#opname').bind("enterKey", function(e){
            populateOperators($('#opname').val(), true)
         });
         $('#opname').keyup(function(e){
             if(e.keyCode == 13)
             {
                 $(this).trigger("enterKey");
             }
         });

        if(!localStorage.getItem('gameRegion') || !localStorage.getItem('webLang')){
            localStorage.setItem("gameRegion", 'cn');
            localStorage.setItem("webLang", 'en');
            reg = "cn";
            lang = "en";

            var vars = getUrlVars();
            if(vars.has("opname")){
                // console.log("TEST1")
            }
        }else{
            console.log(localStorage.getItem('webLang'));
            reg = "cn";
            lang = "en";
        }
        if(!localStorage.getItem('selectedOPDetails')){
            console.log("selected OP undefined");
            var vars = getUrlVars();
            console.log(vars)
            if(vars.has("opname")){
                vars.set("opname", decodeURIComponent(vars.get("opname").replace("_", " ")));
                console.log(vars.get("opname"));
                var char = query(db.chars, "appellation", vars.get("opname"), true, true);
                console.log(char)
                if(char){
                    $.each(char, function(key, _){
                        opid = key;
                    });
                    selectOperator(opid);
                }else{
                    refreshurl("delete")
                }
            }else{
                refreshurl("delete")
            }
        }else{
            console.log("selected OP defined");
            var vars = getUrlVars();
            if(vars.has("opname")){
                var char = {};
                var opname = decodeURIComponent(vars.get("opname"));
                var unreadable = query(db.unreadNameTL, "name_en", opname.replace(/_/g, " "))
                var correctname = unreadable?unreadable.name:opname.replace(/_/g, " ")
                if(vars.get("gamemode")){
                    var chars = query(db.chars2, "name_en", correctname, false, false);
                    gmapp = vars.get("gamemode")
                    char = query(chars, "gamemode", gmapp, true, false)
                    opid = char.id
                }else{
                    char = query(db.chars ,"appellation", correctname, true, true);
                    console.log(char)
                    opid = Object.keys(char)[0]
                    gmapp = opid?query(db.chars2, "gamemode", opid, false, false):"";
                }
                opapp = correctname
            }else{
                opid = localStorage.getItem('selectedOPDetails');
            }

            if (opid) selectOperator(opid, "cookies");
            else refreshurl("delete")

            if(vars.has("story")){
                $('#opstory').modal('show')
            }else if(vars.has("voice")){
                currVoiceID = opdataFull.id
                GetAudio()
                $('#opaudio').modal('show')
            }else if(vars.has("sfx")){
                GetSFX(opdataFull)
                $('#opsfx').modal('show')
            }

        }
        if (window.history && window.history.pushState) {
            $(window).on('popstate', function() {
                var vars = getUrlVars()
                console.log(opapp, gmapp)
                console.log(vars)
                var historyopname = vars.get("opname")?vars.get("opname"):""
                var historygamemode = vars.get("gamemode")?vars.get("gamemode"):"BASE"
                console.log(historyopname, opapp, historyopname != opapp, historygamemode, gmapp, historygamemode != gmapp,(historyopname && historyopname != opapp) || (historygamemode && historygamemode != gmapp))
                if(historyopname && (historyopname != opapp || (historygamemode && historygamemode != gmapp))){
                    var unreadable = query(db.unreadNameTL, "name_en",historyopname.replace(/_/g, " "))
                    var correctname = (unreadable?unreadable.name:historyopname.replace(/_/g, " "))
                    console.log(correctname)
                    if(vars.get("gamemode")){
                        var chars = query(db.chars2, "name_en", correctname, false, false);
                        gmapp = vars.get("gamemode")
                        char = query(chars, "gamemode", gmapp, true, false)
                        opid = char.id
                    }else{
                        char = query(db.chars, "appellation", correctname, true, true);
                        console.log(char)
                        opid = Object.keys(char)[0]
                        gmapp = query(db.chars2, "gamemode", opid, false, false);
                    }
                    opapp = correctname
                    
                    if (opid) selectOperator(opid, "cookies");
                    else refreshurl("delete")
                    
                }else{
                    console.log("gone")
                    opapp = ""
                    gmapp = "BASE"
                    $('#chara-detail-container').hide();
                }

                if(vars.has("story")){
                    $('#opstory').modal('show')
                    $('#opaudio').modal('hide')
                }else if(vars.has("voice")){
                    $('#opaudio').modal('show')
                    $('#opstory').modal('hide')
                }else{
                    $('#opstory').modal('hide')
                    $('#opaudio').modal('hide')
                }
            //   alert('Back button was pressed.');
            });

        }

        $('#opstory').on('shown.bs.modal', function(){
            var url = new URL(window.location.href);
            url.searchParams.set('story', 0);
            history.replaceState(null, '', url);
        });
        $('#opstory').on('hidden.bs.modal', function(){
            var url = new URL(window.location.href);
            url.searchParams.delete('story');
            history.replaceState(null, '', url);
        });
        $('#opaudio').on('shown.bs.modal', function(){
            var url = new URL(window.location.href);
            url.searchParams.set('voice', 0);
            history.replaceState(null, '', url);
        });
        $('#opaudio').on('hidden.bs.modal', function(){
            var url = new URL(window.location.href);
            url.searchParams.delete('voice');
            history.replaceState(null, '', url);
        });
        $('#opsfx').on('shown.bs.modal', function(){
            var url = new URL(window.location.href);
            url.searchParams.set('sfx', 0);
            history.replaceState(null, '', url);
        });
        $('#opsfx').on('hidden.bs.modal', function(){
            var url = new URL(window.location.href);
            url.searchParams.delete('sfx');
            history.replaceState(null, '', url);
        });

        $('.reg[value='+reg+']').addClass('selected');
        $('.lang[value='+lang+']').addClass('selected');

        window.onhashchange = function() {
            console.log(window.location.pathname)
        }

        $(".op-gender").each((_, btn) => $(btn).text(db.gender[$(btn).attr("data-id")][`sex_${lang}`]));
        $(".op-tag").each((_, btn) => $(btn).text(db.ktags[$(btn).attr("data-id")][lang]));

        $("audio").on("play", function () {
            $("audio").not(this).each(function () {
                this.pause();
                //this.currentTime = 0; //pause/stop
            });
        });

        $('#opaudio').on('hidden.bs.modal', function () {
            $(this).find("audio").each(function () {
                this.pause();
                this.currentTime = 0;
                });
            });
    });

    $.getScript("js/arrive.min.js", function(){
        $(document).arrive("#regionDropdown", function(){
            $("#navitemRegion").addClass('ak-disable2');
            $("#navitemLanguage").addClass('ak-disable2');
        });
    });

    function refreshurl(mode = "default"){
        const url = new URL(window.location.href)
        const urlVars = url.searchParams
        const urlkeys = [...urlVars.keys()] 

        // kill all param
        if(mode == "delete"){
            urlkeys.forEach(param => urlVars.delete(param))
            history.replaceState(null, '', window.location.pathname);
            return
        }
        // check if there "opname" then clean else CLEANSE
        if (urlkeys.includes("opname")){
            urlkeys.forEach(param =>{
                    if (!validparam.includes(param) || !urlVars.get(param)) urlVars.delete(param)
                })
            history.replaceState(null, '', url)
        }else{
            urlkeys.forEach(param => urlVars.delete(param))
            clickBtnClear()
        }
    }

    function tooltip_activate(){
        $('[data-toggle="tooltip"]').tooltip({
        trigger: 'hover click', // allow both hover and click
        html: true
    })}
    // Resize-height when rotate
    $(window).on("resize orientationchange", function () {
        $(".collapsible-open").each(function () {
            let target = $(`#${$(this).attr("target")}`);
            let newHeight = target[0].scrollHeight;
            target.css("max-height", `${newHeight}px`);
        });
    });
    // Close tooltip
    $(document).on('click touchstart', function (e) {
        $('[data-toggle="tooltip"]').each(function () {
            if (!$(this).is(e.target) && $(this).has(e.target).length === 0 && $('.tooltip').has(e.target).length === 0) {
                $(this).tooltip('hide');
            }
        });
    });

    const root = document.documentElement;

    document.addEventListener('mousemove', evt => {
        let x = evt.clientX / innerWidth;
        let y = evt.clientY / innerHeight;

        root.style.setProperty('--mouse-x', x);
        root.style.setProperty('--mouse-y', y);
    });

    function clickID(){
        console.log("copy ID", opdataFull.id)
        navigator.clipboard.writeText(opdataFull.id)
    }

    function clickBtnClear(){
        $("#chara-detail-container").hide();
        $("#elite-sidenav").empty();
        $("#tabs-opCG").empty();
        $("#elite-topnav").empty();
        $("#tabs-opData").empty();
        $("#op-taglist").empty();
        $("#opname").val("");
        $('#operatorsResult').empty();
        $('#operatorsResult').hide();
        localStorage.removeItem('selectedOPDetails');
        localStorage.removeItem('selectedOPGamemode');
        history.replaceState(null, '', window.location.pathname);
    }

    function selOpClass(cname){
        $("#selectedopclass").empty();

        var result
        if(cname != ""){
            result = query(db.chars, "profession", cname, false, true);
        }else{
            result = ObjectToArray(db.chars)

        }

        //add extra filter later
        result = result.filter(search => {
            var searchOb = search[Object.keys(search)[0]]

            switch(searchOb.profession){
                case "TOKEN" :
                case "TRAP" : return false
            }
            return true
        })

        //add extra sort later
        result = result.sort((ak, bk) => {
            var a = ak[Object.keys(ak)[0]]
            var b = bk[Object.keys(bk)[0]]
            // console.log(ak)
            if(a.rarity < b.rarity) return 1
            if(a.rarity > b.rarity) return -1
            if(a.appellation > b.appellation) return 1
            if(a.appellation < b.appellation) return -1
        })
        var listtype = "Grid"
        var showtype = "a"

        for (var i = 0; i < result.length; i++) {
            var html;
            $.each(result[i], function(key, val){ // key = char_230_savage, val = data (obj)
                var type = query(db.classes, "type_data", val.profession);
                var classlogo = type?type.type_en.toLowerCase():""
                var camplogo = val.displayLogo
                switch (listtype) {

                    case "List":
                                html =
                                `
                                    <li class='selectop-list ak-shadow' onclick='selectOperator("${key}")'>
                                        <img loading='lazy' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/${key}.png'>
                                        <div class='name ak-font-novecento'>${getENname(val.name)}</div>
                                        <div class='rarity op-rarity-${val.rarity + 1}'>
                                            ${(`<i class='fa fa-star'></i>`).repeat(val.rarity + 1)}
                                        </div>
                                    </li>
                                `
                        break;

                    case "Grid":
                                html =
                                `
                                    <li class='selectop-grid ak-shadow' onclick='selectOperator("${key}")'>
                                        <img loading='lazy' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/${key}.png'>
                                        <div class='name ak-font-novecento ak-center'>${getENname(val.name)}</div>
                                        <div class='ak-rare-${val.rarity + 1}'></div>
                                        <div class='ak-showsubclass'><img loading='lazy' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/subclass/sub_${val.subProfessionId}_icon.png'></div>
                                        ${cname == "" && classlogo?`<div class='ak-showclass'><img loading='lazy' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/classes/class_${classlogo}.png'></div>`:""}
                                        ${showtype && camplogo?`<div class='ak-showfaction'><img loading='lazy' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/factions/${camplogo.toLowerCase()}.png' title='${db.campdata[camplogo]}' ></div>`:""}
                                        <div class='grid-box op-rarity-${val.rarity + 1}'></div>
                                    </li>
                                `

                        break;

                    default:
                        break;
                }
            });
            $("#selectedopclass").append(html);
        }
    }

    function getENname (CNname){
        var result;
        var found = false;
        $.each(db.chars2, function(key, val){
            if(val.name_cn.toLowerCase() == CNname.toLowerCase()){
                found = true;
                result = val.name_en;
            }
        });
        if(found){
            return result;
        }else{
            return false;
        }
    }

    function populateOperators(el, isenter = false){
        let inputs
        if(isenter)
            inputs = el
        else
            inputs = el.value
        if(($('#operatorsResult').css("display") == "block") &&
            ((el == "Browse" && $("#operatorsResult").hasClass("opbrowse1")) ||
             (el == "Browse2" && $("#operatorsResult").hasClass("opbrowse2")))){
            $("#operatorsResult").removeClass("opbrowse1");
            $("#operatorsResult").removeClass("opbrowse2");
            $('#operatorsResult').hide();
            return;
        }
        if(el.value != "" || el == "Browse" || el == "Browse2" || isenter && el){
            var result = [];

            $.each(db.chars2,function(_, char){
                var languages   = ['cn', 'en', 'jp', 'kr'];
                var found       = false;

                if(el == "Browse" || el == "Browse2"){
                    found = true;
                }else{
                    for (var i = 0; i < languages.length; i++) {
                        var charname    = char['name_' + languages[i]];
                        var unreadable  = query(db.unreadNameTL, "name", char.name_en)
                        var input       = inputs.toUpperCase();
                        var search      = inputs.match(/char_[1-9]{1,4}/g)?(unreadable ? (unreadable.name_en + charname + char.id).toUpperCase().search(input) : (charname + char.id).toUpperCase().search(input))
                                            :(unreadable ? (unreadable.name_en + charname + char.id.replace("char_","")).toUpperCase().search(input) : (charname + char.id.replace("char_","")).toUpperCase().search(input));
                        if(search != -1){
                            found = true;
                            break;
                        };
                    }
                }
                if(found){
                    // console.log(char)
                    var name_cn = char.name_cn;
                    var name = char['name_' + reg];
                    var unreadable = query(db.unreadNameTL, "name", char.name_en).name_en
                    var nameTL = char['name_' + lang];
                    var id = char.id
                    var rarity = char.level;
                    var gamemode = query(db.chars2, "id", char.id).gamemode

                    // console.log(rarity);
                    if(rarity != 0)
                        result.push({'name':name, 'name_cn':name_cn, 'name_readable':unreadable, 'nameTL':nameTL, 'id':id, rarity, gamemode});
                }
            });
            // console.log(result)
            result.sort((a,b) => b.rarity - a.rarity)
            if(result.length > 0){
                if(isenter){
                    $('#operatorsResult').hide();
                    selectOperator(result[0].id)
                    return
                }
                $('#operatorsResult').empty();
                $('#operatorsResult').show();
                var numrar = 0
                var rarity = -1
                for (var i = 0; i < result.length; i++) {
                    let image = `<img style="height:40px;padding:2px" src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/${result[i].id}.png">  `
                    // console.log(image)
                    $("#operatorsResult").removeClass("opbrowse1");
                    $("#operatorsResult").removeClass("opbrowse2");
                    if(el == "Browse3"){
                        image = `<img loading='lazy' class='opres-img' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/${result[i].id}.png">  `
                        var charaname = `${result[i].name_readable?`[${result[i].name_readable}]`:""}${result[i].nameTL}`
                        $("#operatorsResult").css("text-align", "center");
                        $("#operatorsResult").removeClass("opresult-list");
                        $("#operatorsResult").addClass("opresult-grid");
                        $("#operatorsResult").addClass("opbrowse1");
                        $("#operatorsResult").append(
                            `<li class="col-2 col-sm-1 ak-shadow-small ak-rare-${result[i].rarity}"style="display:inline-block;cursor: pointer;width:75px;margin:2px;margin-bottom:2px;padding:1px;border-radius:2px" onclick="selectOperator('${result[i].id}')">
                             <div style="white-space: nowrap;padding:0px;text-align:center;margin:0 ">${image}</div>
                             <div style="white-space: nowrap;padding:0px;text-align:center;margin:0 ">${charaname}</div>
                             </li>
                            `);

                    }else if(el == "Browse2"){
                        image = `<img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/${result[i].id}.png">  `
                        $("#operatorsResult").css("text-align", "center");
                        $("#operatorsResult").removeClass("opresult-list");
                        $("#operatorsResult").addClass("opresult-grid");
                        $("#operatorsResult").addClass("opbrowse2");

                        var opcurrname = `${result[i].name_readable?`[${result[i].name_readable}]`:""} ${result[i].nameTL}`
                        var extrathing = ''
                        if (rarity != result[i].rarity){
                            rarity = result[i].rarity
                            extrathing = `
                            ${titledMaker(`
                            ${titledMaker(``, "", `ak-rare-${rarity} ak-shadow`, "", `height:3px;width:calc(100% + 20px);margin:-28px -10px -10px -10px;padding:0px`)}
                            <div style="margin-top:-15px">
                            ${(`<i class="fa fa-star"></i>`).repeat((rarity))}
                            </div>
                            `, "", `op-rarity2-${rarity}`, "", `font-size:12px;height:20px;width:calc(100% + 20px);margin:0px -10px -5px -10px;text-align:center;padding-top:0px`)}
                            <div style="padding-bottom:10px"></div>
                            `
                            numrar += 1
                        }
                        $("#operatorsResult").append(
                            `${extrathing}<li class="selectop-grid2" onclick="selectOperator('${result[i].id}')">
                            <div class="op-image-grid2">
                                ${result[i].gamemode=="BASE"?"":'<div class="op-grid-gamemode ' + result[i].gamemode +'">' + result[i].gamemode + '</div>'}
                                ${image}
                            </div>
                            <div class="${opcurrname.length>12?opcurrname.length>16?"namesmaller":"namesmall":"name"} ak-font-novecento ak-center nameshadow">${opcurrname}</div>
                            <div class='ak-rare-${result[i].rarity} selectopopgridline'></div>
                            </li>`
                        )
                    }else if(el == "Browse"){
                        image = `<img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/${result[i].id}.png">  `
                        $("#operatorsResult").css("text-align", "center");
                        $("#operatorsResult").removeClass("opresult-list");
                        $("#operatorsResult").addClass("opresult-grid");
                        $("#operatorsResult").addClass("opbrowse1");

                        var opcurrname = (result[i].name_readable?`[${result[i].name_readable}] `:"") + result[i].nameTL
                        $("#operatorsResult").append(
                            `<li class="selectop-grid3 ak-rare-${result[i].rarity}" onclick="selectOperator('${result[i].id}')">
                            <div class="op-image-grid2">
                                ${result[i].gamemode == "BASE"?"":'<div class="op-grid-gamemode ' + result[i].gamemode +'">' + result[i].gamemode + '</div>'}
                                ${image}
                            </div>
                            <div class="nametext ${opcurrname.length > 10?opcurrname.length > 15?"namesmaller":"name":"nameshort"} ak-center blacktext">${opcurrname}</div>
                            </div>
                            </li>`
                        )
                    }else{
                        $("#operatorsResult").removeClass("opresult-grid");
                        $("#operatorsResult").addClass("opresult-list");
                        $("#operatorsResult").css("text-align","left");
                        $("#operatorsResult").append(`
                            <li class=" ak-shadow-small ak-rare-${result[i].rarity}" style="width:100%; cursor:pointer; margin-bottom:2px; position:relative;" onclick="selectOperator('${result[i].id}')">
                                ${image}
                                ${result[i].name_readable?`[${result[i].name_readable}]`:""} ${result[i].nameTL} (${result[i].name})
                                ${result[i].gamemode == "BASE"?"":'<div class="op-grid-gamemode ' + result[i].gamemode +'">' + result[i].gamemode + '</div>'}
                            </li>`);
                    }
                }
            }else{
                $('#operatorsResult').empty();
                $('#operatorsResult').append(`
                    <li cstyle="width:100%;cursor: pointer;margin-bottom:2px;" style="color: red; font-size: large;" ><img style="height:40px;padding:2px" src="extra/not_found.png"> No result</li>`);
            }

        }else{
            $('#operatorsResult').empty();
            $('#operatorsResult').hide();
        }
    }

    function collapse(el) {
        $(el).toggleClass("collapsible-closed collapsible-open");
        $(el).children("div").toggleClass("fa-angle-down fa-angle-up");

        let target = $(`#${$(el).attr("target")}`);
        let size = target[0].scrollHeight;
        let delay = 200 / size;

        if ($(el).hasClass("collapsible-open")) {
            for (i = 0; i < size; i++) setTimeout((i) => target.css("max-height", `${i}px`), delay * i, i);
        }else{
            for (i = 0; i < size; i++) setTimeout((i) => target.css("max-height",`${size - i}px`), delay * i, i);
        }
    }

    function getBranchclassHtml(btn) {
        function branchclassHtml(data_id, data_name) {
            return `<div class="btn-secondary op-branch filter-img tooltip2" onclick="toggleBtn(this)" section="branch" data-id="${data_id}">
            <img loading='lazy' src="${`https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/subclass/sub_${data_id}_icon.png`}" style="width:33px;height:33px;object-fit: contain;display: inline-block;" alt="${data_name}">
            <span class="tooltiptext tooltipstyle1 nohover">${data_name}</span>
            </div>`
        }

        var list = ""
        db.tlsubclass.list[$(btn).attr("data-id")].forEach(element => {
            console.log(element)
            var branchname = element
            if(db.tlsubclass.subclass[element]){
                var currsub = db.tlsubclass.subclass[element]
                if(currsub.en && currsub.en.length>0){
                    branchname = currsub.en
                }else if(currsub.tl && currsub.tl.length>0){
                    branchname = currsub.tl
                }else if(currsub.name){
                    branchname = currsub.name
                }
            }
            list += branchclassHtml(element,branchname)
        });
        return list
    }

    function actualizeBranch(){
        $("#branch-container").html($(".op-class.btn-primary").map((_, btn) => getBranchclassHtml(btn)).get().join(""));
    }

    function toggleExclusive(el) {
        $(el).toggleClass("filter-exclusive filter-nonexclusive");
        if ($(el).attr("id") !== "filter-name-faction") clearFilter($(`#clear-filter-${$(el).attr("id").slice(12)}`).attr("clear-data"));
        else $(el).html($(el).html() == "Main Faction"?"All Factions":"Main Faction")
        if ($(el).attr("id") == "filter-name-class") actualizeBranch();

        actualizeFilter();
    }

    function toggleBtn(el) {
        let section = $(el).attr("section");
        let exclusive = section && $(el).hasClass("btn-secondary") && ($(`#filter-name-${section}`).hasClass("filter-exclusive") || section == "faction");

        if (exclusive) $(`.op-${section}`).removeClass("btn-primary").addClass("btn-secondary");
        $(el).toggleClass("btn-secondary btn-primary");
        if (!$(".op-gamemode.btn-primary").map((_, btn) => $(btn).attr("data-id")).get().length) $(".ALL").removeClass("btn-secondary").addClass("btn-primary");
        if ($(el).hasClass("op-class")){
            actualizeBranch();
        }

        actualizeFilter();
    }

    function toggleGroup(el){
        $(el).toggleClass("btn-secondary btn-primary");
        israritygrouped = !israritygrouped
        localStorage.setItem("israritygrouped", JSON.stringify(israritygrouped))
        actualizeFilter();
    }

    function clearFilter(cls) {
        $(cls).removeClass("btn-primary").addClass("btn-secondary");
        if (cls.includes(".op-class")) actualizeBranch();

        actualizeFilter();
    }

    function switchState(el) {
        $(el).toggleClass("btn-disabled btn-enabled");

        actualizeFilter();
    }

    function invertSort(el) {
        $(el).toggleClass("fa-sort-amount-down fa-sort-amount-up");

        actualizeFilter();
    }

    function resetSorting() {
        $("#sort-atk").removeClass("btn-enabled").addClass("btn-disabled");
        $("#sort-def").removeClass("btn-enabled").addClass("btn-disabled");
        $("#sort-hp").removeClass("btn-enabled").addClass("btn-disabled");
        $("#sort-dp").removeClass("btn-enabled").addClass("btn-disabled");
        $("#sort-block").removeClass("btn-enabled").addClass("btn-disabled");
        $("#sort-rarity").removeClass("btn-disabled").addClass("btn-enabled");

        $("#order-atk").removeClass("fa-sort-amount-up").addClass("fa-sort-amount-down");
        $("#order-def").removeClass("fa-sort-amount-up").addClass("fa-sort-amount-down");
        $("#order-hp").removeClass("fa-sort-amount-up").addClass("fa-sort-amount-down");
        $("#order-dp").removeClass("fa-sort-amount-up").addClass("fa-sort-amount-down");
        $("#order-block").removeClass("fa-sort-amount-up").addClass("fa-sort-amount-down");
        $("#order-rarity").removeClass("fa-sort-amount-up").addClass("fa-sort-amount-down");

        actualizeFilter();
    }

    function sortFilter(val_a, val_b, stat_class) {
        if ($(`#sort-${stat_class}`).hasClass("btn-disabled")) return 0;

        return $(`#order-${stat_class}`).hasClass("fa-sort-amount-down") ? val_b - val_a : val_a - val_b;
    }

    // can't use array methods without discarding id and id isn't stored right inside char *sigh*
    function getId(char) {
        return char.phases[0].characterPrefabKey;
    }

    function getStat(char, stat_class) {
        return char.phases.slice(-1)[0].attributesKeyFrames[1].data[stat_class];
    }

    function getTags(char) {
        return char.tagList.concat(char.position == "MELEE" || char.position == "ALL" ? ["近战位"] : [],    // Melee
                                   char.position == "RANGED" || char.position == "ALL" ? ["远程位"] : [],   // Ranged
                                   char.rarity == 1 ? ["新手"] : [],                                        // Starter
    )}

    function getBranchClass(char){
        return char.subProfessionId
    }

    function actualizeFilter() {
        $("#selectedopclass").html("");

        let op_class = $(".op-class.btn-primary").map((_, btn) => $(btn).attr("data-id")).get();
        let op_branch = $(".op-branch.btn-primary").map((_, btn) => $(btn).attr("data-id")).get();
        let op_rarity = $(".op-rarity.btn-primary").map((_, btn) => parseInt($(btn).attr("data-id"))).get();
        let op_gamemode = $(".op-gamemode.btn-primary").map((_, btn) => $(btn).attr("data-id")).get()[0];
        let op_gender = $(".op-gender.btn-primary").map((_, btn) => db.gender[$(btn).attr("data-id")]["sex_cn"]).get();
        let op_tag = $(".op-tag.btn-primary").map((_, btn) => db.ktags[$(btn).attr("data-id")]["cn"]).get();
        let op_faction = $(".op-faction.btn-primary").map((_, btn) => $(btn).attr("data-id")).get();
        let op_skill = $(".op-skill.btn-primary").map((_, btn) => parseInt($(btn).attr("data-id"))).get();
        let op_ammo = $(".op-ammo.btn-primary").map((_, btn) => $(btn).attr("data-id")).get();

        let exclusive_class = $("#filter-name-class").hasClass("filter-exclusive");
        let exclusive_gender = $("#filter-name-gender").hasClass("filter-exclusive");
        let exclusive_tag = $("#filter-name-tag").hasClass("filter-exclusive");
        let exclusive_faction = $("#filter-name-faction").hasClass("filter-exclusive");
        let exclusive_skill = $("#filter-name-skill").hasClass("filter-exclusive");

        var totalRarity = {}
        // Advanced options
        if (op_gamemode == "ALL" &&
            op_gender.length == 0 &&
            op_tag.length == 0 &&
            op_faction.length == 0 &&
            op_skill.length == 0 &&
            op_ammo.length == 0) $("#adv-filter").removeClass("btn-primary")
        else $("#adv-filter").addClass("btn-primary")

        if (op_class.length == 0 &&
            op_branch.length == 0 &&
            op_gamemode == "ALL" &&
            op_rarity.length == 0 &&
            op_gender.length == 0 &&
            op_tag.length == 0 &&
            op_faction.length == 0 &&
            $("#filter-equip").hasClass("btn-secondary") &&
            op_skill.length == 0 &&
            op_ammo.length == 0) return;

        // EXTRACTION
        let ops = []
        Object.keys(db.chars).forEach(id => {
            let curops = db.chars[id]
            curops.id = id
            if(curops.profession != "TOKEN" && curops.profession != "TRAP" && id !="char_512_aprot"){
                ops.push(curops)
            }
        });
        console.log(ops)

        // FILTERING
        if (op_gamemode !== "ALL") ops = ops.filter(char => op_gamemode == "BASE" ? ["BASE", "SO"].includes(query(db.chars2, "id", char.id).gamemode)
                                                                                    :op_gamemode == query(db.chars2, "id", char.id).gamemode)
        if (op_class.length) ops = exclusive_class ? ops.filter(char => op_class[0] == char.profession)
                                                    : ops.filter(char => op_class.includes(char.profession));
        if (op_branch.length) ops = ops.filter(char => {
            //add support for multiple subclass per operator

            var checksubclass = getBranchClass(char)
            if(Array.isArray(checksubclass)){
                var exist = false
                $.each(op_branch,function(key,v){
                    if(op_branch.includes(v)) exist = true
                })
                return exist
            }else{
                return op_branch.includes(checksubclass)
            }
        });

        console.log(op_rarity)
        // using query in a lambda is really awful. "sex" should be in chars, not chars2
        if (op_rarity.length)  ops = ops.filter(char => {
            return op_rarity.includes(char.rarity)
        })
        if (op_gender.length) ops = exclusive_gender ? ops.filter(char => op_gender[0] == query(db.chars2, "name_cn", char.name).sex)
                                                        : ops.filter(char => op_gender.includes(query(db.chars2, "name_cn", char.name).sex));
        if (op_tag.length) ops = exclusive_tag ? ops.filter(char => getTags(char).filter(tag => op_tag.includes(tag)).length == op_tag.length)
                                                : ops.filter(char => getTags(char).filter(tag => op_tag.includes(tag)).length > 0);
        if (op_faction.length) ops = exclusive_faction ? ops.filter(char => Object.values(char.mainPower).includes(op_faction[0]))
                                                        : ops.filter(char => [Object.values(char.mainPower), (char.subPower ?? []).map(a=>Object.values(a)).flat()].flat().includes(op_faction[0]))
        if (op_skill.length) ops = exclusive_skill ? ops.filter(char =>
                                                        char.skills.filter(skill =>
                                                            db.skills[skill.skillId].levels.filter(sp =>
                                                                op_skill[0] == SkillTypeConvert(sp.spData.spType)).length).length)
                                                    : ops.filter(char =>
                                                        char.skills.filter(skill =>
                                                            db.skills[skill.skillId].levels.filter(sp =>
                                                                op_skill.includes(SkillTypeConvert(sp.spData.spType))).length).length);
        if (op_ammo.length) ops =  ops.filter(char =>
                                                char.skills.filter(skill =>
                                                    db.skills[skill.skillId].levels.filter(lv =>
                                                        lv.durationType == "AMMO" || lv.durationType == 1).length).length)

        if ($("#filter-equip").hasClass("btn-primary")) ops = ops.filter(char=>Object.keys(db.uniequip.charEquip).includes(char.id))

        // SORTING
        ops = ops.sort((a, b) => sortFilter(getStat(a, "atk"), getStat(b, "atk"), "atk")    * 100000 * 10000 * 1000 + // def is never more than 1 000
                                 sortFilter(getStat(a, "def"), getStat(b, "def"), "def")    * 100000 * 10000 +        // maxHp is never more than 10 000
                                 sortFilter(getStat(a, "maxHp"), getStat(b, "maxHp"), "hp") * 100000 +                // dp cost is never more than 100
                                 sortFilter(getStat(a, "cost"), getStat(b, "cost"), "dp")   * 1000 +
                                 sortFilter(getStat(a, "blockCnt"), getStat(b, "blockCnt"), "block")   * 100 +
                                 sortFilter(a.rarity, b.rarity, "rarity") * 10 +
                                //  (db.names[getId(a)][lang].localeCompare(db.names[getId(b)][lang]))
                                 (b.appellation>a.appellation?-1 :+1)
                                 );

        ops.forEach(char => {
            totalRarity[char.rarity]=1
        });
        totalRarity = Object.keys(totalRarity).length
        // CONSTRUCTION
        var showfaction = false
        if(op_class.length>1||op_class.length==0)
        showfaction=true
        var rarity = -1
        var numrar=0
        // console.log($("#order-atk").hasClass("btn-enabled"))

        var isgrouped = israritygrouped
        if(
        $("#sort-atk").hasClass("btn-enabled")||
        $("#sort-def").hasClass("btn-enabled")||
        $("#sort-hp").hasClass("btn-enabled")||
        $("#sort-dp").hasClass("btn-enabled")||
        $("#sort-block").hasClass("btn-enabled")||
        $("#sort-rarity").hasClass("btn-disabled")){

            isgrouped = false
        }


        console.log(totalRarity)
        $("#selectedopclass").html(ops.map(char =>{
            var extrathing = ""
            if (rarity!=char.rarity&&isgrouped){
                rarity = char.rarity
                extrathing = `
                ${numrar!=0?"</div>":""}
                ${titledMaker(`
                ${titledMaker(``,"",`ak-rare-${rarity+1} ak-shadow`,"",`height:3px;width:calc(100% + 20px);margin:-28px -10px -10px -10px;padding:0px`)}
                <div style="margin-top:-15px">
                ${(`<i class="fa fa-star"></i>`).repeat((rarity+1))}
                </div>
                `,"",`op-rarity2-${rarity+1}`,"",`font-size:12px;height:20px;width:calc(100% + 20px);margin:-10px -10px -10px -10px;text-align:center;padding-top:0px`)}
                <div style="background:#333;padding-bottom:10px">
                `
                numrar+=1
            }
            var unreadable = query(db.unreadNameTL,"name",char.appellation).name_en
            var gamemode = query(db.chars2, "id", char.id).gamemode
            return `
            ${extrathing}
            <li class="selectop-grid ak-shadow" onclick="selectOperator('${getId(char)}')">
            <div class="op-image-grid">
                ${GetLogo(char)?`<div class="op-grid-faction"><img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/factions/${GetLogo(char)?GetLogo(char).toLowerCase():"none"}.png" title="${GetLogo(char)?GetLogoInfo(char).powerCode:"None"}"></div>`:""}
                ${gamemode=="BASE"?"":'<div class="op-grid-gamemode ' + gamemode +'">' + gamemode + '</div>'}
                <img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/${getId(char)}.png">
            </div>
            <div class="${char.appellation.length>12?char.appellation.length>16?"namesmaller":"namesmall":"name"} ak-font-novecento ak-center">${unreadable?`[${unreadable}]`:""} ${char.appellation}</div>
            <div class='selectopopgridline ak-rare-${char.rarity + 1}'></div>

            ${showfaction?`<div class='ak-showclass'><img loading='lazy' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/classes/class_${db.classes.find(search=>search.type_data==char.profession).type_en.toLowerCase()}.png'></div>`:""}
            ${op_branch.length!=1?`<div class='ak-showsubclass'><img loading='lazy' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/subclass/sub_${char.subProfessionId}_icon.png'></div>`:""}

            </li>`
        }).join(" "));

            //
    }

    function openOPZOOMmodal(){
        $('#opzoom').modal();
        $('#charazoom').css("margin","auto")
        $('#charazoom').css("margin-left","0px")
        $('#charazoom').css("width","100%")
        $('#charazoom').css("height","85vh")
        $('#charazoom').css("max-width","100%")
        $('#charazoom').css("max-height","100%")
        $('#charazoomslider').val(100);
        $('#charazoominput').val(100)
        var image = $('#tabs-opCG').children('.active').children('img').attr('src');
        ChangeZoomChara('',image);
    }
    function ChangeZoomChara(skinName, src=''){



        if(skinName != ''){
            $("#charazoom").attr("src","https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/characters/"+skinName+(sus && opdataFull.id == "char_298_susuro"?"sus":"")+".png");
        }else{
            $("#charazoom").attr("src",src);
        }
        $('#charazoom').modal('handleUpdate')
    }
    function selectOperator(opid, from = 'Selecting Operator From Browse'){
        attempt = 0
        skinsuffix = ""
        $("#opchoosemodal").modal('hide');

        if(spinewidgetcg){
            spinewidgetcg.pause()
        }
        if(opid){
            if (opid === "char_512_aprot") opid = "char_4025_aprot2";
            curropid = opid

            $("#chara-detail-container").show();
            console.log("SELECT OPERATOR");
            console.log(opid);
            $("#opname").val("");
            $('#operatorsResult').empty();
            $('#operatorsResult').hide();
            var opdata = query(db.chars2, "id", opid);
            var opdata2 = {[opid]:db.chars[opid]}
            var opcode = Object.keys(opdata2)[0]
            var gamemode = query(db.chars2, "id", opid, true, false).gamemode
            console.log(gamemode)

            var opKey = ""
            $.each(opdata2,function(key, v){
                v['id'] = key;
                console.log(v);
                opdataFull = v;
                opKey = key;
                return false
            });


            console.log(opKey)

            console.log(opdataFull.appellation)
            gtag('event', 'Selecting Operator', {
                'event_category' : 'Operator Details',
                'event_label' : opdataFull.appellation ,
                'value' : from
            });

            //get globaltoken early for tokenchibi (L:1465-)
            defaulttoken = null
            $.each(opdataFull.talents, (_, t) => {
                if (!defaulttoken && t.candidates[0].tokenKey){
                    defaulttoken = t.candidates[0].tokenKey
                    return false
                }
            })
            globaltoken = defaulttoken?defaulttoken:opdataFull.skills[0]?opdataFull.skills[0].overrideTokenKey:null
            globalskill = 0

            tokenname   = globaltoken
            currskin    = opcode

            const url = new URL(window.location.href)
            const urlVars = url.searchParams
            var unreadable = query(db.unreadNameTL,"name",opdataFull.appellation)
            var correctname = (unreadable?unreadable.name_en.replace(/ /g,"_"):opdataFull.appellation.replace(/ /g,"_"))
            opapp = correctname
            gmapp = gamemode

            if(urlVars.get("opname") !== correctname || urlVars.get("gamemode") !== gamemode){
                urlVars.set("opname", correctname);

                if(gamemode != "BASE") urlVars.set("gamemode", gamemode)
                else urlVars.delete("gamemode")

                if (from == "cookies") history.replaceState(null, '', url);
                else history.pushState(null, '', url);
            }
            
            if(opKey == AmiyaCaster){
                $('#class-change-1').show()
                $('#class-change-2').show()
                switch (Amiyacurrclass){
                    case 'caster' :
                            opcode = AmiyaCaster
                            opKey = opcode
                            opdataFull.id = opcode
                            currskin = opcode
                            break;
                    case 'guard' :
                            opcode = AmiyaGuard
                            opKey = opcode
                            opdataFull = db.charpatch.patchChars[AmiyaGuard]
                            opdataFull.id = opcode
                            currskin = opcode
                            break;
                    case 'medic' :
                            opcode = AmiyaMedic
                            opKey = opcode
                            opdataFull = db.charpatch.patchChars[AmiyaMedic]
                            opdataFull.id = opcode
                            currskin = opcode
                            break;
                    default:
                        $('#class-change-1').show()
                        $('#class-change-2').show()
                }
            }else{
                ChangeSTypeHTML(1,"guard")
                ChangeSTypeHTML(2,"medic")
                $('#class-change-1').hide()
                $('#class-change-2').hide()
                Amiyacurrclass='caster'
            }


            console.log(opdataFull)
            currVoiceID = opdataFull.id
            var linkconvert = opdataFull.appellation.replace(/[ ']/g,"-").toLowerCase()
            //var guidelink = db.sanitygone[opKey];
            console.log(linkconvert)
            //console.log(guidelink)

            /*if(guidelink){
                $("#sanitygone").show()
                $("#sanitylink").attr("href",`https://sanitygone.help${guidelink}`)
                $("#sanitylink").attr("title",`${opdataFull.appellation} Sanity;Gone guide link`)
            }else{
                $("#sanitylink").attr("href",`https://sanitygone.help/operators/`)
                $("#sanitygone").hide()
            }*/

            // use opdata to get the operator data based on tl-akhr.json
            // use opdataFull to get the operator data based on character_table.json

            // Get operator elite skins
            var skinList = db.skintable.buildinEvolveMap[opdataFull.id];
            var extraSkin = []
            Object.keys(db.skintable.charSkins).forEach(element => {
                // console.log(element)
                if(element.startsWith(opdataFull.id)){
                    if(db.skintable.charSkins[element].displaySkin.skinName){
                        extraSkin.push(db.skintable.charSkins[element])
                    }

                }
            });
            // console.log(extraSkin)
            // console.log(skinList);


            var tabbtn = [];
            var tabbtn2 = [];
            var tabcontent = [];
            var tabcontent2 = [];
            var zoombtn = [];

            $("#spine-frame-op").fadeOut(10)
            $("#tabs-opCG").fadeIn(10)
            $("#elite-sidenav").empty();
            $("#tabs-opCG").empty();
            $("#elite-topnav").empty();
            $("#tabs-opData").empty();
            $("#op-taglist").empty();
            $("#op-faction-btn").empty().attr("onclick","")
            $("#op-faction-sub").empty().css("display","none")

            var logo = GetLogo(opdataFull)

            if(logo){
                var faction_all = [logo.replace("logo_", "")]
                var faction_sub = Object.values(opdataFull.mainPower).filter(k => k)
                var faction_hidden = (opdataFull.subPower ?? []).map(a => Object.values(a)).flat().filter(k => k)
                var faction_sub_text = ""
                
                faction_sub.pop()
                
                if (faction_sub.length){
                    faction_sub_text += `<div class="op-sub-faction" ${!faction_hidden.length?'style="width:100%"':""}>Sub Faction :`
                    for(faction of faction_sub){
                        if(!faction_all.includes(faction)){
                            faction_sub_text += `<div>
                                                    <div id="op-faction-image" style="display: inline;">
                                                        <img loading='lazy' id="op-faction-image3" src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/factions/logo_${faction}.png">
                                                    </div>
                                                    <div id="op-faction-text" style="display: inline;">
                                                        ${db.handbookTeam[faction]?db.handbookTeam[faction].powerCode:""}
                                                    </div>
                                                </div>`
                            faction_all.push(faction)
                        }
                    }
                    faction_sub_text += `</div>`
                }
                if (faction_hidden.length){
                    faction_sub_text += `<div class="op-hid-faction" ${!faction_sub.length?'style="width:100%"':""}>Hidden Faction :`
                    for(faction of faction_hidden){
                        if(!faction_all.includes(faction)){
                            faction_sub_text += `<div>
                                                    <div id="op-faction-image" style="display: inline;">
                                                        <img loading='lazy' id="op-faction-image3" src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/factions/logo_${faction}.png">
                                                    </div>
                                                    <div id="op-faction-text" style="display: inline;">
                                                        ${db.handbookTeam[faction]?db.handbookTeam[faction].powerCode:""}
                                                    </div>
                                                </div>`
                        }
                    }
                    faction_sub_text += `</div>`
                }
                $("#op-faction").attr("src","https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/factions/"+logo.toLowerCase()+".png");

                $("#op-faction-btn").html(`
                    <div id="op-faction-image" style="display: inline;">
                        <img id='op-faction-image2' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/factions/${logo.toLowerCase()}.png'>
                    </div>
                    <div id="op-faction-text">
                        ${GetLogoInfo(opdataFull).powerCode}
                    </div>
                    ${faction_sub_text?'<i class="fas fa-caret-down"></i>':""}`)

                if (faction_sub_text) {
                    $("#op-faction-btn").attr("onclick", 'SlideToggler2("op-faction-sub", $(this))')
                    $("#op-faction-sub").html(faction_sub_text)
                }
            }else{
                $("#op-faction").attr("src","https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/factions/none.png")
            }

            charName = opcode;
            chibiName = opcode
            globalelite = 0
            globallevel = [1,1,1]
            chibipers = Chibi_per()
            console.log(chibipers)
            if(chibipers == 'build') chibiName = "build_" + chibiName
            console.log(chibiName)
            folder = `https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/spineassets/${chibitype}/${charName}/${chibipers}/`
            // if(spinewidget)


            if(loadchibi){
                LoadAnimation()
                LoadAnimationToken()
                // $("#spine-frame").fadeIn(10)
            }
            else $("#spine-frame").hide()


            for (var i = 0; i < opdataFull.phases.length; i++) {
                var l = opdataFull.phases.length;

                var dynextra
                if(skinList){
                    if(skinList[i]){
                        var currentskin = db.skintable.charSkins[skinList[i]]
                        console.log(currentskin)
                        if(currentskin&&currentskin.dynIllustId){
                            dynextra=currentskin.dynIllustId
                        }

                    }
                }
                tabbtn[l-i] = $(`
                <li class='nav-item'>
                ${dynextra?`<button class='btn tabbing-btns tabbing-btns-middle' data-toggle='pill' style='width:24px;height:25px;display:inline-block' title="Show Animated CG" onClick='ShowDynamic("${opcode}")'>
                        <i class="fas fa-play-circle"></i>
                    </button><button class='btn tabbing-btns tabbing-btns-middle' style='width:19px;height:25px;display:inline-block' title="Play Interact Animation" onClick='CreateAnimation(spinewidgetcg,["Interact","Idle"])'>
                        <i class="fas fa-hand-point-down"></i>
                    </button><button class='btn tabbing-btns tabbing-btns-middle' style='width:19px;height:25px;display:inline-block' title="Play Special Animation" onClick='CreateAnimation(spinewidgetcg,["Special","Idle"])'>
                        <i class="far fa-star"></i>
                    </button>
                    `:""}

                    <button class='btn tabbing-btns tabbing-btns-middle ${l==0?"active":""}' data-toggle='pill' style='${dynextra?"width:62px;":""}height:30px' href='#opCG_${i}_tab' onClick='ChangeSkin("${i}")'>
                        <img style='max-height:30px' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/${i}-s.png'>
                    </button>
                </li>`);

                //CreateAnimation(spinewidget,"Relax")
                tabbtn2[i] = $(`
                <li class='nav-item'>
                    <a class='btn tabbing-btns horiz-small nav-link ${i==0?"active":""} tablink' data-toggle='pill' onclick='UpdateElite(${i})'href='#elite_${i}_tab'>
                        <img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/${i}.png" style="width:20px;margin:-12px 0px -6px 0px" title="Elite${i}">E${i}
                    </a>
                </li>`);

                // if(i == 0){
                //     if(l == 1){
                //         tabbtn[l] = $("<li class='nav-item' style='height:30px'><button class='btn tabbing-btns tabbing-btns-middle active' style='height:30px'>"
                //             + "<img style='max-height:30px' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/0-s.png' data-toggle='pill' href='#opCG_0_tab'></button></li>");
                //         tabbtn2[i] = $(`<li class='nav-item'><a class='btn tabbing-btns horiz-small nav-link active tablink' data-toggle='pill' onclick='UpdateElite(0)' href='#elite_0_tab'>Non-Elite</a></li>`);
                //     }else{
                //         tabbtn[l] = $(`<li class='nav-item'><button class='btn tabbing-btns tabbing-btns-middle active' data-toggle='pill' style='height:30px' href='#opCG_${i}_tab' onClick='ChangeSkin("${opcode}")'>`
                //                             + "<img style='max-height:30px' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/0-s.png'></button></li>");
                //         tabbtn2[i] = $(`<li class='nav-item'><a class='btn tabbing-btns horiz-small nav-link active tablink' data-toggle='pill' onclick='UpdateElite(${i})'href='#elite_${i}_tab'><img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/0.png" style="width:20px;margin:-12px 0px -6px 0px" title="Elite0">E0</a></li>`);
                //     }
                // } else if( i == l-1 ){
                //     tabbtn[0] = $(`<li class='nav-item' style='height:30px'><button class='btn tabbing-btns tabbing-btns-middle'  style='height:30px' data-toggle='pill' href='#opCG_${i}_tab' onClick='ChangeSkin("${opcode}")'>`
                //                             + "<img style='max-height:30px' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/"+i+"-s.png'></button></li>");
                //     tabbtn2[i] = $(`<li class='nav-item'><a class='btn tabbing-btns horiz-small nav-link tablink' data-toggle='pill' style='height:30px' onclick='UpdateElite(${i})' href='#elite_${i}_tab'><img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/${i}.png" style="width:20px;margin:-12px 0px -6px 0px" title="Elite${i}">E${i}</a></li>`);
                // }else{
                //     tabbtn[l-i] = $(`<li class='nav-item' style='height:30px'><button class='btn tabbing-btns tabbing-btns-middle'  style='height:30px' data-toggle='pill' href='#opCG_${i}_tab' onClick='ChangeSkin("${opcode}")'>`
                //                             + "<img style='max-height:30px' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/"+i+"-s.png'></button></li>");
                //     tabbtn2[i] = $("<li class='nav-item'><a class='btn tabbing-btns horiz-small nav-link tablink' data-toggle='pill' style='height:30px' onclick='UpdateElite("+i+")' href='#elite_"+i+"_tab'>Elite "+i+"</a></li>");
                // }

                var skindata;
                if(skinList){
                    if(!(skinList[i] in db.skintable.charSkins)){
                        skindata = db.skintable.charSkins[skinList[i-1]];
                    }else{
                        skindata = db.skintable.charSkins[skinList[i]];
                    }
                }
                if(skindata){
                    console.log(skindata)
                    zoombtn.push($(`<button class="btn ak-c-black btn-dark" style="margin:2px;padding:2px; height: 50px; width: 50px;" onclick="ChangeZoomChara('${skindata.portraitId}')"><img src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/${i}-s.png'></button>`))
                    if(i == 0){
                        $("#charazoom").attr("src","https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/characters/"+skindata.portraitId+(sus && opdataFull.id == "char_298_susuro"?"sus":"")+".png");
                        $('#charazoom').modal('handleUpdate')

                        tabcontent.push($("<div class='tab-pane container active' id='opCG_0_tab'>"
                            +"<img class='chara-image' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/characters/"+skindata.portraitId+(sus && opdataFull.id == "char_298_susuro"?"sus":"")+".png'>"
                            +"</div>"));
                    }else{
                        tabcontent.push($("<div class='tab-pane container' id='opCG_"+i+"_tab'>"
                            +"<img class='chara-image' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/characters/"+skindata.portraitId+(sus && opdataFull.id == "char_298_susuro"?"sus":"")+".png'>"
                            +"</div>"));
                    }
                }

                if(AmiyaPatchID.includes(opKey)){
                    zoombtn.push($(`<button class="btn ak-c-black btn-dark" style="margin:2px;padding:2px; height: 50px; width: 50px;" onclick="ChangeZoomChara('`+opKey+`')"><img src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/${i}-s.png'></button>`))
                    if(i == 0){
                        $("#charazoom").attr("src","https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/characters/"+opKey+"_2.png");
                        $('#charazoom').modal('handleUpdate')

                        tabcontent.push($("<div class='tab-pane container active' id='opCG_0_tab'>"
                            +"<img class='chara-image' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/characters/"+opKey+"_2.png'>"
                            +"</div>"));
                    }else{
                        tabcontent.push($("<div class='tab-pane container' id='opCG_"+i+"_tab'>"
                            +"<img class='chara-image' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/characters/"+opKey+"_2.png'>"
                            +"</div>"));
                    }
                }


                var elitehtml = getEliteHTML(i,opdataFull);
                tabcontent2.push(elitehtml);
            }


            if(extraSkin.length>0){
                let dropdowntab = []

                for(var i=0;i<extraSkin.length;i++){

                    // var currskingroupsplit = extraSkin[i].displaySkin.skinGroupId.split("#")
                    // var currskingroup = `${currskingroupsplit[0]}#${currskingroupsplit[1]}`
                    var currskingroup = extraSkin[i].displaySkin.skinGroupId
                    console.log(extraSkin[i]);
                    console.log(currskingroup)
                    zoombtn.push($(`<button class="btn ak-c-black btn-dark" style="margin:2px;padding:2px; height: 50px; width: 50px;" onclick="ChangeZoomChara('${encodeURIComponent(extraSkin[i].portraitId)}')">
                    <img style="max-width:40px;max-height:40px;" src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/${encodeURIComponent(extraSkin[i].avatarId)}${sus && opdataFull.id == "char_298_susuro"?"sus":""}.png'>
                    </button>`))

                    tabcontent.push($(`
                    <div class='tab-pane container' id='opCG_S${i}_tab'>
                    <img class='chara-image' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/characters/${encodeURIComponent(extraSkin[i].portraitId)}${sus && opdataFull.id == "char_298_susuro"?"sus":""}.png'>
                    </div>
                    `))

                    dropdowntab.push(`
                        <li class='nav-item' ${i==0?`style="margin-top:5px"`:""}>
                        ${extraSkin[i].dynIllustId?`
                            <button class='btn tabbing-btns tabbing-btns-middle' data-toggle='pill' style='width:24px;height:25px;display:inline-block' title="Show Animated CG" onClick='ShowDynamic("${opcode}",true,"${encodeURIComponent(extraSkin[i].dynIllustId)}")'>
                                <i class="fas fa-play-circle"></i>
                            </button><button class='btn tabbing-btns tabbing-btns-middle' style='width:19px;height:25px;display:inline-block' title="Play Interact Animation" onClick='CreateAnimation(spinewidgetcg,["Interact","Idle"])'>
                                <i class="fas fa-hand-point-down"></i>
                            </button><button class='btn tabbing-btns tabbing-btns-middle' style='width:19px;height:25px;display:inline-block' title="Play Special Animation" onClick='CreateAnimation(spinewidgetcg,["Special","Idle"])'>
                                <i class="far fa-star"></i>
                            </button>
                        `:""}

                        <a class="btn tabbing-btns tabbing-btns-middle" style="${extraSkin[i].dynIllustId?"width:62px":""}" data-toggle='pill' href='#opCG_S${i}_tab' onClick='ChangeSkin("${extraSkin[i].portraitId}","","${extraSkin[i].skinId}"${extraSkin[i].spIllustId?`,"#opCG_S${i}_tab"`:""})'>
                            <div style="display:inline-block;height:100%;vertical-align:middle;"></div>
                            <img class='skinimage' style="max-width: 48px;max-height: 48px;margin-left:-5px;margin-top:1px" src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/${encodeURIComponent(extraSkin[i].avatarId)}${sus && opdataFull.id == "char_298_susuro"?"sus":""}.png'>
                        </a></li>
                        `)
                }

                tabbtn.push(`

                    ${dropdowntab.join("")}

                `)

            }
            tabbtn.push($(`<button type="button" class="btn tabbing-btns  tabbing-btns-middle ak-btn" style="width:50px;height:50px;margin-top:5px;" onclick="openOPZOOMmodal()"><span style="font-size: 1.5em" class="fa fa-search-plus"></span></button>`))
            tabbtn.push($(`<button type="button" class="btn tabbing-btns tabbing-btns-middle ak-btn" style="width:50px;height:50px" data-toggle="modal" data-target="#opstory">
            <div>
                <img class='audioprofilebutton' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/story/profile.png" style="max-width:40px;max-height:40px">
                <div class="btn-story-header" style="border-radius:0px">Profile</div>
            </div>
            </button>`))

            tabbtn.push($(`<button type="button" class="btn tabbing-btns ak-btn  tabbing-btns-middle" style="width:50px;height:50px" data-toggle="modal" data-target="#opaudio" onclick="GetAudio()">
            <div>
                <img class='audioprofilebutton' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/story/audio.png" style="max-width:40px;max-height:40px">
                <div class="btn-story-header">Audio</div>
            </div>
            </button>`))
            tabbtn.push($(`<button type="button" class="btn tabbing-btns tabbing-btns-middle ak-btn" style="width:50px;height:18px" data-toggle="modal" data-target="#opsfx" onclick="GetSFX(opdataFull)">
            <div>
                <div class="btn-story-header" style="margin-top: 0px;">SFX</div>
            </div>
            </button>`))

            $("#charazoom-button").html(zoombtn)
            $("#elite-sidenav").html(tabbtn);
            $("#tabs-opCG").html(tabcontent);
            $("#elite-topnav").html(tabbtn2);
            $("#tabs-opData").html(tabcontent2);

            for (var i = 0; i < opdataFull.phases.length; i++) {
                EliteStatsDisplay(1,i);
            }

            var unreadable = query(db.unreadNameTL,"name",opdata.name_en).name_en
            // $("#op-nameTL").html(opdata['name_'+lang]);
            // $("#op-nameREG").html("["+opdata['name_'+reg]+"]");
            $("#op-nameTL").removeClass("smallopname");
            $("#op-nameREG").removeClass("smallopname");
            if(opdataFull.appellation.length+opdataFull.name.length>16){
                $("#op-nameTL").addClass("smallopname");
                $("#op-nameREG").addClass("smallopname");
            }

            $("#op-nameTL").html(opdataFull.appellation);
            $("#op-nameREG").html(opdataFull.name);

            $("#op-displaynum").html(`${opdataFull.displayNumber?`${opdataFull.displayNumber} | `:""}<a id="copy-id" onclick="clickID()">${opdataFull.id.split("_")[1]}</a> | ${opdataFull.id.split("_")[2]}`)
            if(unreadable){
                $("#op-nameRead").html(`[ ${unreadable} ]`);
            }else{
                $("#op-nameRead").empty()
            }
            var gender = query(db.gender,"sex_cn",opdata.sex);
            $("#op-gender").removeClass(`gender-male`)
            $("#op-gender").removeClass(`gender-female`)
            $("#op-gender").html(`<i class="fas fa-${gender['sex_'+lang].toLowerCase()}"></i> ${gender['sex_'+lang]}`)
            $("#op-gender").addClass(`gender-${gender['sex_'+lang].toLowerCase()}`)
            var position = query(db.tags,"tag_cn",opdataFull.position);
            $("#op-position").html(position['tag_'+lang],`Position`)



            var type = query(db.classes,"type_data",opdataFull.profession);
            $("#op-classImage").attr("src","https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/classes/black/icon_profession_"+type['type_'+lang].toLowerCase()+"_large.png")
            $("#op-className").html(type['type_'+lang])
            $("#op-subclassImage").attr("src",`https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/subclass/sub_${opdataFull.subProfessionId}_icon.png`)
            var capsubclass = opdataFull.subProfessionId.charAt(0).toUpperCase()+opdataFull.subProfessionId.slice(1)
            if(db.tlsubclass.subclass[opdataFull.subProfessionId]){
                var currsub = db.tlsubclass.subclass[opdataFull.subProfessionId]
                if(currsub.en && currsub.en.length>0){
                    capsubclass = currsub.en
                }else if(currsub.tl && currsub.tl.length>0){
                    capsubclass = currsub.tl
                }else if(currsub.name){
                    capsubclass = currsub.name
                }
            }
            $("#op-subclassName").html(capsubclass)
            $("#op-subclassName").addClass("subclasssmall")

            //TRAIT MAKING
            $("#op-atktype").html(GetTrait(opdataFull.description,opdataFull.trait))

            $("#op-rarity").empty();
            $("#op-rarity").attr("class","op-rarity-"+(opdataFull.rarity+1))
            $("#op-trust").html(GetTrust(opdataFull))

            var potentials = GetPotential(opdataFull)
            var potentialist = []
            potentialist.push(`<div style="height:4px"></div>`)
            for(i=0;i<potentials.length;i++){
                potentialist.push(`<div style="font-size:13px;padding:1px;margin-left:-6px;color:#DDD;vertical-align:bottom"><img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/potential/${i+2}.png" style="margin-top:-4px;width:20px;background:#222;border-radius:25%;padding:2px"> ${potentials[i]}</div>`)
            }
            // console.log(potentials)
            if (opdataFull.talents){
                GetTalent(opKey,opdataFull)
            }else{
                $("#op-talentlist").html("")
            }

            if (gmapp == "SO"){
                GetMastery(opid)
            }else{
                $("#op-masterlist").html("")
            }

            if(potentials.length>0){
                $("#op-potentialist").html(titledMaker(potentialist.join(""),"Potentials"))
            }else{
                $("#op-potentialist").empty()
            }
            for (var i = 0; i < (opdataFull.rarity+1); i++) {
                $("#op-rarity").append("<i class='fa fa-star'></i>");
            }
            var tags_html = [];
            $.each(opdataFull.tagList,function(_,v){
                var tag = query(db.tags,"tag_cn",v);
                if(tag){
                    var tagReg = tag['tag_'+reg];
                    var tagTL = tag['tag_'+lang];
                    tags_html.push(`
                        ${titledMaker2(tagTL,"")}
                    `)
                    // tags_html.push("<li style=\"list-style-type:none; padding-bottom: 10px;\"><button readonly type=\"button\" class=\"btn btn-sm ak-shadow-small ak-btn btn-secondary btn-char my-1\" data-toggle=\"tooltip\" data-placement=\"top\" title=\""+ tagReg +"\">" +
                    //         (tagReg == tagTL ? "" : '<a class="ak-subtitle2" style="font-size:11px;margin-left:-9px;margin-bottom:-15px">'+tagReg+'</a>') +tagTL + "</button></li>");
                }
            });
            var newtags = `<div style=''>${tags_html.join("")}</div>`
            // $("#op-potentialist").html(titledMaker(potentialist.join(""),"Potentials"))
            $("#op-taglist").append(newtags);


            GetRiic(opdata2)
            // console.log(charaRiic)


            //Story

            if(db.handbookInfo.handbookDict[opdataFull.id]|| AmiyaPatchID.includes(opdataFull.id)){
                GetStory(opdataFull)
            }else{
                $("#opstorycredits").html(``)
                $("#opstorycontent").html(`<div class="row storyrow"> </div>`)
                update_illustrator()
                $('#info-voiceactor').html(`
                                            <div class="voiceactor-None">
                                                <div id="lang-voiceactor-None" class="btn-infoleft ak-shadow">
                                                    <i class="fas fa-microphone-alt" title="Voice Actor">
                                                    </i>
                                                </div>
                                                <div id="name-voiceactor-None" class="btn-inforight">
                                                    -
                                                </div>
                                            </div>
                                            `)
            }

            $('#opaudiocontent').empty()
            $('#opsfxcontent').empty()
            $('#opaudiotranslator').empty()
            $('#opaudioproofreader').empty()
            ///////////////////////////////////////////////// SKILLS SECTION //////////////////////////////////////////////////

            $("#skill-tabs").empty();
            $("#skill-contents").empty();
            skillValue = Array.from({ length: opdataFull.skills.length}, () => 0)
            $.each(opdataFull.skills,function(i,v){
                var maxSkillLevel = opdataFull.skills[i].levelUpCostCond.length;
                var skillId = opdataFull.skills[i].skillId;
                var skillData = db.skills[skillId];
                var skillname
                var tables = "";
                var grid = ""
                var grid2 = "";
                //console.log(skillData)
                // var materialList2 = []
                $.each(skillData.levels,function(i2,v2){
                    // console.log(v2['spData'].spCost);
                    var currSkill = skillData.levels[i2]
                    skillname = db.skillsEN[skillId]?db.skillsEN[skillId].levels[0].name:db.skillsTL[skillId]?db.skillsTL[skillId].name:currSkill.name;
                    // if (db.skillsEN[skillId]&&db.skillsEN[skillId].levels[i2])skillname = db.skillsEN[skillId].levels[i2].name
                    var skilldesc = getSkillDesc(skillId,i2);
                    var skillMat = GetSkillCost(i2,i,opdataFull)
                    var force
                    var materialist = []
                    if(skillMat){
                        skillMat.forEach(mat => {
                            materialist.push(CreateMaterial(mat.id,mat.count))
                        });
                    }
                    var materialHtml =``
                    if(i2 >= 7){
                        var time = opdataFull.skills[i].levelUpCostCond[i2-7].lvlUpTime
                        var condLeveling = opdataFull.skills[i].levelUpCostCond[i2-7].unlockCond
                        var condUnlocking = opdataFull.skills[i].unlockCond
                        var phase = Math.max(PhaseConvert(condLeveling.phase),PhaseConvert(condUnlocking.phase))
                        var level = Math.max(condLeveling.level,condUnlocking.level)
                        var SO_condUnlocking = gmapp != "SO"?"":db.special_operator[opid].unlock["skill" + (i + 1).toString()][i2 - 7]
                        materialHtml = `
                                        <div style="text-align:center;background:#222">
                                            ${(i2 == 0?"Unlock":"Rank Up")} Requirements
                                        </div>
                                        ${SO_condUnlocking == ""?"":
                                            `<div class = "SO-Unlock">
                                                ${ChangeDescriptionColor2(SO_condUnlocking)}
                                            </div>`}
                                        <div style="margin-top:15px">
                                            ${titledMaker((phase > 0?"Elite " + phase + " ":"") + (level > 0?"Level " + level:""), "Level Required")}
                                            ${gmapp == "SO"?"":titledMaker(time/60/60 + " Hour", "Time Required")}
                                        </div>
                                        ${(materialist.length > 0?materialist.join(""):"")}`
                    }else{
                        var condLeveling = (opdataFull.allSkillLvlup[i2 - 1]?opdataFull.allSkillLvlup[i2 - 1].unlockCond:{phase:"TIER_0",level:0})
                        var condUnlocking = opdataFull.skills[i].unlockCond
                        var phase = Math.max(PhaseConvert(condLeveling.phase), PhaseConvert(condUnlocking.phase))
                        var level = Math.max(condLeveling.level,condUnlocking.level)
                        var SO_condUnlocking = gmapp != "SO"?"":db.special_operator[opid].unlock["skill"][i2]
                        materialHtml = `
                                        <div style="text-align:center;background:#222">
                                            ${(i2 == 0?"Unlock":"Rank Up")} Requirements
                                        </div>
                                        ${SO_condUnlocking == ""?"":
                                            `<div class = "SO-Unlock">
                                                ${ChangeDescriptionColor2(SO_condUnlocking)}
                                            </div>`}
                                        <div style="margin-top:15px">
                                            ${titledMaker((phase > 0?"Elite " + phase + " ":"") + (level > 0?"Level " + level:""), "Level Required")}
                                        </div>
                                        ${(materialist.length > 0?materialist.join(""):"")}`
                    }

                    if(v2.rangeId)grid = rangeMaker(v2.rangeId)

                    var skillblacklistrange = [
                        "skchr_tachak_2"
                    ]

                    if(skillblacklistrange.includes(v2.prefabId)){
                        grid = ""
                    }

                    var spDuration
                    var spDurType
                    var spDurationName
                    var spType = (v2.spData.spType)
                    var spTypeHtml = ""
                    switch (spType){
                        case "INCREASE_WITH_TIME": spTypeHtml = "Auto Recovery"; break;
                        case "INCREASE_WHEN_ATTACK": spTypeHtml = "Offensive Recovery"; break;
                        case "INCREASE_WHEN_TAKEN_DAMAGE": spTypeHtml = "Defensive Recovery"; break;
                        case 8: spTypeHtml = "Passive"; break;
                        default: spTypeHtml = spType; break;
                    }

                    if(v2.duration > 0){
                        spDuration = v2.duration + " Seconds"
                        spDurType = "Number"
                        spDurationName = "Duration"
                    }else if(TRUE_INFINITY.includes(skillId)){
                        spDuration = "Infinite"
                        spDurType = "Infinite"
                        spDurationName = "Duration"
                    }else if(v2.durationType == "AMMO"){
                        spDuration = "Ammo-based"
                        spDurType = "Ammo-based"
                        spDurationName = ""
                    }else{
                        spDuration = "Instant Attack"
                        spDurType = "Instant"
                        spDurationName = ""
                    }

                    var skilldetails =[]
                    // console.log(skillname)
                    // console.log(skillData.levels[i2])
                    skillData.levels[i2].blackboard.forEach(skillinfo => {
                        // console.log(skillinfo)
                        var skilljson = {}
                        skilljson.name = db.effect[skillinfo.key]?db.effect[skillinfo.key]:skillinfo.key
                        skilljson.key = skillinfo.key
                        skilljson.value = skillinfo.valueStr?["range_id", "projectile_range", "attack@projectile_range"].includes(skillinfo.key)?(skillinfo.valueStr + rangeMaker(skillinfo.valueStr)):skillinfo.valueStr:skillinfo.value

                        skilldetails.push(skilljson)
                        if(skillinfo.key=="force"||skillinfo.key=="base_force_level"||skillinfo.key=="attack@force") force= skillinfo.value
                        if(v2.duration == -1){
                            if(["duration", "projectile_delay_time", "max_duration"].includes(skillinfo.key)){
                                if (["skchr_liskam_1"].includes(skillId)){
                                    spDuration = skillinfo.value + " Seconds"
                                    spDurType = "Number"
                                    spDurationName = "Duration"
                                }else if (spDuration != "Infinite"){
                                    spDuration = skillinfo.value;
                                    spDurationName = "Target Effect Duration"
                                }
                            }
                        }
                        if(skillinfo.key == "ability_range_forward_extend"){
                            allrange = new Set(opdataFull.phases.map(phase => phase.rangeId))
                            if (allrange.size - 1){
                                if (i===2 || i2 + 1 >= 8) grid = rangeMaker(opdataFull.phases[2].rangeId, true, skillinfo.value, "E2")
                                else if (i===1 || i2 + 1 >= 5) grid = rangeMaker(opdataFull.phases[Math.max(1, globalelite)].rangeId, true, skillinfo.value, "E" + Math.max(1, globalelite))
                                else grid = rangeMaker(opdataFull.phases[globalelite].rangeId, true, skillinfo.value, "E" + globalelite)
                            }else{
                                grid = rangeMaker(opdataFull.phases[i].rangeId, true, skillinfo.value)
                            }
                        }
                        if(v2.prefabId=="skchr_fartth_3"){
                            grid2 = `
                            <div class="rangelongtable">${rangeMaker("ft",false,200)}</div>`
                        }
                    });
                    // console.log(skilldetails)
                    switch (force) {
                        case -1: force = "Very Small [-1]";break;
                        case 0: force = "Small [0]";break;
                        case 1: force = "Medium [1]";break;
                        case 2: force = "Large [2]";break;
                        case 3: force = "Huge [3]";break;
                        case 4: force = "Extreme [4]";break;
                    }
                    // console.log(currSkill)
                    var skillType = ""
                    switch(currSkill.skillType){
                        case "PASSIVE": skillType = "Passive"; break;
                        case "MANUAL": skillType = "Manual"; break;
                        case "AUTO": skillType = "Auto"; break;
                    }
                    console.log(currSkill.skillType)
                    var skillType = titledMaker(skillType, "Activation", `skillType-${currSkill.skillType}`)
                    var spTypeHtml = (currSkill.skillType == 0?"":titledMaker(spTypeHtml, "SP Type", `spType-${spType}`))
                    // console.log(materialList2)
                    // console.log(parseInt(v2.duration)>0)
                    //skilltype
                    //0 = on deploy
                    //1 = manual
                    //2 = auto
                    tables +=`<table id='skill${i}level${i2}stats' class='${lefthand=="true"?"left-hand":""} skillstats ${(i2!=0 ? '' : 'active')}'>
                             <tr >
                                <td colspan='${grid?5:4}'>${spTypeHtml}${skillType}${titledMaker(spDuration,spDurationName,`spDuration-${spDurType}`)}</td>
                            </tr>
                            <tr style="height:10px"></tr>
                            <tr>
                                <td colspan='${grid?3:2}' class='skilldesc'>${skilldesc}</td>
                            </tr>
                            `

                    var detailtable = []
                    if(skilldetails.length>0){
                        var skillhtmldetail = ""

                        skilldetails.forEach(currdetails => {

                            skillhtmldetail+=`
                            <div style="background:#444;margin:4px;padding:2px;padding-top:8px;border-radius:2px;color: #999999">
                                    ${titledMaker2(currdetails.name,currdetails.key)}  ${currdetails.value}
                            </div>`
                        });
                        detailtable = `<button id='skilldetailtitle' class='btn btn-sm btn-block ak-btn' onclick='SlideToggler("skilldetailcontent",$(this))'style="color:#fff;text-align:center;background:#222;padding:2px">Skill Details <i class="fas fa-caret-down"></i></button>
                            <div id='skilldetailcontent' class="ak-shadow skilldetailcontent" style="display:none;margin-bottom:8px;padding-top:10px;padding:2px;background:#666">
                                ${skillhtmldetail}
                            </div>
                        </div>`
                    }else{
                        detailtable=""
                    }

                    if(grid){
                        tables+=
                        `
                            <tr>
                                <td>
                                    <div class="skill-detail-grid">
                                        <div id="skill${i}lv${i2}grid" class="skill-grid">
                                                ${grid?grid:""}
                                        </div>
                                        <div class="skill-grid-num">
                                            <div>${titledMaker(v2['spData'].spCost,opdataFull.id=="char_4141_marcil"?"Max Mana":"SP Cost")}</div>
                                            <div>${titledMaker(v2['spData'].initSp,opdataFull.id=="char_4141_marcil"?"Initial Mana":"Initial SP")}</div>
                                            <div>${force!=undefined?`${titledMaker(force,"Force Level")}`: ""}</div>
                                        </div>
                                    </div>
                                </td>
                            </tr>
                            ${detailtable==""?"":`<tr><td colspan=3>${detailtable}</td></tr>`}
                            <tr>
                                <td colspan=3> ${materialHtml} </td>
                            </tr>
                        </table>
                        `
                    }else{
                        var extrastuff = `
                        <tr style="background: #444;text-align:center">
                            <td colspan=4>
                                <div id="skill${i}lv${i2}grid" class="skill-grid" style="text-align:center">
                                        ${grid2?grid2:""}
                                </div>
                            </td>
                        </tr>
                        <tr style="background: #444;text-align:center">
                            <td colspan=4>
                                Range
                            </td>
                        </tr>
                        <tr style="height:10px"></tr>
                        `
                        tables+=
                        `
                            <tr style="height:10px"></tr>
                            ${grid2?extrastuff:""}
                            <tr>
                                <td>
                                    ${titledMaker(v2['spData'].spCost,opdataFull.id=="char_4141_marcil"?"Max Mana":"SP Cost")}
                                    ${titledMaker(v2['spData'].initSp,opdataFull.id=="char_4141_marcil"?"Initial Mana":"Initial SP")}
                                    ${force!=undefined?`${titledMaker(force,"Force Level")}`: ""}
                                </td>
                            </tr>

                            ${detailtable==""?"":`<tr><td colspan=4>${detailtable}</td></tr>`}
                            <tr>
                                <td colspan=4>${materialHtml} </td>
                            </tr>
                        </table>
                        `
                    }
                })

                if(skillData.iconId == null){
                    var skillIcon = skillId;
                }else{
                    var skillIcon = skillData.iconId;
                }

                var skilltoken = opdataFull.skills[i].overrideTokenKey?opdataFull.skills[i].overrideTokenKey:defaulttoken

                var tabItem = $(`
                <li class='nav-item'>
                    <button class='btn tabbing-btns horiz-small nav-link ${(i!=0 ? '' : 'active')} tablink' data-toggle='pill' onclick='UpdateToken("${skilltoken}",${i},${opdataFull.skills.length})' href='#skill${i}'>
                    <p><img class='ak-shadow skill-image notclickthrough' id='skill${i}image' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/skills/skill_icon_${skillIcon}.png' style='width: 20px;margin:-4px 6px 0px -5px'>Skill ${i+1}</p>
                    </button>
                </li>
                `)

                var tabContents = $(`
                <div class='tab-pane container clickthrough ${i!=0 ? '' : 'active'}' id='skill${i}'>
                    <div class='small-container' style='margin-top: 50px;'>
                        <p class='large-text'>Skill ${i+1}</p>
                        <span class='custom-span skillname notclickthrough'><div>${skillname}</div></span>
                            <div class='topright'>
                                <div style='margin-top:-10px;padding:10px'>
                                    <img class='ak-shadow skill-image notclickthrough' id='skill${i}image' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/skills/skill_icon_${skillIcon}.png' style='width: 100%;'>
                                </div>
                            </div>

                    </div>
                    <div class='dividerdark'> </div>
                    <div id='skill${i}StatsCollapsible' class='collapse collapsible notclickthrough ak-shadow show' >
                        <input type='range' value='1' min='1' max=${skillData.levels.length} name='skillLevel' id='skill${i}Level' oninput='changeSkillLevel(this,${i})'style="margin-top:10px" class='${lefthand=="true"?"lefthandskillLevelInput":""} skillLevelInput'>
                            <div class='${lefthand=="true"?"lefthandskillleveldisplaycontainer":""} skillleveldisplaycontainer'><span class="custom-span ak-btn btn btn-sm ak-c-black" id='skill${i}LevelDisplay'>${SkillRankDisplay(1)}</span></div>
                        ${tables}
                    </div>
                <div>

                `)
                $("#skill-tabs").append(tabItem);
                $("#skill-contents").append(tabContents);
            });
            //TOKEN SOON ??
            $("#token-contents").html("")
            globalelite = 0
            UpdateTokenContent()
            //EQUIP CHECK
            $("#equip-tabs").html("");
            $("#equip-contents").html("");

            if(db.uniequip.charEquip[opKey]){
                var equiplist = db.uniequip.charEquip[opKey]
                
                ModuletalentValue = Array.from({ length: db.uniequip.charEquip[opKey].length-1 }, () => [0, 0])
                var num = 1
                var tabhtml = ""
                var contenthtml = ""

                equiplist.forEach(element => {
                    var currequip = db.uniequip.equipDict[element]
                    var currequipEN = db.uniequipEN.equipDict[element]
                    var currebattequip
                    var equiphtml = []
                    if(db.battle_equip[currequip.uniEquipId]){
                        currebattequip = db.battle_equip[currequip.uniEquipId]
                    }
                    var greek = {"x":"&Chi;","y":"&Upsilon;","d":"&Delta;","a":"&alpha;"}
                    tabhtml =`
                    <li class='nav-item'>
                        <button class='btn horiz-small nav-link ${(num!=2 ? '' : 'active')} equiplink' data-toggle='pill' href='#equip${num}'>
                            <div style = "display:inline-block;text-align:center;">
                                <div style = "display:inline-block; height:40px">
                                    <img class='equip-image' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/equip/shining/${currequip.equipShiningColor}_shining.png' style='width: 50px; margin: 0px -5px 0px -5px'></img>
                                    <div style = "display:inline-block; position:absolute;margin: -1px 0px 0px -35px">
                                        <img class='equip-image' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/equip/type/${currequip.typeIcon.toLowerCase()}.png' style='width: 30px; position:absolute;'></img>
                                    </div>
                                    <div style = "position:absolute;margin: 0px 0px 0px 0px">
                                        <div style = "width:60px;margin: 4px 0px 0px -10px;background:#222;color:#ddd;font-size:10px">${currequip.typeIcon.slice(0,-1).toUpperCase()}${greek[currequip.typeIcon.slice(-1)]?greek[currequip.typeIcon.slice(-1)]:currequip.typeIcon.slice(-1).toUpperCase()}</div>
                                    </div>
                                </div>
                            </div>
                        </button>
                    </li>
                    `

                    if(currebattequip){
                        var curreqphase = 0
                        var trait_range_id
                        currebattequip.phases.forEach(phase => {
                            equiphtml[curreqphase] = ""
                            phase.parts.forEach(part => {
                                if((part.target == "TRAIT" && part.isToken == false)||(part.target == "TRAIT_DATA_ONLY")||(part.target == "DISPLAY")){
                                    if(part.overrideTraitDataBundle.candidates[0].additionalDescription == null && part.overrideTraitDataBundle.candidates[0].overrideDescripton == null){
                                        return
                                    }else if(part.overrideTraitDataBundle.candidates[0].additionalDescription == null){
                                        equiphtml[curreqphase] +=
                                        `
                                            <div>
                                            ${GetTrait(part.overrideTraitDataBundle.candidates[0].overrideDescripton,part.overrideTraitDataBundle)}
                                            </div>
                                        `
                                    }else{
                                        equiphtml[curreqphase] +=
                                        `
                                            <div>
                                            ${GetTrait(part.overrideTraitDataBundle.candidates[0].additionalDescription,part.overrideTraitDataBundle,"Additional Traits")}
                                            </div>
                                        `
                                        }
                                    }
                                if(part.target == "TALENT"){
                                    console.log(part.rangeId)
                                    if(part.addOrOverrideTalentDataBundle.candidates[0].rangeId && part.addOrOverrideTalentDataBundle.candidates[0].displayRangeId){
                                        equiphtml[curreqphase]+=`${titledMaker2(rangeMaker(part.addOrOverrideTalentDataBundle.candidates[0].rangeId,false),"")}`
                                        trait_range_id = part.addOrOverrideTalentDataBundle.candidates[0].rangeId
                                    }
                                }
                            });
                            //insert Module Talent with potentials
                            if(curreqphase>0) equiphtml[curreqphase]+=`${GetModuleTalent(phase.parts,element,num,curreqphase,trait_range_id)}`

                            if(phase.attributeBlackboard.length>0){
                                var statcontent = ''
                                phase.attributeBlackboard.forEach(stat => {
                                    var tlstat = db.effect[stat.key]
                                    statcontent +=
                                        `
                                            <div class="stats">
                                                <div class="stats-l">${tlstat?tlstat:stat.key}</div><div class="stats-r" >${stat.value}</div>
                                            </div>
                                        `
                                });
                                equiphtml[curreqphase] += `
                                <div style='margin:12px;width:100%'> </div>
                                ${titledMaker(statcontent,"Additional Stats","","","padding:6px 10px 6px 10px;margin-bottom:6px;width:100%;white-space:initial")}
                                `
                            }
                            // console.log(Object.keys(phase.tokenAttributeBlackboard))
                            if(Object.keys(phase.tokenAttributeBlackboard).length>0){
                                var tokenlist = Object.keys(phase.tokenAttributeBlackboard)
                                tokenlist.forEach(token => {
                                    var curtoken = phase.tokenAttributeBlackboard[token]
                                    var tokenfulldata = db.chars[token]
                                    var statcontent = ''
                                    curtoken.forEach(stat => {
                                        var tlstat = db.effect[stat.key]
                                        statcontent +=
                                            `
                                                <div class="stats">
                                                    <div class="stats-l">${tlstat?tlstat:stat.key}</div><div class="stats-r" >${stat.value}</div>
                                                </div>
                                            `
                                    });
                                    equiphtml[curreqphase] += `
                                    <div style='margin:12px;width:100%'> </div>
                                    ${titledMaker(statcontent,`Additional Summon Stats (${tokenfulldata?tokenfulldata.appellation:token})`,"","","padding:3px 10px 6px 10px;width:100%;white-space:initial")}
                                    `
                                });
                            }
                            curreqphase += 1
                        });
                    }

                    if(currequip.itemCost){
                        var curreqphase = 0

                        $.each(currequip.itemCost,function(key,v){
                            var imagereq = []
                            if(currequip.unlockEvolvePhase)
                            imagereq.push(`
                                <div style="color:#fff;font-size:13px;background:#444;display:inline-block;padding:2px;border-radius:2px">
                                    <img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/${currequip.unlockEvolvePhase.slice(-1)}.png" style="width:20px;margin:-12px 0px -6px 0px" title="Elite ${currequip.unlockEvolvePhase.slice(-1)}">
                                </div>
                            `)
                            if(currequip.unlockLevel >1)
                            imagereq.push(`
                                <div style="color:#fff;font-size:13px;background:#444;display:inline-block;padding:2px;border-radius:2px">
                                    <span style="font-size:8px">Lv.</span>${currequip.unlockLevel}
                                </div>
                            `)
                            if(currequip.unlockFavors){
                                let trust = db.favor.favorFrames.find(favor=>favor.level==currequip.unlockFavors[key])
                                imagereq.push(`
                                <div style="color:#fff;font-size:13px;background:#444;display:inline-block;padding:2px;border-radius:2px">
                                    ${trust.data.percent}% <span style="font-size:8px">Trust</span>
                                </div>
                                `)
                            }

                            equiphtml[curreqphase] += `
                                <div style="text-align:center;background:#222;color:#fff;margin-top:5px">Unlock Requirements</div>
                                <div style="text-align:center;background:#222;color:#fff;margin:0px;padding:0px 0px 2px 0px">${imagereq.join(" ")}</div>
                                <div style="text-align:center">
                                `
                            if(gmapp == "SO"){
                                SO_condUnlocking = db.special_operator[opdataFull.id].unlock["uniequip1"][curreqphase] // might need to change "uniequip1" later
                                equiphtml[curreqphase] += `
                                                            <div class = "SO-Unlock">
                                                                ${ChangeDescriptionColor2(SO_condUnlocking)}
                                                            </div>
                                                        `
                            }
                            if(v){
                                v.forEach(item => {
                                    equiphtml[curreqphase] += CreateMaterial(item.id,item.count)
                                });
                            }
                            if(currequip.missionList.length){
                                equiphtml[curreqphase] += `
                                </div>
                                <div style="text-align:center;background:#222;color:#fff">Unlock Mission</div>
                                `
                                var missionnum = 1
                                var missionhtml = ``
                                currequip.missionList.forEach(mission => {
                                    var currmission = db.uniequip.missionList[mission]
                                    var currmissionEN = db.uniequipEN.missionList[mission]
                                    var missioncheck = ModuleMissionDescription(currmission,currmissionEN)
                                    missionhtml +=`
                                    ${titledMaker2(missioncheck,`Mission ${missionnum}`,``,``,"margin:8px 0px 4px 0px;white-space:initial;")}
                                    </br>
                                    `
                                    missionnum +=1
                                });
                                equiphtml[curreqphase] +=`
                                ${titledMaker(missionhtml,"",``,``,"width:100%")}
                                `
                            }else equiphtml[curreqphase] += `</div>`

                            curreqphase +=1
                        })
                    }

                    if(currequip.typeIcon=="original"){
                        equiphtml[0] = titledMaker(currequipEN?currequipEN.uniEquipDesc:currequip.uniEquipDesc,`Basic Information`,``,``,"margin:8px 0px 4px 0px;white-space:initial;")
                    }


                    leveltabhtml = ``
                    equiptabhtml = ``
                    for(i=0 ; i<equiphtml.length;i++){
                        leveltabhtml += `
                        <li class='nav-item'>
                            <button class='btn horiz-small nav-link ${(i!=0 ? '' : 'active')} equiplevel' data-toggle='pill' href='#equip${num}level${i}' style ='padding:0;border-radius:0px'>
                                <div style = "display:inline-block;text-align:center;">
                                    <div style = "width:50px;margin: 2px;color:#ddd;font-size:10px">
                                        <div style="font-size:20px;margin:-5px 0px;padding:0px">
                                            ${i+1}
                                        </div>
                                        <div style="font-size:8px;margin:0px;padding:0px">
                                            Stage
                                        </div>
                                    </div>
                                </div>
                            </button>
                        </li>
                        `
                        equiptabhtml +=`
                        <div class='tab-pane container ${i!=0 ? '' : 'active'}' id='equip${num}level${i}'>
                            ${equiphtml[i]}
                        </div>
                        `
                    }

                    contenthtml =`
                    <div class='tab-pane container ${num!=2 ? '' : 'active'}' id='equip${num}'>
                        <div class='small-container' style='margin-top: 50px;'>
                            <span class='custom-span equipname'><div>${currequipEN?currequipEN.uniEquipName:currequip.uniEquipName}</div></span>
                                <div class='equipimage'>
                                    <button type="button" class="btn ak-button" style="width:90px;height:90px" data-toggle="modal" data-target="#opmodulestory" onclick="GetModuleStory('${element}')">
                                        <span style="position:absolute;font-size: 14px;bottom:4px;left:4px;color:#fff;background:#222222dd;padding:4px;border-radius:2px" class="fa fa-search-plus"> Info</span>
                                        ${currequip.uniEquipId.search("001")!=-1?`<img class='equip-image' id='equip${i}image_add' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/subclass/sub_${opdataFull.subProfessionId}_icon.png'style='z-index: 1;  width: 21%;  top: 27.7%;  position: absolute;  left: 37.2%;  max-height: 21%;object-fit: contain;  filter: invert(5%) sepia(6%) saturate(913%) hue-rotate(12deg) brightness(83%) contrast(86%);'>`:""}
                                        <img loading='lazy' class='equip-image' id='equip${num}image' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/equip/icon/${currequip.uniEquipIcon.search("001")==-1?currequip.uniEquipIcon:"original"}.png' style='width: 90px;height:90px;object-fit:contain' onerror="this.src='extra/not_found.png';">
                                    </button>
                                </div>
                        </div>
                            <ul class='nav nav-pills' id='equip-tabs' style="background:#222">
                                ${leveltabhtml}
                            </ul>
                        <div class="tab-content" id="equip-phases" style="margin: 0px 0px 0px 0px;padding:15px 5px 10px 5px">${equiptabhtml}</div>
                    `

                    //${currequip.uniEquipDesc}
                    $("#equip-tabs").append(tabhtml);
                    $("#equip-contents").append(contenthtml)
                    num +=1
                });
                //${equiphtml}


            }
            localStorage.setItem('selectedOPDetails', opid);
            localStorage.setItem('selectedOPGamemode', gamemode);
            UpdateElite(0)
            tooltip_activate()
        }
    }

    function ModuleMissionDescription(mission,missionEN){
        // console.log(mission)
        var tl = ''
        var squadinfo =''
        //probably good
        // <@ba.kw> = Blue Highlight
        switch (mission.template) {
            case "EquipmentCharKilled":
                if(mission.paramList[0].includes(";")){
                    var splitchara = mission.paramList[0].split(";")
                    var allcharalist = []
                    splitchara.forEach(chara => {
                        allcharalist.push(`<@ba.kw>${db.chars[chara].appellation}</>`)
                    });
                    tl = `
                        Kill <@ba.kw>${mission.paramList[1]}</> enemies with Non-Borrowed ${allcharalist.join(" or ")}
                    `
                }else{
                    tl = `
                        Kill <@ba.kw>${mission.paramList[1]}</> enemies with Non-Borrowed <@ba.kw>${db.chars[mission.paramList[0]]?db.chars[mission.paramList[0]].appellation:db.charpatch.patchChars[mission.paramList[0]].appellation}</>
                    `
                }
                break;
            case "EquipmentDeployStage":
                var character = db.chars[mission.paramList[2].split(";")[0]]
                var extra = ""
                console.log(character)
                if (character.profession=="TOKEN") extra = "summons of"
                tl=`
                    Complete <@ba.kw>${mission.paramList[0]}</> stages, Deploy at least <@ba.kw>${mission.paramList[1]}</> ${extra} Non-Borrowed <@ba.kw>${db.chars[mission.paramList[3]]?db.chars[mission.paramList[3]].appellation:db.charpatch.patchChars[mission.paramList[3]].appellation}</> in each stage
                    `
                break;
            case "EquipmentDeployTotal":
                var character = db.chars[mission.paramList[1].split(";")[0]]
                var extra = ""
                console.log(character)
                if (character.profession=="TOKEN") extra = "summons of"
                tl=`
                    Deploy <@ba.kw>${mission.paramList[0]}</> ${extra} Non-Borrowed <@ba.kw>${db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]].appellation:db.charpatch.patchChars[mission.paramList[2]].appellation}</>
                `
                break;
            case "EquipmentSquadPro":
                var stage = db.stage[mission.paramList[1]]
                var splitall = mission.paramList[3].split(";")
                var squadinfo = ""
                var squadprefix = ""
                var squadsuffix = ""
                splitall.forEach(squadtype => {
                    var splitsquad = squadtype.split(",")
                    if(splitsquad[0]==13||splitsquad[0]==999){ // dusk case | 999
                        var currclass = query(db.classes,"type_data",splitsquad[1])
                        squadprefix = "and"
                        squadinfo += ` <@ba.kw>${currclass.type_en}</>`
                        squadsuffix = " operators only in party"
                    }
                    else if(splitsquad[0]>0){
                        var currclass = query(db.classes,"type_data",splitsquad[1])
                        squadprefix = "and up to"
                        squadinfo += ` <@ba.kw>${splitsquad[0]}</> <@ba.kw>${currclass.type_en}</>`
                        squadsuffix = " operators only"
                    }else if(splitsquad[0]==0){
                        squadinfo += ` with no other operator`
                    }
                });
                tl=`
                    Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star </br>
                    Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]].appellation:db.charpatch.patchChars[mission.paramList[2]].appellation}</> ${squadprefix}${squadinfo}${squadsuffix}
                 `
                break;
            case "EquipmentSquadProEx":
                var splitsquad = mission.paramList[3].split(";")
                var stage = db.stage[mission.paramList[1]]
                var squads = []
                splitsquad.forEach(element => {
                    squads.push(query(db.classes,"type_data",element).type_en)
                });
                tl=`
                    Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star </br>
                    Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]].appellation:db.charpatch.patchChars[mission.paramList[2]].appellation}</>
                    </br>Other <@ba.kw>${squads.join(", ")}</> operators not allowed in party
                    `
                break;
            case "EquipmentSquadProStage":
                var splitsquad = mission.paramList[2].split(",")
                var currclass = query(db.classes,"type_data",splitsquad[1])
                if(splitsquad[0]==13||splitsquad[0]==999){ //swire case | 999
                    squadinfo = ` and <@ba.kw>${currclass.type_en}</> operators only in party`
                }
                else if(splitsquad[0]>0){
                    squadinfo = ` and up to <@ba.kw>${splitsquad[0]}</> <@ba.kw>${currclass.type_en}</> class only`
                }else if(splitsquad[0]==0){
                    squadinfo = ` with no other operator`
                }
                tl=`
                    Clear <@ba.kw>${mission.paramList[0]}</> stages
                    </br>Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[1]]?db.chars[mission.paramList[1]].appellation:db.charpatch.patchChars[mission.paramList[1]].appellation}</> ${squadinfo}
                 `
                break;
            case "EquipmentSquadPos":
                var splitsquad = mission.paramList[3].split(",")
                var stage = db.stage[mission.paramList[1]]
                var currclass = splitsquad[1]=="MELEE"?"Melee":"Ranged"
                if(splitsquad[0]==13){
                    squadinfo = ` and <@ba.kw>${currclass}</> operators only in party`
                }
                else if(splitsquad[0]>0){
                    squadinfo = ` and up to <@ba.kw>${splitsquad[0]}</> <@ba.kw>${currclass}</> operator`
                }else if(splitsquad[0]==0){
                    squadinfo = ` with no other operator`
                }
                tl=`
                    Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star </br>
                    Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]].appellation:db.charpatch.patchChars[mission.paramList[2]].appellation}</> ${squadinfo}
                    `
                break;
            case "EquipmentSquadNum":
                var stage = db.stage[mission.paramList[1]]
                tl=`
                    Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star </br>
                    Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]].appellation:db.charpatch.patchChars[mission.paramList[2]].appellation}</> and max of <@ba.kw>${mission.paramList[3]}</> other operator
                    `
                break;
            case "EquipmentSquadStarStage":
                var splitsquad = mission.paramList[2].split(",")
                var currclass = `${splitsquad[1]} Star`
                if(splitsquad[0]==13||splitsquad[0]==999){ // doberman case | 999
                    squadinfo = ` and <@ba.kw>${currclass}</> operators only in party`
                }
                else if(splitsquad[0]>0){
                    squadinfo = ` and up to <@ba.kw>${splitsquad[0]}</> <@ba.kw>${currclass}</> operator only`
                }else if(splitsquad[0]==0){
                    squadinfo = ` with no other operator`
                }
                tl=`
                    Clear <@ba.kw>${mission.paramList[0]}</> stages
                    </br>Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[1]]?db.chars[mission.paramList[1]].appellation:db.charpatch.patchChars[mission.paramList[1]].appellation}</> ${squadinfo}
                    `
                break;
            case "EquipmentSquadStar":
                var splitsquad = mission.paramList[3].split(",")
                var stage = db.stage[mission.paramList[1]]
                var currclass = `${splitsquad[1]} Star`
                if(splitsquad[0]==13){
                    squadinfo = ` and <@ba.kw>${currclass}</> operators only in party`
                }
                else if(splitsquad[0]>0){
                    squadinfo = ` and up to <@ba.kw>${splitsquad[0]}</> <@ba.kw>${currclass}</> operator`
                }else if(splitsquad[0]==0){
                    squadinfo = ` with no other operator`
                }
                tl=`
                    Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star </br>
                    Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]].appellation:db.charpatch.patchChars[mission.paramList[2]].appellation}</> ${squadinfo}
                    `
                break;
            case "EquipmentSkillCastStage":
                var stage = db.stage[mission.paramList[1]]
                var skillId = mission.paramList[2].split(";")
                var skillimg=[]

                skillId.forEach(eachskillId =>{
                    var currSkill = db.skills[eachskillId].levels[0]
                    var skillname = db.skillsEN[eachskillId]?db.skillsEN[eachskillId].levels[0].name:db.skillsTL[eachskillId]?db.skillsTL[eachskillId].name:currSkill.name;
                    var skillnum = opdataFull.skills.findIndex(skill => skill.eachskillId==eachskillId)
    
                    if(skillnum>=0){
                        skillnum = `(Skill ${skillnum+1})`
                    }else{
                        skillnum = ''
                    }

                    skillimg.push(`<@ba.kw><img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/skills/skill_icon_${eachskillId}.png" style="max-width:20px;margin:2px">${skillname} ${skillnum}</>`)
                })

                console.log(opdataFull.skills)
                console.log(skillnum)

                tl=`
                    Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star </br>
                    Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[4]]?db.chars[mission.paramList[4]].appellation:db.charpatch.patchChars[mission.paramList[4]].appellation}</>,
                    </br>Cast ${skillimg.join(" or ")} <@ba.kw>${mission.paramList[3]}</> times
                    `
                break;
            case "EquipmentSkillCast":
                var skillId = mission.paramList[1]
                var currSkill = db.skills[skillId].levels[0]
                var skillname = db.skillsEN[skillId]?db.skillsEN[skillId].levels[0].name:db.skillsTL[skillId]?db.skillsTL[skillId].name:currSkill.name;
                var skillnum = opdataFull.skills.findIndex(skill => skill.skillId==skillId)

                if(skillnum>=0){
                    skillnum = `(Skill ${skillnum+1})`
                }else{
                    skillnum = ''
                }
                console.log(opdataFull.skills)
                console.log(skillnum)
                tl=`
                    Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[0]]?db.chars[mission.paramList[0]].appellation:db.charpatch.patchChars[mission.paramList[0]].appellation}</>
                    </br>Cast <@ba.kw><img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/skills/skill_icon_${skillId}.png" style="max-width:20px;margin:2px"> ${skillname} ${skillnum}</> <@ba.kw>${mission.paramList[2]}</> times
                    `
                break;
            case "EquipmentDamageStage":
                var stage = db.stage[mission.paramList[1]]
                tl=`
                    Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star
                    <br>Deal total of <@ba.kw>${mission.paramList[3]}</> damage </br>
                    Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]].appellation:db.charpatch.patchChars[mission.paramList[2]].appellation}</>
                    `   
                break;
            case "EquipmentDamageTotal":
                tl=`
                    Deal total of <@ba.kw>${mission.paramList[1]}</> damage </br>
                    Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[0]]?db.chars[mission.paramList[0]].appellation:db.charpatch.patchChars[mission.paramList[0]].appellation}</>
                    `
                break;
            case "EquipmentDamageTotalWithToken":
                tl=`
                    Deal total of <@ba.kw>${mission.paramList[1]}</> damage </br>
                    Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[0].split(";")[0]]?db.chars[mission.paramList[0].split(";")[0]].appellation:db.charpatch.patchChars[mission.paramList[0].split(";")[0]].appellation}</> or <@ba.kw>${db.chars[mission.paramList[0].split(";")[1]]?db.chars[mission.paramList[0].split(";")[1]].appellation:db.charpatch.patchChars[mission.paramList[0].split(";")[1]].appellation}</>
                    `
                break;
            case "EquipmentCharKilledStage":
                var stage = db.stage[mission.paramList[1]]
                tl=`
                    Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star
                    </br>Kill <@ba.kw>${mission.paramList[3]}</> enemies
                    Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[2].split(";")[0]]?db.chars[mission.paramList[2].split(";")[0]].appellation:db.charpatch.patchChars[mission.paramList[2].split(";")[0]].appellation}</>
                    `
                break;
            case "EquipmentEventStageKill":
                var stage = db.stage[mission.paramList[1]]
                var enemyid= mission.paramList[4].split(",")[2]

                var enemyName = db.enemy[enemyid]

                tl=`
                    Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star
                    </br>Kill <@ba.kw>${mission.paramList[3]}</> enemies including <@ba.kw>${mission.paramList[5]}</> <@ba.kw>${enemyName}</>
                    <img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/enemy/${enemyid}.png" style="max-width:50px">
                    </br>Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]].appellation:db.charpatch.patchChars[mission.paramList[2]].appellation}</>
                    `
                break;
            case "EquipmentEventTotal":
                var splitreq = mission.paramList[1].split(",")
                var objective = ""
                var enemytype = ""
                var wordtype = ""

                switch (splitreq[0]) {
                    case "DEATHDETAIL":
                        objective = "Kill"
                        break;
                    case "PROJECTILEBORN":
                        objective = "Launch"
                        break;
                    case "SPAWN": // Dusk case
                        objective = "Summon"
                        break;
                    default:
                        objective = "???"
                        break;
                }
                switch (splitreq[splitreq.length-1]) {
                    case "infection":
                        enemytype = "Infected enemies"
                        wordtype = "<br> Using"
                        break;
                    case "drone": // Glaucus case
                        enemytype = "Drone enemies"
                        wordtype = "<br> Using"
                        break;
                    case "sarkaz": // Toddifons case
                        enemytype = "Sarkaz enemies"
                        wordtype = "<br> Using"
                        break;
                    case "ELITE":
                        enemytype = splitreq[splitreq.length-2]=="BOSS"?"Elite or Leader enemies":"Elite enemies" // Ash case Elite only
                        wordtype = "<br> Using"
                        break;
                    case "RANGED":
                        enemytype = "Ranged enemies"
                        wordtype = "<br> Using"
                        break;
                    case "projectile_breeze_s2":
                        enemytype = "Skill 2 heal projectile"
                        wordtype = "of"
                        break;
                    case "1":   // Leizi
                    case "2":   // Ambriel
                        skillid = "skchr_"+mission.paramList[0].split("_")[2]+"_2"
                        console.log(skillid)
                        skillname = db.skillsEN[skillid]?db.skillsEN[skillid].levels[0].name:db.skills[skillid].levels[0].name
                        enemytype = "Enemies"
                        wordtype = `with <@ba.kw> <img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/skills/skill_icon_${skillid}.png" style="max-width:20px;margin:2px"> ${skillname} (Skill 2)</> </br>Using`
                        break;
                    case "ability":
                        enemytype = "enemies"
                        wordtype = "with any skill of"
                        break;
                    case "killcount": // W case
                        enemytype = "enemies"
                        wordtype = "<br> Using"
                        break;
                    case splitreq[splitreq.length-1].match(/token_/)?.input: // Dusk case
                        enemytype = db.chars[splitreq[splitreq.length-1]].appellation
                        wordtype = "with"
                        break;
                    default:
                        wordtype = "Nani !?"
                        enemytype = "???"
                        break;
                }
                var extra = ""
                if(splitreq.length>3){
                    if(db.skills[splitreq[2]]){
                        var skillId = splitreq[2]
                        var skillname = db.skills[splitreq[2]].levels[0].name
                        skillname = db.skillsEN[skillId]?db.skillsEN[skillId].levels[0].name:db.skillsTL[skillId]?db.skillsTL[skillId].name:skillname;
                        var skillnum = opdataFull.skills.findIndex(skill => skill.skillId==skillId)
                        skillnum = `(Skill ${skillnum+1})`
                        extra = `
                        's <@ba.kw><img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/skills/skill_icon_${skillId}.png" style="max-width:20px;margin:2px"> ${skillname} ${skillnum}</>
                        `
                    }
                }

                tl=`
                    ${objective} <@ba.kw>${mission.paramList[2]}</> <@ba.kw>${enemytype}</>
                    ${wordtype} Non-Borrowed <@ba.kw>${db.chars[mission.paramList[0]]?db.chars[mission.paramList[0]].appellation:db.charpatch.patchChars[mission.paramList[0]].appellation}</>${extra}
                    `
                break;
            case "EquipmentEventStageMore" :
                var stage = db.stage[mission.paramList[1]]
                var splitreq = mission.paramList[3].split(";")[0].split(",")
                var chara = db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]]:db.charpatch.patchChars[mission.paramList[2]]
                var chara2
                var objective = ""
                var objective2 = ""
                var enemies=""
                var enemyid
                var enemyid2
                var enemyName
                var enemyName2
                var skillid
                var skill

                switch (splitreq[0]) {
                    case "DEATHDETAIL":
                        objective = "Kill"
                        switch (splitreq.length){
                            case 2: // Leonhardt case | Skill Code
                                skill = splitreq[1]
                                skillid = splitreq[1].slice(-1)
                                break;
                            case 3:
                                switch(splitreq[2]){
                                    case "killcount":   // kazemaru case
                                        chara2 = mission.paramList[4]
                                        break;
                                    case "ability": // kafka case
                                        chara2 = mission.paramList[4]
                                        objective2="any skills of "
                                        break;
                                    case "sarkaz":  // flamebringer case
                                        chara2 = mission.paramList[4]
                                        enemies="<@ba.kw>Sarkaz</> "
                                        break;
                                    case "3": // fartooth case | Skill Num
                                        skill=db.chars[splitreq[1]].skills[parseInt(splitreq[2])-1].skillId
                                        skillid=splitreq[2]
                                        break;
                                    default: // enemies
                                        enemyid=splitreq[2]
                                        break;
                                }
                                break;
                            case 4:
                                if (splitreq[2]=="1"){  //pudding case
                                    skill=db.chars[splitreq[1]].skills[parseInt(splitreq[2])].skillId
                                    skillid=parseInt(splitreq[2])+1
                                    enemyid=splitreq[3]
                                }else if(splitreq[2].includes("skchr")){    // cutter case
                                    skill = splitreq[2]
                                    skillid = splitreq[2].slice(-1)
                                    enemyid=splitreq[3]
                                }else if(splitreq[2].includes("enemy")){    // NTR case
                                    enemyid=splitreq[2]
                                    enemyid2=splitreq[3]
                                }
                                break;
                        }
                        break;
                    case "SIMPLE":  // fall_down
                        switch (splitreq[2]){
                            case "fall_down":
                                objective = "Cause"
                                objective2 = "to fall in a pit"
                                enemyid = splitreq[1]
                                break;
                            case "output_unmovable":
                                objective = "Bind"
                                objective2 = ""
                                enemyid = splitreq[1]
                                break;
                        }
                        break;
                    default:
                    objective = "???"
                    break;
                }

                //Enemies
                if(enemyid){
                    enemyName = db.enemy[enemyid]
                }
                if(enemyid2){
                    enemyName2 = db.enemy[enemyid2]
                    objective2 = `</br>or <@ba.kw>${mission.paramList[4]}</> <@ba.kw>${enemyName2}</>
                    <img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/enemy/${enemyid2}.png" style="max-width:50px">`
                }
                
                //Skill
                if(skill){
                    console.log(skill)
                    skillname = db.skillsEN[skill]?db.skillsEN[skill].levels[0].name:db.skillsTL[skill]?db.skillsTL[skill].name:db.skills[skill].levels[0].name;
                }

                if(enemyName&&skill){
                    tl=`
                    Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star
                    </br>${objective} <@ba.kw>${mission.paramList[4]}</> <@ba.kw>${enemyName}</>
                    <img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/enemy/${enemyid}.png" style="max-width:50px">
                    </br>with <@ba.kw> <img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/skills/skill_icon_${skill}.png" style="max-width:20px;margin:2px"> ${skillname} (Skill ${skillid})</>
                    </br>Using Non-Borrowed <@ba.kw>${chara.appellation}</>
                    `
                }
                else if (enemyName){
                    if(enemyName == "any"){
                        tl=`
                            Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star
                            </br>${objective} <@ba.kw>${mission.paramList[4]}</> enemies ${objective2}
                            </br>Using Non-Borrowed <@ba.kw>${chara.appellation}</>
                        `
                    }else{
                        tl=`
                            Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star
                            </br>${objective} <@ba.kw>${mission.paramList[4]}</> <@ba.kw>${enemyName}</>
                            <img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/enemy/${enemyid}.png" style="max-width:50px"> ${objective2}
                            </br>Using Non-Borrowed <@ba.kw>${chara.appellation}</>
                        `
                    }
                }else if (skill){
                    tl=`
                    Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star
                    </br>${objective} <@ba.kw>${mission.paramList[4]}</> enemies using <@ba.kw> loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/skills/skill_icon_${skill}.png" style="max-width:20px;margin:2px"> ${skillname} (Skill ${skillid})</>
                    </br>Using Non-Borrowed <@ba.kw>${chara.appellation}</>
                    `
                }else if(chara2){
                    tl=`
                        Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star
                        </br>${objective} <@ba.kw>${mission.paramList[4]}</> ${enemies}enemies
                        using ${objective2}Non-Borrowed <@ba.kw>${chara.appellation}</>
                    `
                }
                break;
            case "EquipmentSquadNoAnyDead" :
                var stage = db.stage[mission.paramList[1]]
                tl=`
                    Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star </br>
                    Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]].appellation:db.charpatch.patchChars[mission.paramList[2]].appellation}</> without any operator get killed
                    `
                break;
            case "EquipmentEventBattleMore" :
                var splitreq = mission.paramList[2].split(",")

                switch(splitreq[0]){
                    case "DEATHDETAIL":
                        tl=`
                            Complete <@ba.kw>${mission.paramList[0]}</> stages </br>
                            Kill at least <@ba.kw>${mission.paramList[3]}</> <@ba.kw>${splitreq[2].charAt(0).toUpperCase()+splitreq[2].slice(1)}s</> </br>
                            Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[1]]?db.chars[mission.paramList[1]].appellation:db.charpatch.patchChars[mission.paramList[1]].appellation}</>
                            `
                        break;
                    case "SIMPLE": // fall_down
                        tl=`
                            Complete <@ba.kw>${mission.paramList[0]}</> stages </br>
                            Cause at least <@ba.kw>${mission.paramList[3]}</> enemies to fall in a pit </br>
                            Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[1]]?db.chars[mission.paramList[1]].appellation:db.charpatch.patchChars[mission.paramList[1]].appellation}</>
                            `
                        break;
                    default:
                        tl="??? ??? ???"
                        break;
                }
                break;
            case "EquipmentSkillCastBattle" :
                var splitskills = mission.paramList[1].split(";")
                var skills = []

                splitskills.forEach(element => {
                    console.log(element)
                    var currSkill = db.skills[element].levels[0]
                    var skillname = db.skillsEN[element]?db.skillsEN[element].levels[0].name:db.skillsTL[element]?db.skillsTL[element].name:currSkill.name;
                    var skillnum = opdataFull.skills.findIndex(skill => skill.skillId==element)
                    skills.push({id:element,name:skillname,num:skillnum+1})
                });

                var skilltext = `Use at least <@ba.kw> ${mission.paramList[2]}</> times of the following skills :`
                skills.forEach(element => {
                    console.log(element.id)
                    skilltext += `<@ba.kw> <img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/skills/skill_icon_${element.id}.png" style="max-width:20px;margin:2px"> ${element.name} (Skill ${element.num})</> </br>`
                });
                tl =`
                        Complete <@ba.kw>${mission.paramList[0]}</> stages </br>
                        ${skilltext}
                        Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[3]]?db.chars[mission.paramList[3]].appellation:db.charpatch.patchChars[mission.paramList[3]].appellation}</>
                    `
                break;
            case "EquipmentDeployCharOrder" :
                var order = ""
                switch (mission.paramList[1]) {
                    case "1":
                        order = "1st"
                        break;
                    case "2":
                        order = "2nd"
                        break;
                    case "3":
                        order = "3rd"
                        break;
                    default:
                        order = `${mission.paramList[1]}th`
                        break;
                }
                tl =`
                        Complete <@ba.kw>${mission.paramList[0]}</> stages </br>
                        Deploy Non-Borrowed <@ba.kw>${db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]].appellation:db.charpatch.patchChars[mission.paramList[2]].appellation}</> on the <@ba.kw>${order}</> order
                    `
                break;
            case "EquipmentDeployOneNoEvac":
                var stage = db.stage[mission.paramList[1]]
                tl =`
                        Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star </br>
                        Deploy Non-Borrowed <@ba.kw>${db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]].appellation:db.charpatch.patchChars[mission.paramList[2]].appellation}</> on the <@ba.kw>1st</> order and not retreated or killed throughout stage
                    `
                break;

            case "EquipmentBattleCharKilled" :
                var splitChara = mission.paramList[1].split(",")
                var splitName = ''
                splitChara.forEach(element => {
                    console.log(element)
                    var currchar = db.chars[element]
                    console.log(currchar.appellation)
                    splitName+=  `</br><@ba.kw> <img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/${element}.png" style="max-width:50px"> ${currchar.appellation} </>`
                });
                tl =`
                        Complete <@ba.kw>${mission.paramList[0]}</> stages </br>
                        Kill at least <@ba.kw>${mission.paramList[2]}</> enemies using Non-Borrowed : 
                        ${splitName}
                    `
                break;
            case "EquipmentStageDeployCntAndSpec":
                var stage = db.stage[mission.paramList[1]]
                tl =`
                        Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star </br>
                        Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]].appellation:db.charpatch.patchChars[mission.paramList[2]].appellation}</> and deploy at max of <@ba.kw>${mission.paramList[3]}</> other operators
                    `
                break;
            case "EquipmentDeployCharAndKillCnt":
                var currchar = db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]]:db.charpatch.patchChars[mission.paramList[2]]
                tl =`
                        Complete <@ba.kw>${mission.paramList[0]}</> stages </br>
                        Kill at least <@ba.kw>${mission.paramList[4]}</> enemies using Non-Borrowed </br>
                        <@ba.kw> <img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/${mission.paramList[2]}.png" style="max-width:50px"> ${currchar.appellation} </>, and at least deployed <@ba.kw>${mission.paramList[1]}</> times
                    `
                break;
            case "EquipmentBattleCharDamage":
                var currchar = db.chars[mission.paramList[1]]?db.chars[mission.paramList[1]]:db.charpatch.patchChars[mission.paramList[1]]
                tl =`
                        Complete <@ba.kw>${mission.paramList[0]}</> stages </br>
                        Deal at least <@ba.kw>${mission.paramList[2]}</> damage using Non-Borrowed </br>
                        <@ba.kw> <img loading='lazy' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/${mission.paramList[1]}.png" style="max-width:50px"> ${currchar.appellation} </>
                    `
                break;

            case "EquipmentElementBurst":
                var currchar = db.chars[mission.paramList[0]]?db.chars[mission.paramList[0]]:db.charpatch.patchChars[mission.paramList[0]]
                tl =`
                        Cause <@ba.kw>Elemental burst</> <@ba.kw>${mission.paramList[1]}</> times
                        <br>Using Non-Borrowed <@ba.kw>${currchar.appellation}</>
                    `
                break;
            
            case "EquipmentElementBurstStage":
                var currchar = db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]]:db.charpatch.patchChars[mission.paramList[2]]
                var stage = db.stage[mission.paramList[1]]
                tl = `
                        Clear <@ba.kw>${stage}</> with <@ba.kw>${mission.paramList[0]}</> Star
                        <br>Cause at least <@ba.kw>${mission.paramList[3]}</> <@ba.kw>Elemental burst</> </br>
                        Using Non-Borrowed <@ba.kw>${db.chars[mission.paramList[2]]?db.chars[mission.paramList[2]].appellation:db.charpatch.patchChars[mission.paramList[2]].appellation}</>
                    `  
                break;
        }
        tl = `
            ${tl?`
            (Auto-translated)</br>
            ${tl}
            </br>
            </br>
            `:""}
            ${missionEN?`
            (Official Translate)</br>
            ${missionEN.desc}
            </br>
            </br>
            `:""}
            (Non-translated)</br>
            ${mission.desc}
        `
        return ChangeDescriptionColor(tl,true)
    }

    function UpdateToken(skilltoken, i, skillLength){
        globaltoken = skilltoken
        ChangeSkillAnim(i, skillLength, skilltoken)
        globalskill = i
        UpdateTokenContent()
        if(loadchibi && !defaulttoken && skilltoken.includes("token_")){
            LoadAnimationToken()
        }
    }

    function UpdateTokenContent(wholetokenupdate = true){
        if(!globaltoken || globaltoken == "null"){
            $("#token-contents").html("");
            return
        }
        var tokenfulldata = db.charsEN[globaltoken]?db.charsEN[globaltoken]:db.chars[globaltoken]
        if(!tokenfulldata){
            return
        }
        //skin problem
        // console.log(currskin)
        // var skinname = currskin.split(opdataFull.id)[1]?currskin.split(opdataFull.id)[1]:""
        // // var skinicon =

        // console.log(tokenname+skinname)
        console.log(tokenfulldata)
        var currlevel = globallevel[globalelite]
        var currelite = globalelite

        if(currelite<globalskill){
            currelite = globalskill
            currlevel = globallevel[globalskill]
        }
        console.log(tokenfulldata)
        var blockCount = statsInterpolation(tokenfulldata,'blockCnt',currlevel,currelite)
        if (blockCount==0&&tokenfulldata.talents){
            if(tokenfulldata.talents[0].candidates){
                var searchCandidate = tokenfulldata.talents[0].candidates.find(cand => {
                    return cand.unlockCondition.phase == currelite
                })
                if(searchCandidate){
                    var actualblockcount = searchCandidate.blackboard.find(eachbb =>{
                        return eachbb.key == "block_cnt"
                    })
                    if(actualblockcount){
                        blockCount = actualblockcount.value
                    }
                }
            }

        }

        console.log(`Elite : ${globalelite} - Level : ${currlevel}`)
        var stats = `
        <div>
            <div class='stats'>
                <div class='stats-l'>Maximum HP</div><div class='stats-r' id='summon-maxHp'>${statsInterpolation(tokenfulldata,'maxHp',currlevel,currelite)}</div>
            </div>
            <div class='stats'>
                <div class='stats-l'>Redeploy Time</div><div class='stats-r' id='summon-respawnTime'>${statsInterpolation(tokenfulldata,'respawnTime',currlevel,currelite)} <div style='display:inline;font-size:10px'> Sec</div></div>
            </div>

            <div class='stats'>
                <div class='stats-l'>Attack Power</div><div class='stats-r' id='summon-atk'>${statsInterpolation(tokenfulldata,'atk',currlevel,currelite)}</div>
            </div>
            <div class='stats'>
                <div class='stats-l'>Cost</div><div class='stats-r' id='summon-cost'>${statsInterpolation(tokenfulldata,'cost',currlevel,currelite)}</div>
            </div>

            <div class='stats'>
                <div class='stats-l'>Defense</div><div class='stats-r' id='summon-def'>${statsInterpolation(tokenfulldata,'def',currlevel,currelite)}</div>
            </div>
            <div class='stats'>
                <div class='stats-l'>Block</div><div class='stats-r' id='summon-blockCnt'>${blockCount}</div>
            </div>

            <div class='stats'>
                <div class='stats-l'>Resistance</div><div class='stats-r' id='summon-magicResistance'>${statsInterpolation(tokenfulldata,'magicResistance',currlevel,currelite)}</div>
            </div>
            <div class='stats'>
                <div class='stats-l'>Attack Time</div><div class='stats-r' id='summon-baseAttackTime'>${statsInterpolation(tokenfulldata,'baseAttackTime',currlevel,currelite,false)} <div style='display:inline;font-size:10px'> Sec</div></div>
            </div>
        </div>
        `
        // array.forEach(element => {
        //     stats.push(`
        //     <div class="stats">
        //         <div class="stats-l">${tlstat?tlstat:stat.key}</div><div class="stats-r" >${stat.value}</div>
        //     </div>
        //     `)
        // });

        if (wholetokenupdate) {
            $("#token-contents").html(
                `
                <div class="token-details" style='background:#333;margin:2px 0px;padding:2px 10px;height:64px'>
                    <div style ="display:inline-block;margin:0px 2px;background:#222222aa">
                        <img loading='lazy' class='token-image notclickthrough' id='Tokenimage' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/${globaltoken}.png' style='width:60px;margin:-0px 0px 0px 0px' onerror="this.src='extra/not_found.png';">
                    </div>
                    <div style ="position:absolute;left:80px;top:7px">
                        <div class='stats'>
                            <div class='stats-l' style="min-width:unset;width:40px;background:#3D3D3D"><img style='max-height:30px;margin:-11px -10px -9px -10px' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/${currelite}-s.png'></div><div class='stats-r' style="min-width:unset">Lv <span id="summon-level">${currlevel}</span></div>
                        </div>
                        <div>
                            ${db.charsEN[globaltoken]?tokenfulldata.name:tokenfulldata.appellation}
                        </div>
                    </div>
                </div>
                <div class="token-trait" style=${tokenfulldata.description?"padding-top:15px;padding-left:15px;padding-right:5px;":""}>
                    ${tokenfulldata.description?GetTrait(tokenfulldata.description,""):""}
                </div>
                <div class="token-skill" style="width:100%;min-width:320px;"></div>
                <div class="token-stats" style="width:100%;text-align:center;padding:4px 5px 5px 10px;min-width:320px">
                <button id='Tokstatdetailtitle' class='btn btn-sm btn-block ak-btn' onclick='SlideToggler("Tokstatdetailcontent",$(this))'style="color:#fff;text-align:center;background:#222;min-width:320px;height:27px;padding-top: 2px;padding-bottom: 2px;">Token Stat <i class="fas fa-caret-up"></i></button>
                    <div class="Tokstatdetailcontent">
                        ${stats}
                        ${rangeMaker(tokenfulldata.phases[globalelite].rangeId)}
                    </div>
                </div>
                `
            )
            UpdateTokenSkill()
        }else{
            $("#token-contents .token-details .stats").html(`<div class='stats-l' style="min-width:unset;width:40px;background:#3D3D3D"><img style='max-height:30px;margin:-11px -10px -9px -10px' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/${currelite}-s.png'></div><div class='stats-r' style="min-width:unset">Lv <span id="summon-level">${currlevel}</span></div>`)
        }

        tooltip_activate()
    }

    function UpdateTokenSkill(token=globaltoken,skill=globalskill){
        var TokenskillID=db.chars[token].skills[skill].skillId //charEN[token]?charEN[token].skills[skill].skillId:charCN[token].skills[skill].skillId
        var Tokenskill=db.skills[TokenskillID]
        if(!Tokenskill) return ;
        if(!Tokenskill.levels[0].description && Tokenskill.levels[0].blackboard.length==0) return ;
        var tables = "";
        var skilllvblackboard
        var ToktabContents

        for(i2=0;i2<10;i2++){
            if(Tokenskill.levels[0].description)
                var TokskillDesc = Tokenskill.levels.length>i2?getSkillDesc(TokenskillID,i2):getSkillDesc(TokenskillID,0);
            else
                var TokskillDesc = ""
            if(Tokenskill.levels[0].rangeId)
                var TokskillRange = rangeMaker(Tokenskill.levels[0].rangeId)
            else
                var TokskillRange = ""
            if(Tokenskill.levels[0].spData.spCost)
                if(TokskillRange)
                    var TokskillSP = `
                                        <div>${titledMaker(Tokenskill.levels[0].spData.spCost,"SP Cost")}</div>
                                        <div>${titledMaker(Tokenskill.levels[0].spData.initSp,"Initial SP")}</div>
                                    `
                else
                    var TokskillSP =`
                                        ${titledMaker(Tokenskill.levels[0].spData.spCost,"SP Cost")}
                                        ${titledMaker(Tokenskill.levels[0].spData.initSp,"Initial SP")}
                                    `
            else
                var TokskillSP = ""
                
            
            if (TokskillRange && TokskillSP)
                TokskillExtraDetails = `<div class="skill-detail-grid Tokskilldetailcontent" style="display:none;">
                                            <div class="skill-grid">
                                                ${TokskillRange}
                                            </div>
                                            <div class="skill-grid-num">
                                                ${TokskillSP}
                                            </div>
                                        </div>`
            else if (TokskillRange)
                TokskillExtraDetails = `<div class="skill-detail-grid Tokskilldetailcontent" style="display:none;">
                                            <div class="skill-grid">
                                                ${TokskillRange}
                                            </div>
                                        </div>`
            else if (TokskillSP)
                TokskillExtraDetails = TokskillSP
            else 
                TokskillExtraDetails = ""

            var Tokskilldetails = []
            var Tokskilltable = TokskillDesc=""?"":`<div class='skilldesc Tokskilldetailcontent' style="display:none;">${TokskillDesc}</div>`
            var Tokdetailtable = ""

            console.log(Tokskilltable)

            skilllvblackboard = Tokenskill.levels.length>i2?i2:0
            Tokenskill.levels[skilllvblackboard].blackboard.forEach(skillinfo => {
                var skilljson = {}
                skilljson.name = db.effect[skillinfo.key]?db.effect[skillinfo.key]:skillinfo.key
                skilljson.key = skillinfo.key
                skilljson.value = skillinfo.value
    
                Tokskilldetails.push(skilljson)
                if(skillinfo.key=="force"||skillinfo.key=="base_force_level"||skillinfo.key=="attack@force") force= skillinfo.value
            });
            
            if(Tokskilldetails.length>0){
                var Tokskillhtmldetail = ""
    
                Tokskilldetails.forEach(currdetails => {
    
                    Tokskillhtmldetail+=`
                    <div style="background:#444;margin:4px;padding:2px;padding-top:8px;border-radius:2px;color:#999999">
                            ${titledMaker2(currdetails.name,currdetails.key)}  ${currdetails.value}
                    </div>`
                });
                Tokdetailtable = Tokskillhtmldetail
            }else{
                Tokdetailtable=""
            }

            tables+=`<table id='Tokskill${skill}level${i2}stats' class='${lefthand=="true"?"left-hand":""} skillstats ${(i2!=skillValue[globalskill] ? '' : 'active')}'>
                        <tbody class='Tokskilldetailcontent' style="display:none;margin-bottom:8px;padding-top:10px;padding:2px;background:#666">
                            ${Tokskilltable==""?"":`<tr style="background: #444;"><td>${Tokskilltable}</td></tr>`}
                            ${(TokskillRange || !TokskillSP)?"":`<tr style="height:10px;background:#4f4f4f"></tr>`}
                            ${TokskillExtraDetails==""?"":`<tr style="background:#4f4f4f"><td>${TokskillExtraDetails}</td></tr>`}
                            <tr>
                                <td>
                                    ${Tokdetailtable}
                                </td>
                            </tr>
                            <tr style="height:5px">
                            </tr>        
                        </tbody>
                    </table>
                    `
        }

        ToktabContents = `<div id='Tokskill${skill}StatsCollapsible' class='collapse collapsible notclickthrough show'>
                            <button id='Tokskilldetailtitle' class='btn btn-sm btn-block ak-btn' onclick='SlideToggler("Tokskilldetailcontent",$(this))' style="color:#fff;text-align:center;background:#222;padding:2px;min-width:320px">
                                Token Skill Description & Details 
                                <i class="fas fa-caret-down"></i>
                            </button>
                            ${tables}
                        </div>`

        $(".token-skill").html(ToktabContents);
    }

    function GetModuleStory(module){
        var currequip = db.uniequip.equipDict[module]
        var currequipEN = db.uniequipEN.equipDict[module]
        $("#opmodulestorycontent").html(`
            <div style="background:#222;padding:6px 5px 6px 5px;font-size:20px;text-align:center">${currequipEN?currequipEN.uniEquipName:currequip.uniEquipName}</div>
            <div class="equip-image-container">
                ${currequip.uniEquipId.search("001")!=-1?`<img class='equip-image' id='equip${i}image_add' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/subclass/sub_${opdataFull.subProfessionId}_icon.png'style='z-index: 1;  width: 21%;  top: 27.7%;  position: absolute;  left: 37.2%;  max-height: 21%;object-fit: contain;filter: invert(5%) sepia(6%) saturate(913%) hue-rotate(12deg) brightness(83%) contrast(86%);'>`:""}
                <img loading='lazy' class='equip-image' id='equip${i}image' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/equip/icon/${currequip.uniEquipIcon.search("001")==-1?currequip.uniEquipIcon:"original"}.png' style='width:100%;max-width:500px' onerror="this.src='extra/not_found.png';">
            </div>

            <div style="background:#222;padding:6px 5px 6px 5px;font-size:20px;text-align:center">Basic Information</div>
            <div style="background:#333;padding:6px 5px 6px 5px;">${currequipEN?currequipEN.uniEquipDesc.replace(/\n/g,"</br>"):currequip.uniEquipDesc.replace(/\n/g,"</br>")}</div>
        `)
    }

    function getEliteHTML(i, opdataFull){
        var container = $("<div class='tab-pane container "+(i!=0 ? '' : 'active')+"' id='elite_"+i+"_tab'></div>");

        var stats = $("<div class='small-container clickthrough'>"
                        +   "<p class='large-text'>Base</p>"
                        +   "<span class='custom-span'>Stats</span>"
                        +   "<div class='topright maxlevel'>"
                        +       "<span class='custom-span maxleveltext'>Max Level</span>"
                        +       "<span class='custom-span leveltext' id='elite_"+i+"_maxLv'>"+opdataFull.phases[i].maxLevel+"</span>"
                        +       "<div class='ring'>"
                        +           "<div class='back ak-shadow'></div>"
                        +           "<div class='back-centre'></div>"
                        +       "</div>"
                        +   "</div>"
                        +"</div>"
                        +"<div class='dividerdark'> </div>");

        var statsCollapsible = $("<div id='elite"+i+"StatsCollapsible' class='eliteStatsContainer ak-shadow greybackground'></div>");
        var eliteCost = GetEliteCost(i,opdataFull)
        var materialist = []

        if(eliteCost){
            eliteCost.forEach(materials => {
                if (materials){
                    materialist.push(CreateMaterial(materials.id,materials.count))
                }
            });
            // console.log(materialist)
        }
        var materialHtml =''
        if(materialist.length>0){
            materialHtml=`
            <div style="text-align:center;background:#222">Elite Requirements</div>
            <div style="text-align:center">${materialist.join("")}</div>`
        }else if(gmapp == "SO" && i > 0){
            SO_condUnlocking = db.special_operator[opdataFull.id].unlock["evolve"][i - 1]
            materialHtml=`
            <div style="text-align:center;background:#222">
                Elite Requirements
            </div>
            <div class = "SO-Unlock" style="padding: 5px 8px;">
                ${ChangeDescriptionColor2(SO_condUnlocking)}
            </div>`
        }
        var keyframes = [];
        $.each(opdataFull.phases[i].attributesKeyFrames,function(j,v){
            keyframes[j] = v;
        });
        // console.log(keyframes);
        // var statsLevelHeader = $(`<span class='stat-level-header ${lefthand=="true"?"lefthand-stat-level-header":"righthand-stat-level-header"} ' style=''>Level</span>`)
        // var statsLevelSlider = $(`<input type='range' value='1' min='1' max='${keyframes[1].level}' name='levelStats' id='elite${i}LevelSlider' oninput='changeEliteLevel(this,${i},${keyframes[1].level})' style='margin-top:20px;width:60%;' class='statlevelInput ${lefthand=="true"?"lefthand-statlevelInput":"righthand-statlevelInput"}'></input>`);
        // var statsLevelDisplay = $(`<div class='form-group stat-input ${lefthand=="true"?"lefthand-stat-input":"righthand-stat-input"}' style='display:inline-block;vertical-align:middle;'><input class='form-control' id='elite${i}LevelDisplay' onchange='changeEliteLevel(this,${i},${keyframes[1].level})' style='line-height:1.1' type='number' value='1' min='1' max='${keyframes[1].level}'></div>`)

        var statsLevelAll = $(`
        <div style='text-align:center'>
        <span class='stat-level-header ${lefthand=="true"?"lefthand-stat-level-header":"righthand-stat-level-header"} ' style=''>Level</span>
        <input type='range' value='1' min='1' max='${keyframes[1].level}' name='levelStats' id='elite${i}LevelSlider' oninput='changeEliteLevel(this,${i},${keyframes[1].level})' style='margin-top:20px;width:60%;' class='statlevelInput ${lefthand=="true"?"lefthand-statlevelInput":"righthand-statlevelInput"}'></input>
        <div class='form-group stat-input ${lefthand=="true"?"lefthand-stat-input":"righthand-stat-input"}' style='display:inline-block;vertical-align:middle;'><input class='form-control' id='elite${i}LevelDisplay' onchange='changeEliteLevel(this,${i},${keyframes[1].level})' style='line-height:1.1' type='number' value='1' min='1' max='${keyframes[1].level}'></div>
        </div>
        `)

        var statsTable = $(`
        <div id='elite${i}Stats' class='${lefthand=="true"?"left-hand":"right-hand"} statlevelcontainer'>
            <table id='elite${i}StatsTable'>
                <tr><td>

                    <div class='stats'><div class='stats-l'>Maximum HP</div><div class='stats-r' id='elite${i}maxHp'></div></div>
                    <div class='stats'><div class='stats-l'>Redeploy Time</div><div class='stats-r' id='elite${i}respawnTime'></div></div>

                    <div class='stats'><div class='stats-l'>Attack Power</div><div class='stats-r' id='elite${i}atk'></div></div>
                    <div class='stats'><div class='stats-l'>Cost</div><div class='stats-r' id='elite${i}cost'></div></div>

                    <div class='stats'><div class='stats-l'>Defense</div><div class='stats-r' id='elite${i}def'></div></div>
                    <div class='stats'><div class='stats-l'>Block</div><div class='stats-r' id='elite${i}blockCnt'></div></div>

                    <div class='stats'><div class='stats-l'>Resistance</div><div class='stats-r' id='elite${i}magicResistance'></div></div>
                    <div class='stats'><div class='stats-l'>Attack Time</div><div class='stats-r' id='elite${i}baseAttackTime'></div></div>
                </tr><td>
                </table>
                ${rangeMaker(opdataFull.phases[i].rangeId)}
                <div>
                ${materialHtml}
                </div>
                </div>
        `);

        statsCollapsible.append(statsLevelAll);
        statsCollapsible.append(statsTable);

        if(i > 0){

            var mats = $("<div class='small-container ak-shadow'>"
                        +   "<p>Elite "+i+"</p>"
                        +   "<span>Required materials</span>"
                        +   "<img class='topright' src='https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/"+i+".png' width='100'>"
                        +   "<button class='btn btn-default btn-collapsible' data-toggle='collapse' data-target='#elite"+i+"MatsCollapsible'><i class='fa fa-sort-down'></i></button>"
                        +   "<div id='elite"+i+"MatsCollapsible' class='collapse collapsible'>"
                        +    materialist.join("")
                        +   "</div></div>");
        }else{
            var mats = $("");
        }
        container.append(stats);
        container.append(statsCollapsible);
        // container.append(mats);
        return container;
    }
    function LinkCheck(url)
    {
        var http = new XMLHttpRequest();
        http.open('HEAD', url, false);
        http.send();
        return http.status!=404;
    }

    function GetLogo (opdataFull){
        if(opdataFull.teamId)
            return "logo_"+opdataFull.teamId
        else if(opdataFull.groupId)
            return "logo_"+opdataFull.groupId
        else if(opdataFull.nationId)
            return "logo_"+opdataFull.nationId

        return null
    }
    function GetLogoInfo (opdataFull){
        var faction
        if(opdataFull.teamId)
            faction= opdataFull.teamId
        else if(opdataFull.groupId)
            faction= opdataFull.groupId
        else if(opdataFull.nationId)
            faction= opdataFull.nationId

        // console.log(faction)

        var factionname = db.handbookTeam[faction]
        // console.log(factionname)
        if (factionname) return factionname

        return null
    }

    function update_illustrator(skinid = ""){
        function IllustratorLister(List){
            var HTML = ""
            for(var i = 0 ; i < List.length; i++){
                ArtistName = List[i].trim()
                if(Object.keys(db.artistTL.Illustrator).includes(ArtistName))
                    ArtistName = db.artistTL.Illustrator[ArtistName]
                if(i > 0)
                    HTML += " & "

                HTML += `<a href="https://www.google.com/search?q=illustrator+${ArtistName}"  target="_blank">${ArtistName}</a>`
            }
            return HTML
        }
        
        let illustratorHTML = ""
        let IllustratorList = [[],[]]
        if(AmiyaPatchID.includes(skinid.split("#")[0]))
            skin = opdataFull.id + "#2"
        else
            skin = skinid?skinid:(currskin + "#1")

        if(db.skintable.charSkins[skin])
            if(db.skintable.charSkins[skin].displaySkin.drawerList){
                IllustratorList[0] = db.skintable.charSkins[skin].displaySkin.drawerList[0].split("、")
                IllustratorList[1] = db.skintable.charSkins[skin].displaySkin.designerList?db.skintable.charSkins[skin].displaySkin.designerList[0].split("、"):""
            }
        else if (db.handbookInfo.npcDict[opdataFull.id])
            IllustratorList[0] = db.handbookInfo.npcDict[opdataFull.id].illustList

        // Drawer
        illustratorHTML = `
            <div class="illustrator-drawer">
                <div class="btn-infoleft ak-shadow">
                    <i class="fas fa-palette" title="Illustrator-Drawer"></i>
                </div>
                <div id="name-illustrator-drawer" class="btn-inforight">
                    ${IllustratorList[0].length > 0?IllustratorLister(IllustratorList[0]):"-"}
                </div>
            </div>`
        
        // Designer
        illustratorHTML += IllustratorList[1].length == 0?"":`
            <div class="illustrator-designer">
                <div class="btn-infoleft ak-shadow">
                    <i class="fas fa-pencil-alt" title="Illustrator-Designer"></i>
                </div>
                <div id="name-illustrator-designer" class="btn-inforight">
                    ${IllustratorLister(IllustratorList[1])}
                </div>
            </div>
            `

        $('#info-illustrator').html(illustratorHTML)
    }
    function VA_lang(voiceLangType = ""){
        const LINKAGE_EN_list = [
                                    "char_456_ash",
                                    "char_457_blitz",
                                    "char_458_rfrost",
                                    "char_459_tachak",
                                    "char_4123_ela",
                                    "char_4124_iana",
                                    "char_4125_rdoc",
                                    "char_4126_fuze"
                                ]
        const LINKAGE_CN_list = [
                                    "char_4019_ncdeer"
                                ]
        const LINKAGE_JP_list = [
                                    "char_4141_marcil",
                                    "char_4142_laios",
                                    "char_4144_chilc",
                                    "char_4143_sensi"
                                ]
        
        switch(voiceLangType) {
            case "LINKAGE":
                if(LINKAGE_EN_list.includes(opdataFull.id))
                    return "EN"
                else if(LINKAGE_CN_list.includes(opdataFull.id))
                    return "CN"
                else if(LINKAGE_JP_list.includes(opdataFull.id))
                    return "JP"
                else 
                    return "None"
            case "CN_MANDARIN":
                return "CN"
            case "CN_TOPOLECT":
                return "CN&#42"
            default:
                return voiceLangType
        }
    }
    function GetAudio(){
        var curraudiolist = []
        var voiceDict = db.charword.voiceLangDict[currVoiceID]
        var checkold = db.voiceold[currVoiceID]
        var preDir = "https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-voices/main/"
        var old_va = ""

        Object.keys(db.charword.charWords).forEach(audio_key => {
            if (db.charword.charWords[audio_key].wordKey == currVoiceID){
                curraudiolist.push(db.charword.charWords[audio_key])
            }
        });

        $('#opaudiocontent').empty()
        $('#opaudio-va').empty()

        curraudiolist.forEach(audio_dict => {
            var voiceTL = audio_dict.voiceText
            var audiolist = []
            var old_audiolist = []
            VAlanglist.forEach(valang => {
                if (!Object.keys(voiceDict).includes(valang))
                    return
                var foldername
                var lang = VA_lang(valang)
                var wordKey = encodeURIComponent(audio_dict.wordKey)
                
                if (audio_dict.voiceId == "CN_043" && ["EN", "KR"].includes(valang)) // temp for EN KR Birthday
                    return

                switch (valang) {
                    case "JP":
                        foldername = "voice"
                        break;
                    case "CN_MANDARIN":
                        foldername = "voice_cn"
                        break;
                    case "EN":
                        foldername = "voice_en"
                        break;
                    case "KR":
                        foldername = "voice_kr"
                        break;
                    case "LINKAGE":
                        foldername = db.charword.LINKAGE[currVoiceID]
                        break;
                    default:
                        foldername = "voice_custom"
                        break;
                }
                
                audiolist.push(`
                    <div id="${valang}-VA" style="display:inline-block;padding-top:15px;vertical-align:top;width:30px;text-align:left;">${lang}</div>
                    <div style="display:inline-block">
                    <audio preload="metadata" controls style="margin-top:10px"> <source src="${preDir}${foldername}/${wordKey.toLowerCase()}${valang == "CN_TOPOLECT"?"_cn_topolect":""}/${audio_dict.voiceId}.mp3" type="audio/mp3">Your browser does not support the audio tag.</audio>
                    <a href="${preDir}${foldername}/${wordKey.toLowerCase()}/${audio_dict.voiceId}.mp3"  target="_blank">
                    <i class='fa fa-download' style='font-size:20px;vertical-align:top;padding-top:17px'></i></a>
                    </div>`)

                if(checkold && checkold[valang] && !["CN_038", "CN_043", "CN_044"].includes(audio_dict.voiceId)){ // New Year, Birthday, Anni
                    old_audiolist.push(`
                    <div id="${valang}-VA0" style="display:inline-block;padding-top:15px;vertical-align:top;width:30px;text-align:left;">${lang}0</div>
                    <div style="display:inline-block">
                    <audio preload="metadata" controls style="margin-top:10px"> <source src="${preDir}voice_old/${foldername}/${audio_dict.voiceAsset}.mp3" type="audio/mp3">Your browser does not support the audio tag.</audio>
                    <a href="${preDir}voice_old/${foldername}/${audio_dict.voiceAsset}.mp3"  target="_blank">
                    <i class='fa fa-download' style='font-size:20px;vertical-align:top;padding-top:17px'></i></a>
                    </div>`)
                }
            });

            var currhtml = $(`
                                <table class="story-table">
                                    <th>${db.storytextTL[audio_dict.voiceTitle]?db.storytextTL[audio_dict.voiceTitle]:audio_dict.voiceTitle}</th>
                                    <tr><td style="text-align:center;background:#1a1a1a;vertical-align:middle">
                                        <div id="audio-displaynum" style="position: absolute;font-weight: 700;font-size:10px;margin-top:0px;color:#999;background:#222;padding:0px;padding-left:2px;padding-right:2px;right:18px">
                                            ${audio_dict.voiceAsset.split("_").slice(-1)[0]}
                                        </div>
                                        ${audiolist.concat(old_audiolist).join(`<tr><td style="text-align:center;background:#1a1a1a;vertical-align:middle">`)}
                                    </td></tr>
                                    <tr><td style="height:10px"></td></tr>
                                    <tr><td>${voiceTL}</td></tr>
                                    <tr><td style="height:10px"></td></tr>
                                </table>
            `)
            $('#opaudiocontent').append($(currhtml))
        });

        VAlanglist.forEach(valang => {
            if (!Object.keys(voiceDict).includes(valang))
                    return
                var lang = VA_lang(valang).split("_")[0]
                $("#" + valang+ "-VA").attr("title", "VA : " + voiceDict[valang])
                $('#opaudio-va').append(`
                                            <div style="text-align:center">
                                                <div class="btn-infoleft" style="width:100px">
                                                    <i class="fas fa-microphone-alt" title="Voice Actor">${lang}</i>
                                                </div>
                                                <div class="btn-inforight" style="width:70%">
                                                    <a href="https://www.google.com/search?q=Voice+Actor+${voiceDict[valang]}"  target="_blank">${voiceDict[valang]}</a>
                                                </div>
                                            </div>
                                        `)
                if (checkold && checkold[valang]){
                    $("#" + valang + "-VA0").attr("title", "VA : " + checkold[valang])
                    old_va += (`
                                            <div style="text-align:center">
                                                <div class="btn-infoleft" style="width:100px">
                                                    <i class="fas fa-microphone-alt" title="Voice Actor">${lang}0</i>
                                                </div>
                                                <div class="btn-inforight" style="width:70%">
                                                    <a href="https://www.google.com/search?q=Voice+Actor+${checkold[valang]}"  target="_blank">${checkold[valang]}</a>
                                                </div>
                                            </div>
                                        `)
                }
        })
        $('#opaudio-va').append(old_va)
    }
    function GetStory (opdataFull){
        // console.log(opdataFull)
        let currStory = db.handbookInfo.handbookDict[opdataFull.id]
        var isEN
        var isAmiya
        if(db.handbookInfoEN.handbookDict[opdataFull.id]){
            currStory = db.handbookInfoEN.handbookDict[opdataFull.id]
            if(opdataFull.id == AmiyaCaster) isAmiya = true
            isEN = true
        }

        if(Object.keys(db.charpatchEN.patchChars).includes(opdataFull.id)) {
            currStory = db.handbookInfoEN.handbookDict[AmiyaCaster]
            console.log("Amiya EN")
            isAmiya = true // Release once medic coom
            isEN = true
        }
        if(Object.keys(db.charpatch.patchChars).includes(opdataFull.id) && !Object.keys(db.charpatchEN.patchChars).includes(opdataFull.id)){
            currStory = db.handbookInfo.handbookDict[AmiyaCaster]
            console.log("Amiya CN")
            isAmiya = true
        }

        update_illustrator()

        var voiceDict = db.charword.voiceLangDict[opdataFull.id]
        var voiceDictEN
        var existvoiceDict = voiceDictEN?{...voiceDict,...voiceDictEN}:voiceDict
        console.log(voiceDict)
        console.log(voiceDictEN)

        var VAlang
        
        VAhtml = ""
        VAlanglist.forEach(valang =>{
            if(existvoiceDict[valang]){
                VAlang = VA_lang(valang)
                VAName = existvoiceDict[valang].trim()
                if(Object.keys(db.artistTL.VA).includes(VAName)) VAName = db.artistTL.VA[VAName]

                VAhtml += `
                            <div class="voiceactor-${VAlang}">
                                <div id="lang-voiceactor-${VAlang}" class="btn-infoleft ak-shadow">
                                    <i class="fas fa-microphone-alt" title="Voice Actor">
                                    </i>
                                    <b ${VAlang.length > 2?`style="font-size:11px"`:""}>
                                        ${VAlang == "None"?"":VAlang}
                                    </b>
                                </div>
                                <div id="name-voiceactor-${VAlang}" class="btn-inforight">
                                    ${VAlang == "None"?VAName:VAName == "-"?VAName:`<a href="https://www.google.com/search?q=Voice+Actor+${VAName}"  target="_blank">${VAName}</a>`}
                                </div>
                            </div>
                        `
            }
        })
        $('#info-voiceactor').html(VAhtml)

        let puretext = []
        let textTL = []
        let islong = false
        puretext.push(opdataFull.appellation)
        puretext.push("")

        //check potential and recruit
        // opdataFull.text

        var recruitcheck = db.charsEN[opdataFull.id]
        if(!recruitcheck) recruitcheck = opdataFull
        if(AmiyaPatchID.includes(opdataFull.id)) recruitcheck = db.charsEN[AmiyaCaster]

        //check potential token
        var pot_token_id = opdataFull.potentialItemId?opdataFull.potentialItemId:opdataFull.activityPotentialItemId
        var pot_token = db.potential_token[pot_token_id]
        console.log(recruitcheck.itemDesc, pot_token_id)


        // post both
        if(recruitcheck.itemDesc){
            textTL.push(`<div class="col-12 ${(!pot_token_id?"col-sm-12":"col-sm-6")} top-buffer storysplit">
                            <table class="story-table"><th colspan=2>Recruitment Contract</th>
                            <tr>
                                <td>${recruitcheck.itemDesc}</td>
                            </tr>
                            <tr>
                                <td>${recruitcheck.itemUsage}</td>
                            </tr></table>
                            </div>`)
            if(pot_token_id){
                textTL.push(`<div class="col-12 col-sm-6 top-buffer storysplit">
                        <table class="story-table"><th colspan=2>${pot_token_id.includes("voucher_")?"Folder":"Token"}</th>
                        <tr>
                            <td>${pot_token.description}</td>
                        </tr>
                        <tr>
                            <td>${pot_token.usage}</td>
                        </tr>
                        </table>
                        </div>`)
            }
        }


        if(currStory.storyTextAudio){
            currStory.storyTextAudio.forEach(storySection => {
                if (isAmiya && !storySection.stories[0].patchIdList.includes(opdataFull.id)) return
                puretext.push(`---------${storySection.storyTitle}-----------`)
                puretext.push(storySection.stories[0].storyText)
                puretext.push("")
                switch(storySection.storyTitle){
                    case "Basic Info":
                    case "基础档案":
                        var basicInfo = storySection.stories[0].storyText.split("\n")
                        var basicInfoTL = []
                        var webTL = []
                        var titlebefore = ""
                        // if(basicInfo.length>20)islong = true;
                        // console.log(basicInfo.length)
                        basicInfo.forEach((info,n) => {
                            var check = isEN? /(\[)(.*)(\])(.*)/ : /(【)(.*)(】)(.*)/
                            var infoTitle = check.exec(info)
                            if(infoTitle){
                                var title = db.storytextTL[infoTitle[2]]?db.storytextTL[infoTitle[2]]:infoTitle[2]
                                var content = infoTitle[4]
                                // console.log(infoTitle)
                                switch (infoTitle[2]) {
                                    case "代号": 
                                        content = opdataFull.appellation;
                                        break;
                                    case "性别":
                                        console.log(content)
                                        content= db.storytextTL[content.trim()]
                                        if (!content) content = infoTitle[4].trim()
                                        $("#op-gender").html(`<i class="fas fa-${content.toLowerCase()}"></i> ${content}`);
                                        break;
                                    case "表演经验":
                                    case "出厂时间":
                                    case "战斗经验":
                                        content= db.storytextTL[content.trim()]
                                        // console.log(infoTitle)
                                        // console.log("WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                                        // console.log(content)
                                        if (!content){
                                            var splitnum = infoTitle[4].trim().split("")
                                            var num = 0
                                            var count = 0
                                            var end = ""
                                            // console.log(splitnum)
                                            splitnum.forEach(eachnum => {
                                                // console.log(eachnum)
                                                // console.log(typeof parseInt(eachnum))
                                                // console.log(parseInt(eachnum))
                                                if(typeof db.storytextTL[eachnum] == "number" ){
                                                    console.log(db.storytextTL[eachnum])
                                                    if(db.storytextTL[eachnum]==10 && count==1){
                                                        num = num*10
                                                    }else{
                                                        num += db.storytextTL[eachnum]
                                                    }
                                                }
                                                else if(typeof parseInt(eachnum)  == "number" && !isNaN(parseInt(eachnum))){
                                                    num += parseInt(eachnum)
                                                }
                                                else{
                                                    end = db.storytextTL[eachnum]
                                                }
                                                // console.log(num)
                                                count++
                                            });

                                            if(num% 1 != 0){
                                                if(num<1){
                                                    num = "Half a"
                                                }else{
                                                    num = Math.floor(num) +" and a half"
                                                }
                                            }
                                            content = `${num} ${end}`
                                        };
                                        break;

                                    case "出厂日":
                                    case "生日":
                                            content = db.storytextTL[content.trim()]?db.storytextTL[content.trim()]:BirthdayText(content);break;
                                    case "矿石病感染情况":
                                        if(db.charastoryTL[opdataFull.id]&&db.charastoryTL[opdataFull.id]["originiumInfection"]&&content){
                                            content = db.charastoryTL[opdataFull.id]["originiumInfection"]
                                        }else if(content){
                                            var datasplit = content.split("，")
                                            // console.log(datasplit)
                                            var arraycontent = []
                                            datasplit.forEach(originiumdesc => {
                                                arraycontent.push(db.storytextTL[originiumdesc]?db.storytextTL[originiumdesc]:originiumdesc)
                                            });
                                            content = arraycontent.join(", ")
                                        }else{
                                            content = db.storytextTL[content.trim()]?db.storytextTL[content.trim()]:content.replace("约","Approximately ");
                                        };
                                        break;
                                    default:
                                        // console.log("WEEI" +titlebefore)
                                        content = db.storytextTL[content.trim()]?db.storytextTL[content.trim()]:content.replace("约","Approximately ");
                                }
                                // console.log(title)
                                titlebefore = title
                                basicInfoTL.push(`[${title}] ${content}`)
                                if(content==""){
                                    webTL.push(`<tr><td colspan="2" style="border-top: 1px solid #555;">${title}</td></tr>`)
                                }else
                                    webTL.push(`<tr><td>${title}</td><td>${content}</td></tr>`)
                            }else{
                                // console.log(info.split("，"))
                                if(titlebefore =="Originium Infection"&& db.charastoryTL[opdataFull.id] && db.charastoryTL[opdataFull.id]["originiumInfection"]){
                                    content = db.charastoryTL[opdataFull.id]["originiumInfection"]
                                    titlebefore=""
                                    webTL.push(`<tr><td colspan=2>${content}</td> </tr>`)
                                }else{
                                    var datasplit = info.split("，")
                                    var content = []
                                    datasplit.forEach(originiumdesc => {
                                        content.push(db.storytextTL[originiumdesc]?db.storytextTL[originiumdesc]:originiumdesc)
                                    });
                                    webTL.push(`<tr><td colspan=2>${content.join(", ")}</td> </tr>`)
                                }
                                // else{
                                //     basicInfoTL.push(info)
                                //     webTL.push(`<tr><td colspan=2>${info}</td> </tr>`)
                                // }
                            }
                        });
                        textTL.push(`<div class="col-12 ${(islong?"":"col-sm-6")} top-buffer storysplit">
                                        <table class="story-table"><th colspan=2>Basic File</th>${webTL.join("")}</table>
                                    </div>`)
                        // textTL.push(basicInfoTL.join("</br>"))
                        // console.log(basicInfoTL.join("\n"));
                        break;
                    case "Physical Exam" :
                    case "Performance Review":
                    case "综合性能检测结果" :
                    case "综合体检测试" :
                        var basicInfo = storySection.stories[0].storyText.split("\n")
                        var basicInfoTL = []
                        var webTL = []
                        basicInfo.forEach(info => {
                            var check = isEN?/(\[)(.*)(\])(.*)/:/(【)(.*)(】)(.*)/
                            var infoTitle = check.exec(info)
                            if(infoTitle){
                                var title = db.storytextTL[infoTitle[2]]?db.storytextTL[infoTitle[2]]:infoTitle[2]
                                var content = infoTitle[4]
                                switch (infoTitle[2]) {
                                    case "代号": content = opdataFull.appellation;break;
                                    default: content = db.storytextTL[content.trim()]?db.storytextTL[content.trim()]:content;
                                }
                                basicInfoTL.push(`[${title}] ${content}`)
                                webTL.push(`<tr><td>${title}</td> <td>${content}</td></tr>`)
                            }
                        })
                        // textTL.push(`<h2>Comprehensive test</h2>${basicInfoTL.join("</br>")}`)
                        textTL.push(`<div class="col-12 ${(islong?"":"col-sm-6")} top-buffer storysplit">
                                        <table class="story-table">
                                        <th colspan=2>${db.storytextTL[storySection.storyTitle]?db.storytextTL[storySection.storyTitle]:storySection.storyTitle}</th>
                                        ${webTL.join("")}</table>
                                    </div>`)
                        // console.log(basicInfoTL.join("\n"))
                        ;break;
                    default:
                        var currstory
                        // console.log(storySection.storyTitle)
                        // console.log(db.charastoryTL[opdataFull.id])
                        if(db.charastoryTL[opdataFull.id]&&db.charastoryTL[opdataFull.id][storySection.storyTitle])
                            currStory = db.charastoryTL[opdataFull.id][storySection.storyTitle].split("\n").join("</br>")
                        else
                            currStory = (storySection.stories[0].storyText.replace(/■/g,"■ ")).split("\n").join("</br>")
                        // console.log(currstory)
                        textTL.push(`<div class="col-12 top-buffer">
                                        <table class="story-table">
                                        <th colspan=2>${db.storytextTL[storySection.storyTitle]?db.storytextTL[storySection.storyTitle]:storySection.storyTitle}</th>
                                        <tr><td>${currStory}</td></tr></table>
                                    </div>`)
                        // textTL.push(`<h2>${storySection.storyTitle}</h2>`)
                        // textTL.push(`</br>`)
                        // textTL.push()
                        // console.log(`---------${storySection.storyTitle}-----------`)
                        // console.log(storySection.stories[0].storyText)
                    }
            });
        }
        if(db.charastoryTL[opdataFull.id]&&db.charastoryTL[opdataFull.id]["credit"]) $("#opstorycredits").html(`<div class="btn-infoleft">Trust Translation</div><div class="btn-inforight">${db.charastoryTL[opdataFull.id]["credit"]}</div>`)
        else $("#opstorycredits").html(``)

        if(isEN){
            $('#opstorycredits').html(`<div class="btn-infoleft">Trust Translation</div><div class="btn-inforight">Official EN Arknights</div>`)
        }
        $("#opstorycontent").html(`<div class="row storyrow">${textTL.join("")}</div>`)
        // console.log(textTL)
        //console.log(puretext.join("\n"))
    }

    function UpdateElite(elite){
        // console.log("waaaaaaaaaaaaaaaaaaa")
        // opdataFull.skills.forEach(i => {
            // console.log(elite)
        globalelite = elite
        UpdateTokenContent(false)
        changeEliteLevel($("#elite"+elite+"LevelSlider"),elite,$("#elite_"+elite+"_maxLv").html())
        $.each(opdataFull.skills,function(i,v){
            // console.log(i)
            var skillId = opdataFull.skills[i].skillId;
            var skillData = db.skills[skillId];
            $.each(skillData.levels,function(i2,v2){
                skillData.levels[i2].blackboard.forEach(skillinfo => {
                    if(skillinfo.key == "ability_range_forward_extend"){
                        allrange = new Set(opdataFull.phases.map(phase => phase.rangeId))
                        if (allrange.size - 1){
                            if (i===2 || i2 + 1 >= 8) $(`#skill${i}lv${i2}grid`).html(rangeMaker(opdataFull.phases[2].rangeId, true, skillinfo.value, "E2"))
                            else if (i===1 || i2 + 1 >= 5) $(`#skill${i}lv${i2}grid`).html(rangeMaker(opdataFull.phases[Math.max(1, globalelite)].rangeId, true, skillinfo.value, "E" + Math.max(1, globalelite)))
                            else $(`#skill${i}lv${i2}grid`).html(rangeMaker(opdataFull.phases[globalelite].rangeId, true, skillinfo.value, "E" + globalelite))
                        }else{
                            $(`#skill${i}lv${i2}grid`).html(rangeMaker(opdataFull.phases[i].rangeId, true, skillinfo.value))
                        }
                    }
                });
            })
        });
    }

    function BirthdayText(date) {
        console.log(date)
        var check = date.split("月")
        if(check[1]){
            var check2 = check[1].split("日")
            var check = `${check[0]}/${check2[0]}`
            var date = check.split("/")
            // console.log(date)
            if (date.length >=2)
            {
                // console.log(date[1])
                const currmonth = date[0]
                const currday = date[1]
                const monthNames = ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
                ];
                // console.log(`${monthNames[currmonth-1]} ${currday}`)
                // console.log(monthNames[currmonth-1])
                if (monthNames[currmonth-1] == undefined){
                    return date
                }
                return  monthNames[currmonth-1] + " " + currday
            }
        }else return date

    }

    function GetSFX(opdataFull){
        $('#opsfxcontent').empty()
        console.log(opdataFull.id)
        var preDir = "https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-voices/main/"
        var filteredFX = []
        console.log(opdataFull)
        db.audio_data.soundFXBanks.forEach(element => {
            if(element.name.includes(opdataFull.id)){
                // console.log(element.name)
                element.sounds.forEach(soundfx => {
                    var fxname = soundfx.asset.split("/")
                    var fxdir = soundfx.asset.split("/").splice(2,2).join("/").toLowerCase()+"/"+fxname[fxname.length-1]
                    filteredFX.push({name:fxname[fxname.length-1],dataname:element.name,dir:fxdir,type:"1"})
                });
            }
            // console.log("_chr_"+opdataFull.id.split("_")[2])
            opdataFull.skills.forEach(skill => {
                if(element.name.includes(skill.skillId)){
                    // console.log(element.name)
                    element.sounds.forEach(soundfx => {
                        var fxname = soundfx.asset.split("/")
                        var fxdir = soundfx.asset.split("/").splice(2,2).join("/").toLowerCase()+"/"+fxname[fxname.length-1]
                        filteredFX.push({name:fxname[fxname.length-1],dataname:element.name,dir:fxdir,type:"2"})
                    });
                }
            });
            if(element.name.includes("_chr_"+opdataFull.id.split("_")[2])){
                element.sounds.forEach(soundfx => {
                    var fxname = soundfx.asset.split("/")

                    var fxdir = soundfx.asset.split("/").splice(2,2).join("/").toLowerCase()+"/"+fxname[fxname.length-1]
                    console.log(fxdir)
                    filteredFX.push({name:fxname[fxname.length-1],dataname:element.name,dir:fxdir,type:"3"})
                });
            }
            if(element.name.includes(globaltoken)){
                // console.log(element.name)
                element.sounds.forEach(soundfx => {
                    var fxname = soundfx.asset.split("/")
                    var fxdir = soundfx.asset.split("/").splice(2,2).join("/").toLowerCase()+"/"+fxname[fxname.length-1]
                    filteredFX.push({name:fxname[fxname.length-1],dataname:element.name,dir:fxdir,type:"4"})
                });
            }


        });
        console.log(filteredFX)
        filteredFX =filteredFX.sort(function(a,b){
            if(a.type>b.type)return 1
            else if(a.type<b.type)return -1
            else return 0
        })
        console.log(filteredFX)
        var sfxnum = 0
        filteredFX.forEach(element => {
            var fxdir = element.dir
            var fxname = element.name
            var fxdataname = element.dataname
            var fxExt = "wav"
            if(fxdir.includes("voice")){
                fxExt = "mp3"
            }
            var curraudio  =`<audio class="sfxplayer" preload="metadata" controls style="margin-top:5px"> <source src="${preDir}${fxdir}.${fxExt}" type="audio/${fxExt}">Your browser does not support the audio tag.</audio> `
            var currhtml = $(`
            <table class="sfx-table">
            <th>${fxdataname}</th>
            <tr><td style="text-align:center;background:#1a1a1a">${curraudio} <a href="${fxdir}.${fxExt}"  target="_blank">
            <i class='fa fa-download' style='font-size:30px;vertical-align:top;padding-top:17px'></i></a>
            <div id="audio-displaynum" style="position: absolute;font-weight: 700;font-size:10px;margin-top:-50px;color:#999;background:#222;padding:0px;padding-left:2px;padding-right:2px;right:18px">${fxname}</div>
            </td></tr>
            </table>

            `)
            $('#opsfxcontent').append($(currhtml))
            sfxnum +=1
        });
        $(".sfxplayer").each(function(a){
            $(".sfxplayer")[a].volume = 0.3;
        })
    }
    function GetPotential(opdataFull){
        var potentials = opdataFull.potentialRanks
        var potentialsTL = []
        // console.log(potentials)
        var potRegex = /(.*?)([-]|[+])(\d*)(.*)|(.*)/
        potentials.forEach(element => {
            let regexDesc = potRegex.exec(element.description)
            // console.log(regexDesc)
            let currDesc = (regexDesc[1]?regexDesc[1]:regexDesc[5])
            let tlDesc = query(db.potentialTL,"skill_cn",currDesc).skill_en
            tlDesc = tlDesc?tlDesc:currDesc
            if(regexDesc[1]){
                tlDesc += " "+regexDesc[2] + regexDesc[3]
            }
            // console.log(tlDesc)
            potentialsTL.push(tlDesc)
        });
        return potentialsTL
    }

    function GetRiic(opdata2){
        var charaRiic = db.build.chars[Object.keys(opdata2)[0]]
        var riicList = []
        var everybuff = []
        var riicTab = []
        var riiccontent = []
        var activeLevel = 0
        var activeElite = 0
        if(!charaRiic){
            $("#op-riic").html("")
            return
        }
        charaRiic.buffChar.forEach(eachbuffchar => {
            everybuff.push(eachbuffchar.buffData)
            eachbuffchar.buffData.forEach(eachbuffdata => {
                var checkphase = riicList.find(search => search.phase == eachbuffdata.cond.phase && search.level == eachbuffdata.cond.level)
                if(!checkphase){
                    riicList.push({phase:eachbuffdata.cond.phase, level:eachbuffdata.cond.level, list:[]})
                }
            });
        });

        if (riicList.length == 0){
            $("#op-riic").html("")
            return
        }
        riicList = riicList.sort((a, b)=>{
            var calc = 0
            calc += (PhaseConvert(a.phase) - PhaseConvert(b.phase)) * 100
            + (a.level - b.level) * 1

            console.log(calc)
            return calc
        })

        riicList.forEach(eachcat =>{
            // checkphase.list.push(eachbuffdata.buffId)
            var currlevel = eachcat.level
            var currphase = PhaseConvert(eachcat.phase)
            var imagereq =[]
            if(currphase >= 0)
                imagereq.push(`<img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/${currphase}.png" style="width:18px;margin-top:-5px">`)
            if(currlevel > 1)
                imagereq.push(`<span style='font-size:11px;margin-left:-2px'><span style='font-size:6px'>Lv.</span>${currlevel}</span>`)

                riicTab.push(`
            <li class='nav-item' style="" title='Elite ${currphase} | Level ${currlevel} '>
                <button class='btn horiz-small nav-link talentlink' data-toggle='pill' id='tabriic${currphase}-${currlevel}' href="#riic${currphase}-${currlevel}" style="padding:0px 0px;margin:0px 2px 0px 0px;background:#666;width:50px">
                ${imagereq.join("")}
                </button>
            </li>
            `)

            if(currphase == 2 && activeElite < 2){
                activeElite = 2
                activeLevel = currlevel
            }
            if(currphase == 1 && activeElite <= 1){
                activeElite = 1
                if(activeLevel < currlevel){
                    activeLevel = currlevel
                }
            }
            if(currphase == 0 && activeElite <= 0){
                activeElite = 0
                if(activeLevel < currlevel){
                    activeLevel = currlevel
                }
            }

            everybuff.forEach(eachbuff => {
                var sortedbuff = eachbuff.sort((a, b) => {
                    if(a.cond.phase < b.cond.phase) return 1
                    if(a.cond.phase > b.cond.phase) return -1
                    if(a.cond.level < b.cond.level) return 1
                    if(a.cond.level > b.cond.level) return -1
                    return 0
                })
                for(i = 0; i < sortedbuff.length; i++){
                    if(eachcat.phase >= sortedbuff[i].cond.phase && eachcat.level >= sortedbuff[i].cond.level){
                        eachcat.list.push(sortedbuff[i].buffId)
                        break;
                    }
                }
            });

            var riicskills = []

            eachcat.list.forEach(id => {
                var currbuff = db.build.buffs[id]
                var currname = currbuff.buffName
                var currdesc = currbuff.description
                var formattedesc = ChangeDescriptionColor2(currdesc)
                formattedesc = formattedesc.replace(/\\n/g, "<br>")
                riicskills.push(`
                <div class="" style="background:#444;margin:4px;padding:0px;border-radius:2px;text-align:left">
                    <div style="background:#999;display:inline-block;padding:2px;width:100%;border-radius:2px 2px 0px 0px;position:relative;height:33px">
                        <img loading='lazy' id="op-riicdetail-img" src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/infrastructure/skill/${currbuff.skillIcon}.png" style="border-radius:50%;background:#333;padding:3px;position:absolute;left:2px;top:2px;width:30px" title=""></img>
                        <div id="op-riicdetail-name" style="display:inline-block;color:#ddd;font-size:13px;background:#333;padding:2px 5px 2px 12px;border-radius:0px 6px 6px 0px;margin:3px 2px 2px 18px;z-index:1">
                            ${currname}
                        </div>
                    </div>
                    <div style="display:inline-block;margin:4px">
                        <div id="op-riicdetail-desc" style="font-size:11px;">
                            ${formattedesc}
                        </div>
                    </div>
                </div>
                `)
            });
            riiccontent.push(`
                <div class='tab-pane container' id='riic${currphase}-${currlevel}'>
                    ${riicskills.join("")}
                </div>
            `)
        })

        var combinehtml =`
            <div style="color:#fff;text-align:center;background:#333;padding-bottom:0px">Infrastructure Skills</div>
                <div class="ak-shadow" style="margin-bottom:8px;padding:0px;padding-bottom:2px;background:#666">
                    <div style="width:100%;background:#444;display:inline-flex;justify-content:space-between">
                        <ul class='nav nav-pills' id='riic-tabs' style="margin: 0px 0px 0px 0px;width:unset">
                            ${riicTab.join("")}
                        </ul>
                    </div>
                    <div class="tab-content" id="riic-contents" style="margin: 2px 0px 2px 0px;">
                        ${riiccontent.join("")}
                    </div>
                </div>
        `
        $("#op-riic").html(combinehtml)

        $(`#tabriic${activeElite}-${activeLevel}`).toggleClass("active")
        $(`#riic${activeElite}-${activeLevel}`).toggleClass("active")
    }

    function ShowRiicDetail(id,title,desc,img){
        if($("#op-riicdetail").is(":visible")&&$("#op-riicdetail-name").html()==title){
            $("#op-riicdetail").slideUp(200)
        }else{
            var currbuff = db.build.buffs[id]
            var currname = currbuff.buffName
            var currdesc = currbuff.description
            var formattedesc = ChangeDescriptionColor2(currdesc)

            console.log(currname)
            console.log(currdesc)
            $("#op-riicdetail-img").attr("src",img)
            $("#op-riicdetail-name").text(title)
            formattedesc = formattedesc.replace(/\\n/g,"<br><br>")
            $("#op-riicdetail-desc").html(formattedesc)
            $("#op-riicdetail").slideDown(200)
        }
        tooltip_activate()
    }
    function GetTalent(id,opdataFull){
        // var combTalents = []
        var talenthtml = []
        var talentnum = 0
        var talenttype = 0
        var talentObject = {req:[],req2:[],talents:[],html:{}}
        var talentTab = []
        var talentTab2 = []
        var elitelevel = []
        var potential = []
        var activeLevel = 0
        var activeElite = 0
        var activePotential = 0
        var lastPotential = 0
        opdataFull.talents.forEach(currTalent => {
            currTalent.candidates.forEach(currCandidate => {
                var currlevel = parseInt(currCandidate.unlockCondition.level)
                var currphase = PhaseConvert(currCandidate.unlockCondition.phase)
                var currpotent = parseInt(currCandidate.requiredPotentialRank)
                if(!talentObject.req.includes(`${currphase}-${currlevel}-${currpotent}`,0)){
                    talentObject.req.push(`${currphase}-${currlevel}-${currpotent}`)
                    talentObject.req2.push([currphase,currlevel,currpotent])
                    talentObject.html[`${currphase}-${currlevel}-${currpotent}`]={req:[currphase,currlevel,currpotent],talents:[]}

                    if(currphase==2&&activeElite<2){
                        activeElite=2
                        activeLevel=currlevel
                    }
                    if(currphase==1&&activeElite<=1){
                        activeElite=1
                        if(activeLevel<currlevel){
                            activeLevel= currlevel
                        }
                        if(opdataFull.rarity<=2&&activePotential<currpotent){
                            activePotential = currpotent
                        }
                    }
                    if(currphase==0&&activeElite<=0){
                        activeElite=0
                        if(activeLevel<currlevel){
                            activeLevel= currlevel
                        }
                        if(opdataFull.rarity<=2&&activePotential<currpotent){
                            activePotential = currpotent
                        }
                    }
                }
                lastPotential = currpotent
            });
            // Add extra Talent slot for non-E2 upgrade talent like Marcille, Exuter
            if(RarityConvert(opdataFull.rarity.toString()) > 2 && activeElite < 2){
                for(i = activeElite + 1; i <= 2; i++){
                    talentObject.req.push(`${i}-${activeLevel}-0`)
                    talentObject.req2.push([i,activeLevel,0])
                    talentObject.html[`${i}-${activeLevel}-0`]={req:[i,activeLevel,0],talents:[]}
                    if (lastPotential > 0) {
                        talentObject.req.push(`${i}-${activeLevel}-${lastPotential}`)
                        talentObject.req2.push([i,activeLevel,lastPotential])
                        talentObject.html[`${i}-${activeLevel}-${lastPotential}`]={req:[activeElite,activeLevel,lastPotential],talents:[]}
                    }
                }
            }
        });
        // console.log(activeElite)
        // console.log(activeLevel)
        // console.log(activePotential)

        console.log(talentObject)
        talentObject.req2 = talentObject.req2.sort((a,b)=>{
            var calc = 0
            calc =+ (a[0]-b[0])*100
            + (a[1]-b[1])*10
            + (a[2]-b[2])*1
            return calc
        })
        talentLimit = talentObject.req2
        talentObject.req2.forEach(reqs => {
            var imagereq = []
            var currlevel = reqs[1]
            var currphase = reqs[0]
            var currpotent = reqs[2]
            var elreq = `${currphase}${currlevel}`
            if(!elitelevel.includes(elreq)){
                if(currphase >=0)
                    imagereq.push(`<img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/${currphase}.png" style="width:18px;margin-top:-5px">`)
                if(currlevel >1)
                    imagereq.push(`<span style='font-size:11px;margin-left:-2px'><span style='font-size:6px'>Lv.</span>${currlevel}</span>`)

                talentTab.push(`
                <li class='nav-item' style="" title='Elite ${currphase} | Level ${currlevel} '>
                    <button class='btn horiz-small nav-link talentlink' data-toggle='pill' id='tabtalent${currphase}-${currlevel}' onclick='TalentShow(${currphase},${currlevel},-1)' style="padding:0px 0px;margin:0px 2px 0px 0px;background:#666;width:50px">
                    ${imagereq.join("")}
                    </button>
                </li>
                `)
                elitelevel.push(elreq)
            }


            var imagereq = []
            if(!potential.includes(currpotent)){

                potential.push(currpotent)
            }
        });

        potential = potential.sort((a,b)=>{
            return a-b
        })
        potential.forEach(currpotent => {
            var imagereq = []
            if(currpotent+1 >0)
                imagereq.push(`<img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/potential/${currpotent+1}.png" style="width:18px"> ${currpotent+1}`)
            talentTab2.push(`
            <li class='nav-item' style="" title='Potential ${currpotent+1}'>
                <button class='btn horiz-small nav-link talentlink talenttabpot' data-toggle='pill' id='tabtalent2${currpotent}' onclick='TalentShow(-1,-1,${currpotent})' style="padding:0px 0px;margin:0px 0px 0px 2px;background:#666;width:50px">
                ${imagereq.join("")}
                </button>
            </li>
            `)
        });

        // console.log(talentObject.req2)
        for(i=0;i<opdataFull.talents.length;i++){
            var currTalent = opdataFull.talents[i]
            // if(!db.talentsTL[id])break;
            var currTalentEN = db.charsEN[charName]?db.charsEN[charName].talents[i]:db.charpatchEN.patchChars[charName]?db.charpatchEN.patchChars[charName].talents[i]:undefined
            var currTalentTL = db.talentsTL[id]?db.talentsTL[id][i]:undefined
            // var talentGroup = []
            talentObject.talents[talenttype]=[]
            for(j=0;j<currTalent.candidates.length;j++){
                var currCandidate = currTalent.candidates[j]
                var currCandidateEN = currTalentEN?currTalentEN.candidates[j]:undefined
                var currCandidateTL = currTalentTL?currTalentTL[j]:undefined
                // talentGroup.push({talent:currCandidate,talentTL:currCandidateTL})
                var currlevel = parseInt(currCandidate.unlockCondition.level)
                var currphase = PhaseConvert(currCandidate.unlockCondition.phase)
                var currpotent = parseInt(currCandidate.requiredPotentialRank)
                talentObject.req2.forEach(requirements => {
                    if(requirements[0]>=currphase&&requirements[1]>=currlevel&&requirements[2]>=currpotent){
                        talentObject.html[`${requirements[0]}-${requirements[1]}-${requirements[2]}`].talents[talenttype]={talent:currCandidate,talentEN:currCandidateEN,talentTL:currCandidateTL}
                    }
                });

            }
            talenttype+=1
            // combTalents.push(talentGroup)
        }
        var talenthtml = ''
        var talentnum = 0
        Object.keys(talentObject.html).forEach(key => {
            var currhtml = talentObject.html[key]
            talenthtml += `
            <div class='tab-pane container alltalentinfo' id='talent${key}'>
            `
            Object.keys(currhtml.talents).forEach(eachtalent => {
                var currtalent = currhtml.talents[eachtalent]

                if (currtalent.talent.isHideTalent)
                    return
                //console.log(currtalent)
                talenthtml +=`
                ${TalentParse2(currtalent,talentnum)}
                `
                talentnum +=1
            });
            talenthtml +=`
            </div>
            `
        });
        // console.log(talenthtml)

        // console.log(talentObject)
        $("#op-talentlist").html(`
        <div style="padding-top:10px">
            <div style="color:#fff;text-align:center;background:#333;padding-bottom:0px">Talents</div>
                <div class="ak-shadow" style="margin-bottom:8px;padding:0px;padding-bottom:2px;background:#666">
                    <div style="width:100%;background:#444;display:inline-flex;justify-content:space-between">
                        <ul class='nav nav-pills' id='talent-tabs' style="margin: 0px 0px 0px 0px;width:unset">
                            ${talentTab.join("")}
                        </ul>
                        <ul class='nav nav-pills' id='talent2-tabs' style="margin: 0px 0px 0px 0px;width:unset;justify-content:right">
                            ${talentTab2.join("")}
                        </ul>
                    </div>
                    <div class="tab-content" id="talents-contents" style="margin: 2px 0px 2px 0px;">
                        ${talenthtml}
                    </div>
                </div>
        </div>
        `)

        //active talent tab E2P1/3*2*1* Max pot  (avoid talent 1 max at E1 case eg. Marcille Exuter)
        let limElite    = Math.max(...talentLimit.map(a=>a[0]))
        let limLevel    = Math.max(...talentLimit.map(a=>a[1]))
        let limPotential= (RarityConvert(opdataFull.rarity.toString()))>2?0:Math.max(...talentLimit.map(a=>a[2]))
        TalentShow(limElite,limLevel,limPotential)
        $(`#tabtalent${limElite}-${limLevel}`).toggleClass("active")
        $(`#tabtalent2${limPotential}`).toggleClass("active")
    }

    function TalentShow(elite,level,potential){
        var waspot = potential

        if(elite == -1) elite = talentValue[0]
        if(level == -1) level = talentValue[1]
        if(potential == -1) {
            potential = talentValue[2]
        }

        // console.log(talentLimit)
        // console.log(`${elite}-${level}-${potential}`)
        // console.log(talentLimit.includes(`${elite}-${level}-${potential}`))
        var currlimit = talentLimit.find(limit =>{
            if(`${limit[0]}-${limit[1]}-${limit[2]}`==`${elite}-${level}-${potential}`){
                return true
            }
            return false
        })

        if (currlimit){
            $(`.alltalentinfo`).removeClass("active")
            $(`#talent${elite}-${level}-${potential}`).addClass("active")
        }else{
            var maxpot = 0
            if(waspot == -1){
                talentLimit.forEach(limit => {
                    if(limit[0]==elite&&limit[1]==level){
                        maxpot = Math.max(maxpot,limit[2])
                    }
                });
                console.log(maxpot)
                $(`.talenttabpot`).removeClass("active")
                $(`#tabtalent2${maxpot}`).toggleClass("active")
                $(`.alltalentinfo`).removeClass("active")
                $(`#talent${elite}-${level}-${maxpot}`).addClass("active")
                potential = maxpot
            }else{

            }
        }





        // $(`#tabtalent${elite}-${level}`).toggleClass("active")




        talentValue = [elite,level,potential]
    }

    function GetMastery(id){
        const Roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
        var masteryHTML     = ""
        var char_masters    = db.special_operator[id].proficiency
        var char_unlock     = db.special_operator[id].unlock
        var masteryKey      = Object.keys(char_masters)
        var masteryArray    = Array.from(Object.keys(char_masters), (key) => char_masters[key])
        var masteryNAV      = ""
        var masteryContent  = ""

        for(i = 0; i < masteryArray.length; i++){
            content = ""
            for(j = 0; j < masteryArray[i].length; j++){
                content += `<div style="background:#444;margin:4px;padding:2px;padding-top:2px;border-radius:2px;">
                                <div style="vertical-align:top;">
                                    <div style="color: #222; font-size: 13px; background: #999; display: inline-block; padding: 2px; border-radius: 2px">
                                        <div style="color: #999; background: #222; display: inline-block; padding: 1px; padding-left: 3px; padding-right: 3px; border-radius: 2px">
                                            <img src="extra/Level/level_${i + 1}.png" style="width: 20px; margin-top: -5px" title="Mastery ${i + 1}">
                                        </div>
                                        ${masteryArray[i][j].name}
                                        <div style="color:#999;background:#222;display:inline-block;padding:1px;padding-left:3px;padding-right:3px;border-radius:2px"><span style="font-size:10px">Lv.</span>${j + 1} </div>
                                    </div>
                                    <div style="font-size:13px; font-family:'Source Sans Pro'">
                                        <div class="ak-line">
                                            ${ChangeDescriptionColor2(masteryArray[i][j].description)}
                                        </div>
                                    <button id="masterydetailtitle-${i + 1}-${j + 1}" class="btn btn-sm btn-block ak-btn" onclick='SlideToggler2("masterydetailcontent-${i + 1}-${j + 1}",$(this))' style="display:inline-block;color:#aaa;text-align:center;background:#333;padding:2px;font-size:12px">
                                        Unlock Requirements <i class="fas fa-caret-down"></i>
                                    </button>
                                    <div id="masterydetailcontent-${i + 1}-${j + 1}" class="ak-shadow masterydetailcontent" style="display:none;padding-top:10px;padding:2px;background:#666">
                                        <div class="SO-Unlock">
                                            ${ChangeDescriptionColor2(char_unlock[masteryKey[i]][j])}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>`
            }//${Roman[i]}
            masteryNAV += `<li class="nav-item" style="" title="Mastery ${i + 1}">
                                <button class="btn horiz-small nav-link talentlink masterytab" data-toggle="pill" id="Mastery${i + 1}" onclick="MasteryShow(${i + 1})" style="padding: 0px 0px; margin: 0px 2px 0px 0px; background: #666; width: 48px">
                                    <img src="extra/Level/level_${i + 1}.png" style="width: 20px; margin-top: -5px" title="Mastery ${i + 1}">
                                </button>
                            </li>`
            masteryContent +=`<div class="tab-pane container allmasteryinfo" id="Mastery${i + 1}-content">
                                ${content}
                            </div>`
        }
        
        masteryHTML = `<div style="padding-top: 10px">
                            <div style="color: #fff; text-align: center; background: #333; padding-bottom: 0px">
                                Proficiency
                            </div>
                            <div class="ak-shadow" style="margin-bottom: 8px; padding: 0px; padding-bottom: 2px; background: #666">
                                <div style="width: 100%; background: #444; display: inline-flex; justify-content: space-between">
                                    <ul class="nav nav-pills" id="mastery-tabs" style="margin: 0px 0px 0px 0px; width: unset; justify-content: right">
                                        ${masteryNAV}
                                    </ul>
                                </div>
                                <div class="tab-content" id="mastery-contents" style="margin: 2px 0px 2px 0px;">
                                    ${masteryContent}
                                </div>
                            </div>
                        </div>
                        `
        
        $("#op-masterlist").html(masteryHTML)
        MasteryShow("1")
    }

    function MasteryShow(tab){
        $(`.masterytab`).removeClass("active")
        $(`.allmasteryinfo`).removeClass("active")
        $(`#Mastery${tab}-content`).toggleClass("active")
        $(`#Mastery${tab}`).toggleClass("active")
    }

    function GetModuleTalent(DataBundle,moduleKey,modulenum,phase,range_id=""){
        var potentialTab = []
        var activePotential = 0
        var ModuleTalenthtml = ''
        var TalentDataBundle = null
        var tempBlackboard=[[],[],null]

        for(i=0;i<DataBundle.length;i++){
            if (DataBundle[i].target.includes('TALENT')){
                for(j=0;j<DataBundle[i].addOrOverrideTalentDataBundle.candidates.length;j++){
                    tempBlackboard[j].push(...DataBundle[i].addOrOverrideTalentDataBundle.candidates[j].blackboard)
                    if(DataBundle[i].addOrOverrideTalentDataBundle.candidates[j].rangeId != null) tempBlackboard[2]=DataBundle[i].addOrOverrideTalentDataBundle.candidates[j].rangeId
                    if(DataBundle[i].addOrOverrideTalentDataBundle.candidates.length==1) tempBlackboard[1].push(...DataBundle[i].addOrOverrideTalentDataBundle.candidates[j].blackboard)
                }
                if(DataBundle[i].addOrOverrideTalentDataBundle.candidates[0].name!=null && DataBundle[i].isToken == false && TalentDataBundle == null) {
                    TalentDataBundle=DataBundle[i].addOrOverrideTalentDataBundle.candidates
                }
            }
        }
        for(k=0;k<TalentDataBundle.length;k++){
            TalentDataBundle[k].blackboard.push(...tempBlackboard[k])
            TalentDataBundle[k].blackboard=[...new Set(TalentDataBundle[k].blackboard)]
            if(tempBlackboard[2] != null) TalentDataBundle[k].rangeId=tempBlackboard[2]
        }

        if (TalentDataBundle[0].talentIndex==-1) var upgradeTalent='Addition Talent'
        else var upgradeTalent='Talent Upgrade'

        for(i=0;i<TalentDataBundle.length;i++) {
            var imagereq = []
            var currpotent = parseInt(TalentDataBundle[i].requiredPotentialRank)
            activePotential = currpotent
            if(currpotent+1 >0)
                imagereq.push(`<img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/potential/${currpotent+1}.png" style="width:18px"> ${currpotent+1}`)
            potentialTab.push(`
            <li class='nav-item' style="" title='Potential ${currpotent+1}'>
                <button class='btn horiz-small nav-link talentlink Moduletalenttabpot ${(currpotent!=0 ? '' : 'active')}' data-toggle='pill' id='Modtabtalent-${modulenum}-${phase}-${currpotent}' onclick='ModuleTalentShow(${modulenum},${phase},${currpotent})' style="padding:0px 0px;margin:0px 0px 0px 2px;background:#666;width:50px">
                ${imagereq.join("")}
                </button>
            </li>
            `)

            var currTalent = TalentDataBundle[i]
            var currTalentTL = db.ModuleTL[moduleKey]?db.ModuleTL[moduleKey][phase-1][i]:undefined
            var currTalentEN = undefined

            if(moduleKey in db.battle_equipEN){
                for(part=0;part<db.battle_equipEN[moduleKey].phases[phase].parts.length;part++){
                    var EN =db.battle_equipEN[moduleKey].phases[phase].parts[part]
                    if(phase>0  &&EN.addOrOverrideTalentDataBundle.candidates!==null&& EN.isToken==false&&part.target != "DISPLAY"){
                        if(EN.addOrOverrideTalentDataBundle.candidates[0].name!==null){
                         currTalentEN = db.battle_equipEN[moduleKey].phases[phase].parts[part].addOrOverrideTalentDataBundle.candidates[i]
                         break
                         }
                    }
                }
            }

            console.log(currTalent)
            console.log(currTalentTL)
            console.log(currTalentEN)

            ModuleTalenthtml += `
                <div class='tab-pane container ModuleTalentinfo ${(currpotent==0?'active':'')}' id='ModuleTalent-${modulenum}-${phase}-${currpotent}'>
                    ${ModuleTalentParse(currTalent,currTalentTL,currTalentEN,modulenum,phase,currpotent,range_id)}
                </div>
            `
        }

        return `
            <div style="padding-top:10px">
                <div style="color:#fff;text-align:center;background:#333;padding-bottom:0px">
                    ${upgradeTalent}
                </div>
                <div class="ak-shadow" style="margin-bottom:8px;padding:0px;padding-bottom:2px;background:#666">
                    <div style="width:100%;background:#444;display:inline-flex;justify-content:space-between">
                        <ul class='nav nav-pills' id='potential-tabs' style="margin: 0px 0px 0px 0px;width:unset;justify-content:right">
                            ${potentialTab.join("")}
                        </ul>
                    </div>
                    <div class="tab-content" id="ModuleTalent-contents-${modulenum}-${phase}" style="margin: 2px 0px 2px 0px;">
                        ${ModuleTalenthtml}
                    </div>
                </div>
            </div>
            `
    }

    function ModuleTalentParse(CN,TL,EN,modulenum,phase,currpotent,range_id=""){
        var imagereq = []
        if(CN.requiredPotentialRank+1>0)
            imagereq.push(`<img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/potential/${CN.requiredPotentialRank+1}.png" style="width:20px" title="Potential ${CN.requiredPotentialRank+1}">`)
        var currModuleTalentName = EN?EN.name:TL?TL.name:CN.name
        var currModuleTalentDesc = EN?EN.upgradeDescription:TL?TL.upgradeDescription:CN.upgradeDescription

        currModuleTalentDesc = ChangeDescriptionColor2(currModuleTalentDesc.replace(/\<([A-z ]+)\>/g,"&lt;"+"$1"+'&gt;').replace(/\n/g,"</br>"))

        var isModuleTalentRange = (CN.rangeId == range_id)?false:CN.rangeId
        var Moduletalentdetails = []
        CN.blackboard.forEach(Stat=>{
            var Moduletalentjson={}
            Moduletalentjson.name = db.effect[Stat.key]?db.effect[Stat.key]:Stat.key
            Moduletalentjson.key = Stat.key
            Moduletalentjson.value = Stat.value
            Moduletalentdetails.push(Moduletalentjson)
        })

        var Moduledetailtable = []
        var ModuledetailHeader = ''

        if(Moduletalentdetails.length>0){
            var Moduletalenthtmldetail = ""

            Moduletalentdetails.forEach(currdetails => {
                Moduletalenthtmldetail+=`
                <div style="background:#444;margin:4px;padding:2px;padding-top:8px;border-radius:2px;color: #999999">
                        ${titledMaker2(currdetails.name,currdetails.key)}
                        ${currdetails.value}
                </div>`
            });

            ModuledetailHeader =    `<button id='Moduletalentdetailtitle-${modulenum}-${phase}-${currpotent}' class='btn btn-sm btn-block ak-btn' onclick='SlideToggler2("Moduletalentdetailcontent-${modulenum}-${phase}-${currpotent}",$(this))'style="display:inline-block;color:#aaa;text-align:center;background:#333;padding:2px;font-size:12px">
                                        Talent Details
                                        <i class="fas fa-caret-down">
                                        </i>
                                    </button>`
            Moduledetailtable = `
                <div id='Moduletalentdetailcontent-${modulenum}-${phase}-${currpotent}' class="ak-shadow Moduletalentdetailcontent" style="display:none;padding-top:10px;padding:2px;background:#666">
                    ${Moduletalenthtmldetail}
                </div>
            `
        }
        else Moduledetailtable=""


        var info = `<div style="color:#999;background:#222;display:inline-block;padding:1px;padding-left:3px;padding-right:3px;border-radius:2px">
                        ${imagereq.join("")}
                    </div>`
        if(imagereq.length==0) info = ""

        return (`
        <div style="background:#444;margin:4px;padding:2px;padding-top:2px;border-radius:2px;">
            <div style="vertical-align:top;${isModuleTalentRange?`width:71%;display:inline-block;padding-right:0px;margin-right:-6px;height:100%`:""}">
                <div style="color:#222;font-size:13px;background:#999;display:inline-block;padding:2px;border-radius:2px">
                    ${currModuleTalentName}
                    ${info}
                </div>
                <div style="font-size:13px; font-family:'Source Sans Pro'">
                    <div class="ak-line" style="color:#999">
                        ${currModuleTalentDesc.replace(/<\/br>/g, '<div class="ak-newline"></div>')}
                    </div>
                    ${ModuledetailHeader}
                    ${Moduledetailtable}
                </div>
            </div>
            ${isModuleTalentRange?`<div style="display:inline-block;width:28%;padding:0px;margin:auto;padding-top:4px">
                                        ${rangeMaker(CN.rangeId,false)}
                                   </div>`:""}
        </div>
        `)
    }

    function ModuleTalentShow(modulenum,phase,potential){

         $(`.Moduletalentdetailcontent`).removeClass("active")

        if (ModuletalentValue[modulenum-2][phase-1]!=potential){

            $(`#Modtabtalent-${modulenum}-${phase}-${ModuletalentValue[modulenum-2][phase-1]}`).removeClass("active")
            $(`#ModuleTalent-${modulenum}-${phase}-${ModuletalentValue[modulenum-2][phase-1]}`).removeClass("active")

            $(`#Modtabtalent-${modulenum}-${phase}-${potential}`).addClass("active")
            $(`#ModuleTalent-${modulenum}-${phase}-${potential}`).addClass("active")
            
            ModuletalentValue[modulenum-2][phase-1]=potential
            }

    }

    function TalentParse2(eachtalent,talentnum){
        // console.log(talentnum)
        var imagereq = []
        if(PhaseConvert(eachtalent.talent.unlockCondition.phase) >=0)
            imagereq.push(`<img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/${PhaseConvert(eachtalent.talent.unlockCondition.phase)}.png" style="width:20px;margin-top:-5px" title="Elite ${eachtalent.talent.unlockCondition.phase}">`)
        if(eachtalent.talent.unlockCondition.level >1)
            imagereq.push(`<span style="font-size:8px">Lv.</span>${eachtalent.talent.unlockCondition.level} `)
        if(eachtalent.talent.requiredPotentialRank >0)
            imagereq.push(`<img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/potential/${eachtalent.talent.requiredPotentialRank+1}.png" style="width:20px" title="Potential ${eachtalent.talent.requiredPotentialRank+1}">`)

        var currTalentName = eachtalent.talentEN?eachtalent.talentEN.name:eachtalent.talentTL?eachtalent.talentTL.name:eachtalent.talent.name
        var currTalentDesc = eachtalent.talentEN?eachtalent.talentEN.description:eachtalent.talentTL?eachtalent.talentTL.desc:eachtalent.talent.description
        currTalentDesc = ChangeDescriptionColor2(currTalentDesc.replace(/\<([A-z ]+)\>/g,"&lt;"+"$1"+'&gt;').replace(/\n/g,"</br>"))
        // console.log(eachtalent.talent.name)
        var isTalentRange = eachtalent.talent.rangeId
        var blacklist =
        ["新人教官"]
        if(blacklist.includes(eachtalent.talent.name)){
            isTalentRange = undefined
        }
        // console.log(eachtalent)
        var isTalentRangeExtend
        var talentdetails = []
        eachtalent.talent.blackboard.forEach(talentInfo=>{
            var talentjson={}
            talentjson.name = db.effect[talentInfo.key]?db.effect[talentInfo.key]:talentInfo.key
            talentjson.key = talentInfo.key
            talentjson.value = talentInfo.value
            if(talentInfo.key=="ability_range_forward_extend"){
                isTalentRangeExtend = rangeMaker(opdataFull.phases[0].rangeId,true,talentjson.value)
            }
            talentdetails.push(talentjson)
        })

        var detailtable = []
        var detailHeader = ''
        // console.log(talentdetails)

        if(talentdetails.length>0){
            var talenthtmldetail = ""

            talentdetails.forEach(currdetails => {

                talenthtmldetail+=`
                <div style="background:#444;margin:4px;padding:2px;padding-top:8px;border-radius:2px;color: #999999">
                        ${titledMaker2(currdetails.name,currdetails.key)}  ${currdetails.value}
                </div>`
            });
            detailHeader = `<button id='talentdetailtitle${talentnum}' class='btn btn-sm btn-block ak-btn' onclick='SlideToggler2("talentdetailcontent${talentnum}",$(this))'style="display:inline-block;color:#aaa;text-align:center;background:#333;padding:2px;font-size:12px">Talent Details <i class="fas fa-caret-down"></i></button>`
            detailtable = `
                <div id='talentdetailcontent${talentnum}' class="ak-shadow talentdetailcontent" style="display:none;padding-top:10px;padding:2px;background:#666">
                    ${talenthtmldetail}
                </div>
            `

        }else{
            detailtable=""
        }

        var info = `<div style="color:#999;background:#222;display:inline-block;padding:1px;padding-left:3px;padding-right:3px;border-radius:2px">${imagereq.join("")}</div>`
        if(imagereq.length==0){
            info = ""
        }
        return (`
        <div style="background:#444;margin:4px;padding:2px;padding-top:2px;border-radius:2px;">
        <div style="vertical-align:top;${isTalentRange||isTalentRangeExtend?`width:71%;display:inline-block;padding-right:0px;margin-right:-6px;height:100%`:""}">
            <div style="color:#222;font-size:13px;background:#999;display:inline-block;padding:2px;border-radius:2px">${currTalentName} ${info}</div>
            <div style="font-size:13px; font-family:'Source Sans Pro'">
            <div class="ak-line">
            ${currTalentDesc.replace(/<\/br>/g, '<div class="ak-newline"></div>')}
            </div>
            ${detailHeader}
            ${detailtable}
            </div>

        </div>
            ${isTalentRange?`<div style="display:inline-block;width:28%;padding:0px;margin:auto;padding-top:4px">${rangeMaker(eachtalent.talent.rangeId,false)}</div>`:""}
            ${isTalentRangeExtend?`<div style="display:inline-block;width:28%;padding:0px;margin:auto;padding-top:4px">${isTalentRangeExtend}</div>`:""}
        </div>
        `)
    }
    
    function GetSkillCost(i2, i, opdataFull){
        let reqmats = []
        if(i2 != 0 && i2 < 7){
            reqmats = opdataFull.allSkillLvlup[i2-1].lvlUpCost

        }else if(i2>=7){
            // console.log(opdataFull.skills[i])
            reqmats = opdataFull.skills[i].levelUpCostCond[i2-7].levelUpCost
        }
        return reqmats
    }
    function GetEliteCost(i,opdataFull){
        if(i > 0){
            let reqmats = [];
            if(reqmats && gmapp == "BASE"){
                if(opdataFull.phases[i]){
                    reqmats=([{"count":(db.dataconst["evolveGoldCost"][opdataFull.rarity][i-1]).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
                                , "id" :4001
                                ,"type":"GOLD" }])
                }
            }
            reqmats = opdataFull.phases[i] ? reqmats.concat(opdataFull.phases[i].evolveCost) : undefined;
            return reqmats
        }else{
            return undefined
        }
    }
    function CreateMaterial(id, count){
        var itemdata = query(db.itemsTL, "itemId", id.toString());
        var material =
        (`<div class="akmat-container" style="position:relative">
            <div class="item-name" title="${itemdata.name_cn}">${(itemdata.name_en?itemdata.name_en:itemdata.name_cn)}</div>
            <div class="item-image">
                <img loading='lazy' id="item-image" src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/items/${itemdata.iconId}.png">
            </div>
            <img loading='lazy' class="item-rarity" src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/material/bg/item-${RarityConvert(itemdata.rarity)+1}.png">
            <div class="item-amount">${count}x</div>
        </div>`)
        return material
    }

    function GetTrust(opdataFull){
        let mintrust = opdataFull.favorKeyFrames[0].data
        let maxtrust = opdataFull.favorKeyFrames[1].data
        let differences = {}
        let differencesnum = 0
        // console.log(mintrust)
        Object.keys(mintrust).forEach(key => {
            // console.log(key)
            if(mintrust[key] != maxtrust[key]){
            differences[key] = maxtrust[key] - mintrust[key]
            differencesnum = differencesnum + 1
            }
        });
        console.log(differences)

        if(differencesnum){
            return TrustParse(differences)
        }else{
            return ""
        }
    }
    function TrustParse(differences) {
        let readable = []
        Object.keys(differences).forEach(key => {
            let currInfo
            switch (key){
                case "maxHp": currInfo="HP"; break;
                case "atk": currInfo="ATK"; break;
                case "def": currInfo="DEF"; break;
                case "magicResistance": currInfo="Magic Resist"; break;
                case "cost": currInfo="Cost"; break;
                case "blockCnt": currInfo="Block Count"; break;
                case "moveSpeed": currInfo="Move Speed"; break;
                case "attackSpeed": currInfo="Attack Speed"; break;
                case "baseAttackTime": currInfo="Attack time"; break;
                case "respawnTime": currInfo="Redeploy time"; break;
                case "hpRecoveryPerSec": currInfo="HP recovery"; break;
                case "spRecoveryPerSec": currInfo="SP recovery"; break;
                default: currInfo = key; break;
            }

            readable.push(`${currInfo} +${differences[key]}`)
        });
        return titledMaker(readable.join("</br>"), "Trust extra status", "", "", "color:#ddd;min-width:120px")
    }

    function GetTrait(desc,trait,traitname = "Traits"){
        console.log(desc)
        console.log(trait)
        if(trait&&(trait.candidates.length>0)){
            var num = 1
            var tabs = []
            var contents = []
            var color
            trait.candidates.forEach(element => {
                var imagereq = []
                if(element.unlockCondition.phase >=0)
                imagereq.push(`<img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/${element.unlockCondition.phase}.png" style="width:20px;margin:-12px 0px -6px 0px" title="Elite ${element.unlockCondition.phase}">`)
                if(element.unlockCondition.level >1)
                imagereq.push(`Lv.${element.unlockCondition.level}`)
                // console.log(s)
                var each = []
                element.blackboard.forEach(eachbb => {
                    each.push(`${eachbb.key} : ${eachbb.value}`)
                });
                console.log(num)
                //<div style="color:#999;background:#222;display:inline-block;padding:1px;padding-left:3px;padding-right:3px;border-radius:2px;margin-right:3px;margin-bottom:2px;margin-top:2px">${each.join("</br>")}</div>
                var info =`
                <li class='nav-item' style="background:#444;">
                    <button class='btn horiz-small nav-link ${(num!=trait.candidates.length ? '' : 'active')} equiplink' data-toggle='pill' href='#trait${num}' style="padding:0px 4px">
                    ${imagereq.join(" ")}
                    </button>
                </li>
                `
                var tl = GetFullTraitsTranslation(trait.candidates[trait.candidates.length-1].additionalDescription)
                console.log(trait.candidates[trait.candidates.length-1])
                if(!tl){
                    tl = GetFullTraitsTranslation(trait.candidates[trait.candidates.length-1].overrideDescripton)
                }
                console.log(`Trait info : ${trait.candidates[trait.candidates.length-1].overrideDescripton}`)
                if(!tl){
                    tl = GetFullTraitsTranslation(desc)
                }

                var traitdescription = ""
                var traitcolor = ""
                if(tl){
                    traitdescription = tl.en
                    traitcolor = tl.color
                }
                if(!traitdescription) {
                    traitdescription = trait.candidates[trait.candidates.length-1].overrideDescripton
                }
                if(!traitdescription){
                    traitdescription = trait.candidates[trait.candidates.length-1].additionalDescription
                }

                if(!tl){
                    traitdescription = desc
                }

                contents.push(`
                <div class='tab-pane container ${num!=trait.candidates.length ? '' : 'active'}' id='trait${num}'>
                    ${ChangeDescriptionColor(ChangeDescriptionContent(traitdescription,element.blackboard),true)}
                </div>
                `)

                num +=1
                if(tl&&!color){
                    color = traitcolor
                }
                if(trait.candidates.length>1){
                    tabs.push(info)
                }
            });

            return titledMaker(`
            <div class="traitsection-container" id="sidemenutab-traits" style="position: relative; margin-top: 0px">
            <ul class='nav nav-pills' id='traits-tabs' style="margin: 4px 0px 0px 0px;">
            ${tabs.join("")}
            </ul>
                <div class="tab-content" id="traits-contents" style="margin: 2px 0px 2px 0px;">
                ${contents.join("")}
                </div>
            </div>
            `,traitname,`${color?`ak-trait ak-trait-${color}`:""}`,"","white-space:initial;")

        }else{
            var curspec = GetFullTraitsTranslation(desc)
            console.log(`Trait info (no candid) : ${desc}`)
            if(curspec){
                var content = curspec.en
                var text = `
                ${ChangeDescriptionColor(content,true)}</br>

                `
                return titledMaker(text,traitname,`ak-trait ak-trait-${curspec.color}`,"","white-space:initial;")
            }
            else{
                return titledMaker(ChangeDescriptionColor(desc).replace("\\n","</br>"),traitname,``,"","white-space: normal;")
            }
        }
    }
    function GetFullTraitsTranslation(description){
        var tl = db.attacktype.full[description]
        if(tl){
            return tl
        }
        return false
    }
    function getSpeciality(description,opdataFull){

        //gonna need to split on "," and "\n" and repeat it
        let descriptions = description.split(/[，(\\n)]/)
        let splitdesc = []
        // console.log("=====================")
        // console.log(descriptions)
        descriptions.forEach(element => {
            if(element){
                // let muhRegex = /<@ba\.kw>(.*?)<\/>/g
                // let currSpeciality = muhRegex.exec(element)
                // console.log(element)
                let currSpeciality = element.replace(/\<(.*?)\>/gi,"")
                // console.log(currSpeciality)
                let filterDesc
                if(currSpeciality){
                    splitdesc.push([currSpeciality])
                }else{
                    splitdesc.push([element])
                }
            }
        });
        // console.log(splitdesc)
        // console.log("===========================")

        return SpecialityHtml(splitdesc,opdataFull)
    }

    function SpecialityHtml(splitdesc,opdataFull){
        let splitdescTL = []
        let color = ""
        let trait = opdataFull.trait
        console.log(splitdesc)
        console.log(trait)
        let isReplaced = false
        splitdesc.forEach(element => {
            if(element.length>0){
                let typetl = db.attacktype.parts.find(search=>search.type_cn==element.join(""))
                // if(!typetl) typetl = db.attacktype.find(search=>search.type_cn==element[1])
                if(typetl&&!color) color = typetl.type_color?typetl.type_color:undefined

                // console.log(element)
                // console.log(trait)
                let muhRegex = /(.*){(.*?)}(.*)/g
                let currTLconv = muhRegex.exec(typetl?typetl.type_en:element.join(""))
                // console.log(currTLconv)
                if(currTLconv){
                    // console.log(currTLconv)
                    var textreplace = 'Value'
                    if(trait && trait.candidates.length>1){
                        textreplace =  `<div style="color:#999;background:#222;display:inline-block;padding:1px;padding-left:3px;padding-right:3px;border-radius:2px">(value)</div>`
                    }else if (trait && trait.candidates.length==1) {
                        textreplace = trait.candidates[0].blackboard[0].value
                        if(currTLconv[2].includes("%")){
                            textreplace= textreplace*100 +("%")
                        }
                        isReplaced = true
                    }
                    // console.log(textreplace)
                }
                let currTLconvfinal = currTLconv?currTLconv[1] + textreplace + currTLconv[3]:typetl?typetl.type_en:element.join("")
                // console.log(currTLconvfinal)
                splitdescTL.push(currTLconvfinal)
            }else{
                var typetl = db.attacktype.parts.find(search=>{
                    if(search.type_detail=="common")
                    return search.type_cn==element[0]
                })
                if(!typetl){
                    typetl = db.attacktype.parts.find(search=>search.type_cn==element.join(""))
                }
                // console.log(element.join(""))

                // console.log(typetl)

                if(typetl&&!color) color = typetl.type_color?typetl.type_color:undefined
                splitdescTL.push(typetl?typetl.type_en:element[0])
            }
        });
        if(trait&&!(isReplaced)){
            trait.candidates.forEach(element => {
                var imagereq = []
                    if(element.unlockCondition.level >0)
                    imagereq.push(`Lv.${element.unlockCondition.level}`)
                    if(element.unlockCondition.phase >0)
                    imagereq.push(`<img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/${element.unlockCondition.phase}.png" style="width:20px;margin-top:-5px" title="Elite ${element.unlockCondition.phase}">`)

                // console.log(s)
                var each = []
                element.blackboard.forEach(eachbb => {
                    each.push(`${eachbb.key} : ${eachbb.value}`)
                });
                var info = `<div style="color:#999;background:#222;display:inline-block;padding:1px;padding-left:3px;padding-right:3px;border-radius:2px;margin-right:3px;margin-bottom:2px;margin-top:2px">${each.join("</br>")}</div>
                <div style="color:#999;background:#222;display:inline-block;padding:1px;padding-left:3px;padding-right:3px;border-radius:2px">${imagereq.join("")}</div>`
                splitdescTL.push(info)
            });
        }
        // console.log(splitdescTL)
        // console.log(color)

        return titledMaker(splitdescTL.join("</br>"),"Traits",`ak-trait ak-trait-${color}`,"","white-space:initial;")
        // splitdescTL
    }

    function titledMaker (content,title,extraClass="",extraId="",extraStyle=""){
        let titledbutton = `

        <div class=\"ak-btn-non btn-sm ak-shadow-small ak-btn ak-btn-bg btn-char  ${extraClass}\" style="text-align:left;min-width:80px;${extraStyle}" data-toggle=\"tooltip\" data-placement=\"top\" id="${extraId}">
        ${(title==""?"":`<a class="ak-subtitle2" style="font-size:11px;margin-left:-9px;margin-bottom:-15px">${title}</a>`)}${content}</div>
        `

        return titledbutton
    }
    function titledMaker2 (content,title,extraClass="",extraId="",extraStyle=""){
        let titledbutton = `
        <div style="padding-top:0px;display:inline-block">
        <div class=\"${extraClass}\" style="color:#222;font-size:13px;background:#999;display:inline-block;padding:2px;border-radius:2px;${extraStyle}" data-toggle=\"tooltip\" data-placement=\"top\" id="${extraId}">
         ${(title==""?"":`<a class="ak-subtitle" style="color:#999;background:#222;display:inline-block;border-radius:0px;padding:0px 3px;margin-left:-4px;margin-top:-12px"> ${title} </a>`)} ${content}</div>
        </div>`

        return titledbutton
    }
    function rangeMaker(rangeId, withText = true, extend = 0, flavortext = ""){
        var rangelist =  Object.assign({},db.range,db.extra_range)
        var rangeData ={}
        var rangeDataOrigin = Object.assign({},rangelist[rangeId])
        // extend =0
        if(rangeDataOrigin){
            let minRow = 0
            let minCol = 0
            let maxRow = 0
            let maxCol = 0
            let table = []
            let grids = []
            let getcol = 0
            // console.log(rangeDataOrigin.grids)
            if(rangeDataOrigin){
                rangeData = Object.assign({},rangeDataOrigin)
                rangeData.grids = []
                rangeDataOrigin.grids.forEach(element => {
                    maxRow = Math.max(maxRow,element.row)
                    maxCol = Math.max(maxCol,element.col)
                    minRow = Math.min(minRow,element.row)
                    minCol = Math.min(minCol,element.col)
                    if(element.row==maxRow||element.row==minRow){
                        getcol=element.col
                     }
                })
                rangeDataOrigin.grids.forEach(element => {

                     if(extend>0){
                         if(element.row==maxRow||element.row==minRow||element.col<=getcol){
                            rangeData.grids.push({row:element.row,col:element.col})
                         }else{
                            rangeData.grids.push({row:element.row,col:element.col+parseFloat(extend)})
                         }
                     }else{
                        rangeData.grids.push({row:element.row,col:element.col})
                     }

                });
                if(extend){
                    maxCol +=extend
                }
                if(extend>0){
                   for(i=minRow;i<=maxRow;i++){
                        for(j=1;j<=extend;j++){
                            // console.log(`${i} : ${j}`)
                            rangeData.grids.push({row:i,col:j+getcol,special:true})

                        }
                   }
                }
                extend = 0
            }
            console.log(rangeData.grids)
            table.push(`<div class="rangeTableContainer"><table class='rangeTable' style="table-layout: fixed;border-spacing:0 15px;padding:4px; border-collapse:separate; border-spacing:2px;width:${(maxCol+minCol+1)*17}px;">`)

            for(r=0;r+minRow<maxRow+1;r++){
                table.push(`<tr style="height:17px">`)
                // if(extend>0&&r>1){
                //     extend--
                //     r=1
                // }
                // console.log(r+minRow)
                for(c=0;c+minCol<maxCol+1;c++){
                    table.push(`<td style=";width:17px`)
                    if(r+minRow==0&&c+minCol==0){
                        table.push(";background:#DDD")
                    }else{
                        rangeData.grids.forEach(element => {
                            if(element.row==r+minRow&&element.col==c+minCol){
                                if(element.special){
                                    table.push(";border: 2px solid #00FF6688;")
                                }else{
                                    table.push(";border: 2px solid #DDDDDD88;")
                                }
                            }
                        });
                    }

                    table.push(`"></td>`)
                }
            }
            table.push(`</table>`);
            table.push(`${withText?`<div><span style="all:inherit">${flavortext + " "}Range</span></div>`:""}</div>`);
            return table.join("")
        }else{
            return undefined
        }
    }

    function changeEliteLevel(el,elite_no,max){
        var value = $(el).val();
        $("#elite"+elite_no+"LevelDisplay").val(value);
        $("#elite"+elite_no+"LevelSlider").val(value);
        EliteStatsDisplay(Math.min(value,max),elite_no);
    }

    function EliteStatsDisplay(level,elite_no){
        globalelite = elite_no
        globallevel[elite_no] = level
        $("#elite"+elite_no+"maxHp").html(statsInterpolation(opdataFull,'maxHp',level,elite_no));
        $("#elite"+elite_no+"def").html(statsInterpolation(opdataFull,'def',level,elite_no));
        $("#elite"+elite_no+"atk").html(statsInterpolation(opdataFull,'atk',level,elite_no));
        $("#elite"+elite_no+"magicResistance").html(statsInterpolation(opdataFull,'magicResistance',level,elite_no));
        $("#elite"+elite_no+"respawnTime").html(statsInterpolation(opdataFull,'respawnTime',level,elite_no)+`<div style='display:inline;font-size:10px'> Sec</div>`);
        $("#elite"+elite_no+"cost").html(statsInterpolation(opdataFull,'cost',level,elite_no));
        $("#elite"+elite_no+"blockCnt").html(statsInterpolation(opdataFull,'blockCnt',level,elite_no));
        $("#elite"+elite_no+"baseAttackTime").html(statsInterpolation(opdataFull,'baseAttackTime',level,elite_no,false)+`<div style='display:inline;font-size:10px'> Sec</div>`);

        var tokenfulldata = db.chars[globaltoken]

        if(tokenfulldata){
            console.log("Update Token")
            var currlevel = globallevel[globalelite]
            var currelite = globalelite

            if(currelite<globalskill){
                currelite = globalskill
                currlevel = globallevel[globalskill]
            }
            $("#summon-level").html(currlevel)
            $("#summon-maxHp").html(statsInterpolation(tokenfulldata,'maxHp',currlevel,currelite));
            $("#summon-def").html(statsInterpolation(tokenfulldata,'def',currlevel,currelite));
            $("#summon-atk").html(statsInterpolation(tokenfulldata,'atk',currlevel,currelite));
            $("#summon-magicResistance").html(statsInterpolation(tokenfulldata,'magicResistance',currlevel,currelite));
            $("#summon-respawnTime").html(statsInterpolation(tokenfulldata,'respawnTime',currlevel,currelite)+`<div style='display:inline;font-size:10px'> Sec</div>`);
            $("#summon-cost").html(statsInterpolation(tokenfulldata,'cost',currlevel,currelite));
            $("#summon-blockCnt").html(statsInterpolation(tokenfulldata,'blockCnt',currlevel,currelite));
            $("#summon-baseAttackTime").html(statsInterpolation(tokenfulldata,'baseAttackTime',currlevel,currelite,false)+`<div style='display:inline;font-size:10px'> Sec</div>`);
        }
    }

    function statsInterpolation(operator,key,level,elite_no,isround=true){
        var kf = [];
        $.each(operator.phases[elite_no].attributesKeyFrames,function(j,v){
            kf[j] = v;
        });
        // console.log([kf[0].level,kf[1].level])
        // console.log([kf[0].data[key],kf[1].data[key]])
        if(kf[0].data[key] == kf[1].data[key]){
        return kf[0].data[key]
        }else {
            var pol = everpolate.linear([level],[kf[0].level,kf[1].level],[kf[0].data[key],kf[1].data[key]]);
            if(isround)
            return Math.round(pol);
                else
            return parseFloat(Math.round(pol*100))/100;
        }

    }

    function changeSkillLevel(el,skill_no){
        var value = $(el).val();
        skillValue[skill_no]=Number(value)-1

        $("#skill"+skill_no+"StatsCollapsible").children("table").removeClass("active");
        $("#skill"+skill_no+"level"+(value-1)+"stats").addClass("active");
        $("#skill"+skill_no+"LevelDisplay").html(SkillRankDisplay(value));

        $("#Tokskill"+skill_no+"StatsCollapsible").children("table").removeClass("active");
        $("#Tokskill"+skill_no+"level"+(value-1)+"stats").addClass("active");

        UpdateElite(globalelite)
    }

    function SkillRankDisplay(skill_no){
        let img = "https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/rank/"
        let html =""
        if(skill_no>0&&skill_no<7){
            img += skill_no+".png"
            html = `<img loading='lazy' src="${img}" style="width:40px">`
        }else if(skill_no>=7){
            let imgM = img +"m-"+ (skill_no-7)+".png"
            img += "7.png"

            html = `<img loading='lazy' src="${img}" style="width:40px"><div class="akrankmastery"><img loading='lazy' src="${imgM}" style="width:40px"></div>`
        }
        return html
    }

    function getSkillDesc(skillId,level){
        var skill = db.skills[skillId].levels[level];
        var skillEN = db.skillsEN[skillId]?db.skillsEN[skillId].levels[level]:undefined;
        var skillTL = db.skillsTL[skillId];
        var desc = skillEN?skillEN.description:skillTL?skillTL.desc[level]:skill.description;

        desc = ChangeDescriptionColor2(desc.replace(/\<([A-z ]+)\>/g,"&lt;"+"$1"+'&gt;').replace(/\n/g,"</br>"))
        if(desc){
            // console.log(skill)
            desc = ChangeDescriptionContent(desc,skill)
        }
        return desc;
    }

    function query(db,key,val,single=true,returnKey=false){
        if(single){
            var result = {};
        }else{
            var result = [];
        }
        var found = false;
        $.each(db,function(key2,v){
            if(v[key].toLowerCase() == val.toLowerCase()){
                found = true;
                if(single){
                    if(returnKey){
                        result[key2] = v;
                    }else{
                        result = v;
                    }
                    return false;
                }else{
                    if(returnKey){
                        var obj = {};
                        obj[key2] = v;
                        result.push(obj);
                    }else{
                        result.push(v);
                    }
                }
            }
        });
        if(found){
            return result;
        }else{
            return false;
        }
    }

    function ChangeDescriptionColor(desc,addbackgroundcolor = false){
        desc = ChangeDesc2(desc)
        desc = ChangeDesc1(desc,addbackgroundcolor)
        return desc
    }
    function ChangeDescriptionColor2(desc,addbackgroundcolor = false){
        desc = ChangeDesc1(desc,addbackgroundcolor)
        desc = ChangeDesc2(desc)
        return desc
    }

    function CreateTooltip(desc,addbackgroundcolor = false){
        desc = ChangeDesc1(desc,addbackgroundcolor)
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
        desc = ChangeDesc1(desc,addbackgroundcolor)
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

    function ChangeDesc1(desc,addbackgroundcolor = false){
        if(!desc){
            console.log("DESC NULL")
            return desc
        }

        // catch </> missing case (Executor the Ex Foedere S1 EN)
        if ((desc.match(/<[@][^>]+>/g) ?? 0).length - (desc.match(/<\/>/g) ?? 0).length == 1) desc += "</>"

        // catch nested <@><@></></> (Shamare S2 / Lumen S3)
        if (desc.match(/<[@][^>]+>(?:(?!<\/>(?=[^<]*<[$@])).)*?<[@][^>]+>(?:(?!<\/>).)+?<\/>(?:(?!<\/>).)+?<\/>/g)){
            desc = desc.replace(/(<[@][^>]+>(?:(?!<\/>(?=[^<]*<[$@])).)*?)<[@]([^>]+)>((?:(?!<\/>).)+?)<\/>((?:(?!<\/>).)+?<\/>)/g, function(m,the_begin, rtf, text, the_rest) {
                console.log([desc])
                console.log([the_begin, rtf, text, the_rest])
                let rich = db.dataconst.richTextStyles[rtf];
                let rich2 = db.named_effects.termDescriptionDict[rtf];
                if (!rich2){
                    rich2 = db.dataconst.termDescriptionDict[rtf]
                }
                if (rich) {
                    let colorRTF = /<color=(#[0-9A-F]+)>\{0\}<\/color>/;
                    if (colorRTF.test(rich)) {
                        let color = colorRTF.exec(rich)[1]
                        return `${the_begin}<span class="${addbackgroundcolor?`stat-important2`:""}" style="color:${color}">${text}</span>${the_rest}</>`
                    }else{
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
        })}
        console.log(desc)

        desc = desc.replace(/<[@]([^>]+)>((?:(?!<\/>).)*)<\/>/g, function(m, rtf, text) { ///<[@](.+?)>(.+?)<\/>/g cant catch blank 2nd capture group (Glaucus S1 EN)
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
                }else{
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
        if(!desc){
            console.log("DESC NULL")
            return desc
        }
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

    function ChangeDescriptionContent(desc,blackboard,getNum = false){
        var num = 0
        var skill
        if(blackboard.blackboard){
            skill = blackboard
            blackboard = skill.blackboard
        }
        // console.log(desc)
        if(!desc){
            console.log("DESC NULL")
            return desc
        }
        desc = desc.replace(/\{(\-?)([A-Z@_a-z\[\]0-9.]+):?([^}]*)\}/g, function(m, neg, content, format) {
            for (var i = 0; i < blackboard.length; i++) {
                if (blackboard[i].key.toLowerCase() == content.toLowerCase() || blackboard[i].key.toLowerCase() == -content.toLowerCase()){
                    if (neg) value = Math.abs(blackboard[i].value)
                    else value = blackboard[i].value
                    console.log(blackboard[i].value, content, neg, value)

                    if (format && format.includes("%")) value = Math.round((value * 100000))/1000 + "%";
                    num += 1
                    return `<div class="stat-important">${value}</div>`
                }
            }
            console.log(content,skill)
            //Duration not in blackboard (Heavyrain S1)
            if (content = "duration") return `<div class="stat-important">${skill.duration}</div>`
            return m
        })

        desc = desc.replace(/\{\-?([A-Z_@a-z.0-9\[\]]+)\}/g, function(m, content) {
            for (var i = 0; i < blackboard.length; i++) {
                if (blackboard[i].key==content){
                    console.log(blackboard[i].value,content)
                    value = Math.abs(blackboard[i].value)
                    if(skill && skill.prefabId == "skchr_angel_3"&&blackboard[i].key =='base_attack_time'){
                        value = value*2;
                        // console.log("DOUBLE!!")
                    }
                    num += 1
                    return `<div class="stat-important">${value}</div>`
                }
            }
            return m
        })
        if(getNum){
            return {desc:desc, num:num}
        }
        return desc

    }

    function ChangeSkillAnim(skillnum, skillmax, token){
        // console.log(skillnum)
        // console.log(token)
        // console.log(skillmax)
        console.log(token)
        tokenname = token
        /*if(spinewidgettoken && token&& spinewidgettoken.loaded){
            LoadAnimationToken(token)
        }*/
        if(spinewidget && spinewidget.loaded){

            /*var animskill = db.animlist[opdataFull.id]
            console.log(skillnum)
            if(animskill && animskill.skills[skillnum]){
                $("#spine-text").text(`Skill ${skillnum+1}`)
                CreateAnimation(spinewidget, animskill.skills[skillnum],true)
            }
            else{*/
                var animlist = Object.keys(spinewidget.customanimation).filter(search => search.includes("Skill"))

                animlist = animlist.sort((a, b) => {
                    if(a < b) return 1
                    if(a > b) return -1
                    return 0
                })

                if(animlist&&animlist.length>0){
                    // console.log(animlist)
                    // console.log(skillmax-skillnum-1)

                    if(animlist[skillmax-skillnum-1]){
                        $("#spine-text").text(`Skill ${skillnum+1}`)
                        CreateAnimation(spinewidget,spinewidget.customanimation[animlist[skillmax-skillnum-1]],true)
                    }
                }
            //}

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
        if(content[1] && content[1].includes(",")){
            splitvalue = content[1].split(",")
        }
        return {key:content[0], value:splitvalue}
    }

    function LoadAnimationCG(opid, dynid, isSkin = false){
        var dynfolder = `https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/spineassets/dynchars/${opid}/`

        skelname = dynid
        if(spinewidgetcg){
            spinewidgetcg.pause()
            spinewidgetcg = undefined
        }
        $("#spine-widget-op").remove()
        $("#spine-frame-op").append(`<div id="spine-widget-op" class="top-layer" style="position:absolute;width: 3000px; height: 3000px;top:-1100px;left:-1300px;;pointer-events: none;z-index: 20;transform: scale(0.6);"></div>`)
        if (chibiName != null && defaultAnimationName != null) {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', dynfolder + skelname + "." + skeletonType, true);
            xhr.responseType = 'arraybuffer';
            var array;
            $("#spine-widget-op").hide()
            var defaultskin ='default'
            xhr.onprogress = function () {
                // console.log('LOADING: ', xhr.status);
                $("#loading-spine-op").fadeIn(200)
            };
            console.log(chibiName)
            xhr.onloadend = function (e) {
                // console.log(xhr.status)
                if (xhr.status != 404) {
                    buffer = xhr.response;
                    array = new Uint8Array(buffer);
                    skelBin = new SkeletonBinary();
                    var jsonskel
                    // console.log(array)
                    if(array.length != 0){
                        if (skeletonType == "skel"){
                            skelBin.data = array
                            SpineVersion = skelBin.readSkeletonVersion()
                            console.log(skelBin, SpineVersion)
                            if (SpineVersion.slice(0,3) == "3.8"){
                                jsonskel = array
                            }else if(SpineVersion.slice(0,3) == "3.5"){
                                skelBin.readSkeletonData()
                                jsonskel = JSON.stringify(skelBin.json)
                            }
                            /*skelBin.data = array
                            skelBin.initJson()
                            jsonskel = JSON.stringify(skelBin.json)
                            var parsedskeljson = JSON.parse(jsonskel)
                            // console.log(JSON.parse(jsonskel))
                            if(!Object.keys(parsedskeljson.animations).find(search=>search==defaultAnimationName)){
                                defaultAnimationName = Object.keys(parsedskeljson.animations)[0]
                            }
                            if(!Object.keys(parsedskeljson.skins).find(search=>search==defaultskin)){
                                defaultskin = Object.keys(parsedskeljson.skins)[0]
                            }*/
                        }else if (skeletonType == "json"){
                            jsonskel = JSON.parse(new TextDecoder("utf-8").decode(array))
                            SpineVersion = jsonskel.skeleton.spine
                        }
                        console.log(SpineVersion, jsonskel)
                        var spineX = parseFloat(3000)/2 - 50
                        var spineY = parseFloat(3000)/2 - 0
                        var xhratlas = new XMLHttpRequest();
                        xhratlas.open('GET', dynfolder + skelname + ".atlas", true);
                        xhratlas.onloadend = function (e) {
                            if (xhratlas.status != 404) {
                                attempt = 0
                                var loadedatlas = xhratlas.response;
                                var imagename = ConvertAtlas(loadedatlas)
                                var atlaslist = []
                                imagename.forEach(image => {
                                    atlaslist.push(image.image)
                                });
                                console.log(atlaslist)
                                var config = {
                                    version: SpineVersion,
                                    jsonContent: jsonskel,
                                    skeltype: skeletonType,
                                    atlas: dynfolder + skelname + ".atlas",
                                    atlasPages: atlaslist,
                                    animation: "Idle",
                                    backgroundColor: "#00000000",
                                    // debug: true,
                                    // imagesPath: chibiName + ".png",
                                    premultipliedAlpha: true,
                                    fitToCanvas : false,
                                    loop: true,
                                    // x:900,
                                    // y:650,
                                    x: spineX,
                                    y: spineY,
                                    //0.5 for normal i guess
                                    scale: 0.55,
                                    success: function (widget) {
                                        animIndex = 0
                                        spinewidgetcg = widget
                                        $("#loading-spine-op").fadeOut(200)
                                        animations = widget.skeleton.data.animations;
                                        $("#spine-widget-op").show()
                                        if(animations.find(search => search.name == "Start")){
                                            CreateAnimation(spinewidgetcg,["Start","Idle"])
                                        }else if(animations.find(search => search.name == "Idle")){
                                            CreateAnimation(spinewidgetcg,"Idle")
                                        }
                                        widget.customanimation = CheckAnimationSet(animations)
                                    }
                                }
                                if (SpineVersion.slice(0,3) == "3.8"){
                                    new spine38.SpineWidget("spine-widget-op", config)
                                }else if(SpineVersion.slice(0,3) == "3.5"){
                                    new spine.SpineWidget("spine-widget-op", config)
                                }
                            }
                        }
                        xhratlas.send()
                    }
                }else{
                    if (attempt == 2) {
                        xhr.abort()
                        $("#loading-spine-op").text("Load Failed 2")
                        $("#spine-frame-op").fadeOut()
                    }else{
                        attempt += 1
                        if(skeletonType == "skel"){
                            skeletonType = "json"
                        }else{
                            skeletonType = "skel"
                        }
                        LoadAnimationCG(opid, dynid)
                    }
                }
            };
            xhr.send()
        }
    }

    function Chibi_per(show = false){
        chibiperscurr = chibiperscurr % (["BASE", "SO"].includes(gmapp)?3:2)

        console.log(chibiperslist[chibiperscurr])

        newpers = ["BASE", "SO"].includes(gmapp)?chibiperslist[chibiperscurr]:chibipersextralist[chibiperscurr]
        if (show) $("#chibi-per").html(newpers[0].toUpperCase() + newpers.slice(1))
        return newpers
    }

    function LoadAnimation(){
        chibiName = chibiName.includes(skinsuffix)?chibiName:chibiName + skinsuffix
        Chibi_per(true)

        $("#loading-spine").text("Loading...")
        if(spinewidget){
            spinewidget.pause()
            spinewidget = undefined
        }
        $("#spine-widget").remove()
        $("#spine-frame").append(`<div id="spine-widget" class="top-layer" style="position:absolute;width: ${wid}px; height: ${hei}px;top:${-hei/2+150 +chibiscale[1]}px;left:-${wid/2-150}px;pointer-events: none;z-index: 20;transform: scale(${chibiscale[0]});"></div>`)
        if (chibiName != null && defaultAnimationName != null) {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', folder + encodeURIComponent(chibiName) + "." +skeletonType, true);
            xhr.responseType = 'arraybuffer';
            var array;
            $("#spine-widget").hide()
            var defaultskin ='default'

            xhr.onprogress = function () {
                $("#loading-spine").fadeIn(200)
            };
            xhr.onloadend = function (e) {
                if (xhr.status != 404) {
                    buffer = xhr.response;
                    array = new Uint8Array(buffer);
                    skelBin = new SkeletonBinary();
                    var jsonskel
                    if(array.length == 0){
                        $("#loading-spine").text("Load Failed (Not Found)")

                    }else{
                        if (skeletonType == "skel"){
                            skelBin.data = array
                            SpineVersion = skelBin.readSkeletonVersion()
                            console.log(skelBin, SpineVersion)
                            if (SpineVersion.slice(0,3) == "3.8"){
                                jsonskel = array
                            }else if(SpineVersion.slice(0,3) == "3.5"){
                                skelBin.readSkeletonData()
                                jsonskel = JSON.stringify(skelBin.json)
                                console.log(jsonskel.animations, jsonskel)
                            }
                            //jsonskel = JSON.stringify(skelBin.json)
                            /*var parsedskeljson = JSON.parse(jsonskel)
                            console.log(JSON.parse(jsonskel))
                            if(!Object.keys(parsedskeljson.animations).find(search=>search==defaultAnimationName)){
                                defaultAnimationName = Object.keys(parsedskeljson.animations)[0]
                            }
                            if(!Object.keys(parsedskeljson.skins).find(search=>search==defaultskin)){
                                defaultskin = Object.keys(parsedskeljson.skins)[0]
                            }*/
                        }else if (skeletonType == "json"){
                            jsonskel = JSON.parse(new TextDecoder("utf-8").decode(array))
                            SpineVersion = jsonskel.skeleton.spine
                            var parsedskeljson = jsonskel
                            if(!Object.keys(parsedskeljson.animations).find(search=>search==defaultAnimationName)){
                                defaultAnimationName = Object.keys(parsedskeljson.animations)[0]
                            }
                            if(!Object.keys(parsedskeljson.skins).find(search=>search==defaultskin)){
                                defaultskin = Object.keys(parsedskeljson.skins)[0]
                            }
                        }

                        var spineX = parseFloat($("#spine-widget").width())/2
                        var spineY = parseFloat($("#spine-widget").height())/2 -200
                        var config = {
                            skeltype : skeletonType,
                            jsonContent: jsonskel,
                            atlas: folder + encodeURIComponent(chibiName) + ".atlas",
                            animation: chibipers == "build"?"Relax":"Idle",
                            backgroundColor: "#00000000",
                            // debug: true,
                            // imagesPath: chibiName + ".png",
                            premultipliedAlpha: true,
                            fitToCanvas : false,
                            loop: true,
                            // x:900,
                            // y:650,
                            x: spineX,
                            y: spineY,
                            //0.5 for normal i guess
                            scale: 1,
                            success: function (widget) {
                                animIndex = 0
                                spinewidget = widget
                                $("#spine-text").text(widget.skeleton.data.animations[0].name)
                                $("#loading-spine").fadeOut(200)
                                animations = widget.skeleton.data.animations;
                                $("#spine-widget").show()
                                if(animations.find(search => search.name.includes("Start"))){
                                    idle_default = animations.map(k => k["name"]).filter(k => k.includes("Idle"))[0]
                                    start_default = animations.map(k => k["name"]).filter(k => k.includes("Start"))[0]
                                    CreateAnimation(spinewidget,[start_default, idle_default])
                                    $("#spine-text").text(idle_default)
                                }else if(animations.find(search=>search.name=="Relax")){
                                    CreateAnimation(spinewidget,"Relax")
                                    $("#spine-text").text("Relax")
                                }

                                widget.customanimation = CheckAnimationSet(animations)
                                
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
                        }
                        if (SpineVersion.slice(0,3) == "3.8"){
                            new spine38.SpineWidget("spine-widget", config)
                        }else if(SpineVersion.slice(0,3) == "3.5"){
                            new spine.SpineWidget("spine-widget", config)
                        }
                    }
                }else{
                    if (attempt == 2) {
                        xhr.abort()
                        $("#loading-spine").text("Load Failed 2")
                        // $("#spine-frame").fadeOut()
                    }else{
                        attempt += 1
                        if(skeletonType == "skel"){
                            skeletonType = "json"
                        }else{
                            skeletonType = "skel"
                        }
                        LoadAnimation()
                    }
                }
            };
            xhr.send()
        }
    }

    function LoadAnimationToken(tokenkey = skinsuffix?globaltoken + skinsuffix:globaltoken){
        var tokenname = tokenkey
        var tokenfolder = `https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/spineassets/token/${opdataFull.id}/${encodeURIComponent(tokenkey)}`
        if(spinewidgettoken){
            // spinewidget.loadWidgets()
            // spinewidget.loadTexture()
            spinewidgettoken.pause()
            spinewidgettoken = undefined
        }

        $("#spine-widget-token").remove()
        $("#spine-frame-token").append(`<div id="spine-widget-token" class="top-layer" style="position:absolute;width: ${wid}px; height: ${hei}px;top:${-hei/2+100 +chibiscale[1]}px;left:-${wid/2-150}px;pointer-events: none;z-index: 20;transform: scale(${chibiscale[0]});"></div>`)

        if (chibiName != null && defaultAnimationName != null) {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', tokenfolder + "." + skeletonType, true);
            xhr.responseType = 'arraybuffer';
            var array;
            $("#spine-widget-token").hide()
            var defaultskin ='default'

            xhr.onloadend = function (e) {
                if (xhr.status != 404) {
                    buffer = xhr.response;
                    array = new Uint8Array(buffer);
                    skelBin = new SkeletonBinary();
                    var jsonskel
                    if(array.length != 0){
                        if (skeletonType == "skel"){
                            skelBin.data = array
                            SpineVersion = skelBin.readSkeletonVersion()
                            console.log(skelBin, SpineVersion)
                            if (SpineVersion.slice(0,3) == "3.8"){
                                jsonskel = array
                            }else if(SpineVersion.slice(0,3) == "3.5"){
                                skelBin.readSkeletonData()
                                jsonskel = JSON.stringify(skelBin.json)
                                console.log(jsonskel)
                            }
                            /*jsonskel = JSON.stringify(skelBin.json)
                            var parsedskeljson = JSON.parse(jsonskel)
                            console.log(JSON.parse(jsonskel))
                            if(!Object.keys(parsedskeljson.animations).find(search=>search==defaultAnimationName)){
                                defaultAnimationName = Object.keys(parsedskeljson.animations)[0]
                            }
                            if(!Object.keys(parsedskeljson.skins).find(search=>search==defaultskin)){
                                defaultskin = Object.keys(parsedskeljson.skins)[0]
                            }*/
                        }else if (skeletonType == "json"){
                            jsonskel = JSON.parse(new TextDecoder("utf-8").decode(array))
                            SpineVersion = jsonskel.skeleton.spine
                            var parsedskeljson = jsonskel
                            console.log(JSON.parse(jsonskel))
                            if(!Object.keys(parsedskeljson.animations).find(search=>search==defaultAnimationName)){
                                defaultAnimationName = Object.keys(parsedskeljson.animations)[0]
                            }
                            if(!Object.keys(parsedskeljson.skins).find(search=>search==defaultskin)){
                                defaultskin = Object.keys(parsedskeljson.skins)[0]
                            }
                        }

                        var spineX = parseFloat($("#spine-widget-token").width())/2
                        var spineY = parseFloat($("#spine-widget-token").height())/2 -300

                        var config = {
                            jsonContent: jsonskel,
                            skeltype : skeletonType,
                            atlas: tokenfolder + ".atlas",
                            animation: "Default",
                            backgroundColor: "#00000000",
                            // debug: true,
                            // imagesPath: chibiName + ".png",
                            premultipliedAlpha: true,
                            fitToCanvas : false,
                            loop: true,
                            x: spineX,
                            y: spineY,
                            //0.5 for normal i guess
                            scale: 1,
                            success: function (widget) {
                                animIndex = 0
                                spinewidgettoken = widget
                                $("#spine-text2").text(widget.skeleton.data.animations[0].name)
                                tokenanimations = widget.skeleton.data.animations;
                                $("#spine-widget-token").show()
                                if (tokenanimations.find(search => search.name == "Loop")){
                                    CreateAnimation(spinewidgettoken,["Start", "Loop"])
                                    $("#spine-text2").text("Loop")
                                }else if(tokenanimations.find(search => search.name == "Start")){
                                    CreateAnimation(spinewidgettoken,["Start", "Idle"])
                                    $("#spine-text2").text("Idle")
                                }else if(tokenanimations.find(search => search.name == "Idle")){
                                    CreateAnimation(spinewidgettoken,"Idle")
                                    $("#spine-text2").text("Idle")
                                }else if(tokenanimations.find(search => search.name == "Relax")){
                                    CreateAnimation(spinewidgettoken,"Relax")
                                    $("#spine-text2").text("Relax")
                                }

                                widget.customanimation = CheckAnimationSet(tokenanimations)
                            }
                        }
                        if (SpineVersion.slice(0,3) == "3.8"){
                            new spine38.SpineWidget("spine-widget-token", config)
                        }else if(SpineVersion.slice(0,3) == "3.5"){
                            new spine.SpineWidget("spine-widget-token", config)
                        }
                    }else{
                        if (attempt == 2) {
                            xhr.abort()
                            $("#spine-widget-token").remove()
                        }else{
                            attempt += 1
                            if(skeletonType == "skel"){
                                skeletonType = "json"
                            }else{
                                skeletonType = "skel"
                            }
                            LoadAnimationToken(tokenkey)
                        }
                    }
                }
            };
            xhr.send()
        }
    }

    function ChangeAnimation2(widget, widgettext, num){
        if(widget == "token") widget = spinewidgettoken
        else widget = spinewidget

        var curranimation = Object.keys(widget.customanimation)
        widget.state.clearTracks()
        if(animationqueue!=undefined)clearInterval(animationqueue)
        animIndex += num;
        // console.log(animIndex)
        // console.log(curranimation)

        if (animIndex >= curranimation.length) animIndex = 0;
        else if (animIndex < 0) animIndex = curranimation.length - 1;
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

    function ChangeAnimation(widget, widgettext, num){
        if(widget == "token") widget = spinewidgettoken
        else widget = spinewidget

        var curranimation = widget.skeleton.data.animations
        widget.state.clearTracks()
        if(animationqueue != undefined) clearInterval(animationqueue)
        animIndex += num;
        // console.log(animIndex)
        // console.log(curranimation)

        if (animIndex >= curranimation.length) animIndex = 0;
        else if (animIndex < 0) animIndex = curranimation.length - 1;
        // spinewidget.state.setDefaultMix(0.1);
        // spinewidget.config.scale = 2
        // console.log(widget)
        // console.log(animIndex)
        // widget.setAnimation(curranimation[animIndex].name)
        // console.log(widget.customanimation[Object.keys(widget.customanimation)[animIndex]])
        // console.log(curranimation[index])
        CreateAnimation(widget, curranimation[animIndex].name)
        // widget.setAnimation(curranimation[animIndex].name)
        // console.log(widgettext)
        $(widgettext).text(curranimation[animIndex].name)
    }

    function SPL2D(SP = false){
        console.log("SP switch")
        $("button.btn.tabbing-btns.tabbing-btns-middle").each(function () {
            const onclickAttr = $(this).attr('onclick');
            if (onclickAttr && onclickAttr.includes(currskin.split("_").slice(0,-1).join("_"))){
                if(SP)
                    $(this).attr('onclick', onclickAttr.replace("sp_dyn_illust", "dyn_illust"));
                else
                    $(this).attr('onclick', onclickAttr.replace("dyn_illust", "sp_dyn_illust"));
            }
        })
    }

    function ChangeSkin(name = "", pers = "", id = "", sp = "", change = false){
        currskin = name
        skinsuffix = currskin.split(opdataFull.id)[1]?name.split(opdataFull.id)[1]:""
        console.log(opdataFull.id)
        console.log(skinsuffix)
        console.log(currskin, skin)
        console.log(db.skintable.charSkins[id])

        if (sp){
            if($(sp).hasClass("skinswitch")){
                if ($(sp+" img").attr("src").includes("_sp")){
                    $(sp+" img").attr("src", $(sp+" img").attr("src").replace("_sp.png",".png"))
                    SPL2D(sp)
                }else{
                    $(sp+" img").attr("src", $(sp+" img").attr("src").replace(".png","_sp.png"))
                    SPL2D()
                }
            }else{
                $(sp).addClass("skinswitch")
                SPL2D(sp)
            }
        }else{
            $("#tabs-opCG div").removeClass(("skinswitch"))
        }

        if(db.skintable.charSkins[id] && db.skintable.charSkins[id].voiceId)
            currVoiceID = db.skintable.charSkins[id].voiceId
        else
            currVoiceID = opdataFull.id

        if(name.length > 1) chibiName = name
        else chibiName = opdataFull.id
        if(pers != "") chibipers = pers
        if(chibipers == 'build')
            chibiName.includes("build")?chibiName = chibiName:chibiName = "build_" + chibiName
        else
            chibiName.includes("build")?chibiName = chibiName.split("_").slice(1).join("_"):chibiName = chibiName
        folder = `https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/spineassets/${chibitype}/${charName}/${chibipers}/`

        if($("#spine-frame-op:visible")){
            $("#spine-frame-op").fadeOut(200)
            $("#tabs-opCG").fadeIn(200)
            if(spinewidgetcg && !pers){
                spinewidgetcg.pause()
            }
        }
        if($("#spine-frame").is(":visible")){
            if(spinewidgettoken){
                console.log("      waaa "+tokenname)
                LoadAnimationToken(tokenname + skinsuffix)
            }
            LoadAnimation()
        }

        // TODO update_illustrator when change chibi perspective
        if (!change) update_illustrator(id?id:(opdataFull.id + "#" + (name != "0"?name:"1"))) // change skin by ID or change Elite (E0 = E1 except amiyi)
    }

    function ShowDynamic(name, isSkin = false, dynid = ""){
        var checkskin = db.skintable.buildinEvolveMap[name]
        if(isSkin){
            console.log(isSkin)
            console.log(name)
            console.log(dynid)
            $("#spine-frame-op").fadeIn(200)
            $("#tabs-opCG").fadeOut(200)
            LoadAnimationCG(name, dynid, true)
            return
        }else if(checkskin){
            if(checkskin[2]){
                var currentskin = db.skintable.charSkins[checkskin[2]]
                console.log(currentskin)
                if(currentskin&&currentskin.dynIllustId){
                    $("#spine-frame-op").fadeIn(200)
                    $("#tabs-opCG").fadeOut(200)
                    LoadAnimationCG(name, currentskin.dynIllustId.split("_").slice(0, -1).join("_"))
                    return
                }

            }
        }

        $("#spine-frame-op").fadeOut(200)
        $("#tabs-opCG").fadeIn(200)
    }

    function ChangeSType(buttonnum, amiyaclass = "caster"){
        ChangeSTypeHTML(buttonnum, Amiyacurrclass)
        Amiyacurrclass = amiyaclass
        selectOperator(curropid)
        update_illustrator(opdataFull.id + "#2")
    }
    function ChangeSTypeHTML(num, classchange){
        changepic = {
                        "caster" : "trans_magic_mark.png",
                        "guard" : "trans_melee_mark.png",
                        "medic" : "trans_medic_mark.png"
                    }

        $('#class-change-'+num.toString()).html(`
            <button id='class-change-${classchange}' class='ak-button' onclick='ChangeSType(${num},"${classchange}")'>
                <div id='class-background-${classchange}'><div id='class-beta'>BETA</div></div>
                <a id="class-button">
                    <img id="class-icon" src='extra\\AmiyaClass\\${changepic[classchange]}' title="${classchange} Amiya in beta phase">
                </a>
            </button>`
        )
    }

    function PlayPause(widget){
        if(widget=="token")
            widget=spinewidgettoken
        else
            widget=spinewidget
        if(widget.isPlaying()){
            console.log("Playing")
            widget.pause()
        }else{
            console.log("Paused")
            widget.play()
        }
    }

    function Mirror(el){
        var currcss
        // if($(el).hasClass("MirrorDiv")){
        //     curcss = $(el).css('transform')
        //     var changex = curcss.split(",")
        //     $(el).css('transform','scaleX("1")')
        //     console.log(changex)
        // }
        // else {
        //     curcss = $(el).css('transform')
        //     $(el).css('transform','scaleX("-1")')
        //     console.log(curcss)
        // }
        currcss = $(el).css('transform')
        var regexcheck = /matrix\((.*)\)/g
        var changex = regexcheck.exec(currcss)[1]
        var changex1 = changex.split(",")
        changex1[0] = changex1[0]*-1
        $(el).css('transform','matrix('+changex1.join(",")+')')
        console.log(changex)
        $(el).toggleClass("MirrorDiv")


    }



    function CreateAnimation(chibiwidget, animArray, endloop = false, skipStart = false, isendstop = false){
        // console.log(animArray)

        // console.log(Array.isArray(animArray))
        // console.log(animArray.length>1)
        // console.log(Array.isArray(animArray[0]))

        if((Array.isArray(animArray) && animArray.length>1)){
            // console.log("ayyyyyy")
            var delay = 0
            var animNum = 0
            if(animationqueue != undefined) clearInterval(animationqueue)
            var curranimplay = Array.isArray(animArray[0])?animArray[0][0]:animArray[0]
            if(chibiwidget.loaded) chibiwidget.setAnimation(curranimplay)
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
                else if(animNum==animArray.length-1) chibiwidget.state.addAnimation(animNum,curranim,!isendstop,delay)
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
                    var curranimplay = Array.isArray(animArray[0])?animArray[0][0]:animArray[0]
                    if(chibiwidget.loaded)chibiwidget.setAnimation(curranimplay)
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
                },delay*1000-20)
            }
        }else{
            // chibiwidget.state.setAnimation(animArray)
            // console.log("WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

            if(animationqueue!=undefined)clearInterval(animationqueue)
            // console.log(animArray)

            var curranimplay = Array.isArray(animArray[0])?animArray[0][0]:animArray
            if(chibiwidget.loaded)chibiwidget.setAnimation(curranimplay)
            chibiwidget.state.clearTracks()

            chibiwidget.state.setAnimation(0,curranimplay,!isendstop)
        }
    }

    function CheckChibi(){
        console.log(spinewidget)
    }

    function CheckAnimationSet(anim){
        // console.log(anim)
        var curranimlist = {}
        if(anim.find(search => search.name == "Interact")){
            //Build Mode
            // console.log("Is Build")

        }else if(anim.find(search => search.name == "Idle")){
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
                    splitnum = splitnum[0]
                }
                else if (!splitnum) splitnum = ""

                if(!curranimlist[`${currsplit}${splitnum}`]){
                    curranimlist[`${currsplit}${splitnum}`] = []
                }
                if(!curranim.name.includes("Down")){
                    curranimlist[`${currsplit}${splitnum}`].push(curranim.name)
                }

            });
            Object.keys(curranimlist).forEach(keys => {
                curranimlist[keys] = curranimlist[keys].sort((a,b) => {
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
                    for(i = 0 ; i < sortarray.length ; i++){
                        // console.log(sortarray[i])
                        if(sortarray[i] == ""){
                            var isAfree = true
                            var isBfree = true
                            for(j = 0 ; j< sortarray.length ; j++){
                                if(sortarray[j] != ""){
                                    if(a.includes(sortarray[j])) isAfree = false
                                    if(b.includes(sortarray[j])) isBfree = false
                                }
                            }
                            if (isAfree) anum += 4
                            if (isBfree) bnum += 4
                        }else{
                            if(a.includes(sortarray[i]))anum += i + 1
                            if(b.includes(sortarray[i]))bnum += i + 1
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
                if(curranimlist[keys].find(search => search.includes("End"))){
                    if(anim.find(search => search.name.includes("Idle_Charge"))) curranimlist[keys].push("Idle_Charge")
                    else curranimlist[keys].push("Idle")
                }
                if(curranimlist[keys].find(search => search.includes("Die"))){
                    if(anim.find(search => search.name.includes("Start"))) curranimlist[keys].push("Start")
                }
                for(i = 0 ; i < curranimlist[keys].length ; i++){
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
                    if (curranimlist[keys].length >= 2 &&(curranimlist[keys][i].includes("Loop") || curranimlist[keys][i].includes("Idle")) && !curranimlist[keys][i].includes("End")) iscomp = false
                    else{
                        iscomp = false
                        filterarray.forEach(element => {
                            if(curranimlist[keys][i].includes(element)) iscomp = true
                        });
                    }
                    if(!iscomp){
                        // console.log(curranimlist[keys][i])
                        var currvariable = anim.find(search => search.name == curranimlist[keys][i])
                        // console.log(currvariable)
                        // console.log("Got "+ Math.round(8/currvariable.duration))
                        if(curranimlist[keys][i].includes("Idle")){
                            if(Math.round(3 / currvariable.duration) > 3)curranimlist[keys][i] = [curranimlist[keys][i],Math.round(3 / currvariable.duration)]
                        }else if(currvariable.duration!=0){
                            curranimlist[keys][i] = [curranimlist[keys][i],Math.round(8 / currvariable.duration)]
                        }
                    }
                }
            });
        }else if(anim.find(search => search.name == "Loop")){

        }
        console.log(curranimlist)
        return curranimlist
    }

    function GetAnimationIndex(anim,name){

        return anim.map(function(e) { return e.name; }).indexOf(name)
    }

    function SlideToggler(el,btel){

            $(`.${el}`).slideToggle(100)
            $("#"+$(btel).attr("id")+" > i").toggleClass("fa-caret-down fa-caret-up").attr("class")
            console.log("WEEEI")
    }
    function SlideToggler2(el,btel){

            $(`#${el}`).slideToggle(100)
            $("#"+$(btel).attr("id")+" > i").toggleClass("fa-caret-down fa-caret-up").attr("class")
            console.log("WEEEI")
    }

    function ZoomChibi(el){

        if (el == 0) el = {value:0}
        var minscale = 0.5
        var maxscale = 2
        var mintop = 0
        var maxtop =-400

        // top:${-hei/2+150}px;left:-${wid/2-150}px
        // var zoomvalue = `${el.value}`
        var currscale = minscale + (maxscale*parseFloat(el.value)/100)
        var currtop = ((maxtop-mintop)*parseFloat(el.value)/100)
        // var currtop2 = mintop+((maxtop-mintop/2)*parseFloat(el.value)/100)

        // console.log(currtop)
        chibiscale = [currscale,currtop]
        $("#spine-widget").css("transform",`scale(${currscale})`)
        $("#spine-widget").css("top",`${(-hei/2+150)+currtop}px`)
        $("#spine-widget-token").css("transform",`scale(${currscale})`)
        $("#spine-widget-token").css("top",`${-hei/2+100 +currtop}px`)
        $("#spine-widget-op").css("transform",`scale(${currscale})`)
    }
    function Zoomchara(el){
        var widthbefore = $('#charazoom').width()
        var heightbefore = $('#charazoom').height()

        $('#charazoominput').val(el.value)
        $('#charazoomslider').val(el.value)
        $('#charazoom').css("max-width",`unset`)
        $('#charazoom').css("max-height",`unset`)
        var zoomvalue = `${el.value}%`
        $('#charazoom').css("width",zoomvalue)
        $('#charazoom').css("height",zoomvalue)
        var widthafter = $('#charazoom').width()
        var heightafter = $('#charazoom').height()
        // console.log(`${widthbefore} => ${widthafter}`)
        var zoommargintop = parseFloat($('#charazoom').css("margin-top").split('px')[0])
        var zoommarginleft = parseFloat($('#charazoom').css("margin-left").split('px')[0])
        console.log(zoommargintop)

        console.log(`${zoommargintop +(heightbefore/2-heightafter/2)}px`)
        console.log(`${zoommarginleft +(widthbefore/2-widthafter/2)}px`)
        $('#charazoom').css("margin-top",`${zoommargintop +(heightbefore/2-heightafter/2)}px`)
        $('#charazoom').css("margin-left",`${zoommarginleft +(widthbefore/2-widthafter/2)}px`)
        console.log(zoomvalue)
    }


    function LoadAnimation2(widget){
        $("#loading-spine").text("Loading...")
        if(spinewidget){
            spinewidget.pause()
            spinewidget = undefined
        }
        $("#spine-widget").remove()
        $("#spine-frame").append(`<div id="spine-widget" class="top-layer" style="position:absolute;width: ${wid}px; height: ${hei}px;top:${-hei/2+150 +chibiscale[1]}px;left:-${wid/2-150}px;pointer-events: none;z-index: 20;transform: scale(${chibiscale[0]});"></div>`)
        if (chibiName != null && defaultAnimationName != null) {
            var xhr = new XMLHttpRequest();
            folder2 = `https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/spineassets/dynchars/char_1012_skadi2/dyn_illust_char_1012_skadi2_2/dyn_illust_char_1012_skadi2`
            xhr.open('GET', folder2 + "." +skeletonType, true);
            xhr.responseType = 'arraybuffer';
            var array;
            $("#spine-widget").hide()
            var defaultskin ='default'

            xhr.onprogress = function () {
                console.log('LOADING: ', xhr.status);
                $("#loading-spine").fadeIn(200)
            };

            console.log(chibiName)
            xhr.onloadend = function (e) {
                console.log(xhr.status)
                if (xhr.status != 404) {
                    buffer = xhr.response;
                    array = new Uint8Array(buffer);
                    skelBin = new SkeletonBinary();
                    var jsonskel
                    if(array.length == 0){
                        $("#loading-spine").text("Load Failed (Not Found)")

                    }else{
                        if (skeletonType== "skel"){
                            skelBin.data = array
                            SpineVersion = skelBin.readSkeletonVersion()
                            console.log(skelBin, SpineVersion)
                            if (SpineVersion.slice(0,3) == "3.8"){
                                jsonskel = array
                            }else if(SpineVersion.slice(0,3) == "3.5"){
                                skelBin.readSkeletonData()
                                jsonskel = JSON.stringify(skelBin.json)
                                console.log(jsonskel)
                            }
                            /*jsonskel = JSON.stringify(skelBin.json)
                            var parsedskeljson = JSON.parse(jsonskel)
                            console.log(JSON.parse(jsonskel))
                            if(!Object.keys(parsedskeljson.animations).find(search=>search==defaultAnimationName)){
                                defaultAnimationName = Object.keys(parsedskeljson.animations)[0]
                            }
                            if(!Object.keys(parsedskeljson.skins).find(search=>search==defaultskin)){
                                defaultskin = Object.keys(parsedskeljson.skins)[0]
                            }*/
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

                        var spineX = parseFloat($("#spine-widget").width())/2
                        var spineY = parseFloat($("#spine-widget").height())/2 -200

                        var config = {
                            jsonContent: jsonskel,
                            atlas: folder2 + ".atlas",
                            animation: "Idle",
                            backgroundColor: "#00000000",
                            // debug: true,
                            // imagesPath: chibiName + ".png",
                            premultipliedAlpha: true,
                            fitToCanvas : false,
                            loop: true,
                            // x:900,
                            // y:650,
                            x: spineX,
                            y: spineY,
                            //0.5 for normal i guess
                            scale: 1,
                            success: function (widget) {
                                animIndex = 0
                                spinewidget = widget
                                $("#spine-text").text(widget.skeleton.data.animations[0].name)
                                $("#loading-spine").fadeOut(200)
                                animations = widget.skeleton.data.animations;

                                $("#spine-widget").show()
                                if(animations.find(search=>search.name=="Start")){
                                    CreateAnimation(spinewidget,["Start","Idle"])
                                    $("#spine-text").text("Idle")
                                }else if(animations.find(search=>search.name=="Relax")){
                                    CreateAnimation(spinewidget,"Relax")
                                    $("#spine-text").text("Relax")
                                }

                                widget.customanimation = CheckAnimationSet(animations)

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
                        }
                        if (SpineVersion.slice(0,3) == "3.8"){
                            new spine38.SpineWidget("spine-widget-op", config)
                        }else if(SpineVersion.slice(0,3) == "3.5"){
                            new spine.SpineWidget("spine-widget-op", config)
                        }
                    }
                }else{
                    $("#loading-spine").text("Load Failed 2")
                }
            };
            xhr.send()
        }
    }

    function RarityConvert(tier){
        return tier.split("_").length>1 ? parseInt(tier.split("_")[1])-1 : tier
    }

    function PhaseConvert(phase){
        return phase.split("_").length>1 ? parseInt(phase.split("_")[1]) : phase
    }

    function SkillTypeConvert(sptype){
        switch (sptype){
            case "INCREASE_WITH_TIME" : return 1;
            case "INCREASE_WHEN_ATTACK" : return 2;
            case "INCREASE_WHEN_TAKEN_DAMAGE" : return 4;
            case 8 : return 8 ;
            default : return sptype;
        }
    }

    function ObjectToArray(db){
        var result = [];
        var found = true;
        $.each(db,function(key2,v){
            console.log(v)
            var obj = {};
            obj[key2] = v;
            result.push(obj);
        });
        if(found){
            return result;
        }else{
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
            case "kr": $("#display-lang").text("Korean"); break;
        }

        getJSONdata("ui",function(data){
            if(data.length != 0){
                $.each(data, function(i,text){
                    $("[translate-id="+text.id).html(text['ui_'+lang]);
                });
            }
        });

        $(".op-tag").each((_, btn) => $(btn).text(db.ktags[$(btn).attr("data-id")][lang]));
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

    function getUrlVars() {
        return new URL(window.location.href).searchParams;
    }



    function dragElement(elmnt,elmnt2 =elmnt.id+ "header") {
        var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
        if (document.getElementById(elmnt2)) {
            // if present, the header is where you move the DIV from:
            document.getElementById(elmnt2).onmousedown = dragMouseDown;
        }else{
            // otherwise, move the DIV from anywhere inside the DIV:
            elmnt.onmousedown = dragMouseDown;
        }

        function dragMouseDown(e) {
            e = e || window.event;
            e.preventDefault();
            // get the mouse cursor position at startup:
            pos3 = e.clientX;
            pos4 = e.clientY;
            document.onmouseup = closeDragElement;
            // call a function whenever the cursor moves:
            document.onmousemove = elementDrag;
        }

        function elementDrag(e) {
            e = e || window.event;
            e.preventDefault();
            // calculate the new cursor position:
            pos1 = pos3 - e.clientX;
            pos2 = pos4 - e.clientY;
            pos3 = e.clientX;
            pos4 = e.clientY;
            // set the element's new position:
            elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
            elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
        }

        function closeDragElement() {
            // stop moving when mouse button is released:
            document.onmouseup = null;
            document.onmousemove = null;
        }
    }
    function dragElement2(elmnt,elmnt2 =elmnt.id+ "header") {
        var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
        if (document.getElementById(elmnt2)) {
            // if present, the header is where you move the DIV from:
            document.getElementById(elmnt2).onmousedown = dragMouseDown;
        }else{
            // otherwise, move the DIV from anywhere inside the DIV:
            elmnt.onmousedown = dragMouseDown;
        }

        function dragMouseDown(e) {
            e = e || window.event;
            e.preventDefault();
            // get the mouse cursor position at startup:
            pos3 = e.clientX;
            pos4 = e.clientY;
            document.onmouseup = closeDragElement;
            // call a function whenever the cursor moves:
            document.onmousemove = elementDrag;
        }

        function elementDrag(e) {
            e = e || window.event;
            e.preventDefault();
            // calculate the new cursor position:
            pos1 = pos3 - e.clientX;
            pos2 = pos4 - e.clientY;
            pos3 = e.clientX;
            pos4 = e.clientY;
            // set the element's new position:
            elmnt.style["margin-top"] = (elmnt.offsetTop - pos2) + "px";
            elmnt.style["margin-left"] = (elmnt.offsetLeft - pos1) + "px";
        }

        function closeDragElement() {
            // stop moving when mouse button is released:
            document.onmouseup = null;
            document.onmousemove = null;
        }
    }
    function LoadAllJsonObjects(obj) {
        var result = {}

        var promises = Object.entries(obj).map(function(url){
            return $.getJSON(url[1]).then(function (res) {
                result[url[0]] = res
            }).catch(function (e) {
                console.error("Failed to load file: " + url[0], e);
                result[url[0]] = {}
            });
        })

        return Promise.all(promises).then(function(){
            return result
        })
    }