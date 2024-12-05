import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from scipy import stats

def scatter_plot(df_resampled):
    # Scatter plot: Volume vs Close Price
    fig = px.scatter(df_resampled, x='Volume', y='Close', 
                     title="Volume vs Close Price", 
                     labels={'Volume': 'Trading Volume', 'Close': 'Close Price'})

    # Add regression line using scipy
    slope, intercept, r_value, p_value, std_err = stats.linregress(df_resampled['Volume'], df_resampled['Close'])
    fig.add_trace(go.Scatter(x=df_resampled['Volume'], 
                             y=slope * df_resampled['Volume'] + intercept, 
                             mode='lines', name='Regression Line', line=dict(color='red', dash='dot')))

    # Add min/max annotations
    max_volume_idx = df_resampled['Volume'].idxmax()
    max_close = df_resampled['Close'].max()
    fig.add_annotation(
        x=max_volume_idx, y=max_close,
        text=f"Max Close: {max_close:.2f}",
        showarrow=True, arrowhead=2
    )
    fig.add_annotation(
        x=max_volume_idx, y=df_resampled['Volume'].max(),
        text=f"Max Volume: {df_resampled['Volume'].max():.0f}",
        showarrow=True, arrowhead=2
    )

    # Adding the range slider for interactivity
    fig.update_layout(
        title="Volume vs Close Price",
        xaxis_title="Trading Volume",
        yaxis_title="Close Price",
        template="plotly_dark",
        showlegend=True,
        xaxis_rangeslider_visible=True,  # Range slider for date navigation
    )

    return fig

def stacked_area_plot(df_resampled):
    # Prepare data for the streamgraph-like effect
    df_streamgraph = df_resampled[['Open', 'High', 'Low', 'Close']].copy()

    # Create a stacked area chart with Plotly
    fig = go.Figure()

    # Add each stream (Open, High, Low, Close) as stacked areas
    for column in df_streamgraph.columns:
        fig.add_trace(go.Scatter(
            x=df_streamgraph.index,
            y=df_streamgraph[column],
            mode='none',  # Hide line
            fill='tonexty',  # Fill area to next trace
            name=column,
            stackgroup='one',  # Stack all traces in the same group
            line=dict(color='rgba(0, 0, 0, 0)')  # Invisible line
        ))

    # Adding the range slider for better navigation
    fig.update_layout(
        title="Simulated Streamgraph (Stacked Area Chart)",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_dark",
        showlegend=True,
        xaxis_rangeslider_visible=True,  # Range slider for date navigation
    )

    return fig

def heatmap_plot(df_resampled):
    # Extract 'Month' and 'Year' from the 'Date' column (assuming 'Date' is in datetime format)
    df_resampled['Month'] = df_resampled.index.month
    df_resampled['Year'] = df_resampled.index.year

    # Pivot the table to prepare for the heatmap
    df_pivot = df_resampled.pivot_table(index='Month', columns='Year', values='Close', aggfunc='mean')

    # Create and return the heatmap plot
    fig = px.imshow(df_pivot,
                     title="Monthly Close Price Heatmap",
                     labels={'x': 'Year', 'y': 'Month', 'color': 'Close Price'},
                     color_continuous_scale='Viridis')

    # Check for the existence of the maximum and minimum values
    if not df_pivot.empty:
        max_price = df_pivot.max().max()
        min_price = df_pivot.min().min()

        # Add annotations for min/max
        max_price_idx = df_pivot.stack().idxmax()
        min_price_idx = df_pivot.stack().idxmin()

        fig.add_annotation(
            x=max_price_idx[1], y=max_price_idx[0],
            text=f"Max Price: {max_price:.2f}",
            showarrow=True, arrowhead=2
        )

        fig.add_annotation(
            x=min_price_idx[1], y=min_price_idx[0],
            text=f"Min Price: {min_price:.2f}",
            showarrow=True, arrowhead=2
        )

    fig.update_layout(
        title="Monthly Close Price Heatmap",
        xaxis_title="Year",
        yaxis_title="Month",
        template="plotly_dark",
        coloraxis_colorbar_title="Avg Close Price",
        showlegend=False
    )

    return fig

def sunburst_correlation_plot(df_resampled):
    # Simplify the hierarchy by aggregating the data yearly and focusing on price changes and volume

    # Add 'Price Change' column to show price change over time
    df_resampled['Price Change'] = df_resampled['Close'].pct_change() * 100  # Percentage change
    
    # We could add "Month" or "Year" for a simpler view
    df_resampled['Year'] = df_resampled.index.year
    df_resampled['Month'] = df_resampled.index.month_name()

    # Create categories based on Year and Price Change
    df_resampled['Price Category'] = pd.cut(df_resampled['Price Change'], 
                                            bins=[-float('inf'), -2, 0, 2, float('inf')],
                                            labels=['Significant Drop', 'Moderate Drop', 'Moderate Gain', 'Significant Gain'])

    # Convert 'Price Category' to a categorical type without using observed=False (removed deprecated argument)
    df_resampled['Price Category'] = pd.Categorical(df_resampled['Price Category'])
    
    # Aggregating the data by Year and Price Category to reduce clutter
    df_aggregated = df_resampled.groupby(['Year', 'Price Category']).agg({'Volume': 'sum'}).reset_index()

    # Now, we create the sunburst plot
    fig = px.sunburst(df_aggregated,
                      path=['Year', 'Price Category'],  # Hierarchy: Year -> Price Category
                      values='Volume',  # Value to visualize (e.g., total Volume)
                      color='Price Category',  # Color based on Price Category
                      title="Yearly Volume Breakdown by Price Change Category",
                      color_discrete_map={ 
                          'Significant Drop': 'red',
                          'Moderate Drop': 'orange',
                          'Moderate Gain': 'yellow',
                          'Significant Gain': 'green'
                      })

    fig.update_layout(
        title="Stock Price Change and Volume Correlation (Sunburst)",
        template="plotly_dark",
        showlegend=True
    )

    return fig

def rolling_mean_volatility_plot(df_resampled):
    # Create 'Price Range' column
    df_resampled['Price Range'] = df_resampled['High'] - df_resampled['Low']

    # Rolling mean and volatility plot
    df_resampled['Rolling Mean'] = df_resampled['Close'].rolling(window=30).mean()
    df_resampled['Rolling Volatility'] = df_resampled['Price Range'].rolling(window=30).mean()

    fig = go.Figure()

    # Add Rolling Mean trace
    fig.add_trace(go.Scatter(x=df_resampled.index, y=df_resampled['Rolling Mean'], 
                            mode='lines', name='30-Day Rolling Mean', line=dict(color='blue')))

    # Add Rolling Volatility trace
    fig.add_trace(go.Scatter(x=df_resampled.index, y=df_resampled['Rolling Volatility'], 
                            mode='lines', name='30-Day Rolling Volatility', line=dict(color='red', dash='dot')))

    # Highlight significant peaks and drops
    max_volatility = df_resampled['Rolling Volatility'].max()
    min_volatility = df_resampled['Rolling Volatility'].min()
    max_volatility_date = df_resampled['Rolling Volatility'].idxmax()
    min_volatility_date = df_resampled['Rolling Volatility'].idxmin()

    fig.add_annotation(
        x=max_volatility_date, y=max_volatility,
        text=f"Max Volatility: {max_volatility:.2f}",
        showarrow=True, arrowhead=2
    )
    fig.add_annotation(
        x=min_volatility_date, y=min_volatility,
        text=f"Min Volatility: {min_volatility:.2f}",
        showarrow=True, arrowhead=2
    )

    # Adding the range slider for better navigation
    fig.update_layout(
        title="Rolling Mean and Volatility of Stock Prices",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_dark",
        showlegend=True,
        xaxis_rangeslider_visible=True,  # Range slider for date navigation
    )

    return fig

