function hello(){
    alert("hello!")
    //try to do some d3 stuff
}

fetch('http://127.0.0.1:5000/gethidata')
    .then(response => console.log((response)))
    .then(data => console.log(data));