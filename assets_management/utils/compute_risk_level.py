import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def compute_risk_level(confidentiality: float, integrity: float, availability: float, classification_value: float) -> float:
    """
    Computes the risk level based on Confidentiality, Integrity, Availability, and Classification Value
    using fuzzy logic.

    Parameters:
    confidentiality (float): The confidentiality level of the asset (0 to 1).
    integrity (float): The integrity level of the asset (0 to 1).
    availability (float): The availability level of the asset (0 to 1).
    classification_value (float): The classification value of the asset (0 to 1).

    Returns:
    float: The computed risk level.
    """

    # Define fuzzy variables
    conf = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'confidentiality')
    integ = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'integrity')
    avail = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'availability')
    classification = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'classification')
    risk_level = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'risk_level')

    # Define membership functions
    conf['very_low'] = fuzz.trimf(conf.universe, [0, 0, 0.2])
    conf['low'] = fuzz.trimf(conf.universe, [0, 0.2, 0.4])
    conf['medium'] = fuzz.trimf(conf.universe, [0.2, 0.5, 0.8])
    conf['high'] = fuzz.trimf(conf.universe, [0.4, 0.7, 1])
    conf['very_high'] = fuzz.trimf(conf.universe, [0.8, 1, 1])

    integ['very_low'] = fuzz.trimf(integ.universe, [0, 0, 0.2])
    integ['low'] = fuzz.trimf(integ.universe, [0, 0.2, 0.4])
    integ['medium'] = fuzz.trimf(integ.universe, [0.2, 0.5, 0.8])
    integ['high'] = fuzz.trimf(integ.universe, [0.4, 0.7, 1])
    integ['very_high'] = fuzz.trimf(integ.universe, [0.8, 1, 1])

    avail['very_low'] = fuzz.trimf(avail.universe, [0, 0, 0.2])
    avail['low'] = fuzz.trimf(avail.universe, [0, 0.2, 0.4])
    avail['medium'] = fuzz.trimf(avail.universe, [0.2, 0.5, 0.8])
    avail['high'] = fuzz.trimf(avail.universe, [0.4, 0.7, 1])
    avail['very_high'] = fuzz.trimf(avail.universe, [0.8, 1, 1])

    classification['very_low'] = fuzz.trimf(classification.universe, [0, 0, 0.2])
    classification['low'] = fuzz.trimf(classification.universe, [0, 0.2, 0.4])
    classification['medium'] = fuzz.trimf(classification.universe, [0.2, 0.5, 0.8])
    classification['high'] = fuzz.trimf(classification.universe, [0.4, 0.7, 1])
    classification['very_high'] = fuzz.trimf(classification.universe, [0.8, 1, 1])

    risk_level['very_low'] = fuzz.trimf(risk_level.universe, [0, 0, 0.2])
    risk_level['low'] = fuzz.trimf(risk_level.universe, [0, 0.2, 0.4])
    risk_level['medium'] = fuzz.trimf(risk_level.universe, [0.2, 0.5, 0.8])
    risk_level['high'] = fuzz.trimf(risk_level.universe, [0.4, 0.7, 1])
    risk_level['very_high'] = fuzz.trimf(risk_level.universe, [0.8, 1, 1])

    # Define fuzzy rules
    rules = [
        # Rules for very_low risk level
        ctrl.Rule(conf['very_low'] & integ['very_low'] & avail['very_low'] & classification['very_low'], risk_level['very_low']),
        ctrl.Rule(conf['very_low'] & integ['very_low'] & avail['very_low'] & classification['low'], risk_level['very_low']),
        ctrl.Rule(conf['very_low'] & integ['very_low'] & avail['very_low'] & classification['medium'], risk_level['low']),
        ctrl.Rule(conf['very_low'] & integ['very_low'] & avail['very_low'] & classification['high'], risk_level['low']),
        ctrl.Rule(conf['very_low'] & integ['very_low'] & avail['very_low'] & classification['very_high'], risk_level['medium']),
        
        # Rules for low risk level
        ctrl.Rule(conf['very_low'] & integ['very_low'] & avail['low'] & classification['very_low'], risk_level['very_low']),
        ctrl.Rule(conf['very_low'] & integ['very_low'] & avail['low'] & classification['low'], risk_level['low']),
        ctrl.Rule(conf['very_low'] & integ['very_low'] & avail['low'] & classification['medium'], risk_level['low']),
        ctrl.Rule(conf['very_low'] & integ['very_low'] & avail['low'] & classification['high'], risk_level['medium']),
        ctrl.Rule(conf['very_low'] & integ['low'] & avail['low'] & classification['very_low'], risk_level['low']),
        ctrl.Rule(conf['very_low'] & integ['low'] & avail['low'] & classification['medium'], risk_level['medium']),
        
        # Rules for medium risk level
        ctrl.Rule(conf['medium'] & integ['medium'] & avail['medium'] & classification['medium'], risk_level['medium']),
        ctrl.Rule(conf['medium'] & integ['medium'] & avail['medium'] & classification['high'], risk_level['high']),
        ctrl.Rule(conf['medium'] & integ['medium'] & avail['medium'] & classification['very_high'], risk_level['high']),
        ctrl.Rule(conf['medium'] & integ['medium'] & avail['high'] & classification['medium'], risk_level['medium']),
        ctrl.Rule(conf['medium'] & integ['high'] & avail['medium'] & classification['medium'], risk_level['medium']),
        ctrl.Rule(conf['medium'] & integ['high'] & avail['high'] & classification['medium'], risk_level['high']),
        
        # Rules for high risk level
        ctrl.Rule(conf['high'] & integ['high'] & avail['high'] & classification['medium'], risk_level['high']),
        ctrl.Rule(conf['high'] & integ['high'] & avail['high'] & classification['high'], risk_level['very_high']),
        ctrl.Rule(conf['high'] & integ['high'] & avail['very_high'] & classification['high'], risk_level['very_high']),
        ctrl.Rule(conf['very_high'] & integ['high'] & avail['very_high'] & classification['medium'], risk_level['very_high']),
        ctrl.Rule(conf['very_high'] & integ['high'] & avail['very_high'] & classification['high'], risk_level['very_high']),
        
        # Additional rules to cover more combinations
        ctrl.Rule(conf['low'] & integ['low'] & avail['low'] & classification['low'], risk_level['low']),
        ctrl.Rule(conf['low'] & integ['low'] & avail['low'] & classification['medium'], risk_level['medium']),
        ctrl.Rule(conf['low'] & integ['low'] & avail['medium'] & classification['medium'], risk_level['medium']),
        ctrl.Rule(conf['low'] & integ['medium'] & avail['medium'] & classification['medium'], risk_level['medium']),
        ctrl.Rule(conf['medium'] & integ['medium'] & avail['medium'] & classification['low'], risk_level['medium']),
        ctrl.Rule(conf['medium'] & integ['medium'] & avail['low'] & classification['low'], risk_level['medium']),
        ctrl.Rule(conf['high'] & integ['medium'] & avail['medium'] & classification['medium'], risk_level['high']),
        ctrl.Rule(conf['high'] & integ['high'] & avail['medium'] & classification['medium'], risk_level['high']),
        ctrl.Rule(conf['very_high'] & integ['very_high'] & avail['very_high'] & classification['very_high'], risk_level['very_high']),
    ]

    # Create the control system and simulation
    risk_ctrl = ctrl.ControlSystem(rules)
    risk_system = ctrl.ControlSystemSimulation(risk_ctrl)

    # Pass inputs to the system
    risk_system.input['confidentiality'] = confidentiality
    risk_system.input['integrity'] = integrity
    risk_system.input['availability'] = availability
    risk_system.input['classification'] = classification_value

    # Perform the computation
    risk_system.compute()

    # Get the output (using Centre of Gravity - CoG)
    risk_level_output = risk_system.output['risk_level']

    return round(risk_level_output, 2)
