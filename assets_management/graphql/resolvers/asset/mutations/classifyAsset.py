import graphene
from graphene_django.types import DjangoObjectType
from assets_management.models import AssetListing, AssetValueMapping, Department
from assets_management.graphql.types.asset.assetListing import AssetListingType
from assets_management.utils.classification import classify_asset

class ClassifyAssetMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    asset = graphene.Field(AssetListingType)

    def mutate(self, info, id):
        try:
            asset = AssetListing.objects.get(id=id)
        except AssetListing.DoesNotExist:
            return ClassifyAssetMutation(success=False, asset=None)

        # Retrieve asset value and department impact from the related models
        asset_value_mapping = asset.asset_value
        department = asset.owner_department

        if not asset_value_mapping or not department:
            return ClassifyAssetMutation(success=False, asset=None)

        # Map asset value and department impact to numeric values
        asset_value_input = asset_value_mapping.crisp_value
        department_impact_input = department.asset_value_mapping.crisp_value

        # Apply fuzzy logic
        classification_value = classify_asset(asset_value_input, department_impact_input)
        print(f'Classification value: {classification_value}')

        # Map numeric classification to a string value
        if classification_value <= 0.2:
            classification_string = 'Very Low'
        elif classification_value <= 0.4:
            classification_string = 'Low'
        elif classification_value <= 0.6:
            classification_string = 'Medium'
        elif classification_value <= 0.8:
            classification_string = 'High'
        else:
            classification_string = 'Very High'

        # Update asset with classification
        asset.classification_value = classification_value
        asset.classification = classification_string
        asset.save()

        return ClassifyAssetMutation(success=True, asset=asset)
