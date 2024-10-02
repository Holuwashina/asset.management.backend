import graphene
from assets_management.graphql.types.asset.assetListing import AssetListingType 
from assets_management.models import AssetListing

class AssetsListing(graphene.ObjectType):
    all_assets_listing = graphene.List(AssetListingType) 

    def resolve_all_assets_listing(self, info):
        return AssetListing.objects.all().order_by('-updated_at') 
