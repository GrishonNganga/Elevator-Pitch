from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50))
    l_name = db.Column(db.String(50))

    def __repr__(self):
        
        return '<User %r>' % self.f_name
