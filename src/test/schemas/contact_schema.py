import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from test.models.models import Contact as ContactModel, ContactData as ContactDataModel, User as UserModel,db
from uuid import uuid4


class ContactData(SQLAlchemyObjectType):
    class Meta:
        model = ContactDataModel

    contactData = graphene.Field(lambda: ContactData)
    contactId = graphene.UUID()

    @staticmethod
    def resolve_contactId(parent, info):
        contact = db.session.query(ContactModel).filter(ContactModel.id == parent.contactid).first()
        return contact.contactId


class Contact(SQLAlchemyObjectType):
    class Meta:
        model = ContactModel

    contact = graphene.Field(lambda: Contact)
    userId = graphene.UUID()

    @staticmethod
    def resolve_userId(parent, info):
        user = db.session.query(UserModel).filter(UserModel.id == parent.userid).first()
        return user.userId

    @staticmethod
    def resolve_contact(parent, info):
        return parent


class ContactDataInput(graphene.InputObjectType):
    type = graphene.String()
    value = graphene.String()


class matchInput(graphene.InputObjectType):
    contactData = graphene.List(ContactDataInput)


class ContactInput(graphene.InputObjectType):
    name = graphene.String()
    userId = graphene.String()
    contactData = graphene.List(ContactDataInput)


class addContacts(graphene.Mutation):
    """Add contacts."""
    contacts = graphene.List(Contact)

    class Arguments:
        input = graphene.List(ContactInput, required=True)

    def mutate(self, info, input):
        contacts = []
        for contact in input:

            contactId = uuid4()

            user = db.session.query(
            UserModel).filter(UserModel.userId == contact["userId"])

            data = {"userid": user[0].id, "name": contact["name"], "contactId": str(contactId)}

            cont = ContactModel(**data)
            db.session.add(cont)
            db.session.commit()

            for contdata in contact["contactData"]:

                co = db.session.query(ContactModel).filter(ContactModel.contactId == str(contactId))
                data = {"type": contdata["type"], "value": contdata["value"], "contactid": co[0].id}
                contd = ContactDataModel(**data)
                db.session.add(contd)
                db.session.commit()

            contacts.append(cont)
        return addContacts(contacts=contacts)


class removeContact(graphene.Mutation):
    """Delete contact."""
    ok = graphene.Boolean()
    msg = graphene.String()

    class Arguments:
        contactId = graphene.String(required=True)

    def mutate(self, info, contactId):
        contact = db.session.query(
            ContactModel).filter(ContactModel.contactId == contactId).first()

        if contact:
            ok = True
            msg = "User deleted"
            db.session.delete(contact)
            db.session.commit()
        else:
            msg = "Contact not found"
            ok = False
        return removeContact(ok=ok, msg=msg)

