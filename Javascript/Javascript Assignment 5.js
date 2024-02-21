document.addEventListener('DOMContentLoaded', function() {
    var formCon = document.getElementById('formCon')

// I couldn't get this to work without 'DOMContentLoaded which I saw on ChatGTP and then researched on a few forums.
// I declared my form container here.

    formCon.addEventListener('submit', function(event) {
        event.preventDefault();

// Here I added the event listener to catch when the submit button goes through + prevent it from trying to find a url

        var valueZone = document.getElementById('valueZone');

        // here is where i declared the area in my HTML body that houses the printed textbox values.

        var fName = document.getElementById('fName').value;
        var lName = document.getElementById('lName').value;
        var eMail = document.getElementById('eMail').value;
        var userAge = document.getElementById('userAge').value;

        var output = fName + lName + eMail + userAge;

        // I declared the output and concatenated & assigned the text-box id's here.
        
        valueZone.innerHTML = output;

        // here is where I tell it to print the output (which I declared the text fields as) to the HTML page
        
    });
});