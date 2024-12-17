# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     chat_id = db.Column(db.String(100), unique=True, nullable=False)
#     facts_sent = db.Column(db.Integer, default=0)
#
#     def __repr__(self):
#         return f'<User {self.chat_id}>'
