import graphene


# Define a graphene ObjectType to encapsulate error and use hierarchy

class ErrorData(graphene.ObjectType):
    error = graphene.String(default_value="")
