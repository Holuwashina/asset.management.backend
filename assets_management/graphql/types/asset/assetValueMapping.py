from graphene_django.types import DjangoObjectType
from assets_management.models import AssetValueMapping

class AssetValueMappingType(DjangoObjectType):
    class Meta:
        model = AssetValueMapping
