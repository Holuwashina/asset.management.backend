import graphene
from assets_management.graphql.types.asset.asset import Asset as AssetGraphQLType
from assets_management.models import AssetType as AssetTypeModel

class AssetTypes(graphene.ObjectType):
    all_asset_types = graphene.List(AssetGraphQLType)

    def resolve_all_asset_types(self, info):
        return AssetTypeModel.objects.all()
