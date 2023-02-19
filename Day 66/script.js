const dynamicContent = document.getElementById("dynamicText");
console.log(dynamicContent);

const phrases = ["A Software Engineer", "An Entrepreneur", "A Mentor", "CTO at Nest Nepal"];
let phraseIndex = 0;
let letterIndex = 0;
const typingSpeed = 150;
const clearSpeed = 75;

function printLetters(phrases) {

    if (letterIndex == phrases.length) {
        // clear the text, phrase which have been typed.
        clearLetter();
    }

    else if (letterIndex < phrases.length) {
        dynamicContent.textContent += phrases.charAt(letterIndex);
        letterIndex += 1;
        setTimeout(function () {
            printLetters(phrases)
        }, typingSpeed)
    }
}

function clearLetter() {
    if (letterIndex == -1) {
        phraseIndex = (phraseIndex + 1) % phrases.length;
        letterIndex = 0;
        printLetters(phrases[phraseIndex]);
    }

    else if (letterIndex > -1) {
        let updatePhrase = "";
        for (let index = 0; index < letterIndex; index++) {
            updatePhrase += phrases[phraseIndex].charAt(index);
        }
        console.log(updatePhrase);
        dynamicContent.textContent = updatePhrase;
        letterIndex -= 1;
        setTimeout(clearLetter, clearSpeed)
    }
}

printLetters(phrases[phraseIndex]);