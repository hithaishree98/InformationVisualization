import os
from data_processing import load_and_process_data
from plotting import scatter_plot, stacked_area_plot, heatmap_plot, sunburst_correlation_plot, rolling_mean_volatility_plot

# Load and process data
df_resampled = load_and_process_data("AMZN.csv")  # Replace with your actual CSV file path

# Create individual plots
fig_scatter = scatter_plot(df_resampled)
fig_streamgraph = stacked_area_plot(df_resampled)
fig_heatmap = heatmap_plot(df_resampled)
fig_corr = sunburst_correlation_plot(df_resampled)
fig_rolling = rolling_mean_volatility_plot(df_resampled)

# Define the directory to save the files (same directory as main.py)
save_dir = os.path.dirname(os.path.realpath(__file__))

# Save each figure as an HTML file (interactive), overwrite if file exists
fig_scatter.write_html(os.path.join(save_dir, 'scatter_plot.html'))
fig_streamgraph.write_html(os.path.join(save_dir, 'stacked_area_plot.html'))
fig_heatmap.write_html(os.path.join(save_dir, 'heatmap_plot.html'))
fig_corr.write_html(os.path.join(save_dir, 'sunburst_plot.html'))
fig_rolling.write_html(os.path.join(save_dir, 'rolling_mean_volatility_plot.html'))

# Optionally, save as static images (PNG), overwrite if file exists
fig_scatter.write_image(os.path.join(save_dir, 'scatter_plot.png'))
fig_streamgraph.write_image(os.path.join(save_dir, 'stacked_area_plot.png'))
fig_heatmap.write_image(os.path.join(save_dir, 'heatmap_plot.png'))
fig_corr.write_image(os.path.join(save_dir, 'sunburst_plot.png'))
fig_rolling.write_image(os.path.join(save_dir, 'rolling_mean_volatility_plot.png'))

print("Plots saved successfully!")
