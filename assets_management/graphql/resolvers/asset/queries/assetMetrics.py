import graphene
from django.db.models import Q
from assets_management.models import AssetListing
from assets_management.graphql.types.asset.assetMetrics import AssetMetricsType

class AssetMetrics(graphene.ObjectType):
    asset_metrics = graphene.Field(AssetMetricsType)

    def resolve_asset_metrics(self, info):
        total_assets = AssetListing.objects.count()
        classified_assets = AssetListing.objects.exclude(classification__isnull=True).exclude(classification__exact='').count()
        risk_analyzed = AssetListing.objects.filter(
            Q(risk_index__isnull=False) |
            Q(dt_predicted_risk_level__isnull=False) |
            Q(rf_predicted_risk_level__isnull=False) |
            Q(ensemble_predicted_risk_level__isnull=False)
        ).count()
        risk_identified = AssetListing.objects.exclude(risk_index__isnull=True).count()

        return AssetMetricsType(
            total_assets=total_assets,
            classified_assets=classified_assets,
            risk_analyzed=risk_analyzed,
            risk_identified=risk_identified
        )
