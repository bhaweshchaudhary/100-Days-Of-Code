// initialize the variable
let songIndex = 0;
let audioElement = new Audio('1.mp3');
let masterPlay = document.getElementById('masterPlay');
let myProgressBar = document.getElementById('myProgressBar');

let songs = [
    {
        songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"
    },
    {
        songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"
    },
    {
        songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"
    },
    {
        songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"
    },
    {
        songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"
    },
    {
        songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"
    },
    {
        songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"
    },
    {
        songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"
    }
]

// audioElement.play();

// Handle play/pause click
masterPlay.addEventListener('click', ()=>{
    if(audioElement.paused || audioElement.currentTime>=0){
        audioElement.play();
    }
})

// Listen to events

myProgressBar.addEventListener('timeupdate', () => {
    console.log('timeupdate');
    // update seekbar

});