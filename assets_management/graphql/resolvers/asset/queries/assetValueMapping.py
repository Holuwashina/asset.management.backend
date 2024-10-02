import graphene
from assets_management.graphql.types.asset.assetValueMapping import AssetValueMappingType
from assets_management.models import AssetValueMapping

class AssetValueMappings(graphene.ObjectType):
    all_asset_value_mapping = graphene.List(AssetValueMappingType)

    def resolve_all_asset_value_mapping(self, info):
        return AssetValueMapping.objects.all()