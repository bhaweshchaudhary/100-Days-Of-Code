// initialize the variable

let songIndex = 0;
let audioElement = new Audio('songs/1.mp3');
let masterPlay = document.getElementById('masterPlay');
let myProgressBar = document.getElementById('myProgressBar');
let gif = document.getElementById('gif');

let songs = [
    {songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"},
    {songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"},
    {songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"},
    {songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"},
    {songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"},
    {songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"},
    {songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"},
    {songName: "despacito", filepath: "songs/1.mp3", coverpath: "cover/1.jpg"},
]

// audioElement.play();

// Handle play/pause click

masterPlay.addEventListener('click', () => {
    if (audioElement.paused || audioElement.currentTime <= 0) {
        audioElement.play();
        masterPlay.classList.remove('fa-play-circle');
        masterPlay.classList.add('fa-circle-pause');
    }
    else {
        audioElement.pause();
        masterPlay.classList.remove('fa-circle-pause');
        masterPlay.classList.add('fa-play-circle');
    }
})

// Listen to events

myProgressBar.addEventListener('timeupdate', () => {
    console.log('timeupdate');
    // update seekbar
});
