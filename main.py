from flask import Flask, render_template,request
import requests
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

response = requests.get("https://api.npoint.io/921b568d74c8959ac84e").json()
print(response)

email_user = os.environ.get("EMAIL_USER")
email_pass = os.environ.get("EMAIL_PASS")
to_email = os.environ.get("MY_EMAIL")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", all_posts=response)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == "GET":
        return render_template("contact.html", success=False)
    else:
        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form["phone"]
        message = request.form["message"]
        email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone_number}\nMessage: {message}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email_user, password=email_pass)
            connection.sendmail(
                from_addr=email_user,
                to_addrs=to_email,
                msg= email_message
            )

        return render_template("contact.html", success=True)


@app.route("/post/<int:num>")
def get_post(num):
    requested_post = None
    for post in response:
        if post["id"] == num:
            requested_post = post
    return render_template("post.html", blog=requested_post)

@app.route("/form-entry", methods=["POST"])
def receive_data():
    pass

if __name__ == "__main__":
    app.run(debug=True)
