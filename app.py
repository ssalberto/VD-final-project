#%%
import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
from constants import *
from load_data import *

 
#%%
def display_map_page():
    st.title("Cortes de Luz y Eventos Climáticos en EE. UU. - Mapa Interactivo")

    # Load data
    storm_data = load_storm_events_data()
    outage_data = load_eaglei_outages_data()

    # Sidebar selector for year (now a slider)
    available_years_map = sorted(list(set(storm_data['YEAR'].unique()) | set(outage_data['YEAR'].unique())))
    min_year_map, max_year_map = min(available_years_map), max(available_years_map)
    default_year_map = max_year_map 
    
    actual_selected_year = st.sidebar.selectbox(
        "Seleccionar Año", options=list(range(2014,2024)), key="map_year_selector",
    )
    
    selected_year_displayed = str(actual_selected_year) 
    
    color_metric_options_display = {
        "Total usuarios sin luz": "customers_out",
        "Total muertes": "DEATHS_DIRECT",
        "Total heridos": "INJURIES_DIRECT",
    }
    selected_color_metric_label_es = st.sidebar.selectbox(
        "Seleccionar Métrica para Color del Mapa", 
        options=list(color_metric_options_display),
        key="map_color_metric_selector"
    )
    
    data = load_data_page1()
    data = data[data['YEAR'] == actual_selected_year]
    inverse_map = {k: v for v, k in STATE_ABBR_TO_EN_NAME.items()}  # Reverse mapping for state names to abbreviations
    data['STATE_ABB'] = data['state'].map(inverse_map)  # Map state names to abbreviations

    if data.empty:
        st.warning(f"{UI_LABELS_ES['No data available for the selected year']}: {selected_year_displayed}. {UI_LABELS_ES['Please select a different year']}.")
        return

    fig = px.choropleth(
        data,
        locations='STATE_ABB',        
        locationmode='USA-states',
        color=color_metric_options_display[selected_color_metric_label_es],
        scope='usa',
        hover_name='state', 
        hover_data={ 
            "customers_out": True,
            "DEATHS_DIRECT": True,
            "INJURIES_DIRECT": True,
            'state': False
        },
        color_continuous_scale="Viridis",
        labels={selected_color_metric_label_es: selected_color_metric_label_es},
        title=f"{selected_color_metric_label_es} en {selected_year_displayed}"
    )
    fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)


def display_visualizations_page():
    st.title("Análisis")

    time_series = load_customers_data_for_time_series()
    print(time_series.head())
    
    all_states_es = sorted(time_series['state'].unique().tolist())
    all_years = sorted(time_series['run_start_time'].dt.year.unique().tolist())
    
    if not all_states_es:
        st.warning(f"{UI_LABELS_ES['No states found in the data']}. {UI_LABELS_ES['Please check the data sources']}.")
        return
    if not all_years:
        st.warning(f"{UI_LABELS_ES['No year data found']}. {UI_LABELS_ES['Please check the data sources']}.")
        return

    selected_state_es = st.selectbox("Selecciona el estado", options=all_states_es, index=0 if all_states_es else -1)
    
    min_year, max_year = int(min(all_years)), int(max(all_years))
    
    if min_year == max_year:
        selected_year_range = (min_year, max_year)
    else:
        selected_year_range = st.slider(
            "Seleccionar Rango de Años",
            min_value=min_year, max_value=max_year, 
            value=(min_year, max_year),
            key="year_range_selector_es"
        )

    start_year, end_year = selected_year_range


    filtered_data = time_series[
        (time_series['state'] == selected_state_es) &
        (time_series.run_start_time.dt.year >= start_year) &
        (time_series.run_start_time.dt.year <= end_year)
    ].copy()


    st.subheader("Usuarios sin luz diarios")
    if not filtered_data.empty:
        filtered_data['run_start_time'] = pd.to_datetime(filtered_data['run_start_time'])
        # Group by date and sum 'usuarios_sin_luz'
        daily_outages = filtered_data.groupby(filtered_data['run_start_time'].dt.date)['customers_out'].sum().reset_index()
        daily_outages.rename(columns={'run_start_time': "Fecha", 'customers_out': "Total de usuarios sin luz"}, inplace=True)
        
        if not daily_outages.empty:
            fig_outages = px.line(daily_outages, x="Fecha", y="Total de usuarios sin luz", 
                                    title=f"Total de usuarios con cortes en {selected_state_es} ({start_year}-{end_year})")
            st.plotly_chart(fig_outages, use_container_width=True)
        else:
            st.info(f"{UI_LABELS_ES['No outage data to display for']} {selected_state_es} {UI_LABELS_ES['between']} {start_year} {UI_LABELS_ES['and']} {end_year} {UI_LABELS_ES['after daily aggregation']}.")
    else:
        st.info(f"{UI_LABELS_ES['No outage data available for']} {selected_state_es} {UI_LABELS_ES['between']} {start_year} {UI_LABELS_ES['and']} {end_year}.")



# --- Page Configuration ---
PAGES = {
    "map_view": {
        "title": "Mapa Interactivo de EE. UU.",
        "function": lambda: display_map_page()
    },
    "visualizations_view": {
        "title": "Análsis a nivel de estado",
        "function": lambda: display_visualizations_page()
    },
}


def main():
    
    if 'current_page_key' not in st.session_state:
        st.session_state.current_page_key = "map_view" 
    if 'selected_state_abbreviation_from_map' not in st.session_state:
        st.session_state.selected_state_abbreviation_from_map = None

    st.sidebar.title("NAVEGACIÓN")
    
    selected_page_key_from_radio = st.sidebar.radio(
        "Ir a",
        options=list(PAGES.keys()),
        
        format_func=lambda page_key: PAGES[page_key]["title"],
        key='navigation_radio',
        index=list(PAGES.keys()).index(st.session_state.current_page_key) 
        
    )

    if selected_page_key_from_radio != st.session_state.current_page_key:
        st.session_state.current_page_key = selected_page_key_from_radio
        st.session_state.selected_state_abbreviation_from_map = None 
        st.rerun() 

    page_to_display_config = PAGES.get(st.session_state.current_page_key)

    if page_to_display_config:
        page_to_display_config["function"]()
    else:
        st.error("Página no encontrada.") 

if __name__ == "__main__":
    main()
