
for (var i = 0; i < 1; i++) {
    // here I created my loop for the array below
            let rowImgs = [
             '<img src="https://i.pinimg.com/564x/86/da/57/86da57ebc5780eddced1fc0530749e48.jpg">',
              '<img src="https://i.pinimg.com/564x/86/da/57/86da57ebc5780eddced1fc0530749e48.jpg">',
             '<img src="https://i.pinimg.com/564x/86/da/57/86da57ebc5780eddced1fc0530749e48.jpg">'
            ];
// here I created an array to house my images in, and linked them accordinly.

   var imgLocation = document.getElementById('imgBody');
   // here I tell it where on the html document I want the images to appear. I created a div with the id"imgBody"
   
    var output = rowImgs.join();
    // instead of .value like in my last assignment, I had to use .join, which I assume is beacause of working wtih an array this time
//I admit I had to use ChatGTP on this part to see what was wrong when I kept using .value, but I'm looking into it for myself now so I'll be ready next time.

       imgLocation.innerHTML += output;
       // here is where it's told to print the array to the DOM
       
       }

       //I used display: flex; to create a row, as the assignment didn't say strictly Javascript, but that's the only CSS I applied.