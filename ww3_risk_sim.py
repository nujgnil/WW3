# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

# Define base risk calculation function
def calculate_conflict_risk(GTI, TWSI, MBR, AFS, EDS, EVI):
    # Coefficients based on risk model
    beta_0 = 1  # Baseline risk %
    beta_1 = 0.05  # Geopolitical tension
    beta_2 = 0.10  # Trade war severity
    beta_3 = 0.07  # Military build-up
    beta_4 = 0.04  # Alliance fragmentation
    beta_5 = 0.06  # Energy dependency
    beta_6 = 0.08  # Economic vulnerability

    # Risk calculation
    risk = (
        beta_0 + 
        beta_1 * GTI + 
        beta_2 * TWSI + 
        beta_3 * MBR + 
        beta_4 * AFS + 
        beta_5 * EDS + 
        beta_6 * EVI
    )

    return risk

# Simulate scenarios
scenarios = 50
np.random.seed(42)

# Generate random values for each parameter within reasonable ranges
GTI_values = np.random.uniform(100, 150, scenarios)  # GPR Index ~100-150
TWSI_values = np.random.uniform(0.2, 0.7, scenarios)  # Trade war severity 20%-70%
MBR_values = np.random.uniform(0.03, 0.08, scenarios)  # Military build-up 3%-8%
AFS_values = np.random.randint(0, 4, scenarios)  # Alliance fragmentation (0-3 major events)
EDS_values = np.random.uniform(0.5, 0.9, scenarios)  # Energy dependency
EVI_values = np.random.uniform(0.4, 0.8, scenarios)  # Economic vulnerability

# Calculate risks for all scenarios
risks = []
for i in range(scenarios):
    risk = calculate_conflict_risk(
        GTI_values[i],
        TWSI_values[i],
        MBR_values[i],
        AFS_values[i],
        EDS_values[i],
        EVI_values[i]
    )
    risks.append(risk)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(range(1, scenarios + 1), risks, marker='o')
plt.title('Simulated Conflict Risk Scenarios')
plt.xlabel('Scenario Number')
plt.ylabel('Conflict Risk (%)')
plt.grid(True)
plt.show()

# Print some sample outputs
for i in range(5):
    print(f"Scenario {i+1}: GTI={GTI_values[i]:.1f}, TWSI={TWSI_values[i]:.2f}, MBR={MBR_values[i]:.3f}, AFS={AFS_values[i]}, EDS={EDS_values[i]:.2f}, EVI={EVI_values[i]:.2f} => Risk={risks[i]:.2f}%")
