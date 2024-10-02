import graphene
from assets_management.graphql.types.asset.asset import Asset as AssetType 
from assets_management.models import Asset as AssetModel

class Assets(graphene.ObjectType):
    all_assets = graphene.List(AssetType) 

    def resolve_all_assets(self, info):
        return AssetModel.objects.all() 
