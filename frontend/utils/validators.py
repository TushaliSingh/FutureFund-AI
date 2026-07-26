def validate_positive_number(value, field_name):
    """
    Validate that a numeric value is greater than zero.
    """

    if value is None:
        raise ValueError(f"{field_name} is required.")

    if value <= 0:
        raise ValueError(f"{field_name} must be greater than zero.")


def validate_percentage(value, field_name):
    """
    Validate percentage values.
    """

    if value < 0 or value > 100:
        raise ValueError(f"{field_name} must be between 0 and 100.")


def validate_years(years):
    """
    Validate investment duration.
    """

    if years <= 0:
        raise ValueError("Years must be greater than zero.")