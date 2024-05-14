// 1. I create my string and assign it a variable
// 2. Then I create my function and inside of that a for loop to iterate over the string
// 3. I then give that for loop an if/else statement

// This was the result for the above "solution", it does not work

// let lowString = "hello there skillspire"

// function capitalize(str){
// for (let i = 1; i < lowString.length; i++){
//     if (lowString[i] != lowString.capitalize()){
//     lowString.capitalize();
//     }
// }
// }
// console.log(capitalize());

// Algo 15 (1) Solution: //

let lowString = "hello there skillspire";

// function capitalize(str){
// return str.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
// }

// console.log(capitalize(lowString));

// Algo 14 (1) With no built in functions that aren't needed
function capitalize(str){
    let words = str.split(' ');
    for (let i = 0; i < words.length; i++){
        words[i] = words[i].charAt(0).toUpperCase() + words[i].slice(1);
    }
    return words.join(' ');
}

console.log(capitalize(lowString));

// Algo 15 (2)

let whiteSpaceStr = "whitespaces  are  cool"

function whiteSpace(whiteSpaceStr.remove())