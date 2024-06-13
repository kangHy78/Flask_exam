from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import Text, db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/friends", methods=["GET", "POST"])
def friends():
    return render_template('friends.html')

@app.route("/chats", methods=["GET", "POST"])
def chats():
    return render_template('chats.html')

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        content = request.form.get('content')
        if content:
            new_text = Text(content=content)
            db.session.add(new_text)
            db.session.commit()
        return redirect(url_for('chat'))

    texts = Text.query.all()
    return render_template('chat.html', texts=texts)

@app.route("/delete_all", methods=["POST"])
def delete_all():
    Text.query.delete()
    db.session.commit()
    return redirect(url_for('chat'))