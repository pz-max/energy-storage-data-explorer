import streamlit as st
import pandas as pd
import plotly.express as px


# Load data
df_storage = pd.read_csv('Data/energy_storage_costs.csv')

# Create plot
fig_cc = px.scatter_3d(
    df_storage,
    x='Charger capital costs [EUR/kW]',
    y='Discharger capital costs [EUR/kW]',
    z='Store capital costs [EUR/kWh]',
    size='efficiency',
    color='type',
    symbol='technology',
    hover_data=['year']
)

fig_ic = px.scatter_3d(
    df_storage,
    x='Charger investment costs [EUR/kW]',
    y='Discharger investment costs [EUR/kW]',
    z='Store investment costs [EUR/kWh]',
    size='efficiency',
    color='type',
    symbol='technology',
    hover_data=['year']
)

# Plot!
tab1, tab2 = st.tabs(["Capital costs", "Investment costs"])
with tab1:
    # Capital costs
    st.plotly_chart(fig_cc, theme="streamlit", use_container_width=True)
with tab2:
    # Investment costs
    st.plotly_chart(fig_ic, theme="streamlit", use_container_width=True)