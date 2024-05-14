let strArr = ["you", "I", "ab"]
let removedStr = ["I", "ab"]

strArr = strArr.filter(item => !removedStr.includes(item));


console.log(strArr)

let evenStrArr = ["Nope!", "its", "Kris", "starting", "with", "K!", "(instead", "of", "Chris", "with", "C)", "."]
let nonEvenStrArr = ["starting", "with", "K!", "(instead", "of", "with", "C)", "." ]

function filterEvenStrings(){
for (let i = 0; i < evenStrArr.length; i++){
    if (evenStrArr[i].length % 2 === 0){
    evenStrArr = evenStrArr.filter(item => !nonEvenStrArr.includes(item));
}
}
return evenStrArr;
}



console.log(filterEvenStrings());