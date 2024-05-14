// 1. I establish my string and the .split method
// 2.



let str = "This is a test";
let arr = str.split("");

function reverse(){
arr.reverse();
let reversedStr = arr.join("");
return reversedStr;
}

console.log(reverse());