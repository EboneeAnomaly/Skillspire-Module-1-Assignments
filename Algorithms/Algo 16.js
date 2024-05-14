// 1. I create a function and label it 'shuffle' that accepts an array called arr
// 2. Then I create a for loop inside of the function so that it iterates over the array


function shuffle(arr){
    for (let i = arr.length - 1; i > 0; i--){
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] =  [arr[j], arr[i]];
    }
    return arr;
}
console.log(shuffle([1, 2, 3]));


// 1. I declare my arr2 and assign it an array
// 2. Then I create my function, and create two variables for min and max
// 3. Then I create a for loop to iterate over the array
// 4. I create the variable temp, and assign it to array index
// 5. I create an if statement 

let arr2 = [1, 2, 3, 4, 5]

function filterRange(arr){
let min = arr[0];
let max = arr[0];
for (let i = 1; i < arr.length; i++){
    let temp = arr[i]
if (temp < min) {
    min = temp;
}
if (temp > max){
    max = temp;
}
}
return{min, max};
}
console.log(filterRange(arr2));