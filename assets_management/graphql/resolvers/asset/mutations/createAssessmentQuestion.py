import graphene
from assets_management.models import AssessmentQuestion, AssessmentCategory
from assets_management.graphql.types.asset.assessmentQuestion import AssessmentQuestion as AssessmentQuestionType
from assets_management.graphql.types.asset.assessmentQuestionInput import AssessmentQuestionInput

class CreateAssessmentQuestion(graphene.Mutation):
    class Arguments:
        input = AssessmentQuestionInput(required=True)

    assessment_question = graphene.Field(AssessmentQuestionType)

    def mutate(self, info, input):
        # Retrieve the related category
        try:
            category = AssessmentCategory.objects.get(id=input.category_id)
        except AssessmentCategory.DoesNotExist:
            raise Exception(f"AssessmentCategory with id {input.category_id} does not exist.")
        
        # Create the AssessmentQuestion instance
        assessment_question = AssessmentQuestion.objects.create(
            category=category,
            question_text=input.question_text
        )

        return CreateAssessmentQuestion(assessment_question=assessment_question)
