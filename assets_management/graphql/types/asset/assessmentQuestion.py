import graphene
from graphene_django.types import DjangoObjectType
from assets_management.models import AssessmentQuestion as AssessmentQuestionModel
from assets_management.graphql.types.asset.assessmentCategory import AssessmentCategory

class AssessmentQuestion(DjangoObjectType):
    class Meta:
        model = AssessmentQuestionModel
        fields = '__all__'

    category = graphene.Field(lambda: AssessmentCategory)

    def resolve_category(self, info):
        return self.category
