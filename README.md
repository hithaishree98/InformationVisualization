# InformationVisualization

Title: Visualization of Stock Market Trends: Analyzing Volume, Price, and Volatility of Amazon Stock
Introduction
This report aims to visualize key stock market trends of Amazon's stock by analyzing its trading volume, price movements, and volatility. The analysis leverages interactive visualizations to provide insights into relationships among various stock metrics.

Key Visualizations
The visualizations include scatter plots, stacked area charts, heatmaps, sunburst plots, and rolling mean/volatility plots. These plots, when combined, offer a comprehensive view of the stock's performance. The integration of these plots into a single dashboard enhances accessibility and allows for intuitive data exploration.

Main Visualization Components
1. Scatter Plot: Volume vs Close Price
This plot highlights the relationship between trading volume and the stock's closing price. It includes:

A regression line to indicate trends.
Annotations for maximum close price and trading volume.
An interactive range slider for date navigation.
2. Stacked Area Chart: Simulated Streamgraph
This chart visualizes price variations (Open, High, Low, Close) over time. Key features include:

Layered area plots for a streamgraph effect.
A range slider for easier temporal analysis.
3. Heatmap: Monthly Close Prices
The heatmap illustrates the average monthly closing prices over the years:

A pivot table aggregates data by month and year.
Annotations highlight the months with the highest and lowest average prices.
4. Sunburst Plot: Volume and Price Change Correlation
This hierarchical chart breaks down trading volumes by year and categories of price change (e.g., Significant Drop, Moderate Gain). The visualization provides:

Clear segmentation of trading volumes across price trends.
Color coding for intuitive analysis of price movements.
5. Rolling Mean and Volatility Plot
This plot reveals trends in the rolling mean of closing prices and volatility over a 30-day window:

Volatility peaks and drops are annotated for key insights.
Interactive features allow for detailed exploration of temporal patterns.
Methodology
Data Processing:
The dataset (AMZN.csv) is preprocessed by:

Parsing and resampling the date column for a consistent time series.
Computing derived metrics like percentage price change and rolling averages.
Visualization Tools:
The visualizations are built using Plotly for dynamic and interactive graphs. All plots adhere to a consistent dark theme for improved readability and aesthetics.

Combined Visualization Dashboard
A comprehensive dashboard integrates the above plots into a single interface with multiple panels:

Layout:

Row 1: Scatter Plot and Stacked Area Chart.
Row 2: Heatmap and Sunburst Plot.
Row 3: Rolling Mean and Volatility Plot.
Enhancements:

Titles and annotations for better context.
Unified interactivity across plots.
The dashboard, saved as combined_plots.html, offers a one-stop visualization suite for understanding Amazon stock trends.

Next Steps:
Further analysis could incorporate advanced machine learning techniques for predictive modeling or extend the dashboard to include comparisons with other stocks.

Code Implementation and Resources
The implementation uses Python with the following scripts:

plotting.py: Contains functions for each visualization.
data_processing.py: Handles data loading and preprocessing.
Main Script: Integrates individual visualizations into a unified dashboard.
For a detailed walkthrough, refer to the attached code files.

