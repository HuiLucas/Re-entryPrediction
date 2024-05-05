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
import os

"""-------------------------------"""
"""Inputs"""
satellite = "Delfi-n3Xt"
TLE_Data = 'TLE-Data_n3Xt.txt'

Folder = "Error vs Cd Delfi-n3Xt/"
TLE1_number = 6700
TLE2_number = 7200

Mass = 2.8

reference_area = 0.087  # Average projection area of a 3U CubeSat
drag_coefficient_lower = 1.3
drag_coefficient_upper = 2.3


iterations = 11

radiation_pressure_coefficient = 1.2

fixed_step_size = 100

Comparisons = 100 #Number of Epochs you compare to the TLE data



"""-------------------------------"""

if (TLE2_number - TLE1_number)%Comparisons != 0:
    print("\n")
    sys.exit("The number of comparisons is not a factor of the number of TLEs")


step_size  = (drag_coefficient_upper - drag_coefficient_lower)/(iterations-1) #Calculates the Drag Coefficient step size
Comp_Epochs = [TLE1_number + (i+1)*int((TLE2_number-TLE1_number)/Comparisons) for i in range(Comparisons)] #Calculates the epochs for the comparisons



# Open the file
with open(TLE_Data, 'r') as file:
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
with open(TLE_Data, 'r') as file:
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
print('It will run for a drag coefficient between', drag_coefficient_lower, 'and', drag_coefficient_upper,'with a step size of', round(step_size,4))
print('\n')
print('Grab yourself some coffee, this might take a while...')

    

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


# Create vehicle objects.
bodies.create_empty_body(satellite)

bodies.get(satellite).mass = Mass


# Create radiation pressure settings, and add to vehicle
reference_area_radiation = reference_area  # Average projection area of a 3U CubeSat
occulting_bodies_dict = dict()
occulting_bodies_dict[ "Sun" ] = [ "Earth" ]
vehicle_target_settings = environment_setup.radiation_pressure.cannonball_radiation_target(
    reference_area_radiation, radiation_pressure_coefficient, occulting_bodies_dict )
environment_setup.add_radiation_pressure_target_model(
    bodies, satellite, vehicle_target_settings)


# Define bodies that are propagated
bodies_to_propagate = [satellite]

# Define central bodies of propagation
central_bodies = ["Earth"]



ephemerisdef = environment.TleEphemeris( "Earth", "J2000", initTLE[TLE1_number], False )
state = ephemerisdef.cartesian_state(simulation_start_epoch)


earth_gravitational_parameter = bodies.get("Earth").gravitational_parameter

ephemerisdef_lst = [] #list of ephemeris definitions for the comparisons
state_lst = [] #list of states for the comparisons
for i in range(Comparisons):
   TLE_number = int(Comp_Epochs[i])
   ephemersisdef_Comp = environment.TleEphemeris( "Earth", "J2000", initTLE[TLE_number], False )
   ephemerisdef_lst.append(ephemersisdef_Comp)
   state_Comp = ephemersisdef_Comp.cartesian_state(sim_epochs[i]) 
   state_lst.append(state_Comp)



ephemerisdef_2 = environment.TleEphemeris( "Earth", "J2000", second_TLE, False )
state_2 = ephemerisdef_2.cartesian_state(simulation_end_epoch)



Semi_major_axisFinal = element_conversion.cartesian_to_keplerian(state_2, bodies.get("Earth").gravitational_parameter)[0]
eccentricityFinal = element_conversion.cartesian_to_keplerian(state_2, bodies.get("Earth").gravitational_parameter)[1]

Semi_major_axis_lst = []
eccentricity_lst = []
for i in range(Comparisons):
    Semi_major_axis = element_conversion.cartesian_to_keplerian(state_lst[i], bodies.get("Earth").gravitational_parameter)[0]
    eccentricity = element_conversion.cartesian_to_keplerian(state_lst[i], bodies.get("Earth").gravitational_parameter)[1]
    Semi_major_axis_lst.append(Semi_major_axis)
    eccentricity_lst.append(eccentricity)


# Define list of dependent variables to save
dependent_variables_to_save = [
    propagation_setup.dependent_variable.total_acceleration(satellite),
    propagation_setup.dependent_variable.keplerian_state(satellite, "Earth"),
    propagation_setup.dependent_variable.latitude(satellite, "Earth"),
    propagation_setup.dependent_variable.longitude(satellite, "Earth"),
    propagation_setup.dependent_variable.single_acceleration_norm(
        propagation_setup.acceleration.point_mass_gravity_type, satellite, "Sun"
    ),
    propagation_setup.dependent_variable.single_acceleration_norm(
        propagation_setup.acceleration.point_mass_gravity_type, satellite, "Moon"
    ),
    propagation_setup.dependent_variable.single_acceleration_norm(
        propagation_setup.acceleration.point_mass_gravity_type, satellite, "Mars"
    ),
    propagation_setup.dependent_variable.single_acceleration_norm(
        propagation_setup.acceleration.point_mass_gravity_type, satellite, "Venus"
    ),
    propagation_setup.dependent_variable.single_acceleration_norm(
        propagation_setup.acceleration.spherical_harmonic_gravity_type, satellite, "Earth"
    ),
    propagation_setup.dependent_variable.single_acceleration_norm(
        propagation_setup.acceleration.aerodynamic_type, satellite, "Earth"
    ),
    propagation_setup.dependent_variable.single_acceleration_norm(
        propagation_setup.acceleration.cannonball_radiation_pressure_type, satellite, "Sun"
    ),
    propagation_setup.dependent_variable.altitude(satellite, "Earth"),
]


# Create termination settings
#termination_condition = propagation_setup.propagator.time_termination(simulation_end_epoch)
termination_settings_list = [propagation_setup.propagator.time_termination(simulation_end_epoch), propagation_setup.propagator.dependent_variable_termination(
  dependent_variable_settings = propagation_setup.dependent_variable.altitude( satellite, "Earth" ),
  limit_value = 100.0E3,
  use_as_lower_limit = True)]
termination_condition = propagation_setup.propagator.hybrid_termination(termination_settings_list, fulfill_single_condition = True)

# Create numerical integrator settings
integrator_settings = propagation_setup.integrator.runge_kutta_fixed_step(time_step=fixed_step_size, coefficient_set=propagation_setup.integrator.rkf_78)



# Specify the directory name
dir_name = Folder + str(str(TLE1_number) + " to " + str(TLE2_number) + " CD " + str(drag_coefficient_lower) + " to " + str(drag_coefficient_upper) + ", " + str(Comparisons) + " Comps")

# Create the directory
os.makedirs(dir_name,exist_ok=True)
i = 0
Error = []
DC = []
for i in range(iterations):
    drag_coefficient = drag_coefficient_lower + i*step_size

    print("\n")
    print("starting the propagtion for a drag coefficient of", drag_coefficient)


    aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
    reference_area, [drag_coefficient, 0, 0]
    )
    environment_setup.add_aerodynamic_coefficient_interface(
    bodies, satellite, aero_coefficient_settings)

    aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
    reference_area, [drag_coefficient, 0, 0]
    )
    environment_setup.add_aerodynamic_coefficient_interface(
        bodies, satellite, aero_coefficient_settings)
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
    acceleration_settings = {satellite: accelerations_settings_delfi_c3}

    acceleration_models = propagation_setup.create_acceleration_models(
    bodies,
    acceleration_settings,
    bodies_to_propagate,
    central_bodies)
    propagator_settings = propagation_setup.propagator.translational(
        central_bodies,
        acceleration_models,
        bodies_to_propagate,
        state,
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

    Output_Epochs = states_array[:,0] #Same kind of format as sim_epochs


# Find the common elements
    common_elements = np.in1d(Output_Epochs, sim_epochs)
# Find the indices of the common elements in Output_Epochs
    indices_in_Output_Epochs = np.where(common_elements)[0]

# Find the indices of the common elements in sim_epochs
    indices_in_sim_epochs = []
    for element in Output_Epochs[indices_in_Output_Epochs]:
        indices_in_sim_epochs.append(np.where(sim_epochs == element)[0][0])


    #Final_altitude = dep_vars_array[-1,19]
    kepler_elements = dep_vars_array[:,4:10]
    SMA = kepler_elements[:,0]
    eccentricity = kepler_elements[:,1]
    inclination = np.rad2deg(kepler_elements[:,2])
    argument_of_periapsis = np.rad2deg(kepler_elements[:,3])
    raan = np.rad2deg(kepler_elements[:,4])
    true_anomaly = np.rad2deg(kepler_elements[:,5])


    #This makes a list of the predicted semi-major axis at the epochs that are compared to the TLE data
    SM_Comp_lst = []
    for i in range(len(indices_in_Output_Epochs)):
        SM_Comp_lst.append(SMA[indices_in_Output_Epochs[i]])

    #This makes a list of the actual semi-major axis at the epochs that are compared to the TLE data
    ACT_Semi_major_lst = []
    for i in indices_in_sim_epochs:
        ACT_Semi_major_lst.append(Semi_major_axis_lst[i])


    # Calculate the Mean Squared Error
    MSE = 0
    for i in range(len(SM_Comp_lst)):
        MSE = MSE + ((ACT_Semi_major_lst[i] - SM_Comp_lst[i])**2)
    MSE = MSE/(len(SM_Comp_lst)*10**6)
    Error.append(MSE)

    # Plot the predicted semi-major axis vs the actual semi-major axis
    plt.figure(figsize=(9, 5))
    plt.title("Semi major axis prediction vs actual semi major axis for a drag coefficient of " + str(drag_coefficient))
    plt.plot(range(len(SM_Comp_lst)), SM_Comp_lst, label="Predicted Semi-Major Axis")
    plt.plot(range(len(ACT_Semi_major_lst)), ACT_Semi_major_lst, label="Real Semi-Major Axis")
    plt.xlabel('Epoch Number')
    plt.ylabel('Semi-Major Axis')
    plt.legend(loc = 'lower left')
    plt.grid(True)
    plt.savefig(f'{dir_name}/Real vs Predicted Semi-Major Axis {drag_coefficient}.png')


    print("the Mean Squared Error is:",MSE)

# Plot the error vs the drag coefficient
plt.figure(figsize=(9, 5))
plt.title("DC vs Error.")
plt.plot(DC, Error)
plt.xlabel('DC')
plt.ylabel('Error')
plt.grid()
plt.tight_layout()
plt.savefig(f'{dir_name}/Error vs Cd.png')