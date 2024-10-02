from django.db import models
import uuid

class TimeStampedModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AssetValueMapping(TimeStampedModel):
    qualitative_value = models.CharField(max_length=20, unique=True)
    crisp_value = models.FloatField()

    def __str__(self):
        return self.qualitative_value
    
class Department(TimeStampedModel):
    name = models.CharField(max_length=255)
    asset_value_mapping = models.ForeignKey(AssetValueMapping, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return self.name

class AssetType(TimeStampedModel):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Asset(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class AssetListing(TimeStampedModel):
    asset = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True) 
    asset_type = models.CharField(max_length=255)
    owner_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    asset_value = models.ForeignKey(AssetValueMapping, on_delete=models.CASCADE)
    classification = models.CharField(max_length=255, null=True, blank=True)
    classification_value = models.FloatField(null=True, blank=True)
    confidentiality = models.FloatField(null=True, blank=True)
    integrity = models.FloatField(null=True, blank=True)
    availability = models.FloatField(null=True, blank=True)
    risk_index = models.FloatField(null=True, blank=True)
    dt_predicted_risk_level = models.CharField(max_length=10, null=True, blank=True)
    rf_predicted_risk_level = models.CharField(max_length=10, null=True, blank=True)
    ensemble_predicted_risk_level = models.CharField(max_length=10, null=True, blank=True)
    risk_treatment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.asset} - {self.classification}"


class AssessmentCategory(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    

class AssessmentQuestion(TimeStampedModel):
    category = models.ForeignKey(
        AssessmentCategory, 
        on_delete=models.CASCADE, 
        related_name='questions'
    )
    question_text = models.TextField()
    
    def __str__(self):
        return self.question_text
    

# Model to store classification report metrics
class ClassificationReport(TimeStampedModel):
    model_name = models.CharField(max_length=255)
    precision = models.FloatField()
    recall = models.FloatField()
    f1_score = models.FloatField()
    support = models.IntegerField()

    def __str__(self):
        return f"{self.model_name} - Precision: {self.precision}, Recall: {self.recall}"


# Model to store confusion matrix results
class ConfusionMatrix(TimeStampedModel):
    model_name = models.CharField(max_length=255)
    true_label = models.CharField(max_length=255)
    predicted_label = models.CharField(max_length=255)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.model_name} - True: {self.true_label}, Predicted: {self.predicted_label}, Count: {self.count}"