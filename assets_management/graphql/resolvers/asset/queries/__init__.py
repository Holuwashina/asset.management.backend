import graphene
from assets_management.graphql.types.asset.asset import Asset
from assets_management.graphql.types.asset.assetType import AssetType
from assets_management.graphql.types.asset.assetDepartment import AssetDepartment
from assets_management.graphql.types.asset.assetValueMapping import AssetValueMappingType
from assets_management.graphql.types.asset.assetListing import AssetListingType
from assets_management.graphql.types.asset.assessmentCategory import AssessmentCategory
from assets_management.graphql.types.asset.assessmentQuestion import AssessmentQuestion
from assets_management.graphql.resolvers.asset.queries.assets import Assets as AssetsResolver
from assets_management.graphql.resolvers.asset.queries.assetTypes import AssetTypes as AssetTypesResolver
from assets_management.graphql.resolvers.asset.queries.assetDepartment import AssetDepartments as AssetDepartmentsResolver
from assets_management.graphql.resolvers.asset.queries.assetValueMapping import AssetValueMappings as AssetValueMappingResolver
from assets_management.graphql.resolvers.asset.queries.assetsListing import AssetsListing as AssetListingResolver
from assets_management.graphql.resolvers.asset.queries.assessmentCategory import AssessmentCategories as AssessmentCategoriesResolver
from assets_management.graphql.resolvers.asset.queries.assessmentQuestions import AssessmentQuestions as AssessmentQuestionsResolver
from assets_management.graphql.resolvers.asset.queries.assetMetrics import AssetMetrics as AssetMetricsResolver
from assets_management.graphql.types.asset.assetMetrics import AssetMetricsType

class AssetQueries(graphene.ObjectType):
    assets = graphene.List(Asset)
    asset_types = graphene.List(AssetType)
    asset_departments = graphene.List(AssetDepartment)
    asset_value_mapping = graphene.List(AssetValueMappingType)
    assets_listing = graphene.List(AssetListingType)
    assessment_categories = graphene.List(AssessmentCategory)
    assessment_questions = graphene.List(AssessmentQuestion)
    confidentiality_questions = graphene.List(AssessmentQuestion)
    integrity_questions = graphene.List(AssessmentQuestion)
    availability_questions = graphene.List(AssessmentQuestion)
    asset_metrics = graphene.Field(AssetMetricsType)

    def resolve_assets(self, info):
        return AssetsResolver().resolve_all_assets(info)

    def resolve_asset_types(self, info):
        return AssetTypesResolver().resolve_all_asset_types(info)

    def resolve_asset_departments(self, info):
        return AssetDepartmentsResolver().resolve_all_asset_departments(info)
    
    def resolve_asset_value_mapping(self, info):
        return AssetValueMappingResolver().resolve_all_asset_value_mapping(info)
    
    def resolve_assets_listing(self, info):
        return AssetListingResolver().resolve_all_assets_listing(info)
    

    def resolve_assessment_categories(self, info):
        return AssessmentCategoriesResolver().resolve_all_assessment_categories(info)

    def resolve_assessment_questions(self, info):
        return AssessmentQuestionsResolver().resolve_all_assessment_questions(info)

    def resolve_confidentiality_questions(self, info):
        return AssessmentQuestionsResolver().resolve_confidentiality_questions(info)

    def resolve_integrity_questions(self, info):
        return AssessmentQuestionsResolver().resolve_integrity_questions(info)

    def resolve_availability_questions(self, info):
        return AssessmentQuestionsResolver().resolve_availability_questions(info)
    
    def resolve_asset_metrics(self, info):
        return AssetMetricsResolver().resolve_asset_metrics(info)