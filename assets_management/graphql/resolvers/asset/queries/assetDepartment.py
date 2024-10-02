import graphene
from assets_management.graphql.types.asset.assetDepartment import AssetDepartment
from assets_management.models import Department

class AssetDepartments(graphene.ObjectType):
    all_asset_departments = graphene.List(AssetDepartment)

    def resolve_all_asset_departments(self, info):
        return Department.objects.select_related('asset_value_mapping').all()