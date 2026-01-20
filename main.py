from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/921b568d74c8959ac84e").json()
print(response)



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", all_posts=response)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def get_post(num):
    requested_post = None
    for post in response:
        if post["id"] == num:
            requested_post = post
    return render_template("post.html", blog=requested_post)

if __name__ == "__main__":
    app.run(debug=True)