function mul(mulArr){
    var multipliedArr = [];

    for (i = 0; i < numArr.length; i++) {

        multipliedArr.push(numArr[i] * 2);
    }
    return multipliedArr;
}

var numArr = [1, 2, 3, 4, 5];

console.log(mul(numArr));