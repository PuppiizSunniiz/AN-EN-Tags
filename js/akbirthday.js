const AVATAR_URL = "https://raw.githubusercontent.com/PuppiizSunniiz/Arknight-Images/main/avatars/"
const BASE_URL = "https://puppiizsunniiz.github.io/AN-EN-Tags/"
const CHAR_SIDE = 73
const LI_HEIGHT = 90
const CHAR_STYLE = `width:${CHAR_SIDE}px !important; height:${CHAR_SIDE}px !important;`
const LI_STYLE = `width:${CHAR_SIDE}px !important; height:${LI_HEIGHT}px !important;`

const db = {}
const op_dict = {}
const birth = {"date": {}, "other": {}}

$(document).ready(() => {
    $.holdReady(true)

    const jsonList = {
        handbookInfo    : "./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/handbook_info_table.json",
        chars2          :"./json/tl-akhr.json",
        storytextTL     :"./json/tl-storytext.json",
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
        // TL
        if (db.storytextTL["本人表示遗忘"] === undefined) {
            db.storytextTL["本人表示遗忘"] = "Claims to have forgotten"
        }
        if (db.storytextTL["本人表示无确切日期"] === undefined) {
            db.storytextTL["本人表示无确切日期"] = "No exact date provided"
        }
        
        // Populate operator dict
        for (let i=0; i<db.chars2.length; ++i) {
            let curr = db.chars2[i]
            op_dict[curr.id] = curr
            delete op_dict[curr.id].id
        }

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
    let prefix = ""
    let content = ""
    let suffix = ""

    // date
    const date = $('#date')
    suffix = `
                            </ul>
                        </div>
                    </div>
                </div>
                `
    for (const [key, value] of Object.entries(birth.date)) {
        // Month
        date.append(`<table class="table ak-table ak-table-striped table-hover my-3 ak-shadow month-${key}" id="table-recommend" style="display:none;">
                        <thead class="ak-thead">
                            <tr><th scope="col" colspan="10" style="text-align: center;">${getMonthName(key)}</th></tr>
                        </thead>
                    </table>`)

        // Day
        days = `    <div class="col-12 ak-bg ak-shadow mt-3 month-${key}" style="padding:15px;padding-right:0;padding-bottom:0;border-radius:0px;display:none;" role="alert">
                        <div class="row col-12" style="padding-right:0;">`
        days_suff = `   </div>
                    </div>`
        all_days = ""
        for (const [key_date, value_date] of Object.entries(value)) {
            prefix=`<div class="table ak-table col-12">
                        <div class="row align-items-center">
                            <div class="col-2">${getMonthDayName(key, key_date)}</div>
                            <div class="col-10">
                                <ul style="margin-bottom:0 !important;">`
            content = ""
            for (let i=0; i<value_date.length; ++i) {
                const op_id = value_date[i]
                content += `<li class="selectop-grid3 ak-rare-${getOperatorRarity(op_id)}" onclick="selectOperator('${op_id}')" style="${LI_STYLE}">
                                <div class="op-image-grid2" style="${CHAR_STYLE}">
                                    <img loading='lazy' src="${AVATAR_URL + op_id}.png" style="${CHAR_STYLE}">
                                </div>
                                <div class="nametext namesmaller ak-center blacktext">
                                    ${getOperatorName(op_id)}
                                </div>
                            </li>`
            }
            all_days += prefix + content + suffix
        }
        date.append(days + all_days + days_suff)
    }

    // other
    const other = $('#other')
    suffix =   `            </ul>
                        </div>
                    </div>
                </div>`
    for (const [key, value] of Object.entries(birth.other)) {
        prefix=`<div class="table ak-table col-12">
                    <div class="row align-items-center">
                        <div class="col-2">${getBirthdayOther(key) ? getBirthdayOther(key) : key}</div>
                        <div class="col-10">
                            <ul style="margin-bottom:0 !important;">`
        content = ""
        for (let i=0; i<value.length; ++i) {
            const op_id = value[i]
            content += `<li class="selectop-grid3 ak-rare-${getOperatorRarity(op_id)}" onclick="selectOperator('${op_id}')" style="${LI_STYLE}">
                            <div class="op-image-grid2" style="${CHAR_STYLE}">
                                <img loading='lazy' src="${AVATAR_URL + op_id}.png" style="${CHAR_STYLE}">
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

const nthNumber = (number) => {
    return number > 0
        ? ["th", "st", "nd", "rd"][
            (number > 3 && number < 21) || number % 10 > 3 ? 0 : number % 10
        ]
        : ""
}
function getMonthName(month) {
    const date = new Date(2000, month-1)
    return date.toLocaleString('default', { month: 'long' })
}
function getMonthDayName(month, day) {
    return `${day}${nthNumber(day)} ${getMonthName(month)}`
}

/// UI Functions
function clickBtnClear() {
    for (let i=1; i<=12; ++i) {
        $('.month-'+i).css('display', 'none')
    }
    $('.month-o').css('display', 'none')
    $('.button-tag').removeClass("btn-primary")
    $('.button-tag').addClass("btn-secondary")
}

function selectOperator(op_id) {
    window.open(BASE_URL + 'akhrchars.html?opname='+getOperatorName(op_id), '_blank')
}

function clickBtnTag(el){
    const checked = $(el).hasClass("btn-primary")
    const tag = $(el).attr('text')

    if (tag === "a") {
        for (let i=1; i<=12; ++i) {
            $('.month-'+i).css('display', '')
        }
        $('.month-o').css('display', '')
        
        $('.button-tag').removeClass("btn-secondary")
        $('.button-tag').addClass("btn-primary")
    } else {
        if (checked === false) {
            $('.month-'+tag).css('display', '')
        } else {
            $('.month-'+tag).css('display', 'none')
        }

        $(el).toggleClass("btn-primary btn-secondary")
    }
}

