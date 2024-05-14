let str = ["Dylan to the"];

function greeting(){
for (let i = 0; i < str.length; i++){
    let sentence = str[i];
    if(sentence.startsWith("D")){
       let shiftedSentence = sentence.substring(1) + sentence.charAt(0);
       return shiftedSentence
    }
}
}
console.log (greeting())

// My idea for the second problem was to capitlize the first letter of every word, 
// and drop the letters that aren't capitalized.
// With my original solution I was only getting the first letter of the string, and
// after class I went to ChatGTP to clean it up and troubleshoot. I needed to create a variable for my new string,
// split the string, and then append the capitlized letter of each word to that new string. Then I had it return that
// string. 
// I packed the result and the array I wanted to pass into the result variable and then called that variable

function acronym(strArr){
    let acronym = "";
    let words = strArr[0].split(" ");
for (let i = 0; i < words.length; i++){
    let word = words[i];
    acronym += word.charAt(0).toUpperCase();

    }
    return acronym;
}

let stringIndex = ["Live From New York, It's Saturday Night!"]
let result = acronym(stringIndex);
console.log(result);

//"Live From New York, It's Saturday Night!"
// "There's No Free Lunch Gotta Pay Your Way."

