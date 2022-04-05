var modal = document.getElementById("myModal");
var btn = document.getElementById("myBtn");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "inline";
}
span.onclick = function() {
    modal.style.display = "none";
}
span.onclick = function() {
        modal.style.display = "none";
    }
    // ------------------ AJAX POST request handling ----------------------------
let xhr = new XMLHttpRequest();
document.getElementById("submit_1").addEventListener("click", function(event) {
    event.preventDefault()
    var modal = document.getElementById("myModal");
    modal.style.display = "none";

    // AJAX request to server handler
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "{{ url_for('user_interface') }}", true)
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    toSend = JSON.stringify({
        text: document.getElementById("diary_text_1").value,
        card: document.getElementById("card-num-1").getAttribute('src')
    })
    console.log(toSend)
    xhr.send(toSend);
    console.log('i was clicked')
});
let div = document.getElementById('myModal');

// ------------------------------ button handing ---------------------------
let indicator = 0;

function card_reveal_1() {;
    document.getElementById('myBtn').removeAttribute('disabled')
    document.getElementById("card-num-1").setAttribute("src", `/{{ cards[0]["CARD_PATH"] }}`);
    let toDisable = document.createAttribute("disabled");
    toDisable.value = "true";
    document.getElementById("reveal-1").setAttribute("disabled", "true");
    //  -------------------------------------- fade in after rendring with fade in 
    document.getElementById("card-num-1").className = "";
    setTimeout(() => {
            document.getElementById("card-num-1").setAttribute("src", `/{{ cards[0]["CARD_PATH"] }}`);
            document.getElementById('card-num-1').className = "card-img-top fade-in-onload"
        }, 5)
        // --------------------------------------

    indicator += 1;
    if (indicator == 4) {
        let toEnable = document.getElementsByClassName("rep");
        for (let i = 0; i < toEnable.length; i++) {
            toEnable[i].removeAttribute("disabled")
        }
    }

}

function card_reveal_2() {


    let att = document.createAttribute("disabled")
    console.log(att)
    att.value = "true";
    document.getElementById("reveal-2").setAttributeNode(att)
    console.log(document.getElementById("card-num-2").setAttribute("class", "card-img-top fade-in-image"))

    //  -------------------------------------- fade in after rendring with fade in 
    document.getElementById("card-num-2").className = "";
    setTimeout(() => {
            document.getElementById("card-num-2").setAttribute("src", `/{{ cards[1]["CARD_PATH"] }}`);
            document.getElementById('card-num-2').className = "card-img-top fade-in-onload"
        }, 5)
        // --------------------------------------


    indicator += 1;
    if (indicator == 4) {
        let toEnable = document.getElementsByClassName("rep");
        for (let i = 0; i < toEnable.length; i++) {
            toEnable[i].removeAttribute("disabled")
        }
    }
}

function card_reveal_3() {


    let att = document.createAttribute("disabled")
    att.value = "true";
    document.getElementById("reveal-3").setAttributeNode(att)
    document.getElementById("card-num-3").setAttribute("class", "fade-in-image")

    //  -------------------------------------- fade in after rendring with fade in 
    document.getElementById("card-num-3").className = "";
    setTimeout(() => {
            document.getElementById("card-num-3").setAttribute("src", `/{{ cards[2]["CARD_PATH"] }}`);
            document.getElementById('card-num-3').className = "card-img-top fade-in-onload"
        }, 5)
        // --------------------------------------


    indicator += 1;
    if (indicator == 4) {
        let toEnable = document.getElementsByClassName("rep");
        for (let i = 0; i < toEnable.length; i++) {
            toEnable[i].removeAttribute("disabled")
        }
    }

}

function card_reveal_4() {

    let att = document.createAttribute("disabled")
    att.value = "true";
    document.getElementById("reveal-4").setAttributeNode(att)
    document.getElementById("card-num-4").setAttribute("class", "fade-in-image")

    //  -------------------------------------- fade in after rendring with fade in 
    document.getElementById("card-num-4").className = "";
    setTimeout(() => {
            document.getElementById("card-num-4").setAttribute("src", `/{{ cards[3]["CARD_PATH"] }}`);
            document.getElementById('card-num-4').className = "card-img-top fade-in-onload"
        }, 5)
        // --------------------------------------

    indicator += 1;
    if (indicator == 4) {
        let toEnable = document.getElementsByClassName("rep");
        for (let i = 0; i < toEnable.length; i++) {
            toEnable[i].removeAttribute("disabled")
        }
    }

}

// ---------------------------- replace card handling functions----------------------------------

function replaceCard_1() {
    document.getElementById('card-num-1').setAttribute("src", `/{{ cards[4]["CARD_PATH"] }}`);
    let btnArr = document.getElementsByClassName("rep");

    for (let i = 0; i < btnArr.length; i++) {
        btnArr[i].setAttribute("disabled", "true")
    }

}

function replaceCard_2() {
    document.getElementById('card-num-2').setAttribute("src", `/{{ cards[4]["CARD_PATH"] }}`);
    let btnArr = document.getElementsByClassName("rep");

    for (let i = 0; i < btnArr.length; i++) {
        btnArr[i].setAttribute("disabled", "true")
    }
}

function replaceCard_3() {
    document.getElementById('card-num-3').setAttribute("src", `/{{ cards[4]["CARD_PATH"] }}`);
    let btnArr = document.getElementsByClassName("rep");

    for (let i = 0; i < btnArr.length; i++) {
        btnArr[i].setAttribute("disabled", "true")
    }
}

function replaceCard_4() {

    document.getElementById('card-num-4').setAttribute("src", `/{{ cards[4]["CARD_PATH"] }}`);
    let btnArr = document.getElementsByClassName("rep");

    for (let i = 0; i < btnArr.length; i++) {
        btnArr[i].setAttribute("disabled", "true")
    }
}