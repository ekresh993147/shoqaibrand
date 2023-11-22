from flask import Flask, redirect, url_for
from werkzeug.utils import secure_filename
from main import available_users, create_entry, get_engine
from connection import User
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import os

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index2.html")

@app.route('/skills.html')
def skills():
    return render_template("skills.html")

@app.route('/register_page.html')
def register_page():
    return render_template("register_page.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/myprojects.html')
def myprojects():
    return render_template("myprojects.html")

@app.route("/upload", methods=["GET", "POST"])
def upload_file(context=None):
    if request.method == "POST":
        f = request.files["file_to_save"]
        if "saved files" not in os.listdir():
            os.mkdir("saved files")
        f.save(f"saved files/{secure_filename(f.filename)}")
        return redirect(url_for('upload_file', context={"Status": "Successfully uploaded"}))
    return render_template("file upload.html", context=context)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print(request.form)
        user_login = request.form.get("login")
        print(user_login)
        if user_login in list(available_users(get_engine())):
            return redirect(url_for('register_page', context={"Status": "UNSUCCESSFUL"}))
        else:
            user = User(login=request.form.get("login"),
                        user_fname=request.form.get("user_fname"),
                        user_sname=request.form.get("user_sname"),
                        password=request.form.get("password1"))
            create_entry([user], get_engine())

        return redirect(url_for('register', context={"Status": "Successfully registered"}))
    return render_template("register_page.html")

if __name__ == "__main__":
    app.run(debug=True)
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         message = request.form['message']
#
#         save_to_database(name, email, message)
#
#     return render_template('contact.html')
#
# def save_to_database(name, email, message):
#     new_message = ContactMessage(name=name, email=email, message=message)
#     db.session.add(new_message)
#     db.session.commit()