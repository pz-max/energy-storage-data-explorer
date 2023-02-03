# energy-storage-data-explorer

Little `streamlit` data explorer for energy storage data.
Application is required to analyse storage costs for Max's dissertation.

Data created by Pull Request:
- PyPSA-Earth: https://github.com/pypsa-meets-earth/pypsa-earth/pull/567
- Technology-data: https://github.com/PyPSA/technology-data/pull/67

Steps to get the `energy_storage_costs.csv` data:
1. Generate data from the Technology-data PR by running `compile_cost_assumptions.py`.
   Before running make sure `parzen_energy_storage: true` in the `config.yaml`
2. Move the technology-data outputs to PyPSA-Earth `resources/costs_<year>.csv`
3. Run the magic script in [Max's fork](https://github.com/pz-max/pypsa-earth/blob/storage-plot/scripts/plot_energy_storage.py`)
4. Move new created file `PyPSA-Earth/resources/energy_storage_costs.csv` to this explorer app `Data/energy_storage_costs.csv`

Thank you to all open-source contributors.

# License

Code is licensed as [MIT](https://opensource.org/licenses/MIT)
Data is licensed as [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
