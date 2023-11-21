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