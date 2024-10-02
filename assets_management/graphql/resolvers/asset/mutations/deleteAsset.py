import graphene
from assets_management.models import AssetListing

class DeleteAsset(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            asset = AssetListing.objects.get(pk=id)
            asset.delete()
            return DeleteAsset(success=True)
        except AssetListing.DoesNotExist:
            return DeleteAsset(success=False)
