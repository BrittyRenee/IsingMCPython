# a script that will make a simulation of the ising model
# based off previous matlab script
# ultimate practice for python and getting physics experience
# improvements planned are adding a slight bias factor in order to get results above and below zero
import ising_tools

L = 100 #This is the dimension of the LxL matrix
p = 0.5 # p == % of "spin ups" that are initializing our lattice
temp = 2.5 #value for the temperature
#Then the number of trials are determined
trials = 500 #number of loops for the Mote Carlo Portion

x = 0 #allocation of our average magnetization

file_title = input("Please enter name for image files: ")

# Then the lattice type: 'donut', 'positive', 'negative', or default
lat_type = 'donut'

exp_runs = input("Please enter the number of experiments: ")
exp_runs = int(exp_runs)

for i in list(range(exp_runs)):
    #Then the lattice is set up using the create_lattice function
    initial_lat = ising_tools.create_lattice(L,p)
    final_lat, val = ising_tools.animate_lattice(trials, initial_lat, L, temp, lat_type, file_title)
    x = x + val

avg_mag = x / exp_runs
print(avg_mag)
