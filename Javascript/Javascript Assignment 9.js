

function nval(){
    let numArray = [-1, 2, -3, 4, -5];
// I declare my function and then initiate array, as well as feed it my negative and positive number base
    for (let i = 0; i < numArray.length; i++) {
        // I initiate my loop, and tell it that my numArray.length is greater than o and to increment by 1
        if (numArray[i] < 0) {
            // here I tell it that if my numArray is less than 0 aka negative to print "Negative"
console.log("Negative");
        } else {
            // here I say otherwise print the number in the array as is.
            console.log(numArray[i]);
    }
}

}
// I pulled from today's lecture to get most of the answer, and had chatGTP check my weakspots to finish.


function backwords(string){
    let words = string.split('');
    // declared my function and then told it to split the string 'string' into an array
    let wordsReversed = words.reverse();
// then I told it to reverse that array
    let inverseWords = wordsReversed.join('');
// then I told it to join that array, while still reversed
    console.log(inverseWords);
    // then I told it to print to console
}

backwords('string');
// here I call my function. I admit I relied on chatGTP as well as Stackoverflow pretty heavily for this one
// - but I will do some more practive with this on my own.