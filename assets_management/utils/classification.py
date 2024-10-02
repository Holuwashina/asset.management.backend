import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def classify_asset(asset_value_input: float, department_impact_input: float) -> float:
    """
    Classifies an asset based on its value and the impact of its owning department
    using fuzzy logic.

    Parameters:
    asset_value_input (float): The value of the asset on a scale from 0 to 1.
    department_impact_input (float): The impact of the department that owns the asset on a scale from 0 to 1.

    Returns:
    float: The classification of the asset on a scale from 0 to 1.
    """

    # Define the fuzzy variables
    asset_value = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'asset_value')
    owner_department = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'owner_department')
    classification = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'classification')

    # Define the membership functions with scale from 0 to 1
    asset_value['very_low'] = fuzz.trimf(asset_value.universe, [0, 0, 0.2])
    asset_value['low'] = fuzz.trimf(asset_value.universe, [0, 0.2, 0.4])
    asset_value['medium'] = fuzz.trimf(asset_value.universe, [0.2, 0.5, 0.8])
    asset_value['high'] = fuzz.trimf(asset_value.universe, [0.4, 0.7, 1])
    asset_value['very_high'] = fuzz.trimf(asset_value.universe, [0.8, 1, 1])

    owner_department['very_low'] = fuzz.trimf(owner_department.universe, [0, 0, 0.2])
    owner_department['low'] = fuzz.trimf(owner_department.universe, [0, 0.2, 0.4])
    owner_department['medium'] = fuzz.trimf(owner_department.universe, [0.2, 0.5, 0.8])
    owner_department['high'] = fuzz.trimf(owner_department.universe, [0.4, 0.7, 1])
    owner_department['very_high'] = fuzz.trimf(owner_department.universe, [0.8, 1, 1])

    classification['very_low'] = fuzz.trimf(classification.universe, [0, 0, 0.2])
    classification['low'] = fuzz.trimf(classification.universe, [0, 0.2, 0.4])
    classification['medium'] = fuzz.trimf(classification.universe, [0.2, 0.5, 0.8])
    classification['high'] = fuzz.trimf(classification.universe, [0.4, 0.7, 1])
    classification['very_high'] = fuzz.trimf(classification.universe, [0.8, 1, 1])

    # Define fuzzy rules that incorporate the new membership functions
    rules = [
        ctrl.Rule(asset_value['very_low'] & owner_department['very_low'], classification['very_low']),
        ctrl.Rule(asset_value['very_low'] & owner_department['low'], classification['very_low']),
        ctrl.Rule(asset_value['very_low'] & owner_department['medium'], classification['low']),
        ctrl.Rule(asset_value['very_low'] & owner_department['high'], classification['low']),
        ctrl.Rule(asset_value['very_low'] & owner_department['very_high'], classification['medium']),

        ctrl.Rule(asset_value['low'] & owner_department['very_low'], classification['very_low']),
        ctrl.Rule(asset_value['low'] & owner_department['low'], classification['low']),
        ctrl.Rule(asset_value['low'] & owner_department['medium'], classification['low']),
        ctrl.Rule(asset_value['low'] & owner_department['high'], classification['medium']),
        ctrl.Rule(asset_value['low'] & owner_department['very_high'], classification['medium']),

        ctrl.Rule(asset_value['medium'] & owner_department['very_low'], classification['low']),
        ctrl.Rule(asset_value['medium'] & owner_department['low'], classification['medium']),
        ctrl.Rule(asset_value['medium'] & owner_department['medium'], classification['medium']),
        ctrl.Rule(asset_value['medium'] & owner_department['high'], classification['high']),
        ctrl.Rule(asset_value['medium'] & owner_department['very_high'], classification['high']),

        ctrl.Rule(asset_value['high'] & owner_department['very_low'], classification['medium']),
        ctrl.Rule(asset_value['high'] & owner_department['low'], classification['medium']),
        ctrl.Rule(asset_value['high'] & owner_department['medium'], classification['high']),
        ctrl.Rule(asset_value['high'] & owner_department['high'], classification['high']),
        ctrl.Rule(asset_value['high'] & owner_department['very_high'], classification['very_high']),

        ctrl.Rule(asset_value['very_high'] & owner_department['very_low'], classification['medium']),
        ctrl.Rule(asset_value['very_high'] & owner_department['low'], classification['high']),
        ctrl.Rule(asset_value['very_high'] & owner_department['medium'], classification['high']),
        ctrl.Rule(asset_value['very_high'] & owner_department['high'], classification['very_high']),
        ctrl.Rule(asset_value['very_high'] & owner_department['very_high'], classification['very_high']),
        
        # Additional rules to cover more combinations
        ctrl.Rule(asset_value['low'] & owner_department['low'], classification['low']),
        ctrl.Rule(asset_value['low'] & owner_department['medium'], classification['medium']),
        ctrl.Rule(asset_value['medium'] & owner_department['low'], classification['medium']),
        ctrl.Rule(asset_value['medium'] & owner_department['high'], classification['high']),
        ctrl.Rule(asset_value['high'] & owner_department['medium'], classification['high']),
        ctrl.Rule(asset_value['very_high'] & owner_department['very_high'], classification['very_high']),
    ]

    # Create the control system and simulation
    classification_ctrl = ctrl.ControlSystem(rules)
    classification_system = ctrl.ControlSystemSimulation(classification_ctrl)

    # Pass inputs to the system
    classification_system.input['asset_value'] = asset_value_input
    classification_system.input['owner_department'] = department_impact_input

    # Perform the computation
    classification_system.compute()

    # Get the output (using Centre of Gravity - CoG)
    classification_output = classification_system.output['classification']

    return round(classification_output, 2)
