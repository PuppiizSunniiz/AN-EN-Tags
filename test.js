function ChangeDescriptionColor2(desc,addbackgroundcolor = false){
    desc = ChangeDesc1(desc,addbackgroundcolor)
    desc = ChangeDesc2(desc)
    return desc
}

function ChangeDesc1(desc,addbackgroundcolor = false){
    if(!desc){
        console.log("DESC NULL")
        return desc
    }
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

function CreateTooltip(desc,addbackgroundcolor = false){
    desc = ChangeDesc1(desc,addbackgroundcolor)
    desc = desc.replace(/<[$](.+?)>(.+?)<\/>/g, function(m, rtf, text) {
        let rich2 = db.named_effects.termDescriptionDict[rtf];
        console.log(m)
        if (!rich2){
            rich2 = db.dataconst.termDescriptionDict[rtf]
        }
        if (rich2) {
            return `<span class="stat-important tooltip3" style="color:#0098DC">${text}<span class="tooltiptext2" style="display:inline-block"><div class="tooltipHeader">${rich2.termName}</div>${CreateTooltip2(rich2.description)}</span></span>`
        }
    })
    console.log(desc)
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
CreateTooltip(rich2.description.replace(/\'/g,"&apos;").replace(/\:/g,"&colon;")
&colon;