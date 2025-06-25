from flask import Flask, render_template
from app import create_app, db

app = create_app()

# ✅ This route serves index.html from templates
@app.route("/")
def home():
    return render_template("index.html")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
