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
    supporter_id = db.Column(db.Integer)
    supported_id = db.Column(db.Integer)
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

@app.route("/articles/1")
def supported_posting():
    # adminのデータを持ってくる
    return render_template("article.html")

# rooting of post
@app.route("/admin/articles")
def supporter_posting():
    # ユーザーのデータを持ってくる
    return render_template("article.html")

# end post rooting

# rooting of past posted
@app.route("/posted_page",methods=["POST"])
def post_page():
    contents = request.form["contents"]
    file.save(file_path)
    # supporter/suppportedのidを取ってくる
    new_article = Message_table(contents=contents)
    db.session.add(new_article)
    db.session.commit()
    return redirect("/")

# the end of past posted

#DBのコマンド
@app.cli.command("initdb")
def initdb_command():
    db.create_all()
