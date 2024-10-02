import graphene
from assets_management.models import AssetListing, Department, AssetValueMapping, AssetType
from assets_management.graphql.types.asset.assetListing import AssetListingType
from assets_management.graphql.types.asset.assetListingInput import AssetListingInput

class CreateAssetListing(graphene.Mutation):
    class Arguments:
        input = AssetListingInput(required=True)

    asset_listing = graphene.Field(AssetListingType)

    def mutate(self, info, input):
        # Retrieve the related objects
        try:
            owner_department = Department.objects.get(id=input.owner_department_id)
            asset_value = AssetValueMapping.objects.get(id=input.asset_value_id)
            asset_type = AssetType.objects.get(name=input.asset_type)  # Assuming asset_type is a string name
        except Department.DoesNotExist:
            raise Exception(f"Department with id {input.owner_department_id} does not exist.")
        except AssetValueMapping.DoesNotExist:
            raise Exception(f"AssetValueMapping with id {input.asset_value_id} does not exist.")
        except AssetType.DoesNotExist:
            raise Exception(f"AssetType with name {input.asset_type} does not exist.")

        # Create the AssetListing instance
        asset_listing = AssetListing.objects.create(
            asset=input.asset,
            asset_type=asset_type,
            owner_department=owner_department,
            asset_value=asset_value,
            description=input.description,
            # classification=input.classification,
            # classification_value=input.classification_value
        )

        return CreateAssetListing(asset_listing=asset_listing)