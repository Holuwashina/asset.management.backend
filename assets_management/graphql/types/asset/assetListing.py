from graphene_django.types import DjangoObjectType
from assets_management.models import AssetListing

class AssetListingType(DjangoObjectType):
    class Meta:
        model = AssetListing