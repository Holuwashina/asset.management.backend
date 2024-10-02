from graphene_django.types import DjangoObjectType
from assets_management.models import AssessmentCategory as AssessmentCategoryModel

class AssessmentCategory(DjangoObjectType):
    class Meta:
        model = AssessmentCategoryModel
        fields = '__all__'
