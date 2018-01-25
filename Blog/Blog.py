from flask import Flask, send_file, request, jsonify
import json
from flask.ext.login import UserMixin,LoginManager,login_user,current_user,logout_user,login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,DateTime
from hashlib import md5
import datetime

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

app.secret_key='thisissecretkey'

db = SQLAlchemy(app)
login_manager=LoginManager()
login_manager.init_app(app)


class User(UserMixin,db.Model):
    id=Column(Integer,primary_key=True,autoincrement=True)
    user_name=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)

    def __init__(self,username,password):
        self.user_name=username
        self.setPassword(password)

    def setPassword(self,password):
        self.password=md5(password.encode()).hexdigest()


class Entry(db.Model):
    __tablename__ = 'entry'

    id = Column(Integer, primary_key=True,autoincrement=True)
    title = Column(String(1024))
    content = Column(String)
    datetime = Column(DateTime,default=datetime.datetime.now)
    user_id = Column(Integer, nullable=False)

    def __init__(self,title,content):
        self.title=title
        self.content = content
        self.user_id = current_user.get_id()


@login_manager.user_loader
def load_user(user_name):
    return User.query.get(user_name)


@app.route("/")
def index():
    db.create_all()
    return send_file("templates/index.html")


@app.route('/register', methods=['POST'])
def register():
    data = json.loads(request.data.decode())
    print(data["userName"])
    print(data["password"])
    username = data["userName"]
    password = data["password"]
    db.session.add(User(username, password))
    db.session.commit()

    return jsonify({'result': 'success'})


@app.route('/login', methods=['POST'])
def login():
    message = 'success'
    data = json.loads(request.data.decode())
    username = data["userName"]
    password = data["password"]

    user = User.query.filter_by(user_name=username, password=md5(password.encode()).hexdigest()).first()
    if user:
        login_user(user=user)
    else:
        message = 'wrong username or password'
    print(message)
    print(current_user.get_id())
    return jsonify({'result': message})


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return "Logout!"


@app.route('/blog', methods=['POST'])
def createNewBlog():
    message = 'success'
    data = json.loads(request.data.decode())
    title = data["title"]
    content = data["content"]

    print(title)
    print(content)
    db.session.add(Entry(title, content))
    db.session.commit()

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
