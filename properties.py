def get_property(data, temperature, glycol_percentage):
    """Function pulls fluid data from the properties tables. Need to specify which table (density_data or viscosity_data)
     in the data argument for this function."""
    # Convert glycol_percentage to the correct key format (e.g., "40%")
    glycol_key = f"{glycol_percentage}%"
    # Search for the entry with the matching temperature
    for entry in data:
        if entry["temperature"] == temperature:
            # Return the viscosity value for the specified glycol percentage
            return entry.get(glycol_key)
    # If no matching entry is found, return None or an error message
    return "No data available for this temperature and glycol percentage."


""" Density of Aqueous Solutions of Inhibited Propylene Glycol
Temperature: °F
Density: lb/ft^3
List of dictionaries at different temps and prop glycol percentages of 0, 30, 40, 50%
Source: Engineering Toolbox and PE Handbook (references the 2013 ASHRAE Fundamentals)"""

density_data = [
    {"temperature": -20, "0%": None, "30%": None, "40%": None, "50%": 66.46},
    {"temperature": -10, "0%": None, "30%": None, "40%": None, "50%": 66.35},
    {"temperature": 0, "0%": None, "30%": None, "40%": 65.71, "50%": 66.23},
    {"temperature": 10, "0%": None, "30%": 65.00, "40%": 65.60, "50%": 66.11},
    {"temperature": 20, "0%": None, "30%": 64.90, "40%": 65.48, "50%": 65.97},
    {"temperature": 30, "0%": None, "30%": 64.79, "40%": 65.35, "50%": 65.82},
    {"temperature": 40, "0%": 62.42, "30%": 64.67, "40%": 65.21, "50%": 65.67},
    {"temperature": 50, "0%": 62.41, "30%": 64.53, "40%": 65.06, "50%": 65.50},
    {"temperature": 60, "0%": 62.36, "30%": 64.39, "40%": 64.90, "50%": 65.33},
    {"temperature": 70, "0%": 62.30, "30%": 64.24, "40%": 64.73, "50%": 65.14},
    {"temperature": 80, "0%": 62.22, "30%": 64.08, "40%": 64.55, "50%": 64.95},
    {"temperature": 90, "0%": 62.11, "30%": 63.91, "40%": 64.36, "50%": 64.74},
    {"temperature": 100, "0%": 62.00, "30%": 63.73, "40%": 64.16, "50%": 64.53},
    {"temperature": 110, "0%": 61.86, "30%": 63.54, "40%": 63.95, "50%": 64.30},
    {"temperature": 120, "0%": 61.71, "30%": 63.33, "40%": 63.74, "50%": 64.06},
    {"temperature": 130, "0%": 61.55, "30%": 63.12, "40%": 63.51, "50%": 63.82},
    {"temperature": 140, "0%": 61.38, "30%": 62.90, "40%": 63.27, "50%": 63.57},
    {"temperature": 150, "0%": 61.16, "30%": 62.67, "40%": 63.02, "50%": 63.30},
    {"temperature": 160, "0%": 61.00, "30%": 62.43, "40%": 62.76, "50%": 63.03},
    {"temperature": 170, "0%": 60.79, "30%": 62.18, "40%": 62.49, "50%": 62.74},
    {"temperature": 180, "0%": 60.58, "30%": 61.92, "40%": 62.22, "50%": 62.45},
    {"temperature": 190, "0%": 60.35, "30%": 61.65, "40%": 61.93, "50%": 62.14},
    {"temperature": 200, "0%": 60.12, "30%": 61.37, "40%": 61.63, "50%": 61.83},
]

""" Viscosity of Aqueous Solutions of Propylene Glycol
Temperature: °F
Viscosity: centipoise
List of dictionaries at different temps and prop glycol percentages of 0, 30, 40, 50%
Source: Engineering Toolbox and PE Handbook (references the 2013 ASHRAE Fundamentals)"""

viscosity_data = [
    {"temperature": -20, "0%": None, "30%": None, "40%": None, "50%": 156.08},
    {"temperature": -10, "0%": None, "30%": None, "40%": None, "50%": 95.97},
    {"temperature": 0, "0%": None, "30%": None, "40%": 40.99, "50%": 61.32},
    {"temperature": 10, "0%": None, "30%": 13.44, "40%": 27.17, "50%": 40.62},
    {"temperature": 20, "0%": None, "30%": 9.91, "40%": 18.64, "50%": 27.83},
    {"temperature": 30, "0%": None, "30%": 7.47, "40%": 13.20, "50%": 19.66},
    {"temperature": 40, "0%": 1.55, "30%": 5.75, "40%": 9.63, "50%": 14.28},
    {"temperature": 50, "0%": 1.31, "30%": 4.52, "40%": 7.22, "50%": 10.65},
    {"temperature": 60, "0%": 1.12, "30%": 3.61, "40%": 5.55, "50%": 8.13},
    {"temperature": 70, "0%": 0.98, "30%": 2.94, "40%": 4.36, "50%": 6.34},
    {"temperature": 80, "0%": 0.86, "30%": 2.43, "40%": 3.50, "50%": 5.04},
    {"temperature": 90, "0%": 0.76, "30%": 2.04, "40%": 2.86, "50%": 4.08},
    {"temperature": 100, "0%": 0.68, "30%": 1.73, "40%": 2.37, "50%": 3.35},
    {"temperature": 110, "0%": 0.62, "30%": 1.49, "40%": 2.00, "50%": 2.79},
    {"temperature": 120, "0%": 0.56, "30%": 1.30, "40%": 1.71, "50%": 2.36},
    {"temperature": 130, "0%": 0.51, "30%": 1.14, "40%": 1.49, "50%": 2.02},
    {"temperature": 140, "0%": 0.47, "30%": 1.01, "40%": 1.30, "50%": 1.75},
    {"temperature": 150, "0%": 0.43, "30%": 0.90, "40%": 1.16, "50%": 1.53},
    {"temperature": 160, "0%": 0.40, "30%": 0.82, "40%": 1.03, "50%": 1.35},
    {"temperature": 170, "0%": 0.37, "30%": 0.74, "40%": 0.93, "50%": 1.20},
    {"temperature": 180, "0%": 0.35, "30%": 0.68, "40%": 0.85, "50%": 1.08},
    {"temperature": 190, "0%": 0.33, "30%": 0.62, "40%": 0.78, "50%": 0.97},
    {"temperature": 200, "0%": 0.31, "30%": 0.58, "40%": 0.72, "50%": 0.88},
]

