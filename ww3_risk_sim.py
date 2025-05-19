# Advanced Geopolitical Conflict Risk Simulator - Interactive Web Dashboard with Timeline Simulation

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define risk calculation function
def calculate_conflict_risk(GTI, TWSI, MBR, AFS, EDS, EVI):
    beta_0 = 1
    beta_1 = 0.05
    beta_2 = 0.10
    beta_3 = 0.07
    beta_4 = 0.04
    beta_5 = 0.06
    beta_6 = 0.08

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

# Country presets for individual tracking
def country_scenario(country):
    scenarios = {
        "United States": {"GTI": 130, "TWSI": 0.7, "MBR": 0.07, "AFS": 2, "EDS": 0.6, "EVI": 0.6},
        "China": {"GTI": 140, "TWSI": 0.8, "MBR": 0.08, "AFS": 2, "EDS": 0.9, "EVI": 0.7},
        "Russia": {"GTI": 135, "TWSI": 0.6, "MBR": 0.08, "AFS": 3, "EDS": 0.85, "EVI": 0.8},
        "European Union": {"GTI": 125, "TWSI": 0.5, "MBR": 0.05, "AFS": 1, "EDS": 0.7, "EVI": 0.6},
        "India": {"GTI": 120, "TWSI": 0.4, "MBR": 0.06, "AFS": 1, "EDS": 0.8, "EVI": 0.7},
        "Middle East": {"GTI": 130, "TWSI": 0.5, "MBR": 0.07, "AFS": 2, "EDS": 0.9, "EVI": 0.8}
    }
    return scenarios.get(country, scenarios["United States"])

# Streamlit web app
st.title("🌍 WW3 Geopolitical Risk Simulator")
st.markdown("Adjust variables or select a scenario to simulate conflict risk.")

# Scenario selection
preset = st.selectbox("Choose a Scenario Preset:", [
    "Custom", "Trade War Escalation", "Energy Crisis", "Cyber Conflict", "Calm Recovery", "Sanctions Spiral", "Alliance Breakdown", "Global Recovery", "Climate Shock Conflict"
])

# Scenario presets
def scenario_preset(preset):
    presets = {
        "Trade War Escalation": {"GTI": 130, "TWSI": 0.7, "MBR": 0.07, "AFS": 2, "EDS": 0.8, "EVI": 0.7},
        "Energy Crisis": {"GTI": 125, "TWSI": 0.4, "MBR": 0.05, "AFS": 1, "EDS": 0.9, "EVI": 0.8},
        "Cyber Conflict": {"GTI": 120, "TWSI": 0.5, "MBR": 0.06, "AFS": 2, "EDS": 0.7, "EVI": 0.6},
        "Calm Recovery": {"GTI": 110, "TWSI": 0.3, "MBR": 0.04, "AFS": 0, "EDS": 0.6, "EVI": 0.5},
        "Sanctions Spiral": {"GTI": 135, "TWSI": 0.8, "MBR": 0.07, "AFS": 2, "EDS": 0.85, "EVI": 0.75},
        "Alliance Breakdown": {"GTI": 140, "TWSI": 0.6, "MBR": 0.07, "AFS": 3, "EDS": 0.8, "EVI": 0.8},
        "Global Recovery": {"GTI": 105, "TWSI": 0.2, "MBR": 0.03, "AFS": 0, "EDS": 0.5, "EVI": 0.4},
        "Climate Shock Conflict": {"GTI": 135, "TWSI": 0.5, "MBR": 0.06, "AFS": 2, "EDS": 0.95, "EVI": 0.85}
    }
    return presets.get(preset, {"GTI": 120, "TWSI": 0.4, "MBR": 0.05, "AFS": 1, "EDS": 0.7, "EVI": 0.6})

scenario = scenario_preset(preset)

# Sliders for custom adjustments
GTI = st.slider("Geopolitical Tension Index (100–150)", 100, 150, int(scenario["GTI"]))
TWSI = st.slider("Trade War Severity Index (0–1)", 0.0, 1.0, float(scenario["TWSI"]))
MBR = st.slider("Military Build-up Rate (0.03–0.08)", 0.03, 0.08, float(scenario["MBR"]))
AFS = st.slider("Alliance Fragmentation Score (0–3)", 0, 3, int(scenario["AFS"]))
EDS = st.slider("Energy Dependency Score (0–1)", 0.0, 1.0, float(scenario["EDS"]))
EVI = st.slider("Economic Vulnerability Index (0–1)", 0.0, 1.0, float(scenario["EVI"]))

# Calculate overall risk
risk = calculate_conflict_risk(GTI, TWSI, MBR, AFS, EDS, EVI)
st.metric(label="Estimated Conflict Risk", value=f"{risk:.2f}%")

# Country-level risk tracking
st.subheader("Country-by-Country Risk Profiles")
countries = ["United States", "China", "Russia", "European Union", "India", "Middle East"]
country_risks = {}
for country in countries:
    factors = country_scenario(country)
    country_risks[country] = calculate_conflict_risk(**factors)

country_df = pd.DataFrame.from_dict(country_risks, orient='index', columns=['Conflict Risk (%)'])
st.table(country_df)

# Plot country risks
fig, ax = plt.subplots()
country_df['Conflict Risk (%)'].plot(kind='bar', color='orange', ax=ax)
plt.ylabel('Conflict Risk (%)')
plt.title('Country Risk Comparison')
st.pyplot(fig)

# Risk Timeline Simulation
st.subheader("📈 Risk Evolution Over Time (2025–2035)")
years = list(range(2025, 2036))
timeline_data = []

# Generate simulated yearly risk data
for year in years:
    fluctuation = np.random.normal(1, 0.02, 6)
    yearly_risk = calculate_conflict_risk(
        GTI * fluctuation[0],
        TWSI * fluctuation[1],
        MBR * fluctuation[2],
        AFS * fluctuation[3],
        EDS * fluctuation[4],
        EVI * fluctuation[5]
    )
    timeline_data.append(yearly_risk)

timeline_df = pd.DataFrame({"Year": years, "Conflict Risk (%)": timeline_data})

# Plot the timeline
fig2, ax2 = plt.subplots()
ax2.plot(timeline_df["Year"], timeline_df["Conflict Risk (%)"], marker='o', color='orange')
ax2.set_xlabel("Year")
ax2.set_ylabel("Conflict Risk (%)")
ax2.set_title("Simulated Conflict Risk Timeline (2025–2035)")
ax2.grid(True)
st.pyplot(fig2)

# Export option
if st.button("Export Scenario to Excel"):
    export_df = pd.DataFrame([{
        "GTI": GTI, "TWSI": TWSI, "MBR": MBR, "AFS": AFS,
        "EDS": EDS, "EVI": EVI, "Overall Risk (%)": risk
    }])
    export_df.to_excel("Conflict_Risk_Scenario.xlsx", index=False)
    timeline_df.to_excel("Conflict_Risk_Timeline.xlsx", index=False)
    st.success("Scenario and timeline exported to Excel!")

st.markdown("---")
st.caption("Developed for advanced geopolitical risk analysis and scenario planning.")
