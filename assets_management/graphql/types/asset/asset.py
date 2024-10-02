from graphene_django.types import DjangoObjectType
from assets_management.models import Asset

class Asset(DjangoObjectType):
    class Meta:
        model = Asset