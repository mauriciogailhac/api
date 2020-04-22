import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from test.models.models import User as UserModel, db
from uuid import uuid4


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel


class addUser(graphene.Mutation):
    """Add user."""
    name = graphene.String()
    userId = graphene.UUID()

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        data = {"name": name, "userId": uuid4()}
        user = UserModel(**data)
        db.session.add(user)
        db.session.commit()

        return addUser(userId=user.userId, name=user.name)


class removeUser(graphene.Mutation):
    """Delete user."""
    ok = graphene.Boolean()
    msg = graphene.String()

    class Arguments:
        userId = graphene.String(required=True)

    def mutate(self, info, userId):
        user = db.session.query(
            UserModel).filter(UserModel.userId == userId).first()
        if user:
            ok = True
            msg = "User deleted"
            db.session.delete(user)
            db.session.commit()
        else:
            msg = "User not found"
            ok = False
        return removeUser(ok=ok, msg=msg)

