from init import db, ma 
from marshmallow import fields 

class Card(db.Model): 
    __tablename__ = "card"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    status = db.Column(db.String)
    priority = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='cards')



    # # {id: 1, title: Card 1, user_id: 2}

class CardSchema(ma.Schema): 

    user = fields.Nested('UserSchema', only = ['name', 'email'])

    class Meta: 
        fields = ('id', 'title', 'description', 'status', 'priority', 'user')

card_schema = CardSchema()
cards_schema = CardSchema(many=True)



    