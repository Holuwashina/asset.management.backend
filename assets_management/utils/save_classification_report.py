from assets_management.models import ClassificationReport
from django.utils import timezone

def save_classification_report(report, model_name):
    for label, metrics in report.items():
        if label != 'accuracy':
            ClassificationReport.objects.create(
                model_name=model_name,
                precision=metrics['precision'],
                recall=metrics['recall'],
                f1_score=metrics['f1-score'],
                support=metrics['support'],
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
