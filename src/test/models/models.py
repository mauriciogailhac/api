from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ContactData(db.Model):
    """
    Class to model data base - ORM
    """
    __tablename__ = 'contactData'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(120), nullable=False)
    value = db.Column(db.String(120), nullable=False)
    contactid = db.Column(db.Integer, db.ForeignKey('contact.id', ondelete='CASCADE'))


class Contact(db.Model):
    """
    Class to model data base - ORM
    """
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    contactId = db.Column(db.String, nullable=False)
    contactData = db.relationship(ContactData, backref='contact', passive_deletes=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))


class User(db.Model):
    """
    Class to model data base - ORM
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    userId = db.Column(db.String, nullable=False)
    contacts = db.relationship(Contact, backref='user', passive_deletes=True)
