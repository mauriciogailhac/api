import re
from graphql import GraphQLError


class Validator(object):

    @staticmethod
    def validate_name(name):
        """
        validate_name: ensure name len
        :param name: string
        :return: name
        """
        if len(name) <= 1:
            raise GraphQLError("Invalid name: name too short")
        return name

    @staticmethod
    def validate_email(email):
        """
        validate_email: email validator
        :param email: string: expected format test@test
        :return: email
        """
        result = re.search(r'\w+@\w+', email)
        if result:
            return email
        else:
            raise GraphQLError("Invalid email address")

    @staticmethod
    def validate_phone(phone):
        """
        validate_phone: phone validator
        :param phone: string: expected format 123-123-1234
        :return: phone
        """
        result = re.search(r'^(\d{3})-(\d{3})-(\d{4})$', phone)
        if result:
            return phone
        else:
            raise GraphQLError("Invalid phone number")

    @staticmethod
    def validate_type(type):
        """
        validate_type: type data validator
        :param type: string: email, phone
        :return: type
        """
        if type in ["email", "phone"]:
            return type
        else:
            raise GraphQLError("Invalid data type")
