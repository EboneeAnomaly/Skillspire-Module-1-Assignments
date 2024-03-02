let colorButton = document.getElementById('colorButton');
// here I declare the submit button from my HTML side as 'colorButton' -
// - and target it here on the JS side.
colorButton.addEventListener('click', function onClick() {
// here I tell it to wait for the button to be clicked and then run the function on the click.
    event.preventDefault();
// I stop the submit button from refreshing the page, which would instantly revert the change here.
    let colorBox = document.getElementById('colorBox');
// I assign the div to change colors to 'colorBox' here.
colorBox.style.border = '2px solid lightblue';
// here I tell it I want the div styled and how
});