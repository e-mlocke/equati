# Acceleration Base: m/s^2
acceleration_dimcon = {'m/s^2': 1, 'in/s^2': 0.0254,
 'ft/s^2': 0.3048, 'km/s^2': 1000, 'mm/s^2': 0.001}

# Angle Base: radians
angle_dimcon = {'radians': 1, 'degrees': 0.017453292519943}

# Area Base: m^2
area_dimcon = {'m^2': 1, 'mile^2': 2589975.2356, 'yard^2': 0.836127,
 'ft^2': 0.092903, 'in^2': 0.000645, 'Mm^2': 10**12,
 'km^2': 10**6, 'cm^2': 10**-4, 'mm^2': 10**-6,
 'um^2': 10**-12, 'nm^2': 10**-18, 'pm^2': 10**-24}

# Density Base: kg/m^3
density_dimcon = {'kg/m^3': 1, 'g/m^3': 1000}

# Energy Base: J
energy_dimcon = {'J': 1, 'N-m': 1, 'Btu': 1055.05585, 'cal': 4.18400,
 'kWh': 3600000, 'eV': 1.60217657*10**-19,
 'ft-lbf': 1.35581795, 'in-lbf': 0.11298483,
 'GJ': 10**9, 'MJ': 10**6, 'kJ': 1000,
 'mJ': 0.001, 'uJ': 10**-6, 'nJ': 10**-9}

# Force Base: N
force_dimcon = {'N': 1, 'klbf': 4448.22162, 'lbf': 4.44822162,
 'MN': 10**6, 'kN': 1000, 'mN': 0.001, 'uN': 10**-6}

# Length Base: m
length_dimcon = {'m':1 , 'mile': 1609.344, 'yard': 0.9144,
 'ft': 0.3048, 'in': 0.0254, 'Mm': 10**6, 'km': 10**3,
 'cm': 0.01, 'mm': 10**-3, 'um': 10**-6, 'nm': 10**-9,
 'pm': 10**-12}

# Mass Base: kg
mass_dimcon = {'kg': 1, 'klbm': 453.592, 'lbm': 0.453592,
 'slugs': 14.5939029, 'Mg': 1000, 'g': 10**-3,
 'mg': 10**-6, 'ug': 10**-9}

# Pressure Base: N/m^2
pressure_dimcon = {'N/m^2': 1, 'TN/m^2': 10**12, 'GN/m^2': 10**9,
 'MN/m^2': 10**6, 'kN/m^2': 10**3, 'mN/m^2': 10**-3,
 'uN/m^2': 10**-6, 'nN/m^2': 10**-9, 'torr': 133.322368,
 'mmHg': 133.322368, 'inWC': 249.088875, 'ftWC': 2989.0665,
 'lbf/in^2': 6894.75729, 'lbf/ft^2': 47.880259,
 'bar': 10**5, 'atm': 101325}

# Temperature Base: K
# temp is tough. the algorithm multiples. these need addition
# The following would work if using symbolic algebra where T = the value to be converted
#temperature = {'K': 1, 'C': 1+273.15/T, 'F': 1+5/9*459.67/T,
# 'R': 5/9}

# Time Base: s
time_dimcon = {'s': 1, 'year': 31556900, 'month': 2629740,
 'week': 604800, 'day': 86400, 'hr': 3600, 'min': 60,
 'ms': 10**-3, 'us': 10**-6, 'ns': 10**-9}

# Velocity Base: m/s
velocity_dimcon = {'m/s': 1, 'mile/hr': 0.44704, 'ft/s': 0.3048,
 'in/s': 0.0254, 'yard/s': 0.9144, 'km/hr': 0.277778,
 'Mm/s': 10**6, 'km/s': 10**3, 'cm/s': 10**-2,
 'mm/s': 10**-3, 'um/s': 10**-6, 'nm/s': 10**-9}

# Volume Base: m^3
volume_dimcon = {'m^3': 1, 'Mm^3': 10**18, 'km^3': 10**9,
 'cm^3': 10**-6, 'mm^3': 10**-9, 'um^3': 10**-18,
 'nm^3': 10**-27, 'ML': 10**3, 'kL': 1, 'L': 10**-3,
 'mL': 10**-6, 'uL': 10**-9, 'nL': 10**-12,
 'mile^3': 4.16818183*10**9, 'yard^3': 0.7645536,
 'ft^3': 0.0283168, 'in^3': 0.0000163871,
 'gal_us': 0.00378541, 'gal_imp': 0.00454609,
 'quart': 0.000946353, 'cup': 0.000236588,
 'oz': 0.0000295735}
