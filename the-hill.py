import polars as pl
import matplotlib.pyplot as plt

# I used Opportunity Atlas data for this tool 

# Hill summary (already computed in your script) 
hill_summary = pl.DataFrame({
    "Variable": [
        "Median Income (Age 35)", 
        "Poverty Rate", 
        "Incarceration Rate", 
        "Single-Parent Households", 
        "Racial Composition (% Non-White)"
    ],
    "Value": [24614.5, 43.5, 5.6, 65.1, 90.3]  # Ensure all values are floats
})

# U.S. averages 
us_avg = pl.DataFrame({
    "Variable": [
        "Median Income (Age 35)", 
        "Poverty Rate", 
        "Incarceration Rate", 
        "Single-Parent Households", 
        "Racial Composition (% Non-White)"
    ],
    "Value": [46645.0, 13.0, 1.2, 30.0, 40.0]  # Explicitly cast all values to floats
})

# Normalize Hill values relative to U.S. = 100 
normalized = hill_summary.join(us_avg, on="Variable", how="inner").with_columns(
    (pl.col("Value") / pl.col("Value_right") * 100).alias("Normalized Value")
)

variables = normalized["Variable"].to_list()
hill_vals = normalized["Normalized Value"].to_list()
us_vals = [100 for _ in variables]  # baseline

# Plot 
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