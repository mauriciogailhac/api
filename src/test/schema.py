import graphene
from test.schemas import user_schema
from test.schemas import contact_schema
from test.resolvers import resolve_allUsers, resolve_allContacts, resolve_allContactData,\
    resolve_getContact, resolve_matchContact, resolve_getUser


class Query(graphene.ObjectType):
    """
    Class to define queries
    """
    allUsers = graphene.List(user_schema.User, resolver=resolve_allUsers)
    allContacts = graphene.List(contact_schema.Contact, resolver=resolve_allContacts)
    allContactData = graphene.List(contact_schema.ContactData, resolver=resolve_allContactData)
    getContact = graphene.Field(
                                    contact_schema.Contact, resolver=resolve_getContact,
                                    contactId=graphene.String(required=True)
                                )
    getUser = graphene.List(user_schema.User, resolver=resolve_getUser, name=graphene.String(required=True))
    matchContact = graphene.List(
                                    contact_schema.Contact, resolver=resolve_matchContact,
                                    input=contact_schema.matchInput()
                                  )


class Mutation(graphene.ObjectType):
    """
    Class to define mutations
    """
    addContacts = contact_schema.addContacts.Field()
    removeContact = contact_schema.removeContact.Field()

    addUser = user_schema.addUser.Field()
    removeUser = user_schema.removeUser.Field()


# Define GraphQL schema of our API


schema = graphene.Schema(query=Query, mutation=Mutation)
