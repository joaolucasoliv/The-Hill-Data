import pandas as pd
import matplotlib.pyplot as plt

# Hill summary (already computed in your script) 
hill_summary = {
    "Median Income (Age 35)": 24614.5,
    "Poverty Rate": 43.5,
    "Incarceration Rate": 5.6,
    "Single-Parent Households": 65.1,
    "Racial Composition (% Non-White)": 90.3
}

# U.S. averages 
us_avg = {
    "Median Income (Age 35)": 46645,
    "Poverty Rate": 13,
    "Incarceration Rate": 1.2,
    "Single-Parent Households": 30,
    "Racial Composition (% Non-White)": 40
}

# --- Normalize Hill values relative to U.S. = 100 ---
variables = list(hill_summary.keys())
hill_vals = [hill_summary[v] / us_avg[v] * 100 for v in variables]
us_vals = [100 for _ in variables]  # baseline

# --- Plot ---
x = range(len(variables))
bar_width = 0.35

fig, ax = plt.subplots(figsize=(10,6))
ax.bar([i - bar_width/2 for i in x], hill_vals, width=bar_width, label="The Hill (Relative to U.S.)", color="steelblue")
ax.bar([i + bar_width/2 for i in x], us_vals, width=bar_width, label="U.S. Average = 100", color="orange")

ax.set_xticks(x)
ax.set_xticklabels(variables, rotation=20, ha="right")
ax.set_ylabel("Relative Value (U.S. = 100)")
ax.set_title("The Hill vs. U.S.: Normalized Comparison")
ax.legend()

plt.tight_layout()
plt.show()
