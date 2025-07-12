from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    items = db.relationship('Item', backref='owner', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100))
    size = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
    tags = db.Column(db.String(200))
    image_filename = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Item {self.title}>"
