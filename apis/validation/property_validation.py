from flask import abort
from ..utils.types import valid_unit_types, valid_features

def validate_property(property):
    validate_unit_type(property["unit_type"])
    validate_features(property["features"])
    validate_non_negative(property["number_of_floors"])

# Validation for unit_type
def validate_unit_type(unit_type):
    unit_type = unit_type.lower()
    if unit_type not in valid_unit_types:
        abort(400, f"Invalid unit_type. Allowed values: {', '.join(valid_unit_types)}")

# Validation for unit_type
def validate_features(features):
    for feature in features:
        feature = feature.lower()
        if feature not in valid_features:
            abort(400, f"Invalid feature: {feature}. Allowed features: {', '.join(valid_features)}")

def validate_non_negative(number_of_floors):
    if number_of_floors < 0:
        abort(400, "Number of floors must be 0 or above.")
    