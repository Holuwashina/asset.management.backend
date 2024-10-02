import graphene
from django.utils import timezone
from django.shortcuts import get_object_or_404
from assets_management.models import AssetListing
from assets_management.graphql.types.asset.assetListing import AssetListingType
import joblib
import pandas as pd
import os
from django.conf import settings

# Define the mitigation suggestion function
def suggest_mitigation(risk_level):
    if risk_level == 'High':
        return "Apply advanced encryption, multi-factor authentication, continuous monitoring."
    elif risk_level == 'Medium':
        return "Apply regular updates, intrusion detection systems, access control."
    else:
        return "Basic security protocols, periodic review."

class RiskAnalyzeMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    asset = graphene.Field(AssetListingType)
    updated_at = graphene.DateTime()

    def mutate(self, info, id):
        try:
            # Retrieve the asset instance
            asset = get_object_or_404(AssetListing, id=id)

            # Ensure all necessary fields are available
            if (asset.confidentiality is not None and 
                asset.integrity is not None and 
                asset.availability is not None and 
                asset.risk_index is not None):
                
                # Update the timestamp
                asset.updated_at = timezone.now()

                # Prepare data for model prediction
                features_df = pd.DataFrame({
                    'Confidentiality': [round(asset.confidentiality, 2)],
                    'Integrity': [round(asset.integrity, 2)],
                    'Availability': [round(asset.availability, 2)],
                    'Risk Index': [round(asset.risk_index, 2)]
                })

                # Load models with error handling
                try:
                    decision_tree = joblib.load(os.path.join(settings.BASE_DIR, 'assets_management', 'best_decision_tree_model.pkl'))
                    random_forest = joblib.load(os.path.join(settings.BASE_DIR, 'assets_management', 'best_random_forest_model.pkl'))
                    ensemble_model = joblib.load(os.path.join(settings.BASE_DIR, 'assets_management', 'best_ensemble_model.pkl'))
                except FileNotFoundError as e:
                    print(f"Model file not found: {e}")
                    return RiskAnalyzeMutation(success=False, asset=None)
                except Exception as e:
                    print(f"Error loading model: {e}")
                    return RiskAnalyzeMutation(success=False, asset=None)

                # Load label encoder
                try:
                    label_encoder = joblib.load(os.path.join(settings.BASE_DIR, 'assets_management', 'label_encoder.pkl'))
                except FileNotFoundError as e:
                    print(f"Label encoder file not found: {e}")
                    return RiskAnalyzeMutation(success=False, asset=None)
                except Exception as e:
                    print(f"Error loading label encoder: {e}")
                    return RiskAnalyzeMutation(success=False, asset=None)

                # Make predictions with error handling
                try:
                    dt_prediction = decision_tree.predict(features_df)[0]
                    rf_prediction = random_forest.predict(features_df)[0]
                    ensemble_prediction = ensemble_model.predict(features_df)[0]

                    # Convert numeric predictions to class labels
                    dt_label = label_encoder.inverse_transform([dt_prediction])[0]
                    rf_label = label_encoder.inverse_transform([rf_prediction])[0]
                    ensemble_label = label_encoder.inverse_transform([ensemble_prediction])[0]

                    print(f"Decision Tree Prediction: {dt_label}")
                    print(f"Random Forest Prediction: {rf_label}")
                    print(f"Ensemble Prediction: {ensemble_label}")

                    # Store predictions in the asset instance
                    asset.dt_predicted_risk_level = dt_label
                    asset.rf_predicted_risk_level = rf_label
                    asset.ensemble_predicted_risk_level = ensemble_label

                    # Suggest risk treatment based on the ensemble prediction
                    asset.risk_treatment = suggest_mitigation(ensemble_label)

                    # Save the asset instance
                    asset.save()
                except Exception as e:
                    print(f"Error making prediction: {e}")
                    return RiskAnalyzeMutation(success=False, asset=None)

            # Return success response
            return RiskAnalyzeMutation(success=True, asset=asset)
        except Exception as e:
            print(f"Error in mutation: {e}")
            return RiskAnalyzeMutation(success=False, asset=None)
