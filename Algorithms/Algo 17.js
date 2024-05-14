let arr = [3, 0, 1]

function missingNum(){
for (let i = 1; i <= arr.length + 1; i++){
    if (!arr.includes(i)){
    return i;
    }
}

}
console.log (missingNum());

// function revArr(){
// for (let i = 1; i > arr.length; i++){
//     let arr[i]
// }
// }