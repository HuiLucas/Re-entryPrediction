### Just for making graphs using numpy arrays ###
# Imports
import matplotlib.pyplot as plt
import numpy as np

# Grapherydoo
t_hist = np.load("PREDICTIONS_SINGLE\Time vector starting 2022-09-06 - 6-6-2024 14h38.npy")
t_pred = np.load("PREDICTIONS_SINGLE\Time vector starting 2022-09-06 - 6-6-2024 14h52.npy")
alt_hist = np.load("PREDICTIONS_SINGLE\Altitude vector - 6-6-2024 14h38.npy")
alt_pred = np.load("PREDICTIONS_SINGLE\Altitude vector - 6-6-2024 14h52.npy")
if max(t_hist) > max(t_pred):
    reentry = np.linspace(100, 100, len(t_hist))
else:
    reentry = np.linspace(100, 100, len(t_pred))

plt.figure(figsize=(9, 5))
plt.plot(t_hist, alt_hist, label="Using historical solar data", color="blue")
plt.plot(t_pred, alt_pred, label="Using old predicted solar data", color="green")
if max(t_hist) > max(t_pred):
    plt.plot(t_hist, reentry, label="Re-entry", color="red", linestyle='dotted')
else:
    plt.plot(t_pred, reentry, label="Re-entry", color="red", linestyle='dotted')
plt.legend(loc="best", bbox_to_anchor=(0.47, 0.3), fontsize=12)
plt.xlabel('Time [days]', fontsize=13)
plt.ylabel('Altitude [km]', fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlim([min(min(t_hist), min(t_pred)), max(max(t_hist), max(t_pred))])
plt.grid()
#plt.tight_layout()
plt.savefig("PREDICTIONS_SINGLE\Plot for report")