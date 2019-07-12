import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User



class UserType(DjangoObjectType):
    class Meta:
        model = User


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = User.objects.create_user(username=username, password=password,email=email)
        user.save()
        return CreateUser(user=user)


class UserMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        username = graphene.String(required=False)
        email = graphene.String(required=False)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
    user = graphene.Field(UserType)


    def mutate(self, info, id, username, email, first_name, last_name):
        user = User.objects.get(id=id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        
        return UserMutation(user=user)


class Mutations(graphene.ObjectType):
    update_user = UserMutation.Field()
    create_user = CreateUser.Field()

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType,
                        id=graphene.Int(),
                        username=graphene.String())

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
            return User.objects.get(id=id)

        if username is not None:
            return User.objects.get(username=username)

        return None
