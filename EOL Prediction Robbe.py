##### End-of-Life Prediction #####
# Load standard modules
import numpy as np

import matplotlib
from matplotlib import pyplot as plt

# Load tudatpy modules
from tudatpy.kernel.interface import spice
from tudatpy.kernel import numerical_simulation
from tudatpy.kernel.numerical_simulation import environment_setup, propagation_setup, environment
from tudatpy.kernel.astro import element_conversion
from tudatpy.kernel import constants
from tudatpy.util import result2array

def get_tle_data(norad_cat_id, dates):
    # Function to implement with eol prediction
    # INPUTS: norad_cat_id = int, date = str
    # OUTPUTS: semi major axis[km], eccentricity[/], inclination[deg], argument of periapsis[deg], 
    #          right ascension of the ascending node[deg], true anomaly[deg]
    # EXAMPLE: get_tle_data(51074, "2022-09-06--2022-09-07")
    import requests
    import re
    import math

    # Define the login data
    login_data = {
        'identity': 'wschaerlaecken@gmail.com',
        'password': 'groupd03123456789'}

    NORAD_CAT_ID = norad_cat_id
    DATE = dates
    # Create a session
    with requests.Session() as session:
        # Post the login data
        post_response = session.post('https://www.space-track.org/ajaxauth/login', data=login_data)

        # Check if login was successful
        if post_response.status_code == 200:
            # If login is successful, make the GET request
            url = f"https://www.space-track.org/basicspacedata/query/class/gp_history/NORAD_CAT_ID/{NORAD_CAT_ID}/orderby/TLE_LINE1%20ASC/EPOCH/{DATE}/format/tle"
            print(url)
            get_response = session.get(url)

            if get_response.status_code == 200:
                data = get_response.text
                print(data)
            else:
                print("Failed to retrieve data. Status code:", get_response.status_code)
                print("Response text:", get_response.text)
        else:
            print("Failed to log in. Status code:", post_response.status_code)
            print("Response text:", post_response.text)

            # Split the data into individual lines
        lines = data.split('\n')

            # Iterate over each line and assign the values to variables
    for line in lines:
        if line.startswith('1 '):
            line1 = line.split(' ')
        elif line.startswith('2 '):
            line2 = line.split(' ')

    for line in lines:
        if line.startswith('1 '):
            line1 = re.findall(r'\d+\.\d+|\d+', line)  # Find all numeric characters and decimal points
        elif line.startswith('2 '):
            line2 = re.findall(r'\d+\.\d+|\d+', line)  # Find all numeric characters and decimal points

    Sat_num = line1[1]
    Int_Des_Year=line1[2][:2]
    Int_Des = line1[2][2:]
    Epoch_Year = line1[3][:2]
    Epoch_Day = line1[3][2:]
    B = int(line1[4])*10**(-8)
    Second_Der_Mean_Motion = (float(line1[5])/100000) * 10**(-int(line1[6]))
    BSTAR = int(line1[7])*10**(-5) * 10**(-int(line1[8]))
    Ephemeris = line1[9]
    Element_Number = line1[10][:3]
    Check_Sum_1 = line1[10][3]

    Inclination = line2[2]
    RAAN = line2[3]
    Eccentricity = int(line2[4])*10**(-7)
    Arg_Perigee = line2[5]
    Mean_Anomaly = line2[6]
    Mean_Motion = line2[7][:11]
    Rev_Num = line2[7][11:16]
    Check_Sum_2 = line2[7][16:]


    # Calculate the period and semi-major axis
    Period = (1*24*3600)/(float(Mean_Motion))
    semi_major_axis = (Period**2 * 3.9860044188*10**14/((2*math.pi)**2))**(1/3)
    rp = semi_major_axis*(1-Eccentricity)
    ra = semi_major_axis*(1+Eccentricity)

    # Calculate eccentric anomaly
    mean_anomaly_rad = float(Mean_Anomaly) * math.pi / 180
    Eccentricity_rad = float(Eccentricity) * math.pi / 180
    converged = False
    E_old = mean_anomaly_rad
    while converged == False:
        E_new = mean_anomaly_rad + Eccentricity * math.sin(E_old)
        if math.abs((E_new - E_old)/E_new) < 0.01:
            converged = True
        E_old = E_new
    eccentric_anomaly = E_old
    true_anomaly_rad = math.acos((math.cos(eccentric_anomaly)-Eccentricity_rad) / (1 - Eccentricity_rad * math.cos(eccentric_anomaly)))
    true_anomaly = true_anomaly_rad * 180 / math.pi

    return semi_major_axis, Eccentricity, Inclination, Arg_Perigee, RAAN, true_anomaly

"""
semi_major_axis=7500.0e3,
eccentricity=0.1,
inclination=np.deg2rad(85.3),
argument_of_periapsis=np.deg2rad(235.7),
longitude_of_ascending_node=np.deg2rad(23.4),
true_anomaly=np.deg2rad(139.87)
"""

# Load spice kernels
spice.load_standard_kernels()

# Set simulation start and end epochs
simulation_start_epoch = 0.0
simulation_end_epoch = constants.JULIAN_DAY

# Define string names for bodies to be created from default.
bodies_to_create = ["Sun", "Earth", "Moon", "Mars", "Venus"]

# Use "Earth"/"J2000" as global frame origin and orientation.
global_frame_origin = "Earth"
global_frame_orientation = "J2000"

# Create default body settings, usually from `spice`.
body_settings = environment_setup.get_default_body_settings(
    bodies_to_create,
    global_frame_origin,
    global_frame_orientation)

# Create system of selected celestial bodies
bodies = environment_setup.create_system_of_bodies(body_settings)

# Create vehicle objects.
satellite = "Delfi-C3"
satellite_norad_cat_id = 32789
satellite_dates = "2008-04-27--2008-04-29"

bodies.create_empty_body(satellite)

bodies.get(satellite).mass = 1.2

# Create aerodynamic coefficient interface settings, and add to vehicle
reference_area = 4.0
drag_coefficient = 1.2
aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
    reference_area, [drag_coefficient, 0, 0]
)
environment_setup.add_aerodynamic_coefficient_interface(
    bodies, satellite, aero_coefficient_settings)

# Create radiation pressure settings, and add to vehicle
reference_area_radiation = 4.0
radiation_pressure_coefficient = 1.2
occulting_bodies = ["Earth"]
radiation_pressure_settings = environment_setup.radiation_pressure.cannonball(
    "Sun", reference_area_radiation, radiation_pressure_coefficient, occulting_bodies
)
environment_setup.add_radiation_pressure_interface(
    bodies, satellite, radiation_pressure_settings)

# Define bodies that are propagated
bodies_to_propagate = [satellite]

# Define central bodies of propagation
central_bodies = ["Earth"]

# Define accelerations acting on satellite by Sun and Earth.
accelerations_settings_satellite = dict(
    Sun=[
        propagation_setup.acceleration.cannonball_radiation_pressure(),
        propagation_setup.acceleration.point_mass_gravity()
    ],
    Earth=[
        propagation_setup.acceleration.spherical_harmonic_gravity(5, 5),
        propagation_setup.acceleration.aerodynamic()
    ],
    Moon=[
        propagation_setup.acceleration.point_mass_gravity()
    ],
    Mars=[
        propagation_setup.acceleration.point_mass_gravity()
    ],
    Venus=[
        propagation_setup.acceleration.point_mass_gravity()
    ]
)

# Create global accelerations settings dictionary.
acceleration_settings = {satellite: accelerations_settings_satellite}

# Create acceleration models.
acceleration_models = propagation_setup.create_acceleration_models(
    bodies,
    acceleration_settings,
    bodies_to_propagate,
    central_bodies)

# Set initial conditions for the satellite that will be
# propagated in this simulation. The initial conditions are given in
# Keplerian elements and later on converted to Cartesian elements
Semi_major_axis, Eccentricity, Inclination, Argument_of_periapsis, RAAN, True_anomaly = get_tle_data(satellite_norad_cat_id, satellite_dates)

earth_gravitational_parameter = bodies.get("Earth").gravitational_parameter
initial_state = element_conversion.keplerian_to_cartesian_elementwise(
    gravitational_parameter=earth_gravitational_parameter,
    semi_major_axis=Semi_major_axis,
    eccentricity=Eccentricity,
    inclination=np.deg2rad(Inclination),
    argument_of_periapsis=np.deg2rad(Argument_of_periapsis),
    longitude_of_ascending_node=np.deg2rad(RAAN),
    true_anomaly=np.deg2rad(True_anomaly),
)

# Define list of dependent variables to save
dependent_variables_to_save = [
    propagation_setup.dependent_variable.altitude(satellite, "Earth"),
]

# Create termination settings
termination_condition = propagation_setup.propagator.time_termination(simulation_end_epoch)

# Create numerical integrator settings
fixed_step_size = 10.0
integrator_settings = propagation_setup.integrator.runge_kutta_4(fixed_step_size)

# Create propagation settings
propagator_settings = propagation_setup.propagator.translational(
    central_bodies,
    acceleration_models,
    bodies_to_propagate,
    initial_state,
    simulation_start_epoch,
    integrator_settings,
    termination_condition,
    output_variables=dependent_variables_to_save
)

# Create simulation object and propagate the dynamics
dynamics_simulator = numerical_simulation.create_dynamics_simulator(
    bodies, propagator_settings
)

# Extract the resulting state and depedent variable history and convert it to an ndarray
states = dynamics_simulator.state_history
states_array = result2array(states)
dep_vars = dynamics_simulator.dependent_variable_history
dep_vars_array = result2array(dep_vars)

# Plot total acceleration as function of time
time_hours = dep_vars_array[:,0]/3600
altitude = dep_vars_array[:,1] / 1000
plt.figure(figsize=(9, 5))
plt.title(f"Total altitude of {satellite} over the course of propagation.")
plt.plot(time_hours, altitude)
plt.xlabel('Time [hr]')
plt.ylabel('Alttitude [km]')
plt.xlim([min(time_hours), max(time_hours)])
plt.grid()
plt.tight_layout()
plt.savefig("Plots/AltGraph")