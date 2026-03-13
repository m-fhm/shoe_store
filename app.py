from flask import Flask, render_template

app = Flask(__name__)

# Mock data representing our shoe collection
SHOES = [
    {"id": 1, "name": "Cloud Walker", "price": 120, "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400"},
    {"id": 2, "name": "Urban Edge", "price": 85, "image": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=400"},
    {"id": 3, "name": "Trail Blazer", "price": 150, "image": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=400"}
]

@app.route('/')
def index():
    return render_template('index.html', shoes=SHOES)

if __name__ == '__main__':
    app.run(debug=True)