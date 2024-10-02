import graphene

class AssetListingInput(graphene.InputObjectType):
    asset = graphene.String(required=True)
    asset_type = graphene.String(required=True)
    owner_department_id = graphene.ID(required=True)
    asset_value_id = graphene.ID(required=True)
    description = graphene.String(required=False)
