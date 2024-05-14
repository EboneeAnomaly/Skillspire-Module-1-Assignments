from flask import Flask, render_template

app = Flask(__name__)

pets = [
    {"id": 'maple.jpg', "name": "Maple", "type": "Dog", "age": 7, "bio": "I am a sassy corgi named Maple"}, 
    {"id": 'morty.jpg', "name": "Morty", "type": "Dog", "age": 4, "bio": "I am a neurotic corgi named Morty"},
    {"id": 'cubby.jpg', "name": "Cubby", "type": "Dog", "age": 3, "bio": "I am an adventurous corgi named Cubby"},
    {"id": 'GumGum.jpg', "name": "GumGum", "type": "Hedgehog", "age": 5, "bio": "I am a feisty hedgehog named GumGum"},
    ]

@app.route("/")
def prc():
    return render_template("Home page: Home - Paws Rescue Center.html", pets=pets)

@app.route("/about")
def about():
    return render_template("About page: About - Paws Rescue Center.html", pets=pets)

@app.route("/<pet_id>")
def pet_details(pet_id):
    pet = next((pet for pet in pets if pet["id"] == pet_id), None)
    if pet:
        return render_template("pet_details.html", pet=pet)
    else:
        return '<strong>' '<h1>' "Not Found" '</h1>' '</strong>'  +  "No pet was found with the given ID", 404



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

