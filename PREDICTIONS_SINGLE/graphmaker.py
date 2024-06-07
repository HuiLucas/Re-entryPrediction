### Just for making graphs using numpy arrays ###
# Imports
import matplotlib.pyplot as plt
import numpy as np

# Grapherydoo
t_hist = np.load("PREDICTIONS_SINGLE\Time vector historical.npy")
t_pred = np.load("PREDICTIONS_SINGLE\Time vector old predictions.npy")
alt_hist = np.load("PREDICTIONS_SINGLE\Altitude vector historical.npy")
alt_pred = np.load("PREDICTIONS_SINGLE\Altitude vector old predictions.npy")

plt.figure(figsize=(9, 5))
plt.plot(t_hist, alt_hist, label="Using historical solar data", color="blue")
plt.plot(t_pred, alt_pred, label="Using old predicted solar data", color="green")
plt.axhline(y=100, label="Re-entry", color='red', linestyle='dotted')
plt.legend(loc="best", bbox_to_anchor=(0.54, 0.09), fontsize=14)
plt.xlabel('Time [days]', fontsize=14)
plt.ylabel('Altitude [km]', fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlim([min(min(t_hist), min(t_pred)), max(max(t_hist), max(t_pred))+5])
plt.grid()
#plt.tight_layout()
plt.savefig("PREDICTIONS_SINGLE\Plot for report")