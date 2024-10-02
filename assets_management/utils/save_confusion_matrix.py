from sklearn.metrics import confusion_matrix
from django.utils import timezone
from assets_management.models import ConfusionMatrix

def save_confusion_matrix(y_true, y_pred, model_name, label_encoder):
    cm = confusion_matrix(y_true, y_pred)
    labels = label_encoder.classes_  # Encoded labels
    
    print("Confusion Matrix:\n", cm)  # Debugging line
    print("Labels:\n", labels)  # Debugging line

    for i, true_label in enumerate(labels):
        for j, predicted_label in enumerate(labels):
            print(f"Saving: Model: {model_name}, True: {true_label}, Predicted: {predicted_label}, Count: {cm[i, j]}")  # Debugging line
            ConfusionMatrix.objects.create(
                model_name=model_name,
                true_label=true_label,
                predicted_label=predicted_label,
                count=cm[i, j],
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
