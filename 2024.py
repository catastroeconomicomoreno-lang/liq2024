import os
import streamlit as st

# ==============================================================================
# CONFIGURACIÓN DE PARÁMETROS - VERSIÓN 2024
# ==============================================================================

TITULO_APP = "LIQUIDADOR TASAS POR SERVICIOS GENERALES - EJERCICIO 2024"

FACTOR_TERRENO_HASTA_10000 = 5
FACTOR_TERRENO_MAS_10000 = 5
FACTOR_EDIFICADO = 100
VALOR_M2_PROTOTIPICO = 382.45

TABLA_BASE_IMPONIBLE = [
    (1800000.0, 0.0, 29520.00, 0.0),
    (2025000.0, 1800000.0, 29520.00, 0.0150),
    (2295000.0, 2025000.0, 33682.50, 0.0152),
    (2565000.0, 2295000.0, 38812.50, 0.0154),
    (4050000.0, 2565000.0, 44010.00, 0.0156),
    (6750000.0, 4050000.0, 89842.50, 0.0160),
    (9450000.0, 6750000.0, 177592.50, 0.0164),
    (12150000.0, 9450000.0, 229567.50, 0.0169),
    (14850000.0, 12150000.0, 300105.00, 0.0170),
    (float("inf"), 14850000.0, 357480.00, 0.0172),
]

PORCENTAJES_AUMENTO = [
    0.0,  # Cuota 1
    0.0,  # Cuota 2
    0.0,  # Cuota 3
    19.66,  # Cuota 4
    19.66,  # Cuota 5
    19.66,  # Cuota 6
    12.50,  # Cuota 7
    11.86,  # Cuota 8
    0.0,  # Cuota 9
    6.68,  # Cuota 10
    6.26,  # Cuota 11
    0.0,  # Cuota 12
]
# ==============================================================================

st.set_page_config(
    page_title=TITULO_APP,
    layout="wide",
)

ruta_base = os.path.dirname(__file__)
ruta_encabezado = os.path.join(ruta_base, "encabezado.png")

if os.path.exists(ruta_encabezado):
    st.image(ruta_encabezado, use_container_width=True)

st.markdown(
    """
    <style>
        .stApp, html, body, [data-testid="stAppViewContainer"],
        label, p, span, div, [data-testid="stWidgetLabel"] p, .stMarkdown p {
            font-family: Arial, sans-serif !important;
            color: #1e293b !important;
            font-size: 12px !important;
        }
        
        div[data-testid="stMarkdownContainer"] p, .stRadio label {
            font-family: Arial, sans-serif !important;
            color: #1e293b !important;
            font-size: 12px !important;
        }
        
        [data-testid="stWidgetLabel"] {
            margin-bottom: 1px !important;
            padding-bottom: 0px !important;
        }
        
        div.row-widget.stRadio > div {
            flex-direction: row !important;
            gap: 8px !important;
        }
        
        .resultado-box {
            background-color: #ffffff !important;
            padding: 5px 10px !important;
            border-radius: 4px !important;
            border: 1px solid #cbd5e1 !important;
            margin-bottom: 3px !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.04) !important;
            text-align: center !important;
            min-height: 28px !important;
        }
        
        .resultado-box-tabla {
            background-color: #ffffff !important;
            padding: 5px 8px !important;
            border-radius: 4px !important;
            border: 1px solid #cbd5e1 !important;
            margin-bottom: 3px !important;
            display: flex !important;
            justify-content: flex-start !important;
            align-items: center !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.04) !important;
            text-align: left !important;
            min-height: 28px !important;
        }
        
        .tabla-header {
            background-color: #ffffff !important;
            color: #1e293b !important;
            font-weight: normal;
            text-align: left;
            padding: 5px 8px !important;
            border: 1px solid #cbd5e1 !important;
            border-radius: 4px !important;
            font-size: 11px !important;
            text-transform: uppercase;
            min-height: 28px !important;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            box-shadow: 0 1px 2px rgba(0,0,0,0.04);
        }
        
        .titulo-seccion-tabla {
            background-color: #ffffff;
            border: 1px solid #cbd5e1;
            padding: 6px 10px;
            font-weight: normal;
            text-align: center;
            margin-bottom: 4px;
            border-radius: 4px;
            font-size: 12px !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.04);
        }
        
        .resultado-label {
            font-family: Arial, sans-serif !important;
            color: #1e293b !important;
            font-weight: normal !important;
            font-size: 12px !important;
        }
        
        .resultado-valor {
            font-family: Arial, sans-serif !important;
            color: #1e293b !important;
            font-weight: normal !important;
            font-size: 12px !important;
        }
        
        .stButton>button {
            background-color: #0284c7 !important;
            color: white !important;
            font-weight: normal !important;
            border-radius: 4px !important;
            border: none !important;
            padding: 6px 12px !important;
            width: 100% !important;
            font-size: 12px !important;
        }

        @media print {
            body, .stApp, [data-testid="stAppViewContainer"] {
                background-color: #ffffff !important;
                color: #000000 !important;
                font-size: 8pt !important;
            }
            header, [data-testid="stSidebar"], [data-testid="stHeader"], .stDeployButton, [data-testid="stDecoration"] {
                display: none !important;
            }
            .stButton {
                display: none !important;
            }
            [data-testid="stAppViewContainer"] {
                overflow: visible !important;
                position: static !important;
            }
            .block-container {
                padding-top: 0 !important;
                padding-bottom: 0 !important;
                max-width: 100% !important;
            }
            .resultado-box, .resultado-box-tabla, .tabla-header, .titulo-seccion-tabla {
                border: 1px solid #cbd5e1 !important;
                page-break-inside: avoid !important;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

col_p1, col_p2, col_p3 = st.columns(3)
with col_p2:
    entry_partida = st.text_input("PARTIDA MUNICIPAL N°:")

st.markdown("---")

col_f1_1, col_f1_2, col_f1_3, col_f1_4 = st.columns(4)
with col_f1_1:
    var_estado = st.radio("Estado:", ["EDIFICADO", "BALDIO"])
with col_f1_2:
    var_uso = st.radio("Uso:", ["RESIDENCIAL", "COMERCIAL", "INDUSTRIAL"])
with col_f1_3:
    var_acceso = st.radio("Acceso Principal:", ["NO", "SI"])
with col_f1_4:
    var_zonif = st.selectbox("Zonificación:", ["A/B", "F", "OTRA"])

st.markdown("---")

st.markdown(
    "<p style='font-weight: normal; margin-bottom: 2px;'>DESCUENTOS:</p>",
