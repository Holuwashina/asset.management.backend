import graphene

class AssessmentQuestionInput(graphene.InputObjectType):
    category_id = graphene.ID(required=True)
    question_text = graphene.String(required=True)
