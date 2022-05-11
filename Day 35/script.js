// initialize the variable

let songIndex = 0;
let audioElement = new Audio('songs/1.mp3');
let masterPlay = document.getElementById('masterPlay')
let myProgressBar = document.getElementById('myProgressBar');
let gif = document.getElementById('gif');
let songItems = Array.from(document.getElementsByClassName('songItem'));

let songs = [
    {songName: "As it was", filepath: "songs/1.mp3", coverpath: "cover/1.jpeg"},
    {songName: "Don't wake me up", filepath: "songs/2.mp3", coverpath: "cover/2.jpg"},
    {songName: "Tsunami", filepath: "songs/3.mp3", coverpath: "cover/3.jpeg"},
    {songName: "To be loved", filepath: "songs/4.mp3", coverpath: "cover/4.jpeg"},
]

songItems.forEach((element, i)=>{
    document.getElementsByName("img")[0].src = songs[i].coverpath;
})

// audioElement.play();

// Handle play/pause click

masterPlay.addEventListener('click', () => {
    if (audioElement.paused || audioElement.currentTime <= 0) {
        audioElement.play();
        masterPlay.classList.remove('fa-play-circle');
        masterPlay.classList.add('fa-circle-pause');
        gif.style.opacity = 1;
    }
    else {
        audioElement.pause();
        masterPlay.classList.remove('fa-circle-pause');
        masterPlay.classList.add('fa-play-circle');
        gif.style.opacity = 0;
    }
})

// Listen to events

audioElement.addEventListener('timeupdate', () => {
    progress=parseInt((audioElement.currentTime/audioElement.duration)*100);
    myProgressBar.value = progress;
});

myProgressBar.addEventListener('change', ()=>{
    audioElement.currentTime = (myProgressBar.value * audioElement.duration)/100;
})
