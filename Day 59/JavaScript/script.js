/*

let js = "amazing";
// if (js === "amazing") alert("js is fun");
console.log(23 + 12 - 40);
console.log("Bhawesh");

let fName = "Bhawesh";
let lName = "Chaudhary";


// Naming convention
// 1. camel case notation is standard eg. myFirstNameIsBhaweshChaudhary
// 2. illegal variable eg. 3years; bhawesh&chadhary
// 3. Js only contain letters, numbers, underscore, or dollar sign
// 4. don't use reserved javascript keyword such as new, this, 
// 5. don't start variable with upper case for normal variable, only use it for constant variables.
// 6. variable name should be descriptive, means, easy to read and understand.

// Assignment 1 

let country = 'Nepal';
let continent = 'South Asia';
let population = '2.91 Crores';

console.log("The continent of " + country + " is " + continent + " and it's population is " + population);


// Data Types

// 7 data types

// Number  ->  for numbers of any kind: integer or floating-point, integers are limited by ±(253-1).


// string -> for strings. A string may have zero or more characters, there’s no separate single-character type.


// let fullName = fName + " " + lName;
// console.log(fullName);
// console.log(`the result of 4+6 is ${4 + 6}`)



// boolean -> for true/false.



// undefined (variable without value) -> for unassigned values – a standalone type that has a single value undefined.

// let number;
// console.log(number)


// Null -> for unknown values – a standalone type that has a single value null.
// let age = null;
// console.log(age)


// Symbol -> for unique identifiers.



// BigInt -> is for integer numbers of arbitrary length.


// object -> for more complex data structures.


// the typeof operator

// console.log(typeof undefined);       // returns undefined
// console.log(typeof alert);          // return function
// console.log(typeof 10n);            // returns bigint
// console.log(typeof true);           // returns boolean
// console.log(typeof 1);              // returns number
// console.log(typeof "id");           // returns string
// console.log(typeof Symbol("id"));   // returns symbol
// console.log(typeof Math);           // returns object
// console.log(typeof null);           // returns object


// alert, prompt, and confirm

// let age = prompt("What is your age ?")
// alert(`You are ${age} yrs old.`)

console.log("6" / "2");


// Basic operator math
// + - * / %
// alert(+"");



let one = "1";
let two = "2";

//alert(one + two); // return 12 by concatenating string
//alert(+one + +two); // return 3 by converting string to number and adding them

// Bitwise operator

// bitwise operator treat arguments as 32 bit integers number and work on the level of their binary representation.
// And &
// Or |
// XOR ^
// Not ~
// Left shift <<
// Right shift >>
// Zero-fill right shift >>>


// COMMA
// The comma operator , is one of the rarest and most unusual operators. Sometimes, it’s used to write shorter code, so we need to know it in order to understand what’s going on.

// The comma operator allows us to evaluate several expressions, dividing them with a comma,.Each of them is evaluated but only the result of the last one is returned.

// let a = (1 + 2, 3 + 4);

// alert(a); // 7 (the result of 3 + 4)


// Comparison


// conditional branching
let age = 16;
// let ages = (age > 15) ? alert("you're young") : alert("You're child");

// Assignment

// let userAnswer = prompt("What's the official name of javascript?");
// let answer = userAnswer == "Ecmascript" ? alert("Right") : alert("You don't know Ecmascript?");



// Logical operators






JavaScript Fundamentals – Part 1 
 
 
Coding Challenge #1 

Mark and John are trying to compare their BMI(Body Mass Index), which is 
calculated using the formula:

BMI = mass / height ** 2 = mass / (height * height)(mass in kg 
and height in meter). 

Your tasks:

1. Store Mark's and John's mass and height in variables

2. Calculate both their BMIs using the formula(you can even implement both 
versions)

3. Create a Boolean variable 'markHigherBMI' containing information about 
whether Mark has a higher BMI than John. 

Test data: 

Data 1: Marks weights 78 kg and is 1.69 m tall.John weights 92 kg and is 1.95 tall. 

Data 2: Marks weights 95 kg and is 1.88 m tall.John weights 85 kg and is 1.76 tall.



let firstGuy = "Mark";
let secondGuy = "John";
let markMass = prompt(`${firstGuy}, Please enter your weight in kg`);
let markHeight = prompt(`${firstGuy}, Please enter your height in meter`);
let markBmi = markMass / markHeight ** 2;
document.getElementById("mark").innerHTML = `Mark your BMI is ${markBmi}`;
let forJohn = confirm("Do you want to calculate BMI for John also?");
if (forJohn == true) {
    let johnMass = prompt(`${secondGuy}, Please enter your weight in kg`);
    let johnHeight = prompt(`${secondGuy}, Please enter your height in meter`);
    let johnBmi = johnMass / johnHeight ** 2;
    document.getElementById("john").innerHTML = `John your BMI is ${johnBmi}`;
}

*/