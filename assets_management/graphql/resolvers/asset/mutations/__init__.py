import graphene
from .createAssetListing import CreateAssetListing
from .deleteAsset import DeleteAsset
from .updateAssetListing import UpdateAssetListing
from .createAssessmentQuestion import CreateAssessmentQuestion
from .deleteAssessmentQuestion import DeleteAssessmentQuestion
from .classifyAsset import ClassifyAssetMutation
from .riskIdentify import RiskIdentificationMutation
from .riskAnalyze import RiskAnalyzeMutation

class AssetMutations(graphene.ObjectType):
    create_asset_listing = CreateAssetListing.Field()
    delete_asset = DeleteAsset.Field()
    update_asset_listing = UpdateAssetListing.Field()
    create_assessment_question = CreateAssessmentQuestion.Field()
    delete_assessment_question = DeleteAssessmentQuestion.Field()
    classify_asset = ClassifyAssetMutation.Field()
    identify_risk = RiskIdentificationMutation.Field()
    analyze_risk = RiskAnalyzeMutation.Field()
