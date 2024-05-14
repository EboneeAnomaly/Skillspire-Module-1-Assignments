// For algo 2: use a dictionary

// 1. I establish my array and create my function
// 2. I create a for loop and tell it that to split 

let arr = [1,[2,3],4[]]

function flattenArr(){
let flattened = [];
arr.forEach(item => {
    if (Array.isArray(item)) {
        flattened.push(...flattenArr(item));
    } else if (item !== undefined && item !== null){
        flattened.push(item);
    }
});
return flattened;
}


console.log(flattenArr(arr));