def calculate_risk(temp, humidity, wind):
    return round((0.4 * temp) + (0.3 * (100 - humidity)) + (0.3 * wind), 2)
