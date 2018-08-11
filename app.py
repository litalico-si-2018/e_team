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
    all_user = User_table.query.all()
    return render_template("all_user.html",all_user = all_user)

# rooting of post
@app.route("/posting_page")
def top_page():
    if current_user.is_authenticated:
        return render_template("posting_page.html")
    else:
        return redirect("/")

# end post rooting

# rooting of past posted
@app.route("/posted_page",methods=["POST"])
def post_page():
    title = request.form["title"]
    contents = request.form["contents"]
    file = request.files["image"]
    file_path = "static/post_img/" + secure_filename(file.filename)
    file.save(file_path)
    new_page = Diary_table(id=current_user.id,title=title, contents=contents,file_path=file_path)
    db.session.add(new_page)
    db.session.commit()
    return redirect("/")

@app.route("/detailed_past_post/<int:diary_id>")
def detailed_past_post(diary_id):
    page = Diary_table.query.filter(Diary_table.diary_id == diary_id).first()
    return render_template("detailed_page.html",page=page)


# the end of past posted

#DBのコマンド
@app.cli.command("initdb")
def initdb_command():
    db.create_all()
