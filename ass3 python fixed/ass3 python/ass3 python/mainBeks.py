# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(50), unique=True)
#     psw = db.Column(db.String(500), nullable=True)
#     data = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return f"<Users {self.id}>"
#
# class Profiles(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=True)
#     old = db.Column(db.Integer)
#     city = db.Column(db.String(100))
#
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#             return f"<profiles {self.id}>"
#
# @app.route('/index2.html') #changed to be / instead of /index2.html
# def main():
#     return render_template("index2.html")
#
#
# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#         app.run(debug=True)