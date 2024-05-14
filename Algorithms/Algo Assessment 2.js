// Array Shuffle: Create a function called shuffle(arr), 
// to efficiently shuffle a given array’s values in random order. 
//Hint: Remember the swap method? Use a random number
// generator to come up index that needs to be swapped. [1,2,3] => [2,1,3], [3,1,2]​

// Steps:
// 1. I create my function and pass it the arr
// 2. I create my for loop to go through the array & tell it to do this backwards
// 3. I tell it to swap the array elements 
// 4. I pass my arguments to the parameter  

function shuffle(arr){
    for (let i = arr.length - 1; i > 0; i--){
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] =  [arr[j], arr[i]];
    }
    return arr;
}
console.log(shuffle([1, 2, 3]));

//----- Algo # 2

// 2. Array: Filter Range. Given arr and values min and max, retain only the array values
// between min and max indexes. Given [1,2,3,4,5],2,4 return [3,4,5].No built-in array
// functions. This does not have to be done in place meaning you don't have to return the same
// array that was passed in as a parameter.

// Steps:
// 1. First function and my arrays + min/max storage 
// 2. I store my array in result
// 3. Then I create a for loop to iterate over that array and I store 2 in min and 4 in max.
// 4. I tell it to push result, which
// I then tell it to return result, and console.log my function and arrays. 

let filteredArr = [1, 2, 3, 4, 5];
let min = 2;
let max = 4;

function filterRange(filteredArr, min, max){
let result = [];
for (let i = min; i <= max; i++){
    result.push(filteredArr[i]);
}
return result;
}

console.log(filterRange(filteredArr, min, max));

//---- Algo #3:

// #3. Create a standalone function that accepts an input string,removes leading and trailing 
// white spaces (at beginning and end only) from the string and capitalizes 
// the first letter of every word, and return that string. ​

// Steps:
// 1. I Create my function & my string
// 2. I store str.trim in str, and store my split string in 'words' variable and then establish a for loop
// 3.  I tell it look at the letters in my string at capitalize the first one
// 4. I join my string back together and then console.log my function and my string

let lowString = '   goodbye and good evening   ';

function capitalizeAndTrim(str){
    str = str.trim();

    let words = str.split(' ');

    for (let i = 0; i < words.length; i++){
        if (words[i] !== '') {
            words[i] = words[i].charAt(0).toUpperCase() + words[i].slice(1).toLowerCase();
        }
    }
    return words.join(' ');
}

console.log(capitalizeAndTrim(lowString));

// ---- # 4:


//---- Algo #4:
// Given a string of words (sentence) create a function that capitalizes every word in the string. 
// Given “hello there skillspire” return “Hello There Skillspire”. Remember don’t use any built in 
// methods to complete this task except any methods that capitalize a character. 
// Remember don’t use any built in methods to complete this task except any methods 
// that capitalize a character.​


// Steps:
// 1. I create my string and function and pass my string to it
// 2. Then I split my string and store that in 'words2'
// 3. I create a for loop and tell it to go over my string and capitalize the first letter of each word
// 4. I then rejoin my string and console.log my function and string

let capitalStr = 'goodbye and have a nice trip';

function capitalize(capitalStr){
    let words2 = capitalStr.split(' ');
    for (let i = 0; i < words2.length; i++){
        words2[i] = words2[i].charAt(0).toUpperCase() + words2[i].slice(1);
    }
    return words2.join(' ');
}

console.log(capitalize(capitalStr));

//---- #5:

// Algo #5:

// Acronyms. Create a function that, given a string, returns the string’s acronym 
// (first letters only, capitalized). Given "there's no free lunch gotta pay yer way", return 
// "TNFLGPYW". Given "Live from New York it's Saturday Night", return "LFNYISN".

// Steps:
// 1. I create my function and my strings
// 2. I store my string in acronym and and split my string and append each letter to my new string, capitalized

let stringIndex = ["Live From New York, It's Saturday Night!"];

let result = acronym(stringIndex);
function acronym(strArr){
    let acronym = "";
    let words = strArr[0].split(" ");
for (let i = 0; i < words.length; i++){
    let word = words[i];
    acronym += word.charAt(0).toUpperCase();

    }
    return acronym;
}


console.log(result);

