import graphene
from assets_management.models import AssessmentQuestion as AssessmentQuestionModel
from assets_management.graphql.types.asset.assessmentQuestion import AssessmentQuestion as AssessmentQuestionGraphQLType

class AssessmentQuestions(graphene.ObjectType):
    def resolve_all_assessment_questions(self, info):
        return AssessmentQuestionModel.objects.all()

    def resolve_confidentiality_questions(self, info):
        return AssessmentQuestionModel.objects.filter(category__name="Confidentiality")

    def resolve_integrity_questions(self, info):
        return AssessmentQuestionModel.objects.filter(category__name="Integrity")

    def resolve_availability_questions(self, info):
        return AssessmentQuestionModel.objects.filter(category__name="Availability")