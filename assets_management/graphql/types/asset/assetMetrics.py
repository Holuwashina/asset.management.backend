import graphene

class AssetMetricsType(graphene.ObjectType):
    total_assets = graphene.Int()
    classified_assets = graphene.Int()
    risk_analyzed = graphene.Int()
    risk_identified = graphene.Int()
