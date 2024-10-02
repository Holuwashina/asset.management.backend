import graphene
from django.utils import timezone
from django.shortcuts import get_object_or_404
from assets_management.models import AssetListing
from assets_management.graphql.types.asset.assetListing import AssetListingType
from assets_management.utils.compute_risk_level import compute_risk_level

class RiskIdentificationMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        confidentiality = graphene.Float()
        integrity = graphene.Float()
        availability = graphene.Float()

    success = graphene.Boolean()
    asset = graphene.Field(AssetListingType)
    updated_at = graphene.DateTime()

    def mutate(self, info, id, confidentiality=None, integrity=None, availability=None):
        asset = get_object_or_404(AssetListing, id=id)

        # Update asset fields with values from frontend
        if confidentiality is not None:
            asset.confidentiality = round(confidentiality, 2)
        if integrity is not None:
            asset.integrity = round(integrity, 2)
        if availability is not None:
            asset.availability = round(availability, 2)

         # Fetch classification_value and round it to 2 decimal places
        classification_value = asset.classification_value or 0
        asset.updated_at = timezone.now()

        # Compute risk level
        if all(value is not None for value in [asset.confidentiality, asset.integrity, asset.availability]):
            asset.risk_index = compute_risk_level(
                asset.confidentiality, 
                asset.integrity, 
                asset.availability, 
                classification_value
            )

        asset.save()

        return RiskIdentificationMutation(success=True, asset=asset)