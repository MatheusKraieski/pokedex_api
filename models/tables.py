from app import db
db.create_all()

class User(db.model):
    __tablename__ = "users"
    id = Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    emial = db.Column(db.String, unique=True)

    def __init__(self, usarname, password, name, email):
        self.usarname = usarname
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.usarname
