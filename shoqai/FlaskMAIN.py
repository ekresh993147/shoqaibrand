from flask import Flask, redirect, url_for
from flask import render_template
from werkzeug.utils import secure_filename
from flask import request 
import os
from main import *
from connection import *

app = Flask(__name__)


@app.route("/")
def home():
    context = {"Data":"Some data here to be sent as dict (JSON)"}
    return render_template("index.html")

@app.route("/suit01.html")
def suit01():
    return render_template("suit01.html")

@app.route("/suit02.html")
def suit02():
    return render_template("suit02.html")

@app.route("/suit03.html")
def suit03():
    return render_template("suit03.html")

@app.route("/suit04.html")
def suit04():
    return render_template("suit04.html")

@app.route("/suit05.html")
def suit05():
    return render_template("suit05.html")

@app.route("/suit06.html")
def suit06():
    return render_template("suit06.html")



@app.route("/upload", methods=["GET", "POST"])
def upload_file(context=None):
    if request.method=="POST":
        f = request.files["file_to_save"]
        if "saved files" not in os.listdir(): 
            os.mkdir("saved files")
        f.save(f"saved files/{secure_filename(f.filename)}")
        return redirect(url_for('upload_file', context={"Status":"Successfully uploaded"}))
    return render_template("file upload.html", context=context)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="POST":
        print(request.form)
        user_login = request.form.get("login")
        print(user_login)
        if user_login in list(available_users(get_engine())):
            return redirect(url_for('register', context={"Status":"UNSUCCESSFUL"}))
        else:

            user = User(login=request.form.get("login"), 
                        user_fname=request.form.get("user_fname"),
                        user_sname=request.form.get("user_sname"),
                        password = request.form.get("password1")
                        )
            create_entry([user], get_engine())
            
        return redirect(url_for('register', context={"Status":"Successfully regsitered"}))
    return render_template("register_page.html")
    




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)