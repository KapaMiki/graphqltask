import graphene
from apps.users.schema import Query as users_query, Mutations


class Query(users_query):
    pass



schema = graphene.Schema(query=Query, mutation=Mutations)