var globalSentence, globalData
var response = ""

document.addEventListener('DOMContentLoaded', function () {
//
    document.getElementById('current-sentence').innerHtml = globalSentence
})

function sendSentence(){
 //delete old marks
//    var marks = document.body.getElementsByTagName("mark");
//    console.log(marks)
////    marks.remove()
//    for (let i = 0; i < marks.length; i++){
//        console.log(marks[i])
//        marks[i].remove()
//    }
    let sentence = document.getElementById('wordbox').value
    console.log("called")
    console.log(sentence)
    globalSentence = sentence
    document.getElementById('current-sentence').innerHtml = globalSentence
//    const request = new XMLHttpRequest()
//    request.open('POST', `/getStanfordData/${JSON.stringify(sentence)}`)
//    request.send()
    $.ajax({
        type: "POST",
        url: "/getStanfordData",
        data: JSON.stringify(sentence),
        contentType: "application/json",
        dataType: 'json',
        async: false
//        success: function(data){
//            console.log("entered")
//            console.log(data);
//        },
//        error: function(err){
//            console.log(err)
//        }
    })
    .done(function(data){
        console.log(data.stanfordData[0])
        $("#left").bind('DOMSubtreeModified', function(data){
            console.log(data)
        })
        globalData = data
//        document.location.reload(true)
        response = data;
        console.log(document.querySelectorAll("*"))
        const matches = document.querySelectorAll("p");
        matches.forEach((userItem) => {
//          console.log(userItem.innerText);
          userItem.innerHtml = "done";
           console.log(userItem.innerText);
        });
        console.log(matches)
    });
}

    //try to do some d3 stuff

//function sendSentence(){
//let sentence = document.getElementById('wordbox').value
//let formData = new FormData();
//    formData.append('data', sentence);
//    fetch('http://127.0.0.1:5000/getStanfordData', {
//        method: 'POST',
//        body: formData
//    })
//     .then(response => response.json())
//     .then(result => console.log(result))
//     .catch(error => {
//      console.log('Error:', error);
//    })
//}
//}
//let response = await fetch('http://127.0.0.1:5000/getStanfordData/%22This%20is%20me%22');
//if (response.ok) { // if HTTP-status is 200-299
//  // get the response body (the method explained below)
//  let json = await response.json();
//} else {
//  alert("HTTP-Error: " + response.status);
//}
//fetch('http://127.0.0.1:5000/getStanfordData/'+stringify(globalSentence))
//    .then(response => response.json())
//    .then(data => console.log(data));

//const user_url = Flask.url_for("getStanfordData", {sentence=${JSON.stringify(sentence)}})
//fetch(user_url)
//    .then(response => response.json())
//    .then(data => console.log(data));
// $.post("/getStanfordData/",  {'sentence': "\"This is Me\""}).done(function(data) {
////     $("#Result").text(data);
//    console.log(data)
// });