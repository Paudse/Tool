import matplotlib.pyplot as plt
import scipy.io 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
import io

# fig setup
fig = plt.figure(figsize=(6,5.5), dpi=300)

# Load DQN result
data_dqn = scipy.io.loadmat('dqn_result_cycle_iteration_61.mat')
sim_t_dqn = data_dqn['sim_t_dqn'][0]
sim_W_ice_dqn = data_dqn['sim_W_ice_dqn'][0]
sim_T_ice_dqn = data_dqn['sim_T_ice_dqn'][0]
sim_P_ice_dqn = data_dqn['sim_P_ice_dqn'][0]
sim_W_mg2_dqn = data_dqn['sim_W_mg2_dqn'][0]
sim_T_mg2_dqn = data_dqn['sim_T_mg2_dqn'][0]
sim_P_mg2_dqn = data_dqn['sim_P_mg2_dqn'][0]
car_kph_dqn = data_dqn['sim_car_kph_dqn'][0]
sim_T_brake_dqn = data_dqn['sim_T_brake_dqn'][0]
sim_gear_dqn = data_dqn['sim_gear_dqn'][0]
sim_fuel_instant_dqn = data_dqn['sim_fuel_instant_dqn'][0]
sim_fuel_accumulate_dqn = data_dqn['sim_fuel_accumulate_dqn'][0]
sim_battery_charge_dqn = data_dqn['sim_battery_charge_dqn'][0]
sim_battery_soc_dqn = data_dqn['sim_battery_soc_dqn'][0]
sim_reward_dqn = data_dqn['sim_reward_dqn'][0]
sim_acum_reward_dqn = data_dqn['sim_acum_reward_dqn'][0]
cycle_iteration_dqn = data_dqn['cycle_iteration_dqn'][0]
ave_cyc_reward_dqn = data_dqn['ave_cyc_reward_dqn'][0]
cyc_fuel_accumulate_dqn = data_dqn['cyc_fuel_accumulate_dqn'][0]
ave_cyc_speed_difference_kmh_dqn = data_dqn['ave_cyc_speed_difference_kmh_dqn'][0]
# speed_difference_kmh_dqn = data_dqn['speed_difference_kmh_dqn'][0]

#### Fig1 ICE ####
plt.subplots_adjust(wspace =1, hspace =0.5)
ax = plt.subplot(3,1,1)
plt.plot(cycle_iteration_dqn,ave_cyc_reward_dqn, label='DQN')
plt.title('(a) Reward', loc='left')
plt.ylabel('')
# plt.xlabel('cycle iteration')
# plt.xlabel('(a)')
plt.xlim(0, max(cycle_iteration_dqn)+1)
plt.grid(color='gray', linestyle='-', linewidth=0.2)
ax.spines['top'].set_linewidth(0)
ax.spines['right'].set_linewidth(0)

# plt.legend(loc='upper left')

ax = plt.subplot(3,1,2)
plt.plot(cycle_iteration_dqn,ave_cyc_speed_difference_kmh_dqn)
plt.title('(b) Speed Deviation', loc='left')
plt.ylabel('km/h')
# plt.xlabel('cycle iteration')
# plt.xlabel('(b)')
plt.xlim(0, max(cycle_iteration_dqn)+1)
plt.grid(color='gray', linestyle='-', linewidth=0.2)
ax.spines['top'].set_linewidth(0)
ax.spines['right'].set_linewidth(0)

ax = plt.subplot(3,1,3)
plt.plot(cycle_iteration_dqn,cyc_fuel_accumulate_dqn)
plt.title('(c) Fuel Consumption', loc='left')
plt.ylabel('g')
plt.xlabel('cycle iteration')
plt.xlim(0, max(cycle_iteration_dqn)+1)
plt.grid(color='gray', linestyle='-', linewidth=0.2)
ax.spines['top'].set_linewidth(0)
ax.spines['right'].set_linewidth(0)

# Save the image in memory in PNG format
png1 = io.BytesIO()
fig.savefig(png1, format="png")

# Load this image into PIL
png2 = Image.open(png1)

# Save as TIFF
png2.save("save.tiff")
png1.close()