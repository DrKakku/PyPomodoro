

function Start() {
    console.log("Start");
}

function Pause() {
    console.log("Pause");
    var now = new Date() //.toString()
    clock.innerHTML = now.toLocaleTimeString()
}

function Stop() {
    console.log("Stop");
}
var clock = document.getElementsByClassName("clock")[0]

function setTime ()
{
    var now = new Date()
    clock.innerHTML = now.toLocaleTimeString()
    console.log("running")
}

let timer = setInterval(
    setTime,500
);


