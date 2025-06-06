# --- Localization Dictionaries (Spanish) ---

STATE_ABBR_TO_STATE_FIPS = {
    'AL': '01', 'AK': '02', 'AZ': '04', 'AR': '05', 'CA': '06', 'CO': '08', 'CT': '09', 'DE': '10',
    'FL': '12', 'GA': '13', 'HI': '15', 'ID': '16', 'IL': '17', 'IN': '18', 'IA': '19', 'KS': '20',
    'KY': '21', 'LA': '22', 'ME': '23', 'MD': '24', 'MA': '25', 'MI': '26', 'MN': '27', 'MS': '28',
    'MO': '29', 'MT': '30', 'NE': '31', 'NV': '32', 'NH': '33', 'NJ': '34', 'NM': '35', 'NY': '36',
    'NC': '37', 'ND': '38', 'OH': '39', 'OK': '40', 'OR': '41', 'PA': '42', 'RI': '44', 'SC': '45',
    'SD': '46', 'TN': '47', 'TX': '48', 'UT': '49', 'VT': '50', 'VA': '51', 'WA': '53', 'WV': '54',
    'WI': '55', 'WY': '56', 'DC': '11', 'PR': '72'
}

STATE_ABBR_TO_EN_NAME = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
    'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota',
    'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island',
    'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas',
    'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia',
    'WI': 'Wisconsin', 'WY': 'Wyoming', 'COUNTY1': 'County1', 'COUNTY2': 'County2',
    'COUNTY_OUTAGE_0': 'County Outage 0', 'COUNTY_OUTAGE_1': 'County Outage 1',
    **{f'COUNTY{i}': f'County{i}' for i in range(50)},
    **{f'COUNTY_OUTAGE_{i}': f'County Outage {i}' for i in range(20)},
}

EVENT_TYPE_TO_ES = {
    'Tornado': 'Tornado', 'Hurricane': 'Huracán', 'Hail': 'Granizo', 'Flood': 'Inundación',
    'Wildfire': 'Incendio Forestal', 'Blizzard': 'Ventisca', 'Drought': 'Sequía',
    'Earthquake': 'Terremoto', 'Winter Storm': 'Tormenta de Invierno',
    'Thunderstorm Wind': 'Viento de Tormenta', 'Heat Wave': 'Ola de Calor',
    'Heavy Rain': 'Lluvia Intensa', 'High Wind': 'Viento Fuerte', 'Dust Storm': 'Tormenta de Polvo'
}

MONTH_NAME_TO_ES = {
    'January': 'Enero', 'February': 'Febrero', 'March': 'Marzo', 'April': 'Abril',
    'May': 'Mayo', 'June': 'Junio', 'July': 'Julio', 'August': 'Agosto',
    'September': 'Septiembre', 'October': 'Octubre', 'November': 'Noviembre', 'December': 'Diciembre'
}

UI_LABELS_ES = {
    # General
    "Navigation": "Navegación",
    "Go to": "Ir a",
    "All Years": "Todos los Años",
    "Select Year": "Seleccionar Año",
    "Select State": "Seleccionar Estado",
    "Select Metric for Map Color": "Seleccionar Métrica para Color del Mapa",
    "No data available for the selected year": "No hay datos disponibles para el año seleccionado",
    "Please select a different year": "Por favor, seleccione un año diferente.",
    "No states found in the data": "No se encontraron estados en los datos",
    "Please check the data sources": "Por favor, verifique las fuentes de datos.",
    "No year data found": "No se encontraron datos de año",
    "Data is only available for the year": "Los datos solo están disponibles para el año",
    "Displaying data for this year": "Mostrando datos para este año.",
    "Select Year Range": "Seleccionar Rango de Años",
    "No outage data available for": "No hay datos de apagones disponibles para",
    "between": "entre",
    "and": "y",
    "after daily aggregation": "después de la agregación diaria.",
    "No storm event data available for": "No hay datos de eventos de tormenta disponibles para",
    "after counting": "después de contar.",
     "No outage data to display for": "No hay datos de apagones para mostrar para",
    "No storm event types to display for": "No hay tipos de eventos de tormenta para mostrar para",
    "No outage data available for {state} in {year}": "No hay datos de apagones disponibles para {state} en {year}.", # Placeholder for format
    "No outage data to display for counties in {state} for {year} after aggregation.": "No hay datos de apagones para mostrar para los condados en {state} para {year} después de la agregación.",


    # Page Titles
    "US Power Outages and Weather Events Dashboard": "Dashboard de Apagones y Eventos Climáticos en EE. UU.",
    "Interactive US Map": "Mapa Interactivo de EE. UU.",
    "State-Level Analysis": "Análisis a Nivel Estatal",
    "Visualizations": "Visualizaciones", # Kept if used as a direct page name
    "County View": "Vista por Condado",
    "County-Level Power Outages": "Apagones a Nivel de Condado",

    # Metrics / Columns
    "Total Customers Out": "Total de Usuarios Sin Luz",
    "Total Events": "Eventos Totales",
    "Total Deaths": "Muertes Totales",
    "Total Injuries": "Lesiones Totales",
    "Most Frequent Event Type": "Tipo de Evento Más Frecuente",
    "Event Type": "Tipo de Evento",
    "Count": "Cantidad",
    "Date": "Fecha",
    "County": "Condado",
    "Correlation Coefficient": "Coeficiente de Correlación",

    # Specific Chart elements
    "Aggregated Data for": "Datos Agregados para",
    "Ver detalles por condado": "Ver detalles por condado", # For map page navigation section
    "Seleccionar Estado para detalles": "Seleccionar Estado para detalles:", # For map page navigation selectbox
    "Ir a la Vista de Condado": "Ir a la Vista de Condado", # For map page navigation button
    "Error al obtener abreviatura": "Error al obtener abreviatura del estado.",
    "No hay estados disponibles en los datos del mapa para la navegación.": "No hay estados disponibles en los datos del mapa para la navegación.",
    "Datos de estado no disponibles para la navegación.": "Datos de estado no disponibles para la navegación.",
    "MapClickIdealSolutionComment": "Idealmente, hacer clic directamente en un estado en el mapa navegaría a la vista del condado. Esto requeriría una configuración más avanzada con `event_data` de `st.plotly_chart` o un componente personalizado de Streamlit.",
    "Página no encontrada.": "Página no encontrada.",
    "Error determinando abreviatura estado": "No se pudo determinar la abreviatura del estado para filtrar. Verifique los mapeos.",
    "Cannot display County View": "No se puede mostrar la Vista por Condado", # For display_county_page warning
    "Daily Power Outages (Customers Out)": "Apagones Diarios (Usuarios Sin Luz)",
    "Daily Outages in": "Apagones Diarios en",
    "Weather Event Types Frequency": "Frecuencia de Tipos de Eventos Climáticos",
    "Event Frequencies in": "Frecuencias de Eventos en",
    "Power Outages by County in": "Apagones por Condado en",
    "Total Customers Out by County": "Total de Usuarios Sin Luz por Condado",
}

