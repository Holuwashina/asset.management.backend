import graphene
from assets_management.models import AssessmentQuestion as AssessmentQuestionModel

class DeleteAssessmentQuestion(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            question = AssessmentQuestionModel.objects.get(pk=id)
            question.delete()
            return DeleteAssessmentQuestion(success=True)
        except AssessmentQuestionModel.DoesNotExist:
            return DeleteAssessmentQuestion(success=False)
