import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# for trenden i de ubehandlede prøvene
def logistisk(T, Emin, Emax, k, T0): 
    return Emin + (Emax - Emin)/(1 + np.exp(-k*(T - T0)))
# Data
temp_varme = [
    -91.20, -52.00, -47.10, -43.90, -38.70, -32.90, -30.30,
    -29.80, -28.40, -27.50, -20.00, -19.60, -10.20, -8.40,
    -5.40, 6.00, 15.30, 20.00, 20.00, 20.00, 22.00, 27.80,
    72.50, 76.50
]

energi_varme = [
    20.89, 46.69, 145.32, 171.71, 101.84, 140.87, 33.22,
    169.18, 157.93, 152.01, 194.94, 80.81, 158.83, 117.81,
    163.13, 180.00, 168.24, 39.77, 37.12, 37.82, 205.00,
    208.73, 58.50, 198.00
]

temp_ubeh = [
    -107.4, -75, -69, -61.6, -55.5, -55.2, -54.3, -53.1,
    -49.1, -47.8, -47.7, -44.7, -44, -43, -41.8, -41.6,
    -41.4, -40.7, -39.8, -38, -36.0, -35, -34.2, -31.4,
    -30.5, -29.7, -29.4, -27.5, -26.9, -23.7, -21.1, -20.2,
    -19.5, -18.9, -9.4, -7.8, -4.6, -0.2, 6, 15.5, 18.8,
    20, 20, 20, 21.6, 22, 26.02, 27.4, 31.2, 34.2, 39.6,
    40.2, 51.3, 58.00, 65.3, 75.4, 76.5, 78.6, 80.50, 80.6,
    83.3
]

energi_ubeh = [
    3.66, 16.25, 8.52, 6.52, 34.83, 8.67, 6.96, 13.34,
    8.81, 57.13, 10.81, 18.77, 70, 109.85, 31.81, 151.19,
    19.29, 19.8, 18.23, 122.75, 128.84, 18.98, 61.99, 30.1,
    124.61, 141.02, 67.41, 91.69, 132.02, 125.25, 147.94,
    154.42, 139.04, 99.82, 174.47, 133.4, 150.38, 150.38,
    165.83, 211.37, 168.84, 172.76, 162.38, 220.76, 202.35,
    178.86, 83.96, 174.84, 214.19, 208.5, 234.7, 233.95,
    255.87, 154.13, 214, 172.58, 168.28, 218.66, 208.42,
    159.2, 211.79
]

# Finner felles størrelser for grafene
all_temp = temp_varme + temp_ubeh
all_energi = energi_varme + energi_ubeh

x_min, x_max = min(all_temp) - 5, max(all_temp) + 5
y_min, y_max = min(all_energi) - 10, max(all_energi) + 10

# Setter opp to subplots side om side med like dimensjoner
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharex=True, sharey=True)

# Plot 1: Varmebehandlet prøve
ax1.scatter(temp_varme, energi_varme, color='red')
# Trendlinje
z = np.polyfit(temp_varme, energi_varme, 1) 
p = np.poly1d(z)
ax1.plot(temp_varme, p(temp_varme), "y--", label="Linear Trend Line")

# Plot 2: Ubehandlet prøve
# Logistisk trendlinje
T = np.array(temp_ubeh)
E = np.array(energi_ubeh)
# Startgjetninger
p0 = [0, 220, 0.05, -25]

parametre, covariance = curve_fit(logistisk, T, E, p0=p0)

Emin, Emax, k, T0 = parametre

x = np.linspace(min(T), max(T), 500)
y = logistisk(x, *parametre)

# Plotter scatter og trenden
plt.scatter(T, E)
plt.plot(x, y, 'y-', linewidth=2)

# Grafikkfelt
# 1 varmebehandlet
ax1.set_title('Varmebehandlet prøve')
ax1.set_xlabel('Temperatur (°C)')
ax1.set_ylabel('Energi (J)')
ax1.set_xlim(x_min, x_max)
ax1.set_ylim(y_min, y_max)
ax1.grid(True, linestyle='--')
# 2 Ubehandlet
ax2.set_title('Ubehandlet prøve')
ax2.set_xlabel('Temperatur (°C)')
ax2.set_ylabel('Energi (J)')
ax2.set_xlim(x_min, x_max)
ax2.set_ylim(y_min, y_max)
ax2.grid(True, linestyle='--')

plt.tight_layout()
plt.show()