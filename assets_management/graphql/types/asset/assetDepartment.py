import graphene
from graphene_django.types import DjangoObjectType
from assets_management.models import Department, AssetValueMapping

class AssetValueMappingType(DjangoObjectType):
    class Meta:
        model = AssetValueMapping
        fields = ('id', 'qualitative_value', 'crisp_value')

class AssetDepartment(DjangoObjectType):
    class Meta:
        model = Department
        fields = ('id', 'name', 'asset_value_mapping', 'reason')

    asset_value_mapping = graphene.Field(AssetValueMappingType)