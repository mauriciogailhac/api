from test.models.models import db, User, Contact, ContactData


# Queries resolvers


def resolve_allUsers(parent, info):
    """
    resolve_allUsers: function to get all users
    :param parent:
    :param info:
    :return: all users
    """
    return db.session.query(User).all()


def resolve_allContacts(parent, info):
    """
    resolve_allContacts: function to get all Contacts
    :param parent:
    :param info:
    :return: all contacts
    """
    return db.session.query(Contact).all()


def resolve_allContactData(parent, info):
    """
    resolve_allContactData: function to get all ContactData
    :param parent:
    :param info:
    :return: all ContactData
    """
    return db.session.query(ContactData).all()


def resolve_getContact(parent, info, contactId):
    """
    resolve_getContact: function to get a contact by contactId
    :param parent:
    :param info:
    :param contactId: UUID: contactId
    :return: Contact
    """
    contact = db.session.query(Contact).filter(Contact.contactId == contactId).first()
    return contact


def resolve_getUser(parent, info, name):
    """
    resolve_getUser: function to get an user by name
    :param parent:
    :param info:
    :param name: string: user name
    :return:
    """
    return db.session.query(User).filter(User.name == name).all()


def resolve_matchContact(parent, info, input):
    """
    resolve_matchContact: function to get any contact that match with an array of contactData
    :param parent:
    :param info:
    :param input: ContactData list
    :return: Contact list
    """
    contact = db.session.query(Contact).join(Contact.contactData)
    for data in input.get("contactData"):
        contact = contact.filter(ContactData.type == data.get("type"),
                                 ContactData.value == data.get("value")).from_self()
    return contact.all()
