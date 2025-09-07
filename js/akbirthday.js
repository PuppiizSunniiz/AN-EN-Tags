$(document).ready(() => {
    $.holdReady(true);

    const jsonList = {
        handbookInfo: "./json/gamedata/ArknightsGameData/zh_CN/gamedata/excel/handbook_info_table.json",
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

    function LoadAllJsonObjects(obj) {
        let result = {}

        let promises = Object.entries(obj).map(url => {
            return $.getJSON(url[1]).then(res => {
                result[url[0]] = res
            }).catch(e => {
                console.error("Failed to load file: " + url[0], e)
                result[url[0]] = {}
            })
        })

        return Promise.all(promises).then(() => {
            return result
        })
    }

    var db = {}
    const birth = {"date": {}, "other": {}}
    LoadAllJsonObjects(jsonList).then(result => {
        db = result
        $.holdReady(false)

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
        console.log(birth)
    })
})

var filter = {"month": []}
function FilterType(type, arg) {
    console.log(type, arg)
}