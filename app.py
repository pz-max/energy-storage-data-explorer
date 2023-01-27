import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df_storage = pd.read_csv('Data/energy_storage_costs.csv')

# Create plot
fig_cc = px.scatter_3d(
    df_storage,
    x='Charger [EUR/kW]_cc',
    y='Discharger [EUR/kW]_cc',
    z='Store [EUR/kWh]_cc',
    size='efficiency',
    color='type',
    symbol='technology',
    hover_data=['year']
)

fig_ic = px.scatter_3d(
    df_storage,
    x='Charger [EUR/kW]_ic',
    y='Discharger [EUR/kW]_ic',
    z='Store [EUR/kWh]_ic',
    size='efficiency',
    color='type',
    symbol='technology',
    hover_data=['year']
)

# Plot!
st.title('19 energy storage technologies by Max Parzen')
tab1, tab2 = st.tabs(["Capital costs", "Investment costs"])
with tab1:
    # Capital costs
    st.title('Capital costs')
    st.plotly_chart(fig_cc, theme="streamlit", use_container_width=True)
with tab2:
    # Investment costs
    st.title('Investment costs')
    st.plotly_chart(fig_ic, theme="streamlit", use_container_width=True)