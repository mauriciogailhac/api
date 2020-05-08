import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from test.models.models import Contact as ContactModel, ContactData as ContactDataModel, User as UserModel,db
from uuid import uuid4
from test.validators import Validator
from test.schemas.error_schema import ErrorData


class ContactData(SQLAlchemyObjectType):
    """
    Create ContactData schema from data base model
    """
    class Meta:
        model = ContactDataModel
    # Add contactData on schema
    contactData = graphene.Field(lambda: ContactData)


class Contact(SQLAlchemyObjectType):
    """
    Create Contact schema from data base model
    """
    class Meta:
        model = ContactModel
    # Add contact and userId on schema
    contact = graphene.Field(lambda: Contact)
    userId = graphene.UUID()

    @staticmethod
    def resolve_userId(parent, info):
        """
        resolve_userId: function to get userId
        :param parent: SQLAlchemyObjectType
        :param info: GraphQL info
        :return: userID: UUID
        """
        # Find user in db to get userId
        user = db.session.query(UserModel).filter(UserModel.id == parent.userid).first()
        return user.userId

    @staticmethod
    def resolve_contact(parent, info):
        """
        resolve_contact: function to get Contact instance
        :param parent: SQLAlchemyObjectType
        :param info: GraphQL info
        :return: Contact: SQLAlchemyObjectType
        """
        # Get the current contact object
        return parent


class ContactDataInput(graphene.InputObjectType):
    """
    Class used to model input data format
    """
    type = graphene.String()
    value = graphene.String()


class matchInput(graphene.InputObjectType):
    """
    Class used to model input data format
    """
    contactData = graphene.List(ContactDataInput)


class ContactInput(graphene.InputObjectType):
    """
    Class used to model input data format
    """
    name = graphene.String()
    userId = graphene.String()
    contactData = graphene.List(ContactDataInput)


class addContacts(graphene.Mutation, ErrorData):
    """Add contacts mutation"""
    contacts = graphene.List(Contact)

    class Arguments:
        # Get input data
        input = graphene.List(ContactInput, required=True)

    def mutate(self, info, input):
        """
        mutate: Function to resolve mutation
        :param info: GraphQL info
        :param input: input data dict
        :return: response Contact list, error
        """
        contacts = []
        # iterate overall contacts
        for contact in input:

            contactId = uuid4()

            user = db.session.query(
            UserModel).filter(UserModel.userId == contact["userId"]).first()
            # check if user exist
            if user is None:
                return addContacts(error="User not found", contacts=[])

            data = {"userid": user.id, "name": contact["name"], "contactId": str(contactId)}
            # Save contact in db
            cont = ContactModel(**data)
            db.session.add(cont)
            db.session.commit()
            # iterate overall contactData
            for contdata in contact["contactData"]:

                co = db.session.query(ContactModel).filter(ContactModel.contactId == str(contactId)).first()

                # Validate type and value
                try:
                    type_data = Validator.validate_type(contdata["type"])

                    value = Validator.validate_email(contdata["value"]) if type_data == "email" \
                        else Validator.validate_phone(contdata["value"])
                except Exception as e:
                    return addContacts(error=str(e), contacts=[])

                data = {"type": type_data, "value": value, "contactid": co.id}
                # Save contactdata in db
                contd = ContactDataModel(**data)
                db.session.add(contd)
                db.session.commit()
            # list used to get desired response
            contacts.append(cont)
        return addContacts(contacts=contacts)


class removeContact(graphene.Mutation, ErrorData):
    """Delete contact mutation"""
    ok = graphene.Boolean()
    msg = graphene.String()

    class Arguments:
        # Get input data
        contactId = graphene.String(required=True)

    def mutate(self, info, contactId):
        """
        mutate: Function to resolve mutation
        :param info: GraphQL info
        :param contactId: UUID: contactId
        :return: response ok, error
        """
        # Get contact from db
        contact = db.session.query(
            ContactModel).filter(ContactModel.contactId == contactId).first()

        if contact:
            ok = True
            msg = ""
            # Delete from db
            db.session.delete(contact)
            db.session.commit()
        else:
            msg = "Contact not found"
            ok = False
        return removeContact(ok=ok, error=msg)
