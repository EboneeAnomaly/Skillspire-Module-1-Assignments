// 1. Declare an array
// 2. Create function and a for loop inside of it to iterate over the array
// 3. create an if statement inside of that for loop to see if the numbers are sequential and if they are tell it
// to return the lowest sequential number - the highest. 

let arr = [1, 13, 14, 15, 16, 37, 38, 39, 70]

function bookNumber(){
    let bookArr = ["-"];
    for(let i = 0; i < arr.length; i++){
        if (arr[i] === 13 & arr[i] > 16 ){
            return bookArr + arr[i]
        }
        
    }
}
console.log(bookNumber(arr))
