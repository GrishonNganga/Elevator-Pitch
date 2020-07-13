from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), nullable = False)
    l_name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(80), unique = True)

    def __repr__(self):
        
        return '<User %r>' % self.f_name

class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1000), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    user = db.relationship('User', backref = db.backref('pitches', lazy = True))
    category = db.relationship('Category', backref = db.backref('categories', lazy = True))

    def __repr__(self):
        
        return '<Pitch %r>' % self.message


class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))

    def __repr__(self):
        
        return '<Category %r>' % self.name

class Upvote(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    pitch = db.relationship('Pitch', db.backref('upvotes', lazy = True))
    user = db.relationship('User', db.backref('upvotes', lazy = True))


class Downvote(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    pitch = db.relationship('Pitch', db.backref('downvotes', lazy = True))
    user = db.relationship('User', db.backref('downvotes', lazy = True))

   