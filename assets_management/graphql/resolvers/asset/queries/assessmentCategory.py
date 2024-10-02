import graphene
from assets_management.models import AssessmentCategory as AssessmentCategoryModel
from assets_management.graphql.types.asset.assessmentCategory import AssessmentCategory as AssessmentCategoryGraphQLType

class AssessmentCategories(graphene.ObjectType):
    all_assessment_categories = graphene.List(AssessmentCategoryGraphQLType)

    def resolve_all_assessment_categories(self, info):
        return AssessmentCategoryModel.objects.all()
