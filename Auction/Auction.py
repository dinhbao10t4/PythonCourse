from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey


app = Flask(__name__)
app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

#Model
class Item(db.Model):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start_time = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, id, name, description, start_time, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.start_time = start_time
        self.user_id = user_id

class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

class UserItem(db.Model):
    __tablename__ = 'user_item'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('item.id'), nullable=False)
    user = db.relationship('User', backref='user_item', lazy=True)
    item = db.relationship('Item', backref='user_item', lazy=True)

    def __init__(self, id, user_id, item_id):
        self.id = id
        self.user_id = user_id
        self.item_id = item_id

class Bid(db.Model):
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    user_item_id = Column(Integer, ForeignKey('user_item.id'))
    user_item = db.relationship('UserItem', backref='user_item', lazy=True)

    def __init__(self, id, price, user_item_id):
        self.id = id
        self.price = price
        self.user_item_id = user_item_id

@app.route('/')
def hello_world():
    db.create_all()
    return 'init database!'

@app.route('/create4User')
def createUser():
    nam = User(1, 'nam', '123456')
    viet = User(2, 'viet', '123456')
    nu = User(3, 'nu', '123456')
    boss = User(4, 'boss', '123456')

    db.session.add(nam)
    db.session.add(viet)
    db.session.add(nu)
    db.session.add(boss)

    db.session.commit()

    return 'create 4 user'

@app.route('/createBaseballAndCar')
def createBaseball():
    baseball = Item(1, 'baseball', 'sport ball', '2009/05/31:12:00:00AM', 4)
    car = Item(2, 'car', 'sport car', '2009/05/31:12:00:00AM', 4)
    db.session.add(baseball)
    db.session.add(car)
    db.session.commit()

    return 'create item baseball & car'

@app.route('/bid-data')
def bidData():
    nam_baseball = UserItem(1, 1, 1)
    viet_baseball = UserItem(2, 2, 1)
    nu_baseball = UserItem(3, 3, 1)

    nam_baseball1 = Bid(1, 10.5, 1)
    nam_baseball2 = Bid(2, 11.5, 1)
    viet_baseball1 = Bid(3, 9.5, 2)
    viet_baseball2 = Bid(4, 13.5, 2)
    nu_baseball1 = Bid(5, 12.5, 3)
    nu_baseball2 = Bid(6, 15.5, 3)

    #create user bid item
    db.session.add(nam_baseball)
    db.session.add(viet_baseball)
    db.session.add(nu_baseball)
    db.session.commit()

    #bid price
    db.session.add(nam_baseball1)
    db.session.add(nam_baseball2)
    db.session.add(viet_baseball1)
    db.session.add(viet_baseball2)
    db.session.add(nu_baseball1)
    db.session.add(nu_baseball2)

    #CAR
    nam_car = UserItem(4, 1, 2)
    viet_car = UserItem(5, 2, 2)
    nu_car = UserItem(6, 3, 2)

    nam_car1 = Bid(7, 10.5, 4)
    nam_car2 = Bid(8, 20.5, 4)
    viet_car1 = Bid(9, 9.5, 5)
    viet_car2 = Bid(10, 13.5, 5)
    nu_car1 = Bid(11, 12.5, 6)
    nu_car2 = Bid(12, 15.5, 6)

    # create user bid item
    db.session.add(nam_car)
    db.session.add(viet_car)
    db.session.add(nu_car)
    db.session.commit()

    # bid price
    db.session.add(nam_car1)
    db.session.add(nam_car2)
    db.session.add(viet_car1)
    db.session.add(viet_car2)
    db.session.add(nu_car1)
    db.session.add(nu_car2)

    db.session.commit()
    return 'init some data bid'

@app.route('/select')
def select():
    query_result = UserItem.query.filter(UserItem.item_id == 1).join(Bid, Bid.user_item_id == UserItem.id).join(User, UserItem.user_id == User.id).add_columns(Bid.price, User.username, UserItem.item_id).order_by(Bid.price.desc()).first()
    return 'user placed the highest bid: ' + str(query_result.username) + ' with ' + str(query_result.price)

if __name__ == '__main__':
    app.run(debug=True)
