from plotly.subplots import make_subplots
from plotting import scatter_plot, stacked_area_plot, heatmap_plot, sunburst_correlation_plot, rolling_mean_volatility_plot
from data_processing import load_and_process_data
import plotly.graph_objects as go
import os

# Load and process data
df_resampled = load_and_process_data("AMZN.csv")  # Replace with your actual CSV file path

# Create individual plots
fig_scatter = scatter_plot(df_resampled)
fig_streamgraph = stacked_area_plot(df_resampled)
fig_heatmap = heatmap_plot(df_resampled)
fig_corr = sunburst_correlation_plot(df_resampled)
fig_rolling = rolling_mean_volatility_plot(df_resampled)

# Define the directory to save the files
save_dir = os.path.dirname(os.path.realpath(__file__))

# Save each individual plot (HTML and PNG)
fig_scatter.write_html(os.path.join(save_dir, 'scatter_plot.html'))
fig_streamgraph.write_html(os.path.join(save_dir, 'stacked_area_plot.html'))
fig_heatmap.write_html(os.path.join(save_dir, 'heatmap_plot.html'))
fig_corr.write_html(os.path.join(save_dir, 'sunburst_plot.html'))
fig_rolling.write_html(os.path.join(save_dir, 'rolling_mean_volatility_plot.html'))

# fig_scatter.write_image(os.path.join(save_dir, 'scatter_plot.png'))
# fig_streamgraph.write_image(os.path.join(save_dir, 'stacked_area_plot.png'))
# fig_heatmap.write_image(os.path.join(save_dir, 'heatmap_plot.png'))
# fig_corr.write_image(os.path.join(save_dir, 'sunburst_plot.png'))
# fig_rolling.write_image(os.path.join(save_dir, 'rolling_mean_volatility_plot.png'))

# Create a combined figure with subplots
combined_fig = make_subplots(
    rows=3, cols=2,  # Define the grid layout
    subplot_titles=[
        "Scatter Plot", "Streamgraph",
        "Heatmap", "Sunburst Plot",
        "Rolling Mean and Volatility"
    ],
    specs=[
        [{"type": "xy"}, {"type": "xy"}],
        [{"type": "heatmap"}, {"type": "domain"}],
        [{"type": "xy"}, None]
    ],
)

# Add each individual plot to the combined figure
combined_fig.add_traces(fig_scatter.data, rows=1, cols=1)
combined_fig.add_traces(fig_streamgraph.data, rows=1, cols=2)
combined_fig.add_traces(fig_heatmap.data, rows=2, cols=1)
combined_fig.add_traces(fig_corr.data, rows=2, cols=2)
combined_fig.add_traces(fig_rolling.data, rows=3, cols=1)

# Update layout of the combined figure
combined_fig.update_layout(
    title="Integrated Visualizations",
    template="plotly_dark",
    height=1200,  # Adjust height for better readability
    showlegend=False,  # Disable legend for combined figure
)

# Save the combined figure
combined_fig.write_html(os.path.join(save_dir, 'combined_plots.html'))


print("All plots saved successfully!")
