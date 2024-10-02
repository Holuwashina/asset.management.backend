import graphene
from assets_management.graphql.resolvers.asset.queries import AssetQueries
from assets_management.graphql.resolvers.asset.mutations import AssetMutations

class Query(AssetQueries, graphene.ObjectType):
    pass

class Mutation(AssetMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
