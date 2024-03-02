var myPics = [
    'https://i.pinimg.com/564x/89/5e/f9/895ef995d6f5f6840bff8da7a5ad11a8.jpg', 
    'https://i.pinimg.com/564x/47/82/53/47825381d51295333fe296166906cf7c.jpg', 
    'https://i.pinimg.com/564x/3c/a4/b8/3ca4b8ae412c76e336e42ee1e640ff3f.jpg'
];
// here I decalred my image array and link the image urls that will be used.
var i = 0;
       var totalPics = myPics.length;
       var loopTimer;
// here I did my declaration for the variables that will be found in the loop below
function loop() {
    if(i >= (totalPics)){
       i = 0;
    }
    // here I initiated my loop that will keep the pictures cycling.
    var imgUrl = myPics[i];
    // here I linked imgUrl to my array
    var picArea = document.getElementById('picArea');
    picArea.innerHTML = '<img src="'+imgUrl+'" />';
    i++;
    loopTimer = setTimeout('loop()',3000);
    // here I told it to print to the 'picArea' div on the DOM, and I set the timer for 3 seconds -
    // - before it iterates to the next image, and loops back to start.
}

loop();
// here is where I call the function to initiate it.