from flask import Flask,render_template,request,session, redirect, make_response,url_for
import psycopg2
import psycopg2.extras
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ufawifyagwer1742yncs2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/litalico'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

#モデルの定義エリア
class User_table(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True)

class Message_table(db.Model):
    diary_id = db.Column(db.Integer,primary_key = True)
    sender_id = db.Column(db.Integer)
    receiver_id = db.Column(db.Integer)
    contents = db.Column(db.String(400))
    attention = db.Column(db.Integer)

#ルーティングエリア
@app.route("/")
def home():
    return "hello_world"

@app.route("/admin/users")
def show_users():
    all_user = User_table.query.filter(User_table.id >= 2)
    return render_template("all_user.html",all_user = all_user)

@app.route("/admin/articles/<int:id>")
def supporter_posting(id):
    if Message_table.query.filter(Message_table.sender_id==2):
        from_message = Message_table.query.filter(Message_table.sender_id==2)
        username = "test"
        return render_template("re_article.html",username=username,from_message=from_message)
    else:
        return render_template("none.html")

@app.route("/posted_page",methods=["POST"])
def post_page():
    id = request.form["id"]
    contents = request.form["contents"]
    sender_id = 2
    receiver_id = 1
    new_article = Message_table(sender_id=sender_id, receiver_id = receiver_id,contents=contents,attention=0)
    db.session.add(new_article)
    db.session.commit()
    return redirect("/")

@app.route("/articles/new")
def supported_posting():
    id = 2
    past_message = Message_table.query.filter(Message_table.sender_id == 2)
    return render_template("article.html",id=id,past_message=past_message)

@app.route("/attention",methods=["POST"])
def attention():
    diary_id = request.form["diary_id"]
    update_attention = Message_table.query.filter(Message_table.diary_id == diary_id).first()
    update_attention.attention = 1
    db.session.commit()
    return redirect("/")

#DBのコマンド
@app.cli.command("initdb")
def initdb_command():
    db.create_all()
