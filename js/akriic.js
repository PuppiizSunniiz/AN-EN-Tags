    $.holdReady(true);
    var db = {};
    var d0 = $.getJSON("json/tl-akhr.json", function(data){
        temp = {}
        data.forEach(op => temp[op.id] = op)
        db["chars"] = temp;
    });
    var d1 = $.getJSON("json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/gamedata_const.json", function(data){
        db["dataconst"] = data;
    });
    var d2 = $.getJSON("json/puppiiz/riic_data.json", function(data){
        db["riic"] = data;
    });
    var d3 = $.getJSON("json/named_effects.json", function(data){
        db["named_effects"] = data;
    });
    var d4 = $.getJSON("json/tl-unreadablename.json", function(data){
        temp = {}
        data.forEach(op => temp[op.name] = op.name_en)
        db["unreadable"] = temp;
    });
    $.when(d0, d1, d2, d3, d4).then(function(){
        $.holdReady(false);
    });

    var lang;
    var reg;
    var reqmats = [];
    var selectedOP;
    let bufflist = []
    let bufflist2 = []
    
    let charaBuff = {}
    let charaFilter= []
    $(document).ready(function(){
        Object.keys(db.riic.buffs).forEach(element => {
            let splitted = element.split("_")
            if(!bufflist.find(search => search == splitted[0])){
                bufflist.push(splitted[0])
            }
        });
        bufflist2 = Object.keys(db.riic.buffs).filter(search => search.includes("meet"))
        
        Object.keys(db.riic.chars).forEach(element => {
            let currChara = db.riic.chars[element]
            charaBuff[element] = []
            currChara.buffChar.forEach(element2 => {
                if(element2.buffData){
                    element2.buffData.forEach(element3 => {
                        if(element3.buffId){
                            charaBuff[element].push({"buffId" : element3.buffId, "cond" : element3.cond})
                        }
                    });
                }
            });
        });
        
        $('#to-tag').click(function() {     // When arrow is clicked
            $('body,html').animate({
                scrollTop : 0               // Scroll to top of body
            }, 500);
        });

        $('.dropdown-trigger').dropdown();
        $('[data-toggle="tooltip"]').tooltip();

        if(!localStorage.getItem("gameRegion") || !localStorage.getItem("webLang")){
            console.log("game region undefined");
            localStorage.setItem("gameRegion", 'cn');
            localStorage.setItem("webLang", 'en');
            reg = "cn";
            lang = "en";
        } else {
            console.log(localStorage.getItem("webLang"));
            reg = localStorage.getItem("gameRegion");
            lang = localStorage.getItem("webLang");
        }

        $(`.reg[value = ${reg}]`).addClass('selected');
        $(`.lang[value = ${lang}]`).addClass('selected');
        changeUILanguage();
    });

    $.getScript("js/arrive.min.js", function(){
        $(document).arrive("#regionDropdown", function(){
            $("#navitemRegion").addClass('ak-disable2');
            $("#navitemLanguage").addClass('ak-disable2');
        });
    });

    function regDropdown(el){
        localStorage.setItem("gameRegion", el.attr("value"));
        $(".dropdown-item.reg").removeClass("selected");
        el.addClass("selected");   
        changeUILanguage();
    }
                
    function langDropdown(el){
        localStorage.setItem("webLang", el.attr("value"));
        console.log(localStorage.getItem("webLang"))
        $(".dropdown-item.lang").removeClass("selected");
        el.addClass("selected");
        changeUILanguage();
    }

    function FilterType(type){
        charaFilter = []
        var sortby
        Object.keys(charaBuff).forEach(char_id => {
            let currChara = charaBuff[char_id]
            var currspecific = ""
            if(currChara.find(search => {
                if(currspecific = search.buffId.startsWith(type)){
                    currspecific = search.buffId
                    if(!sortby && db.riic.buffs[currspecific].description.includes("%"))
                        sortby = true
                }
                return search.buffId.startsWith(type)
            }))
            charaFilter.push({"id" : char_id, "buff" : currChara, "specific" : currspecific})
        });
        // console.log(db.riic.buffs)
        console.log(charaFilter)
        charaFilter.sort((a, b) => {
            // var acurr 
            // var bcurr
            
            var acurr = db.riic.buffs[a.specific]
            var bcurr = db.riic.buffs[b.specific]
            
            // console.log(db.riic.buffs[b.specific])
            
            let muhRegex = /<@cc\.vup>(.*?)<\/>/
            
            var acurrreg = muhRegex.exec(acurr.description)
            var bcurrreg = muhRegex.exec(bcurr.description)
            if(acurrreg & bcurrreg){
                var acurrNum = muhRegex.exec(acurr.description)[1]
                var bcurrNum = muhRegex.exec(bcurr.description)[1]
                let muhRegex2 = /(\d+)(%?)/ 
                var acurrNum2 = parseInt(muhRegex2.exec(acurrNum)[1])
                var bcurrNum2 = parseInt(muhRegex2.exec(bcurrNum)[1])
                return (acurrNum2 < bcurrNum2)
            }
        })

        let currHtml = []
        $("#tbody-list").empty()
        charaFilter.forEach(element => {
            let chara = db.chars[element.id]
            
            let extraInfo = ""
            let extrainfo2 = ''
            
            currHtml.push(`<div class="row riicbody" style="">
                                <div class="riic-avatar" style="">
                                    <div class="riic-avatar2">
                                        <div>
                                        <img loading="lazy" class='riic-pic' src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/${element.id}.png">
                                    </div>
                                    <div class="riic-name">
                                        ${db.unreadable[chara.name_en]?`[${db.unreadable[chara.name_en]}] ${chara.name_en}`:chara.name_en}
                                    </div>
                                </div>
                            </div>
                            <div class="riic-desc" style=""> ` )

                element.buff.forEach((buff, i) => {
                    let buffId = buff.buffId;
                    let currBuff2 = db.riic.buffs[buffId]
                    let clue = ''
                    let buffName = currBuff2.buffName
                    let description = currBuff2.description
                    let place = buffId.split("_")[0]

                    extrainfo2 = ''
                    extraInfo = ``
                    
                    if(buffId.startsWith("control")){
                        extraInfo = `<div class="btn btn-sm ak-disable ak-btn riic-type ak-riic-control" style=""><img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/infrastructure/control.png" style="height:20px;padding-bottom:3px"> HQ </div>`
                    }else if(buffId.startsWith("power")){
                        extraInfo = `<div class="btn btn-sm ak-disable ak-btn riic-type ak-riic-power" style=""><img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/infrastructure/power.png" style="height:20px;padding-bottom:3px"> Power </div>`
                    }else if(buffId.startsWith("manu")){
                        extraInfo = `<div class="btn btn-sm ak-disable ak-btn riic-type ak-riic-manu" style=""><img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/infrastructure/manu.png" style="height:20px;padding-bottom:3px">Manufacture </div>`
                        let currbuff = description
                        // console.log([currBuff2.buffId])
                        // console.log(currbuff)
                        // console.log(`${description}`)
                        if(buffId.includes("prod")){
                            
                        }else if (buffId.includes("formula")){
                            let muhRegex = /<@cc\.kw>(.*?)<\/>/g
                            let muhRegex2 = /<@cc\.vup>(.*?)<\/>/g
                            let extra = muhRegex.exec(currbuff)[1]
                            let extra2 = muhRegex2.exec(currbuff)[1]
                            // console.log([extra])
                            // switch (extra) {
                            //     case "源石": console.log(["Originium"]) ;extrainfo2=`Originium ${extra2}`;break;
                            //     case "贵金属": console.log(["Gold Bar"]);extrainfo2=`Gold Bar ${extra2}`;break;
                            //     case "作战记录": console.log(["EXP Card"]);extrainfo2=`EXP Card ${extra2}`;break;
                            //     default: break;
                            // }
                        }
                    
                    }else if(buffId.startsWith("trade")){
                        extraInfo = `<div class="btn btn-sm ak-disable ak-btn riic-type ak-riic-trade" style=""><img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/infrastructure/trade.png" style="height:20px;padding-bottom:3px"> Trading </div>`
                    }else if(buffId.startsWith("workshop")){
                        extraInfo = `<div class="btn btn-sm ak-disable ak-btn riic-type ak-riic-workshop" style=""><img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/infrastructure/workshop.png" style="height:20px;padding-bottom:3px"> Workshop </div>`
                    }else if(buffId.startsWith("train")){
                        extraInfo = `<div class="btn btn-sm ak-disable ak-btn riic-type ak-riic-train" style=""><img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/infrastructure/train.png" style="height:20px;padding-bottom:3px"> Training </div>`
                    }else if(buffId.startsWith("dorm")){
                        extraInfo = `<div class="btn btn-sm ak-disable ak-btn riic-type ak-riic-dorm" style=""><img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/infrastructure/dorm.png" style="height:20px;padding-bottom:3px"> Dorm </div>`
                    }else if(buffId.startsWith("hire")){
                        extraInfo = `<div class="btn btn-sm ak-disable ak-btn riic-type ak-riic-hire" style=""><img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/infrastructure/hire.png" style="height:20px;padding-bottom:3px"> Hiring </div>`
                        if(buffId.includes("hire_spd&clue2"))
                            clue = clue_search(description)
                    }else if(buffId.startsWith("meet")){
                        extraInfo = `<div class="btn btn-sm ak-disable ak-btn riic-type ak-riic-meet" style=""><img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/infrastructure/meet.png" style="height:20px;padding-bottom:3px"> Meeting </div>`
                        if(buffId.includes("team") || buffId.includes("flag") || buffId.includes("mustget"))
                            clue = clue_search(description)
                    }
                    
                    description = description.replace(/\\n/g,"<br><br>")
                    description = ChangeDescriptionColor2(description)
                    let req = ``
                    if(buff.cond.phase){
                        req += `<img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/elite/${buff.cond.phase.slice(-1)}.png" style="width:20px;height:20px" title="Elite ${buff.cond.phase.slice(-1)}">`
                    }
                    if(buff.cond.level>1){
                        req += `Lv.${buff.cond.level}`
                    }
                    if(req !== ""){
                        req = `<div class="riic-req" style="">${req}</div>`
                    }
                    var bufficon = `<img loading="lazy" src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/infrastructure/skill/${currBuff2.skillIcon}.png" style="width:40px;height:40px" title="">`
                    currHtml.push(`
                    <div class='riic-tab'>
                        <div class='riic-icon'>
                            ${bufficon}
                            ${clue?`<div class='riic-clue'><img src="https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/ui/clue/${clue}-s.png" style="width:40px" title="Clue ${clue}"></div>`:""}
                        </div>
                        <div class="riic-eachdesc">
                            <div class='riic-desc-title riic-color-${place}' style="">
                                ${extraInfo}${req}${buffName}
                            </div>
                            <div class='riic-desc-desc riic-color-${place}-sub'style="">
                                ${extrainfo2==""?"":`<div style="display:inline;background:#222;padding:3px">${extrainfo2}</div>`} 
                                ${description}
                            </div>
                        </div>
                    </div>
                    ` )
                });
            currHtml.push(`</div></div> `)
        });
        // console.log(currHtml)
        $("#tbody-list").html(currHtml.join(""))
    }

    function clue_search(desc = ""){
        let clue
        if(desc.indexOf("<@cc.kw>") > 0){
            Regex_match = desc.match(/<@cc\.kw>(.+?)<\/>/g)
            for (let matched_Regex of Regex_match){
                let kw = /<@cc\.kw>(.+?)<\/>/.exec(matched_Regex)
                if (!kw) continue
                else if (["Rhine Lab"].includes(kw[1]))
                    clue = 1;
                else if (["Penguin Logistics"].includes(kw[1]))
                    clue = 2;
                else if (["Blacksteel Worldwide", "Blacksteel"].includes(kw[1]))
                    clue = 3;
                else if (["Ursus Student Self-Governing Group"].includes(kw[1]))
                    clue = 4;
                else if (["Glasgow", "Glasgow Gang"].includes(kw[1]))
                    clue = 5;
                else if (["Karlan Trade"].includes(kw[1]))
                    clue = 6;
                else if (["Rhodes Island", "Rhodes Island Pharmaceuticals"].includes(kw[1]))
                    clue = 7;
                if(clue) return clue
            }
        }
    }

    function clickBtnClear(){
        console.log(lang);
        $("#tbody-list").empty()
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
            //console.log(m)
            if (!rich2){
                rich2 = db.dataconst.termDescriptionDict[rtf]
            }
            if (rich2) {
                return `<span class="stat-important tooltip3" style="color:#0098DC">${text}<span class="tooltiptext2" style="display:inline-block"><div class="tooltipHeader">${rich2.termName}</div>${CreateTooltip2(rich2.description)}</span></span>`
            }
        })
        return desc
    }
    function CreateTooltip2(desc,addbackgroundcolor = false){
        desc = ChangeDesc1(desc,addbackgroundcolor)
        desc = desc.replace(/<[$](.+?)>(.+?)<\/>/g, function(m, rtf, text) {
            let rich2 = db.named_effects.termDescriptionDict[rtf];
            //console.log(m)
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
        desc = desc.replace(/<[@](.+?)>(.+?)<\/>/g, function(m, rtf, text) {
            let rich = db.dataconst.richTextStyles[rtf];
            if (rich) {
                let colorRTF = /<color=(#[0-9A-F]+)>\{0\}<\/color>/;
                if (colorRTF.test(rich)) {
                    let color = colorRTF.exec(rich)[1]
                    return `<span class="${addbackgroundcolor?`stat-important2`:""}" style="color:${color}">${text}</span>`
                } else {
                    return rich.replace('{0}', text)
                }
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
                return `<span class="stathover tooltip2" style="color:#0098DC">${text}<span class="tooltiptext" style="display:inline-block"><div class="tooltipHeader">${rich2.termName}</div>${CreateTooltip(rich2.description)}</span></span>`
            }
        })
        return desc
    }
    // function 

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
        reg = localStorage.getItem("gameRegion");
        lang = localStorage.getItem("webLang");

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