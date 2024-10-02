import pandas as pd
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata

# Load the sample data
data = pd.read_excel('sample_data.xlsx')

# Create metadata for the synthesizer
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(data)

# Initialize and fit the GaussianCopulaSynthesizer model
synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(data)

# Generate synthetic data
num_synthetic_samples = 1000  # Number of synthetic samples to generate
synthetic_data = synthesizer.sample(num_rows=num_synthetic_samples)

# Define the risk level mapping based on Risk Index
def assign_risk_level(risk_index):
    if risk_index >= 0.7:
        return 'High'
    elif risk_index >= 0.4:
        return 'Medium'
    else:
        return 'Low'

# Apply the mapping to the 'Risk Level' column
synthetic_data['Risk Level'] = synthetic_data['Risk Index'].apply(assign_risk_level)

# Replace the 'Asset ID' with meaningful values if required
synthetic_data['Asset ID'] = [f'A{i+1}' for i in range(len(synthetic_data))]

# Save the adjusted synthetic data to a CSV file
synthetic_data.to_csv('adjusted_synthetic_data.csv', index=False)

# Display the first few rows of the adjusted synthetic data
print(synthetic_data.head())
