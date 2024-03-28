# Load basic modules
import numpy as np
import datetime
import pandas as pd
import re
from datetime import datetime, timedelta
import math
import matplotlib
from matplotlib import pyplot as plt

# Load tudatpy modules
from tudatpy.interface import spice
from tudatpy import numerical_simulation
from tudatpy.numerical_simulation import environment
from tudatpy.numerical_simulation import environment_setup, propagation_setup
from tudatpy.astro import element_conversion, time_conversion
from tudatpy import constants
from tudatpy.util import result2array
from tudatpy.astro.time_conversion import DateTime
import sys
from dateutil.relativedelta import relativedelta

"""-------------------------------"""
"""Inputs"""
TLE1_number = 8300
TLE2_number = 8782

Mass = 2.2

reference_area = 0.08  # Average projection area of a 3U CubeSat
drag_coefficient_lower = 1.4
drag_coefficient_upper = 2.0


itterations = 14

radiation_pressure_coefficient = 1.2

fixed_step_size = 50

"""Change to a lower step size when the code works"""

"""-------------------------------"""


step_size  = (drag_coefficient_upper - drag_coefficient_lower)/itterations


# Open the file
with open('TLE-Data_C3.txt', 'r') as file:
    # Read lines two at a time
    lines = file.readlines()
    TLE_sets = [(lines[i].strip(), lines[i + 1].strip()) for i in range(0, len(lines), 2)]


initTLE = []
# Now you can use the TLE_sets in your code like this:
for TLE_set in TLE_sets:
    initTLE.append(environment.Tle(TLE_set[0], TLE_set[1]))


def convert_epoch_day_to_date(epoch_year, epoch_day):
    # Create a datetime object for the start of the epoch year
    start_of_year = datetime(int(epoch_year), 1, 1)

    # Add the epoch day to the start of the year, subtracting one because
    # datetime's day count starts at 1, not 0
    epoch_date = start_of_year + timedelta(days=float(epoch_day) - 1)

    # Extract the month, day, and hour
    month = epoch_date.month
    day = epoch_date.day
    hour = epoch_date.hour

    return month, day, hour
# Open the file
with open('TLE-Data_C3.txt', 'r') as file:
    # Read lines two at a time
    lines = file.readlines()
    TLE_sets = [(lines[i], lines[i + 1]) for i in range(0, len(lines), 2)]



# Create lists to store the split lines
split_TLE_sets = []

# Loop over each TLE set
for TLE_set in TLE_sets:
    # Split each line and extract the numeric values
    line1 = re.findall(r'\d+\.\d+|\d+', TLE_set[0])  # Find all numeric characters and decimal points
    line2 = re.findall(r'\d+\.\d+|\d+', TLE_set[1])  # Find all numeric characters and decimal points

    # Add the split lines to the list
    split_TLE_sets.append((line1, line2))


# Now split_TLE_sets is a list of tuples, where each tuple is a pair of split lines (a TLE set)
# You can access the first split TLE set like this:
TLE_1 = split_TLE_sets[TLE1_number]
TLE_2 = split_TLE_sets[TLE2_number]



def parse_TLE(TLE):
    TLE_line1 = TLE[0]
    TLE_line2 = TLE[1]

    Int_Des_Year = TLE_line1[2][:2]
    Int_Des = TLE_line1[2][2:]
    Epoch_Year = TLE_line1[3][:2]
    Epoch_Day = TLE_line1[3][2:]
    Inclination = TLE_line2[2]
    RAAN = TLE_line2[3]
    Eccentricity = int(TLE_line2[4])*10**(-7)
    Arg_Perigee = TLE_line2[5]
    Mean_Anomaly = TLE_line2[6]
    Mean_Motion = TLE_line2[7][:11]
    Rev_Num = TLE_line2[7][11:16]

    # Calculate the launch year
    if int(Int_Des_Year) < 57:
        launch_year = int(Int_Des_Year)+2000
    else:
        launch_year = int(Int_Des_Year)+1900

    # Calculate the period and semi-major axis
    Period = (1*24*3600)/(float(Mean_Motion))
    semi_major_axis = (Period**2 * 3.9860044188*10**14/((2*math.pi)**2))**(1/3)
    rp = semi_major_axis*(1-Eccentricity)
    ra = semi_major_axis*(1+Eccentricity)

    Height_apo = ra/1000 - 6371
    Height_peri = rp/1000 - 6371

    # Calculating the velocity
    Vp = math.sqrt((3.9860044188*10**14*2*ra)/(rp*(ra+rp)))
    Va = math.sqrt((3.9860044188*10**14*2*rp)/(ra*(ra+rp)))

    # Convert the epoch year and day to an actual date and time
    if int(Epoch_Year) < 30:
        epoch_year = int(Epoch_Year) + 2000  # Add 2000 to get the full year
    else:
        epoch_year = int(Epoch_Year) + 1900  
    start_of_year = datetime(epoch_year, 1, 1)  # January 1 of the epoch year
    epoch_day = float(Epoch_Day)  # Convert to float to handle fractional days

    epoch_date = start_of_year + timedelta(days=epoch_day)

    month, day, hour = convert_epoch_day_to_date(epoch_year, epoch_day)
    if epoch_year % 4 == 0 and month > 2:
        day = day - 1

    parsed_values = {
        'Int_Des_Year': Int_Des_Year,
        'Int_Des': Int_Des,
        'Epoch_Year': Epoch_Year,
        'Epoch_Day': Epoch_Day,
        'Inclination': Inclination,
        'RAAN': RAAN,
        'Eccentricity': Eccentricity,
        'Arg_Perigee': Arg_Perigee,
        'Mean_Anomaly': Mean_Anomaly,
        'Mean_Motion': Mean_Motion,
        'Rev_Num': Rev_Num,
        'Launch_Year': launch_year,
        'Period': Period,
        'Semi_Major_Axis': semi_major_axis,
        'Height_Apo': Height_apo,
        'Height_Peri': Height_peri,
        'Vp': Vp,
        'Va': Va,
        'Year_Actual': epoch_year,
        'Start_of_Year': start_of_year,
        'Day_Float': epoch_day,
        'Date': epoch_date,
        'Month': month,
        'Day': day,
        'Hour': hour
    }

    return parsed_values

# Now you can parse each TLE set like this:
parsed_TLE1 = parse_TLE(TLE_1)
parsed_TLE2 = parse_TLE(TLE_2)


second_TLE = initTLE[TLE2_number]    
# And access the values like this:
"""print(parsed_TLE1['Epoch_Year_Actual'])"""

# ## Configuration
# NAIF's `SPICE` kernels are first loaded, so that the position of various bodies such as the Earth can be make known to `tudatpy`.
# 
# Then, the start and end simulation epochs are setups. In this case, the start epoch is set to `0`, corresponding to the 1st of January 2000. The times should be specified in seconds since J2000.
# Please refer to the API documentation of the `time_conversion module` [here](https://tudatpy.readthedocs.io/en/latest/time_conversion.html) for more information on this.

# Load spice kernels
spice.load_standard_kernels()

# Set simulation start and end epochs
start_date = datetime(2000, 1, 1, 0, 0, 0, 0)+relativedelta(years= int(parsed_TLE1['Epoch_Year']))+timedelta(days = float(parsed_TLE1['Epoch_Day'])-1)
simulation_start_epoch = time_conversion.datetime_to_tudat(start_date).epoch()
end_date  = datetime(2000, 1, 1, 0, 0, 0, 0)+relativedelta(years= int(parsed_TLE2['Epoch_Year']))+timedelta(days = float(parsed_TLE2['Epoch_Day'])-1)
simulation_end_epoch = time_conversion.datetime_to_tudat(end_date).epoch()



print('\n')
print("The code will run from", start_date, "to", end_date)
print('It will run for a drag coefficient between', drag_coefficient_lower, 'and', drag_coefficient_upper,'with a step size of', step_size)
print('\n')
print('Grab yourself some coffee, this might take a while...')
print('\n')





# ## Environment setup
# Let’s create the environment for our simulation. This setup covers the creation of (celestial) bodies, vehicle(s), and environment interfaces.
# 
# ### Create the bodies
# Bodies can be created by making a list of strings with the bodies that is to be included in the simulation.
# 
# The default body settings (such as atmosphere, body shape, rotation model) are taken from `SPICE`.
# 
# These settings can be adjusted. Please refere to the [Available Environment Models](https://tudat-space.readthedocs.io/en/latest/_src_user_guide/state_propagation/environment_setup/create_models/available.html#available-environment-models) in the user guide for more details.
# 
# Finally, the system of bodies is created using the settings. This system of bodies is stored into the variable `bodies`.


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

body_settings.get("Earth").atmosphere_settings = environment_setup.atmosphere.nrlmsise00()

# Create system of selected celestial bodies
bodies = environment_setup.create_system_of_bodies(body_settings)


# ### Create the vehicle
# Let's now create the 400kg satellite for which the perturbed orbit around Earth will be propagated.


# Create vehicle objects.
bodies.create_empty_body("Delfi-C3")

bodies.get("Delfi-C3").mass = Mass


# To account for the pressure of the solar radiation on the satellite, let's add another interface. This takes a radiation pressure coefficient of 1.2, and a radiation area of 4m$^2$. This interface also accounts for the variation in pressure cause by the shadow of Earth.


# Create radiation pressure settings, and add to vehicle
reference_area_radiation = reference_area  # Average projection area of a 3U CubeSat
occulting_bodies_dict = dict()
occulting_bodies_dict[ "Sun" ] = [ "Earth" ]
vehicle_target_settings = environment_setup.radiation_pressure.cannonball_radiation_target(
    reference_area_radiation, radiation_pressure_coefficient, occulting_bodies_dict )
environment_setup.add_radiation_pressure_target_model(
    bodies, "Delfi-C3", vehicle_target_settings)


# ## Propagation setup
# Now that the environment is created, the propagation setup is defined.
# 
# First, the bodies to be propagated and the central bodies will be defined.
# Central bodies are the bodies with respect to which the state of the respective propagated bodies is defined.

# Define bodies that are propagated
bodies_to_propagate = ["Delfi-C3"]

# Define central bodies of propagation
central_bodies = ["Earth"]

# ### Create the acceleration model
# First off, the acceleration settings that act on `Delfi-C3` are to be defined.
# In this case, these consist in the followings:
# - Graviational acceleration of Earth modeled as Spherical Harmonics, taken up to a degree and order 5.
# - Gravitational acceleration of the Sun, the Moon, Mars, and Venus, modeled as a Point Mass.
# - Aerodynamic acceleration caused by the atmosphere of the Earth (using the aerodynamic interface defined earlier).
# - Radiation pressure acceleration caused by the Sun (using the radiation interface defined earlier).
# 
# The acceleration settings defined are then applied to `Delfi-C3` in a dictionary.
# 
# This dictionary is finally input to the propagation setup to create the acceleration models.

# Define accelerations acting on Delfi-C3 by Sun and Earth.
accelerations_settings_delfi_c3 = dict(
    Sun=[
        propagation_setup.acceleration.radiation_pressure(),
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
acceleration_settings = {"Delfi-C3": accelerations_settings_delfi_c3}

# Create acceleration models.

# ### Define the initial state
# The initial state of the vehicle that will be propagated is now defined. 
# 
# This initial state always has to be provided as a cartesian state, in the form of a list with the first three elements reprensenting the initial position, and the three remaining elements representing the initial velocity.
# 
# Within this example, we will retrieve the initial state of Delfi-C3 using its Two-Line-Elements (TLE) the date of its launch (April the 28th, 2008). The TLE strings are obtained from [space-track.org](https://www.space-track.org).

# Set initial conditions for the satellite that will be
# propagated in this simulation. The initial conditions are given in
# Keplerian elements and later on converted to Cartesian elements


ephemerisdef = environment.TleEphemeris( "Earth", "J2000", initTLE[TLE1_number], False )
state = ephemerisdef.cartesian_state(simulation_start_epoch)
#print(element_conversion.cartesian_to_keplerian(state, bodies.get("Earth").gravitational_parameter))



earth_gravitational_parameter = bodies.get("Earth").gravitational_parameter
initial_state = element_conversion.keplerian_to_cartesian_elementwise(
    gravitational_parameter=earth_gravitational_parameter,
    semi_major_axis= float(element_conversion.cartesian_to_keplerian(state, bodies.get("Earth").gravitational_parameter)[0]),
    eccentricity= float(element_conversion.cartesian_to_keplerian(state, bodies.get("Earth").gravitational_parameter)[1]),
    inclination=float(element_conversion.cartesian_to_keplerian(state, bodies.get("Earth").gravitational_parameter)[2]),
    argument_of_periapsis=float(element_conversion.cartesian_to_keplerian(state, bodies.get("Earth").gravitational_parameter)[3]),
    longitude_of_ascending_node=float(element_conversion.cartesian_to_keplerian(state, bodies.get("Earth").gravitational_parameter)[4]),
    true_anomaly=element_conversion.mean_to_true_anomaly(float(element_conversion.cartesian_to_keplerian(state, bodies.get("Earth").gravitational_parameter)[1]), mean_anomaly=float(float(element_conversion.cartesian_to_keplerian(state, bodies.get("Earth").gravitational_parameter)[5]))),
)


ephemerisdef_2 = environment.TleEphemeris( "Earth", "J2000", second_TLE, False )
state_2 = ephemerisdef_2.cartesian_state(simulation_end_epoch)
#print(element_conversion.cartesian_to_keplerian(state_2, bodies.get("Earth").gravitational_parameter))

Semi_major_axisFinal = element_conversion.cartesian_to_keplerian(state_2, bodies.get("Earth").gravitational_parameter)[0]
eccentricityFinal = element_conversion.cartesian_to_keplerian(state_2, bodies.get("Earth").gravitational_parameter)[1]

#print(parsed_TLE1['Semi_Major_Axis'])
#print(parsed_TLE1['Eccentricity'])
#print(element_conversion.cartesian_to_keplerian(state, bodies.get("Earth").gravitational_parameter)[0])
#print(parsed_TLE2['Semi_Major_Axis'])
#print(element_conversion.cartesian_to_keplerian(state_2, bodies.get("Earth").gravitational_parameter)[0])
#print(state)
#print(state_2)
#print(element_conversion.cartesian_to_keplerian(state, bodies.get("Earth").gravitational_parameter)) and print(element_conversion.cartesian_to_keplerian(state_2, bodies.get("Earth").gravitational_parameter))

RaFinal = Semi_major_axisFinal*(1+eccentricityFinal)
RpFinal = Semi_major_axisFinal*(1-eccentricityFinal)

Height_apoFinal = RaFinal/1000 - 6371
Height_periFinal = RpFinal/1000 - 6371
VaFinal = math.sqrt((3.9860044188*10**14*2*RpFinal)/(RaFinal*(RaFinal+RpFinal)))
VpFinal = math.sqrt((3.9860044188*10**14*2*RaFinal)/(RpFinal*(RaFinal+RpFinal)))
# ### Define dependent variables to save
# In this example, we are interested in saving not only the propagated state of the satellite over time, but also a set of so-called dependent variables, that are to be computed (or extracted and saved) at each integration step.
# 
# [This page](https://tudatpy.readthedocs.io/en/latest/dependent_variable.html) of the tudatpy API website provides a detailled explanation of all the dependent variables that are available.

# Define list of dependent variables to save
dependent_variables_to_save = [
    propagation_setup.dependent_variable.total_acceleration("Delfi-C3"),
    propagation_setup.dependent_variable.keplerian_state("Delfi-C3", "Earth"),
    propagation_setup.dependent_variable.latitude("Delfi-C3", "Earth"),
    propagation_setup.dependent_variable.longitude("Delfi-C3", "Earth"),
    propagation_setup.dependent_variable.single_acceleration_norm(
        propagation_setup.acceleration.point_mass_gravity_type, "Delfi-C3", "Sun"
    ),
    propagation_setup.dependent_variable.single_acceleration_norm(
        propagation_setup.acceleration.point_mass_gravity_type, "Delfi-C3", "Moon"
    ),
    propagation_setup.dependent_variable.single_acceleration_norm(
        propagation_setup.acceleration.point_mass_gravity_type, "Delfi-C3", "Mars"
    ),
    propagation_setup.dependent_variable.single_acceleration_norm(
        propagation_setup.acceleration.point_mass_gravity_type, "Delfi-C3", "Venus"
    ),
    propagation_setup.dependent_variable.single_acceleration_norm(
        propagation_setup.acceleration.spherical_harmonic_gravity_type, "Delfi-C3", "Earth"
    ),
    propagation_setup.dependent_variable.single_acceleration_norm(
        propagation_setup.acceleration.aerodynamic_type, "Delfi-C3", "Earth"
    ),
    propagation_setup.dependent_variable.single_acceleration_norm(
        propagation_setup.acceleration.cannonball_radiation_pressure_type, "Delfi-C3", "Sun"
    ),
    propagation_setup.dependent_variable.altitude("Delfi-C3", "Earth"),
]

print(propagation_setup.dependent_variable.PropagationDependentVariables(1))
# ### Create the propagator settings
# The propagator is finally setup.
# 
# First, a termination condition is defined so that the propagation will stop when the end epochs that was defined is reached.
# 
# Subsequently, the integrator settings are defined using a RK4 integrator with the fixed step size of 10 seconds.
# 
# Then, the translational propagator settings are defined. These are used to simulate the orbit of `Delfi-C3` around Earth.


# Create termination settings
#termination_condition = propagation_setup.propagator.time_termination(simulation_end_epoch)
termination_settings_list = [propagation_setup.propagator.time_termination(simulation_end_epoch), propagation_setup.propagator.dependent_variable_termination(
  dependent_variable_settings = propagation_setup.dependent_variable.altitude( "Delfi-C3", "Earth" ),
  limit_value = 100.0E3,
  use_as_lower_limit = True)]
termination_condition = propagation_setup.propagator.hybrid_termination(termination_settings_list, fulfill_single_condition = True)

# Create numerical integrator settings

#integrator_settings = propagation_setup.integrator.runge_kutta_4(fixed_step_size)
# integrator_settings = propagation_setup.integrator.adams_bashforth_moulton(fixed_step_size, 5.0, 150, minimum_order=6, maximum_order=11)
#integrator_settings = propagation_setup.integrator.bulirsch_stoer_variable_step(initial_time_step=fixed_step_size,extrapolation_sequence = propagation_setup.integrator.deufelhard_sequence, maximum_number_of_steps=7, 
                                                                                #step_size_control_settings =propagation_setup.integrator.step_size_control_elementwise_scalar_tolerance(1.0E-10, 1.0E-10, minimum_factor_increase=0.05),
                                                                                #step_size_validation_settings =propagation_setup.integrator.step_size_validation(0.1, 10000.0),
                                                                                #assess_termination_on_minor_steps = False)
integrator_settings = propagation_setup.integrator.runge_kutta_fixed_step(time_step=fixed_step_size, coefficient_set=propagation_setup.integrator.rkf_78)

# processing_settings = propagation_setup.propagator.SingleArcPropagatorProcessingSettings()



# Create propagation settings

#print(propagator_settings.print_settings)


# ## Propagate the orbit
# The orbit is now ready to be propagated.
# 
# This is done by calling the `create_dynamics_simulator()` function of the `numerical_simulation module`.
# This function requires the `bodies` and `propagator_settings` that have all been defined earlier.
# 
# After this, the history of the propagated state over time, containing both the position and velocity history, is extracted.
# This history, taking the form of a dictionary, is then converted to an array containing 7 columns:
# - Column 0: Time history, in seconds since J2000.
# - Columns 1 to 3: Position history, in meters, in the frame that was specified in the `body_settings`.
# - Columns 4 to 6: Velocity history, in meters per second, in the frame that was specified in the `body_settings`.
# 
# The same is done with the dependent variable history. The column indexes corresponding to a given dependent variable in the `dep_vars` variable are printed when the simulation is run, when `create_dynamics_simulator()` is called.
# Do mind that converting to an ndarray using the `result2array()` utility will shift these indexes, since the first column (index 0) will then be the times.
Error = []
DC = []
FA= []
for i in range(itterations):
    drag_coefficient = drag_coefficient_lower + i*step_size
    print("-----Starting simulation for a drag coefficient of:", drag_coefficient,'-----')
    print('\n')

    aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
    reference_area, [drag_coefficient, 0, 0]
    )
    environment_setup.add_aerodynamic_coefficient_interface(
    bodies, "Delfi-C3", aero_coefficient_settings)

    acceleration_models = propagation_setup.create_acceleration_models(
    bodies,
    acceleration_settings,
    bodies_to_propagate,
    central_bodies)
    propagator_settings = propagation_setup.propagator.translational(
        central_bodies,
        acceleration_models,
        bodies_to_propagate,
        initial_state,
        simulation_start_epoch,
        integrator_settings,
        termination_condition,
        output_variables=dependent_variables_to_save,
    )
    propagator_settings.print_settings.print_dependent_variable_indices = False
    propagator_settings.print_settings.print_state_indices = False
    # propagator_settings.print_settings.results_print_frequency_in_seconds = 0.5e7
    #propagator_settings.print_settings.results_print_frequency_in_steps =100000
    propagator_settings.print_settings.results_print_frequency_in_steps = False

   
    DC.append(drag_coefficient)
    

# Create simulation object and propagate the dynamics
    dynamics_simulator = numerical_simulation.create_dynamics_simulator(
        bodies, propagator_settings)


# Extract the resulting state and depedent variable history and convert it to an ndarray
    states = dynamics_simulator.state_history
    states_array = result2array(states)
    dep_vars = dynamics_simulator.dependent_variable_history
    dep_vars_array = result2array(dep_vars)

    #Final_altitude = dep_vars_array[-1,19]
    kepler_elements = dep_vars_array[:,4:10]
    Semi_major_axis = kepler_elements[:,0]
    eccentricity = kepler_elements[:,1]
    inclination = np.rad2deg(kepler_elements[:,2])
    argument_of_periapsis = np.rad2deg(kepler_elements[:,3])
    raan = np.rad2deg(kepler_elements[:,4])
    true_anomaly = np.rad2deg(kepler_elements[:,5])

    Rp = Semi_major_axis*(1-eccentricity[-1])
    Ra = Semi_major_axis*(1+eccentricity[-1])

    Height_apo = Ra/1000 - 6371
    Height_peri = Rp/1000 - 6371

    # Calculating the velocity
    Vp = math.sqrt((3.9860044188*10**14*2*Ra[-1])/(Rp[-1]*(Ra[-1]+Rp[-1])))
    Va = math.sqrt((3.9860044188*10**14*2*Rp[-1])/(Ra[-1]*(Ra[-1]+Rp[-1])))
    print('For a drag coefficient of',round(drag_coefficient,2),'the TLE data versus the simulation data is as follows:')
    print(Height_apoFinal, Height_apo[-1])
    print(Height_periFinal, Height_peri[-1])
    print(VpFinal, Vp)
    print(VaFinal, Va)
    print('\n')





    MSE = (1/4) * ((Height_apo[-1] - Height_apoFinal)**2 + (Height_peri[-1] - Height_periFinal)**2 + (Vp - VpFinal)**2 + (Va - VaFinal)**2)
    print(MSE)
    print('\n')

    Error.append(MSE)
    FA.append(Height_apo[-1])

print(DC)
print(FA)
print(Error)

# ## Post-process the propagation results
# The results of the propagation are then processed to a more user-friendly form.
# 
# ### Total acceleration over time
# Let's first plot the total acceleration on the satellite over time. This can be done by taking the norm of the first three columns of the dependent variable list.


# Plot total acceleration as function of time
"""start_time=(time_conversion.calendar_date_to_julian_day(datetime.datetime(2022, 9, 6, 0, 27, 0, 970272))-time_conversion.calendar_date_to_julian_day(datetime.datetime(2000, 1, 1, 0, 0, 0, 0)))
print(dep_vars_array[:,0]/(3600*24))
time_days = dep_vars_array[:,0]/(3600*24) - start_time
total_acceleration_norm = np.linalg.norm(dep_vars_array[:,1:4], axis=1)
plt.figure(figsize=(9, 5))
plt.title("Total acceleration norm on Delfi-C3 over the course of propagation.")
plt.plot(time_days, total_acceleration_norm)
plt.xlabel('Time [days]')
plt.ylabel('Total Acceleration [m/s$^2$]')
plt.xlim([min(time_days), max(time_days)])
plt.grid()
plt.tight_layout()
plt.show()"""

#print(dep_vars_array[0,:])
# altitude over time
"""altitude = dep_vars_array[:,19]
dates = [time_conversion.julian_day_to_calendar_date(start_date.julian_day()) + datetime.timedelta(days=day) for day in time_days]
plt.figure(figsize=(9, 5))
plt.title("Altitude of Delfi-C3 over the course of propagation.")
plt.plot(dates, altitude)
plt.gcf().autofmt_xdate()
plt.xlabel('Time [days]')
plt.ylabel('Altitude [m]')
plt.xlim([min(dates), max(dates)])
plt.grid()
plt.tight_layout()
plt.show()
plt.savefig('altitude.png')"""


plt.figure(figsize=(9, 5))
plt.title("DC vs FA.")
plt.plot(DC, FA)
plt.xlabel('DC')
plt.ylabel('Altitude [m]')
plt.grid()
plt.tight_layout()
plt.show()
plt.savefig('apoapsis vs DC.png')

plt.figure(figsize=(9, 5))
plt.title("DC vs Error.")
plt.plot(DC, Error)
plt.xlabel('DC')
plt.ylabel('Error')
plt.grid()
plt.tight_layout()
plt.show()
plt.savefig('Error vs DC.png')


# ### Ground track
# Let's then plot the ground track of the satellite in its first 3 hours. This makes use of the latitude and longitude dependent variables.


# Plot ground track for a period of 3 hours
"""latitude = dep_vars_array[:,10]
longitude = dep_vars_array[:,11]
hours = 3
subset = int(len(time_days) / 24 * hours)
latitude = np.rad2deg(latitude[0: subset])
longitude = np.rad2deg(longitude[0: subset])
plt.figure(figsize=(9, 5))
plt.title("3 hour ground track of Delfi-C3")
plt.scatter(longitude, latitude, s=1)
plt.xlabel('Longitude [deg]')
plt.ylabel('Latitude [deg]')
plt.xlim([min(longitude), max(longitude)])
plt.yticks(np.arange(-90, 91, step=45))
plt.grid()
plt.tight_layout()
plt.show()
plt.savefig('ground track.png')"""

# ### Kepler elements over time
# Let's now plot each of the 6 Kepler element as a function of time, also as saved in the dependent variables.


# Plot Kepler elements as a function of time
"""kepler_elements = dep_vars_array[:,4:10]
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2, figsize=(9, 12))
fig.suptitle('Evolution of Kepler elements over the course of the propagation.')

# Semi-major Axis
semi_major_axis = kepler_elements[:,0] / 1e3
ax1.plot(time_days, semi_major_axis, linewidth=1)
ax1.set_ylabel('Semi-major axis [km]')

# Eccentricity
eccentricity = kepler_elements[:,1]
ax2.plot(time_days, eccentricity, linewidth=1)
ax2.set_ylabel('Eccentricity [-]')

# Inclination
inclination = np.rad2deg(kepler_elements[:,2])
ax3.plot(time_days, inclination, linewidth=1)
ax3.set_ylabel('Inclination [deg]')

# Argument of Periapsis
argument_of_periapsis = np.rad2deg(kepler_elements[:,3])
ax4.plot(time_days, argument_of_periapsis, linewidth=1)
ax4.set_ylabel('Argument of Periapsis [deg]')

# Right Ascension of the Ascending Node
raan = np.rad2deg(kepler_elements[:,4])
ax5.plot(time_days, raan, linewidth=1)
ax5.set_ylabel('RAAN [deg]')

# True Anomaly
true_anomaly = np.rad2deg(kepler_elements[:,5])
ax6.scatter(time_days, true_anomaly, s=1, linewidths=1)
ax6.set_ylabel('True Anomaly [deg]')
ax6.set_yticks(np.arange(0, 361, step=60))

for ax in fig.get_axes():
    ax.set_xlabel('Time [days]')
    ax.set_xlim([min(time_days), max(time_days)])
    ax.grid()
plt.tight_layout()
plt.show()
plt.savefig('test.png')"""


# ### Accelerations over time
# Finally, let's plot and compare each of the included accelerations.

"""plt.figure(figsize=(9, 5))

# Point Mass Gravity Acceleration Sun
acceleration_norm_pm_sun = dep_vars_array[:,12]
plt.plot(time_days, acceleration_norm_pm_sun, label='PM Sun', linewidth=1)

# Point Mass Gravity Acceleration Moon
acceleration_norm_pm_moon = dep_vars_array[:,13]
plt.plot(time_days, acceleration_norm_pm_moon, label='PM Moon', linewidth=1)

# Point Mass Gravity Acceleration Mars
acceleration_norm_pm_mars = dep_vars_array[:,14]
plt.plot(time_days, acceleration_norm_pm_mars, label='PM Mars', linewidth=1)

# Point Mass Gravity Acceleration Venus
acceleration_norm_pm_venus = dep_vars_array[:,15]
plt.plot(time_days, acceleration_norm_pm_venus, label='PM Venus', linewidth=1)

# Spherical Harmonic Gravity Acceleration Earth
acceleration_norm_sh_earth = dep_vars_array[:,16]
plt.plot(time_days, acceleration_norm_sh_earth, label='SH Earth', linewidth=1)

# Aerodynamic Acceleration Earth
acceleration_norm_aero_earth = dep_vars_array[:,17]
plt.plot(time_days, acceleration_norm_aero_earth, label='Aerodynamic Earth', linewidth=1)

# Cannonball Radiation Pressure Acceleration Sun
acceleration_norm_rp_sun = dep_vars_array[:,18]
plt.plot(time_days, acceleration_norm_rp_sun, label='Radiation Pressure Sun', linewidth=1)

plt.xlim([min(time_days), max(time_days)])
plt.xlabel('Time [days]')
plt.ylabel('Acceleration Norm [m/s$^2$]')

plt.legend(bbox_to_anchor=(1.005, 1))
plt.suptitle("Accelerations norms on Delfi-C3, distinguished by type and origin, over the course of propagation.")
plt.yscale('log')
plt.grid()
plt.tight_layout()
plt.show()
plt.savefig('test2.png')"""