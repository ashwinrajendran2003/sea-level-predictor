import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# Load data
df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data", color="blue")

    # Perform first linear regression for all data
    slope_all, intercept_all, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred_all = intercept_all + slope_all * years_extended
    ax.plot(years_extended, sea_level_pred_all, color="red", label="Best Fit Line (1880-2050)")

    # Perform second linear regression for data from 2000 onwards
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_extended_recent = pd.Series(range(2000, 2051))
    sea_level_pred_recent = intercept_recent + slope_recent * years_extended_recent
    ax.plot(years_extended_recent, sea_level_pred_recent, color="green", label="Best Fit Line (2000-2050)")

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # Save and return plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()
