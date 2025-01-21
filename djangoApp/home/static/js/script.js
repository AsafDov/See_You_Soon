

function getFriends(){
    console.log("Hi");
    alert("HELLLOOO")
}

function onClickUsername(e){
    console.log("Going to user:")
    
}

function onClickFriend(e){
    statsDiv = e.lastElementChild;
    if (statsDiv.classList.contains("d-none")) {
        statsDiv.classList.remove("d-none");
    }
    else{
        statsDiv.classList.add("d-none");
    }
    
}

function fetchStats(e,user,friend){
    statsDiv = e.nextElementSibling;
    if (statsDiv.classList.contains("d-none")) {
        statsDiv.classList.remove("d-none");
        avgDiv = statsDiv.children[0].children[1]
        maxDiv = statsDiv.children[1].children[1]
        fetch(`/api/getStats/${user}/${friend}`)
        .then(response => response.json())
        .then(data => {
            avgDiv.innerText=data.avg;
            maxDiv.innerText=data.max;
        });
    }
    else{
        statsDiv.classList.add("d-none");
    }
}