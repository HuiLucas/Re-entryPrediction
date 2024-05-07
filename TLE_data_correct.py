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

"""-------------------------------"""
"""Inputs"""
TLE1_number = 3500
TLE2_number = 9000

Mass = 2.2

reference_area = 0.08  # Average projection area of a 3U CubeSat
drag_coefficient_lower = 1.2
drag_coefficient_upper = 2.0


itterations = 20

radiation_pressure_coefficient = 1.2

fixed_step_size = 1
"""Change to a lower step size when the code works"""

Comparisons = 100 #Number of Epochs you compare to the TLE data


"""-------------------------------"""

if (TLE2_number - TLE1_number)%Comparisons != 0:
    print("\n")
    sys.exit("The number of comparisons is not a factor of the number of TLEs")


step_size  = (drag_coefficient_upper - drag_coefficient_lower)/itterations #Calculates the Drag Coefficient step size
Comp_Epochs = [TLE1_number + (i+1)*int((TLE2_number-TLE1_number)/Comparisons) for i in range(Comparisons)] #Calculates the epochs for the comparisons



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

parsed_TLE_LST = [parsed_TLE1] #List of parsed TLEs starting from TLE1 to TLE2 with the step size of Comparisons
for i in Comp_Epochs:
    parsed_TLE_LST.append(parse_TLE(split_TLE_sets[i]))




second_TLE = initTLE[TLE2_number]



print('\n')
print("The code will run from", parsed_TLE1['Date'], "to", parsed_TLE2['Date'])
print('It will run for a drag coefficient between', drag_coefficient_lower, 'and', drag_coefficient_upper,'with a step size of', step_size)
print('\n')
print('Grab yourself some coffee, this might take a while...')
print('\n')

    
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
start_date = DateTime(parsed_TLE1['Year_Actual'], parsed_TLE1['Month'], parsed_TLE1['Day'], parsed_TLE1['Hour'])
simulation_start_epoch = start_date.epoch()
simulation_end_epoch   = DateTime(parsed_TLE2['Year_Actual'], parsed_TLE2['Month'], parsed_TLE2['Day'], parsed_TLE2['Hour']).epoch()

sim_epochs=[]
for i in range(Comparisons):
    Comp_date = DateTime(parsed_TLE_LST[i+1]['Year_Actual'], parsed_TLE_LST[i+1]['Month'], parsed_TLE_LST[i+1]['Day'], parsed_TLE_LST[i+1]['Hour']).epoch()
    sim_epochs.append(Comp_date)

#print(sim_epochs)

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

ephemerisdef_lst = [] #list of ephemeris definitions for the comparisons
state_lst = [] #list of states for the comparisons
for i in range(Comparisons):
   TLE_number = int(Comp_Epochs[i])
   ephemersisdef_Comp = environment.TleEphemeris( "Earth", "J2000", initTLE[TLE_number], False )
   ephemerisdef_lst.append(ephemersisdef_Comp)
   state_Comp = ephemersisdef_Comp.cartesian_state(sim_epochs[i]) #This is obv wrong it shouldnt be the start epoch, FIX THIS!!!!
   state_lst.append(state_Comp)



ephemerisdef_2 = environment.TleEphemeris( "Earth", "J2000", second_TLE, False )
state_2 = ephemerisdef_2.cartesian_state(simulation_end_epoch)
#print(element_conversion.cartesian_to_keplerian(state_2, bodies.get("Earth").gravitational_parameter))



Semi_major_axisFinal = element_conversion.cartesian_to_keplerian(state_2, bodies.get("Earth").gravitational_parameter)[0]
eccentricityFinal = element_conversion.cartesian_to_keplerian(state_2, bodies.get("Earth").gravitational_parameter)[1]

Semi_major_axis_lst = []
eccentricity_lst = []
for i in range(Comparisons):
    Semi_major_axis = element_conversion.cartesian_to_keplerian(state_lst[i], bodies.get("Earth").gravitational_parameter)[0]
    eccentricity = element_conversion.cartesian_to_keplerian(state_lst[i], bodies.get("Earth").gravitational_parameter)[1]
    Semi_major_axis_lst.append(Semi_major_axis)
    eccentricity_lst.append(eccentricity)



# Plotting the semi-major axis list over the epoch number
plt.plot(range(Comparisons), Semi_major_axis_lst)
plt.xlabel('Epoch Number')
plt.ylabel('Semi-Major Axis')
plt.title('Semi-Major Axis vs Epoch Number')
plt.grid(True)
plt.show()



# Extract the years from the parsed TLEs
start_year = parsed_TLE1['Year_Actual']
end_year = parsed_TLE2['Year_Actual']

# Calculate the number of years between the start and end years
num_years = end_year - start_year + 1

# Create a list of years
years = list(range(start_year, end_year + 1))

# Slice the Semi_major_axis_lst list to match the length of years
Semi_major_axis_lst = Semi_major_axis_lst[:len(years)]

# Plot the semi-major axis over the years
plt.plot(years, Semi_major_axis_lst)
plt.xlabel('Year')
plt.ylabel('Semi-Major Axis')
plt.title('Semi-Major Axis vs Year')
plt.grid(True)
plt.show()