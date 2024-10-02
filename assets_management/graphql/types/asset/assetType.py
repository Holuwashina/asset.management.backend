from graphene_django.types import DjangoObjectType
from assets_management.models import AssetType

class AssetType(DjangoObjectType):
    class Meta:
        model = AssetType