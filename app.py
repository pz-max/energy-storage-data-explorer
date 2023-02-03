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
st.title('20 energy storage technologies between 2020-2050')
st.markdown(
    "WORK IN PROGRESS. VALIDATION NEEDED. \n\n"
    
    "The total costs of an energy storage is the sum of charger, \n"
    "discharger and store cost. Instead of lumping these costs together \n"
    "the 3D image breaks it down. The overnight 'capital costs' are annualised to net present \n"
    "investment costs with a discount rate over the economic lifetime \n"
    "using the annuity factor.\n\n"
    "The capital cost equation is documented in [PyPSA](https://pypsa-eur.readthedocs.io/en/latest/costs.html#cost-assumptions) \n"
    "To reproduce the data, checkout the [GitHub](https://github.com/pz-max/energy-storage-data-explorer#energy-storage-data-explorer) \n"
    "Goal of the data is to apply the data to energy system models. \n\n"
    "Reach out to [Max Parzen](https://www.linkedin.com/in/maximilian-parzen-b047a1126/) \n"
    "for questions or enquiries. Thanks to the [PyPSA community](https://pypsa-meets-earth.github.io/projects.html)! \n "
)
tab1, tab2 = st.tabs(["Investment costs", "Capital costs"])
with tab1:
    # Investment costs
    st.title('Investment costs')
    st.plotly_chart(fig_ic, theme="streamlit", use_container_width=True)
with tab2:
    # Capital costs
    st.title('Capital costs')
    st.plotly_chart(fig_cc, theme="streamlit", use_container_width=True)
