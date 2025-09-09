const avatar_url = "https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/"
const base_url = "http://127.0.0.1:8080/"
const db = {}
const op_dict = {}
const birth = {"date": {}, "other": {}}

$(document).ready(() => {
    $.holdReady(true);

    const jsonList = {
        handbookInfo    : "./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/handbook_info_table.json",
        //charsEN         :"./json/gamedata/ArknightsGameData_YoStar/en_US/gamedata/excel/character_table.json",
        chars2          :"./json/tl-akhr.json",
        storytextTL     :"./json/tl-storytext.json",
    }

    const monthNames = {
        1: "January", 
        2: "February", 
        3: "March", 
        4: "April", 
        5: "May", 
        6: "June",
        7: "July", 
        8: "August", 
        9: "September", 
        10: "October", 
        11:"November", 
        12: "December",
    }

    async function LoadAllJsonObjects(obj, db) {
        const promises = Object.entries(obj).map(url => {
            return $.getJSON(url[1]).then(res => {
                db[url[0]] = res
            }).catch(e => {
                console.error("Failed to load file: " + url[0], e)
                db[url[0]] = {}
            })
        })

        return Promise.all(promises).then(() => {
            return 
        })
    }

    LoadAllJsonObjects(jsonList, db).then(() => {
        console.log(db)

        // TL
        db.storytextTL["本人表示遗忘"] = "Claims to have forgotten"
        db.storytextTL["本人表示无确切日期"] = "No exact date provided"
        
        // Populate operator dict
        for (let i=0; i<db.chars2.length; ++i) {
            let curr = db.chars2[i]
            op_dict[curr.id] = curr
            delete op_dict[curr.id].id
        }
        console.log(op_dict)

        // Populate birthdates
        const dict = db.handbookInfo.handbookDict
        for (const [key, value] of Object.entries(dict)) {
            const basic_info = value.storyTextAudio[0].stories[0].storyText.split("\n")
            for (let i=0; i<basic_info.length; ++i) {
                if (basic_info[i].trimStart().startsWith("【生日】") === true) {
                    const date = basic_info[i].trim().slice(4)
                    if (date.slice(-1) === "日" && date.includes("月") === true) {
                        const date_split = date.slice(0, -1).split("月")
                        const month = parseInt(date_split[0])
                        const day = parseInt(date_split[1])
                        if (birth.date[month] === undefined) {
                            birth.date[month] = {}
                        }
                        if (birth.date[month][day] == undefined) {
                            birth.date[month][day] = []
                        }
                        birth.date[month][day].push(key)
                    } else {
                        if (birth.other[date] === undefined) {
                            birth.other[date] = []
                        }
                        birth.other[date].push(key)
                    }
                    break
                }
            }
        }
        CreateBirthdayTables(birth)

        $.holdReady(false)
    })
})

function CreateBirthdayTables(birth) {
    console.log(birth)
    let prefix = ""
    let content = ""
    let suffix = ""

    // date
    const date = $('#date')
    for (let i=1; i<=12; ++i) {
        const days = new Date(1972, i, 0).getDate()
        //console.log(i, days)
    }

    // other
    const other = $('#other')
    suffix =   `            </ul>
                        </div>
                    </div>
                </div>`
    for (const [key, value] of Object.entries(birth.other)) {
        prefix=`<div class="table ak-table col-12" id="other-1">
                    <div class="row align-items-center">
                        <div class="col-2">${getBirthdayOther(key) ? getBirthdayOther(key) : key}</div>
                        <div class="col-10">
                            <ul style="margin-bottom:0 !important;">`
        content = ""
        for (let i=0; i<value.length; ++i) {
            const op_id = value[i]
            content += `<li class="selectop-grid3 ak-rare-${getOperatorRarity(op_id)}" onclick="selectOperator('${op_id}')">
                            <div class="op-image-grid2">
                                <img loading='lazy' src="${avatar_url + op_id}.png">
                            </div>
                            <div class="nametext namesmaller ak-center blacktext">
                                ${getOperatorName(op_id)}
                            </div>
                        </li>`
        }
        other.append(prefix + content + suffix)
    }
}

/// Utilities
function getBirthdayOther(cn_text) {
    return db.storytextTL[cn_text]
}

function getOperatorRarity(op_id) {
    return op_dict[op_id].level
}

function getOperatorName(op_id) {
    return op_dict[op_id].name_en
}

/// UI Functions
var filter = {"month": []}
function FilterType(type, arg) {
    console.log(type, arg)
}

function clickBtnClear() {
    console.log("clear filter")
}

function selectOperator(op_id) {
    window.open(base_url + 'akhrchars.html?opname='+getOperatorName(op_id), '_blank');
}


