from test.models.models import db, User, Contact, ContactData


def resolve_allUsers(parent, info):
    return db.session.query(User).all()


def resolve_allContacts(parent, info):
    return db.session.query(Contact).all()


def resolve_allContactData(parent, info):
    return db.session.query(ContactData).all()

def resolve_getUser(parent, info, name):
    return db.session.query(User).filter(User.name == name).all()


def resolve_getContact(parent, info, contactId):
    contact = db.session.query(Contact).filter(Contact.contactId == contactId).first()
    return contact


def resolve_matchContact(parent, info, input):
    contact = db.session.query(Contact).join(Contact.contactData)
    for data in input.get("contactData"):
        contact = contact.filter(ContactData.type == data.get("type"),
                                 ContactData.value == data.get("value")).from_self()
    return contact.all()
