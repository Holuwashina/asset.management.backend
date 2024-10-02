import graphene
from assets_management.models import AssetListing, Department, AssetValueMapping, AssetType
from assets_management.graphql.types.asset.assetListing import AssetListingType
from assets_management.graphql.types.asset.assetListingInput import AssetListingInput

class UpdateAssetListing(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = AssetListingInput(required=True)

    asset_listing = graphene.Field(AssetListingType)

    def mutate(self, info, id, input):
        # Retrieve the asset listing to update
        try:
            asset_listing = AssetListing.objects.get(id=id)
        except AssetListing.DoesNotExist:
            raise Exception(f"AssetListing with id {id} does not exist.")

        # Update related objects if needed
        if input.owner_department_id:
            try:
                owner_department = Department.objects.get(id=input.owner_department_id)
                asset_listing.owner_department = owner_department
            except Department.DoesNotExist:
                raise Exception(f"Department with id {input.owner_department_id} does not exist.")

        if input.asset_value_id:
            try:
                asset_value = AssetValueMapping.objects.get(id=input.asset_value_id)
                asset_listing.asset_value = asset_value
            except AssetValueMapping.DoesNotExist:
                raise Exception(f"AssetValueMapping with id {input.asset_value_id} does not exist.")

        # Update fields
        asset_listing.asset = input.asset
        asset_listing.description = input.description
        asset_listing.asset_type = input.asset_type
        # asset_listing.classification = input.classification
        # asset_listing.classification_value = input.classification_value

        asset_listing.save()

        return UpdateAssetListing(asset_listing=asset_listing)
