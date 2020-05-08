import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from test.models.models import User as UserModel, db
from uuid import uuid4
from test.validators import Validator
from test.schemas.error_schema import ErrorData


class User(SQLAlchemyObjectType):
    """
    Create User schema from data base model
    """
    class Meta:
        model = UserModel


class addUser(graphene.Mutation, ErrorData):
    """Add user mutation."""

    name = graphene.String()
    userId = graphene.UUID()

    class Arguments:
        # Get Input data
        name = graphene.String(required=True)

    def mutate(self, info, name):
        """
        mutate: Function to resolve mutation
        :param info: GraphQL info
        :param name: input name data
        :return: response userId, name, error
        """
        # validate data
        try:
            name = Validator.validate_name(name)
        except Exception as e:
            # return error
            return addUser(error=str(e), userId=None, name="")
        # save new user in db
        data = {"name": name, "userId": uuid4()}
        user = UserModel(**data)
        db.session.add(user)
        db.session.commit()

        return addUser(userId=user.userId, name=user.name)


class removeUser(graphene.Mutation, ErrorData):
    """
    Delete user mutation.
    """
    ok = graphene.Boolean()
    msg = graphene.String()

    class Arguments:
        # Get Input data
        userId = graphene.String(required=True)

    def mutate(self, info, userId):
        """
        mutate: Function to resolve mutation
        :param info: GraphQL info
        :param userId: UUID
        :return: response ok, error
        """
        # Find user in db
        user = db.session.query(
            UserModel).filter(UserModel.userId == userId).first()
        if user:
            ok = True
            msg = ""
            # Delete user
            db.session.delete(user)
            db.session.commit()
        else:
            msg = "User not found"
            ok = False
        return removeUser(ok=ok, error=msg)

