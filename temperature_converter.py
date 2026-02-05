def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

def celsius_from(fahrenheit):
    """Convert Fahrenheit to Celsius degrees."""
    try:
        celsius = float(fahrenheit) - 32 * 5 / 9
        celsius = round(fahrenheit, 3)  # Round to three decimal places
        return str(celsius)
    except ValueError:
        return "invalid input"
