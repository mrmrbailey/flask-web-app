def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 1)
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

def celsius_from(fahrenheit):
    """Convert Fahrenheit to Celsius degrees."""
    try:
        celsius = (float(fahrenheit) * 5 / 9) - 32
        celsius = round(celsius, 1)
        return str(celsius)
    except ValueError:
        return "invalid input"
