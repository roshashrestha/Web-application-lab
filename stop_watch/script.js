let hour=0;
let min=0;
let sec=0;

let timer=null;

let timepara=document.querySelector(".initial p");

//Start
document.getElementById("start").addEventListener("click", function () {
    if (timer===null) {
        timer=setInterval(function () {
            sec++;
            if (sec===60) {
                sec=0;
                min++;
            }
            if (min===60) {
                min=0;
                hour++;
            }
            let h=hour<10? "0" + hour:hour;
            let m=min<10? "0" + min:min;
            let s=sec<10? "0" + sec:sec;
            timepara.textContent=h+":"+m+":"+s;
        }, 1000);
    }
});


//Stopp
document.getElementById("stop").addEventListener("click", function(){
    clearInterval(timer);
    timer=null;
});


//Reset
document.getElementById("reset").addEventListener("click", function(){
    clearInterval(timer);
    timer=null;
    hour=0;
    min=0;
    sec=0;
    timepara.textContent="00:00:00";

    let laps=document.getElementsByClassName("lapTime");
    while(laps.length > 0) {
        laps[0].remove();
    }
});

//Lap time
document.getElementById("lap").addEventListener("click", function(){

    let lap = document.createElement("p");
    lap.textContent="Lap: "+timepara.textContent;
    lap.className="lapTime";

    document.getElementById("container").appendChild(lap);
});
