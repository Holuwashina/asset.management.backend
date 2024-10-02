import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assets_management.settings')

# Initialize Django
django.setup()


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.metrics import confusion_matrix

# Import custom functions to save the classification report and confusion matrix
from assets_management.utils.save_classification_report import save_classification_report
from assets_management.utils.save_confusion_matrix import save_confusion_matrix

# Load the synthetic data
synthetic_data = pd.read_csv('adjusted_synthetic_data.csv')

# Encode the 'Risk Level' to numeric values
label_encoder = LabelEncoder()
synthetic_data['Risk Level'] = label_encoder.fit_transform(synthetic_data['Risk Level'])

# Save the label encoder
joblib.dump(label_encoder, 'label_encoder.pkl')

# Define features (X) and the target (y)
X = synthetic_data[['Confidentiality', 'Integrity', 'Availability', 'Risk Index']]
y = synthetic_data['Risk Level']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Apply SMOTE for handling class imbalance
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Initialize models
decision_tree = DecisionTreeClassifier(random_state=42)
random_forest = RandomForestClassifier(random_state=42)

# Define hyperparameter grids
dt_param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
}

rf_param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
}

# Perform GridSearchCV for Decision Tree
dt_grid_search = GridSearchCV(estimator=decision_tree, param_grid=dt_param_grid, cv=5, scoring='accuracy')
dt_grid_search.fit(X_train_res, y_train_res)
best_dt_model = dt_grid_search.best_estimator_

# Perform GridSearchCV for Random Forest
rf_grid_search = GridSearchCV(estimator=random_forest, param_grid=rf_param_grid, cv=5, scoring='accuracy')
rf_grid_search.fit(X_train_res, y_train_res)
best_rf_model = rf_grid_search.best_estimator_

# Define and fit the ensemble model
ensemble_model = VotingClassifier(estimators=[
    ('dt', best_dt_model),
    ('rf', best_rf_model)
], voting='soft')

ensemble_model.fit(X_train_res, y_train_res)

# Perform cross-validation
dt_cv_scores = cross_val_score(best_dt_model, X_train_res, y_train_res, cv=5, scoring='accuracy')
rf_cv_scores = cross_val_score(best_rf_model, X_train_res, y_train_res, cv=5, scoring='accuracy')

print(f"Decision Tree Cross-Validation Scores: {dt_cv_scores}")
print(f"Random Forest Cross-Validation Scores: {rf_cv_scores}")

# Train the models
best_dt_model.fit(X_train_res, y_train_res)
best_rf_model.fit(X_train_res, y_train_res)

# Make predictions
dt_predictions = best_dt_model.predict(X_test)
rf_predictions = best_rf_model.predict(X_test)
ensemble_predictions = ensemble_model.predict(X_test)

# Evaluate the models
print("Decision Tree Accuracy:", accuracy_score(y_test, dt_predictions))
print("Random Forest Accuracy:", accuracy_score(y_test, rf_predictions))
print("Ensemble Model Accuracy:", accuracy_score(y_test, ensemble_predictions))

# Generate classification reports
dt_report = classification_report(y_test, dt_predictions, output_dict=True)
rf_report = classification_report(y_test, rf_predictions, output_dict=True)
ensemble_report = classification_report(y_test, ensemble_predictions, output_dict=True)

# Save the classification reports
save_classification_report(dt_report, 'Decision Tree')
save_classification_report(rf_report, 'Random Forest')
save_classification_report(ensemble_report, 'Ensemble Model')

# Save confusion matrices
save_confusion_matrix(y_test, dt_predictions, 'Decision Tree', label_encoder)
save_confusion_matrix(y_test, rf_predictions, 'Random Forest', label_encoder)
save_confusion_matrix(y_test, ensemble_predictions, 'Ensemble Model', label_encoder)

# Function to plot and save classification report
def plot_classification_report(report, title='Classification Report', filename=None):
    report_df = pd.DataFrame(report).transpose()
    report_df = report_df.iloc[:-1, :]  # Remove the 'accuracy' row
    plt.figure(figsize=(10, 6))
    sns.heatmap(report_df, annot=True, cmap='Blues', fmt='.2f')
    plt.title(title)
    if filename:
        plt.savefig(filename)
    plt.show()

# Plot and save the classification reports
plot_classification_report(dt_report, title='Decision Tree Classification Report', filename='dt_classification_report.png')
plot_classification_report(rf_report, title='Random Forest Classification Report', filename='rf_classification_report.png')
plot_classification_report(ensemble_report, title='Ensemble Model Classification Report', filename='ensemble_classification_report.png')

# Function to plot confusion matrix
def plot_confusion_matrix(y_true, y_pred, title='Confusion Matrix', filename=None):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title(title)
    if filename:
        plt.savefig(filename)
    plt.show()

# Plot and save confusion matrices
plot_confusion_matrix(y_test, dt_predictions, title='Decision Tree Confusion Matrix', filename='dt_confusion_matrix.png')
plot_confusion_matrix(y_test, rf_predictions, title='Random Forest Confusion Matrix', filename='rf_confusion_matrix.png')
plot_confusion_matrix(y_test, ensemble_predictions, title='Ensemble Confusion Matrix', filename='ensemble_confusion_matrix.png')

# Save the trained models
joblib.dump(best_dt_model, 'best_decision_tree_model.pkl')
joblib.dump(best_rf_model, 'best_random_forest_model.pkl')
joblib.dump(ensemble_model, 'best_ensemble_model.pkl')
