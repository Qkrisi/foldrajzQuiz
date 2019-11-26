let score = 0
let answered = 0
let maxScore = q.length

function validate(i, n) {
    if(q[i].validated) return
    q[i].validated = true
    let corr = q[i].answers[n].correct
    let me = document.querySelectorAll('.qclass')[i]
    if(corr) {
        me.style.backgroundColor = "#00ff00"
        score++
    } else {
        me.style.backgroundColor = "#ff0000"
    }
    answered++
    setTimeout(_ => {
        me.style.display = "none"
        if(answered == maxScore) {
            let main = document.getElementById("injectionDiv")
    
            let grade = 0
            let message = ""
            let k = score / maxScore

            // 40 55 70 80
            if(k < 0.4) {
                grade = 1
                message = "Erre inkább nem mondok semmit..."
            } else if(k < 0.55) {
                grade = 2
                message = ":face_palm:"
            } else if(k < 0.70) {
                grade = 3
                message = "Legalább a fele megvan :P"
            } else if(k < 0.80) {
                grade = 4
                message = "I mean... Majdnem"
            } else {
                grade = 5
                message = "Ez már majdnem olyan kreatív, mint az ananász!"
            }

            let scoreText = document.createElement("div")
            scoreText.setAttribute("class", "score")
            scoreText.innerHTML = `Elért eredményed<br>${score} / ${maxScore}<br>Érdemjegy: ${grade}<br>${message}`

            main.insertBefore(scoreText, main.childNodes[0])
            
            let n = 1
            document.querySelectorAll('.qclass').forEach(r => {
                setTimeout(function() {
                    r.style.display = "flex"
                }, 1000 * n)
                n++
            })
        }
    }, 600)
}

function render(e) {
    for(var i in e) {
        let main = document.getElementById("injectionDiv")

        let qclass = document.createElement("div")
        qclass.setAttribute("class", "qclass")


        let qtext = document.createElement("p")
        qtext.setAttribute("class", "qtext")
        qtext.innerHTML = e[i].question
        qclass.appendChild(qtext)

        let aclass = document.createElement("div")
        aclass.setAttribute("class", "aclass")

        let c = 0

        e[i].answers.forEach(j => {
            let tmp = document.createElement("div")
            tmp.setAttribute("class", "atext")
            tmp.setAttribute("onclick", `validate(${i}, ${c})`)
            tmp.innerHTML = j.text
            
            aclass.appendChild(tmp)
            c++
        })
        
        qclass.appendChild(aclass)
        main.appendChild(qclass)
    }
}

window.onload = function() {
    render(q)
}
