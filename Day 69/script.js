// strict mode js helps write secure js
'use strict';

let hasDriverLicense = false;
const passTest = true;

if (passTest) hasDriverLicense = true;
if (hasDriverLicense) console.log("hello i can drive now")


// function declaration

function myAge(birthYear) {
    return 2023 - birthYear
}

let findingAge = myAge(2002)
console.log(findingAge)
// function expression

let whatMyAge = function(birthYear) {
    return 2023 - birthYear
}

let ageIs = whatMyAge(2002)

console.log(ageIs);

// arrow function added in es6

// type one
let siwaniAge = birthYear => 2022 - birthYear;
console.log(`siwani age is ${siwaniAge(2002)}`);

// type two
let ramAge = birthYear => {
    let hisAge = 2022 - birthYear;
    let retirement = 95 - hisAge;
    return retirement;
}

console.log(`his retirement year remain is ${ramAge(2002)}`);

// type three

let Juice = (numberApple, numberOrange) => {
    return numberApple;
}
let appleJuice = Juice(2, 3);
console.log(appleJuice);


// calling a function inside other function

const cutPieces = function(fruit) {
    return fruit * 2
};

const fruitProcessor = function(apples, oranges) {
    const applePieces = cutPieces(apples);
    const orangePieces = cutPieces(oranges);

    const juice = `Juice with ${applePieces} pieces of apple and ${orangePieces} pieces of orange`;

    return juice;
};

console.log(fruitProcessor(2, 3));

// =====================================================================

