import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import requests

# =========================
# NATION DATA
# =========================

nation_data = pd.read_excel("網路APP檔案.xlsx")

countries = sorted(
    nation_data["Country"]
    .dropna()
    .astype(str)
    .str.strip()
    .tolist()
)

# =========================
# PAGE SETUP
# =========================
st.set_page_config(
    page_title="MY NET ZERO | GNPA",

    layout="wide"
)


# =========================
# HERO VIDEO
# =========================
if st.session_state.get("hero_visible", True):
    st.video(
        "hero.mp4",
        autoplay=True,
        muted=True,
        loop=False
    )

# =========================
# COLORS / STYLE
# =========================
st.markdown("""
<style>

.stApp {
    background-color: #FAFAF7;
}

.block-container {
    max-width: 1150px;
    padding-top: 45px;
    padding-bottom: 80px;
}

.gnpa {
    color: #2F765D;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 3px;
}

.agency {
    color: #68757D;
    font-size: 15px;
    margin-top: 5px;
}

.main-title {
    color: #123047;
    font-size: 70px;
    font-weight: 750;
    letter-spacing: -3px;
    margin-top: 55px;
    margin-bottom: 5px;
}

.world-title {
    color: #2F765D;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 4px;
    margin-bottom: 70px;
}

.small-title {
    color: #68757D;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.formula {
    color: #123047;
    font-size: 42px;
    font-weight: 650;
    margin-top: 10px;
    margin-bottom: 35px;
}

.divider {
    height: 1px;
    background-color: #D9DEDB;
    margin-top: 25px;
    margin-bottom: 50px;
}

.diet-title {
    color: #123047;
    font-size: 32px;
    font-weight: 750;
    letter-spacing: 3px;
}

.number-title {
    color: #68757D;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
}

.big-number {
    color: #123047;
    font-size: 43px;
    font-weight: 700;
}

.small-number {
    color: #68757D;
    font-size: 14px;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================
# GNPA
# =========================
st.markdown(
    '<div style="font-size:24px; font-weight:800; color:#2F765D; '
    'letter-spacing:6px; margin-top:28px; margin-bottom:6px;">'
    'GNPA'
    '</div>'
    '<div style="font-size:14px; font-weight:600; color:#123047; '
    'letter-spacing:1.6px; text-transform:uppercase; margin-bottom:34px;">'
    'Global Nature & Plant-based Diet Shift Agency'
    '</div>'
    '<div style="font-size:13px; font-weight:500; color:#68757D; '
    'letter-spacing:0.5px; margin-top:-28px; margin-bottom:34px;">'
    'Agencia Global para la Naturaleza y la Transición hacia una Alimentación Vegetal'
    '</div>',
    unsafe_allow_html=True
)

# =========================
# ACERCA DE GNPA
# =========================

with st.expander("ACERCA DE GNPA"):
    st.markdown(
        """
**Global Nature & Plant-based Diet Shift Agency (GNPA)**

GNPA es una iniciativa centrada en la investigación que explora la relación entre
los sistemas alimentarios, la restauración de la naturaleza, el cambio climático y la trayectoria hacia el Net Zero.

**MY NET ZERO** traduce esta investigación en una plataforma interactiva,
permitiendo que individuos, países y audiencias globales exploren cómo los cambios
alimentarios y la restauración de la naturaleza pueden influir en los resultados climáticos.

La plataforma está diseñada para conectar la investigación científica con la comprensión
pública y el debate sobre políticas.
        """
    )

# =========================
# CONTACTO / HACER UNA PREGUNTA
# =========================

with st.expander("CONTACTO / HACER UNA PREGUNTA"):

    with st.form("contact_form"):

        contact_name = st.text_input("Nombre")
        contact_organization = st.text_input("Organización")
        contact_country = st.text_input("País")
        contact_email = st.text_input("Email")
        contact_message = st.text_area("Pregunta / Mensaje")

        contact_submit = st.form_submit_button("ENVIAR")

    if contact_submit:

        if not contact_name or not contact_email or not contact_message:
            st.warning(
                "Por favor, complete su nombre, correo electrónico y pregunta/mensaje."
            )

        else:
            form_data = {
                "name": contact_name,
                "organization": contact_organization,
                "country": contact_country,
                "email": contact_email,
                "message": contact_message
            }

            try:
                response = requests.post(
                    "https://formspree.io/f/xeaobwry",
                    data=form_data,
                    timeout=10
                )

                if response.ok:
                    st.success(
                        "Gracias. Su mensaje se ha enviado correctamente."
                    )
                else:
                    st.error(
                        "No se pudo enviar su mensaje. Por favor, inténtelo de nuevo."
                    )

            except requests.RequestException:
                st.error(
                    "No se pudo enviar su mensaje. Por favor, inténtelo de nuevo."
                )

    st.caption(
        "Su información se utilizará únicamente para responder a su consulta."
    )

# =========================
# MY NET ZERO
# =========================
st.markdown(
    '<div class="main-title">MY NET ZERO</div>',
    unsafe_allow_html=True
)

# =========================
# MAIN NAVIGATION
# =========================

nav1, nav2, nav3, nav4 = st.columns(4)

with nav1:
    for_me = st.button(
        "PARA MÍ",
        use_container_width=True
    )

with nav2:
    my_nation = st.button(
        "MI PAÍS",
        use_container_width=True
    )

with nav3:
    our_world = st.button(
        "NUESTRO MUNDO",
        use_container_width=True
    )

with nav4:
    beyond_net_zero = st.button(
        "MÁS ALLÁ DEL NET ZERO",
        use_container_width=True
    )


# =========================
# MI PAÍS SELECTOR
# =========================

# =========================
# PAGE SELECTION
# =========================

if "show_nation" not in st.session_state:
    st.session_state.show_nation = False

if "show_for_me" not in st.session_state:
    st.session_state.show_for_me = False

if "show_beyond" not in st.session_state:
    st.session_state.show_beyond = False

if "hero_visible" not in st.session_state:
    st.session_state.hero_visible = True

if for_me:
    st.session_state.show_for_me = True
    st.session_state.show_nation = False
    st.session_state.show_beyond = False
    st.session_state.hero_visible = False

if my_nation:
    st.session_state.show_for_me = False
    st.session_state.show_nation = True
    st.session_state.show_beyond = False
    st.session_state.hero_visible = False

if our_world:
    st.session_state.show_for_me = False
    st.session_state.show_nation = False
    st.session_state.show_beyond = False
    st.session_state.hero_visible = False

if beyond_net_zero:
    st.session_state.show_for_me = False
    st.session_state.show_nation = False
    st.session_state.show_beyond = True
    st.session_state.hero_visible = False

# =========================
# PAGE BACKGROUND
# =========================

if st.session_state.show_for_me:
    page_bg = "#FCECEF"

elif st.session_state.show_nation:
    page_bg = "#F6F0DF"

elif st.session_state.show_beyond:
    page_bg = "#EAF5ED"

else:
    page_bg = "#EAF4F8"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {page_bg};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# MÁS ALLÁ DEL NET ZERO
# =========================

if st.session_state.show_beyond:

    st.markdown(
        '<div style="font-size:48px; font-weight:750; color:#123047; '
        'margin-top:55px; letter-spacing:-1px;">'
        'MÁS ALLÁ DEL NET ZERO'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="font-size:30px; font-weight:700; color:#2F765D; '
        'margin-top:8px; margin-bottom:35px;">'
        'UN FUTURO PRÓSPERO'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="font-size:21px; line-height:1.8; color:#123047; '
        'max-width:850px; margin-bottom:50px;">'
        'Cambiar un sistema insostenible no significa renunciar al futuro.<br>'
        'Se trata de abrir la puerta a un futuro más abundante, más avanzado '
        'y más emocionante de lo que imaginábamos.'
        '</div>',
        unsafe_allow_html=True
    )

    future1, future2, future3, future4 = st.columns(4)

    with future1:
        st.markdown("### SEGURIDAD ALIMENTARIA")

    with future2:
        st.markdown("### UN PLANETA RESTAURADO")

    with future3:
        st.markdown("### ESTABILIDAD CLIMÁTICA")

    with future4:
        st.markdown("### PROGRESO HUMANO")
     
# =========================
# PARA MÍ
# =========================

if st.session_state.show_for_me:

    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:30px;">PARA MÍ</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#2F765D; font-size:15px; font-weight:700; '
        'letter-spacing:2px; margin-top:25px;">ÍNDICE MY NET ZERO</div>',
        unsafe_allow_html=True
    )

    if "diet_choice" not in st.session_state:
        st.session_state.diet_choice = "ANIMAL-BASED"

    if st.session_state.diet_choice == "PLANT-BASED":
        my_net_zero_index = -6
    else:
        my_net_zero_index = 10

    st.markdown(
        f'<div style="font-size:64px; font-weight:750; color:#123047; '
        f'margin-top:5px; margin-bottom:30px;">{my_net_zero_index}</div>',
        unsafe_allow_html=True
    )
    

    personal1, personal2 = st.columns(2)

    with personal1:
        st.markdown(
            '<div class="number-title">VIDA COTIDIANA</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size:46px; font-weight:700; color:#123047; '
            'margin-top:10px;">2</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="small-number">'
            'Energía · Transporte · Cocina · Electrodomésticos'
            '</div>',
            unsafe_allow_html=True
        )

    with personal2:

        st.markdown(
            '<div class="number-title">ALIMENTACIÓN</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size:46px; font-weight:700; color:#123047; '
            'margin-top:10px;">8</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="small-number">'
            'Sistema alimentario de origen animal'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div style="height:35px;"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#2F765D; font-size:15px; font-weight:700; '
        'letter-spacing:2px;">SU ALIMENTACIÓN</div>',
        unsafe_allow_html=True
    )

    diet1, diet2 = st.columns(2)

    if "diet_choice" not in st.session_state:
        st.session_state.diet_choice = "ANIMAL-BASED"

    with diet1:
        plant_based = st.button(
            "DE ORIGEN VEGETAL",
            use_container_width=True
        )

        if plant_based:
            st.session_state.diet_choice = "PLANT-BASED"
            st.rerun()

    with diet2:
        animal_based = st.button(
            "DE ORIGEN ANIMAL",
            use_container_width=True
        )

        if animal_based:
            st.session_state.diet_choice = "ANIMAL-BASED"
            st.rerun()

  
    if st.session_state.diet_choice == "PLANT-BASED":

        st.markdown(
            '<div style="height:35px;"></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div style="color:#2F765D; font-size:15px; font-weight:700; '
            'letter-spacing:2px; margin-bottom:20px;">¿QUÉ CAMBIA?</div>',
            unsafe_allow_html=True
        )

        # FIRST ROW
        change1, change2, change3 = st.columns(3)

        with change1:
            st.markdown(
                '<div class="number-title">REDUCCIÓN DE METANO</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:27px; font-weight:700; color:#123047; '
                'margin-top:10px;">REDUCIDO</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">emisiones de metano relacionadas con la ganadería</div>',
                unsafe_allow_html=True
            )

        with change2:
            st.markdown(
                '<div class="number-title">TIERRAS LIBERADAS</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">78%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">de las tierras agrícolas mundiales</div>',
                unsafe_allow_html=True
            )

        with change3:
            st.markdown(
                '<div class="number-title">RECUPERACIÓN FORESTAL</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">41%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">de la deforestación tropical vinculada a la producción de carne de vacuno</div>',
                unsafe_allow_html=True
            )

        # SPACE BETWEEN TWO ROWS
        st.markdown(
            '<div style="height:30px;"></div>',
            unsafe_allow_html=True
        )

        # SECOND ROW
        change4, change5, change6 = st.columns(3)

        with change4:
            st.markdown(
                '<div class="number-title">ABSORCIÓN NATURAL DE CO₂</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:27px; font-weight:700; color:#123047; '
                'margin-top:10px;">RESTAURADA</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">mediante la recuperación de los ecosistemas</div>',
                unsafe_allow_html=True
            )

        with change5:
            st.markdown(
                '<div class="number-title">RECUPERACIÓN DE ZONAS MUERTAS OCEÁNICAS</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">80%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">las zonas muertas se recuperan y los bosques marinos costeros reanudan la absorción de CO₂</div>',
                unsafe_allow_html=True
            )

        with change6:
            st.markdown(
                '<div class="number-title">REDUCCIÓN DE ENERGÍA FÓSIL</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">41%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">atribuida al uso de energía del sistema ganadero</div>',
                unsafe_allow_html=True
            )

if st.session_state.show_nation:
    selected_country = st.selectbox(
        "SELECCIONE SU PAÍS",
        countries
    )

    selected_row = nation_data[
        nation_data["Country"].astype(str).str.strip() == selected_country
    ].iloc[0]

    selected_region = selected_row["Groups"]

    st.markdown(
        f'<div style="font-size:32px; font-weight:700; color:#123047; '
        f'margin-top:25px;">{selected_country.upper()}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div style="font-size:16px; color:#68757D; '
        f'margin-top:5px;">{selected_region}</div>',
        unsafe_allow_html=True
    )
    
     
    co2_impact = selected_row["Cow's CO2  impact "]
    gdp_impact = selected_row["COW's GDP impacts"]

  
    # =========================
    # PUNTUACIÓN NET ZERO
    # =========================

    ghg_net_zero = selected_row["Net Zero Score --GHG-IPCC"]
    my_net_zero = selected_row["MY NZ Research Model Outome"]

    st.markdown(
        '<div style="font-size:20px; font-weight:800; color:#2F765D; '
        'letter-spacing:2px; margin-top:40px; margin-bottom:18px;">'
        'PUNTUACIÓN NET ZERO'
        '</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):

        score1, score2 = st.columns(2)

        with score1:
            st.markdown(
                '<div style="font-size:14px; font-weight:700; color:#2F765D; '
                'letter-spacing:2px;">GEI — MODELO DEL IPCC</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                f'<div style="font-size:30px; font-weight:700; color:#123047; '
                f'margin-top:18px; margin-bottom:18px;">{ghg_net_zero}</div>',
                unsafe_allow_html=True
            )

        with score2:
            st.markdown(
                '<div style="font-size:14px; font-weight:700; color:#2F765D; '
                'letter-spacing:2px;">MODELO DE INVESTIGACIÓN MY NET ZERO</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                f'<div style="font-size:30px; font-weight:700; color:#123047; '
                f'margin-top:18px; margin-bottom:18px;">{my_net_zero}</div>',
                unsafe_allow_html=True
            )

    st.markdown(
        '<div style="height:35px;"></div>',
        unsafe_allow_html=True
    )






    result1, result2 = st.columns(2)

    with result1:
        st.markdown(
            '<div class="number-title">IMPACTO DE CO₂ DE LA GANADERÍA</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:38px; font-weight:700; '
            f'color:#123047; margin-top:10px;">{co2_impact*100:,.0f}%</div>',
            unsafe_allow_html=True
        )

    with result2:
        st.markdown(
            '<div class="number-title">IMPACTO DE LA GANADERÍA EN EL PIB</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:38px; font-weight:700; '
            f'color:#123047; margin-top:10px;">{gdp_impact*100:,.0f}%</div>',
            unsafe_allow_html=True
        )

    regional_co2 = selected_row["Livestock CO2 Region"]
    regional_gdp = selected_row["Livestock GDP Region"]

    st.markdown(
        f'<div style="font-size:15px; font-weight:700; color:#2F765D; '
        f'letter-spacing:2px; margin-top:35px;">'
        f'{selected_region.upper()} — COMPARACIÓN REGIONAL</div>',
        unsafe_allow_html=True
    )

    region1, region2 = st.columns(2)

    with region1:
        st.markdown(
            '<div class="number-title">IMPACTO REGIONAL DE CO₂</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:30px; font-weight:700; color:#123047; '
            f'margin-top:8px;">{regional_co2 * 100:,.0f}%</div>',
            unsafe_allow_html=True
        )

    with region2:
        st.markdown(
            '<div class="number-title">IMPACTO REGIONAL EN EL PIB</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:30px; font-weight:700; color:#123047; '
            f'margin-top:8px;">{regional_gdp * 100:,.0f}%</div>',
            unsafe_allow_html=True
        )


    # =========================
    # BASE DE CÁLCULO
    # =========================

    st.markdown(
        '<div style="height:25px;"></div>',
        unsafe_allow_html=True
    )

    basis1, basis2 = st.columns(2)

    with basis1:
        st.markdown(
            '<div style="border:1px solid #D9DEDB; border-radius:8px; padding:20px 24px; min-height:250px;">'
            '<div style="color:#123047; font-size:15px; font-weight:700; letter-spacing:1.5px; margin-bottom:18px;">IMPACTO DE CO₂ — BASE DE CÁLCULO</div>'
            '<div style="color:#68757D; font-size:15px; line-height:2;">Emisiones de metano<br>Tierras de pastoreo<br>Deforestación<br>Uso de energía<br>Combustibles fósiles</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with basis2:
        st.markdown(
            '<div style="border:1px solid #D9DEDB; border-radius:8px; padding:20px 24px; min-height:250px;">'
            '<div style="color:#123047; font-size:15px; font-weight:700; letter-spacing:1.5px; margin-bottom:18px;">IMPACTO EN EL PIB — BASE DE CÁLCULO</div>'
            '<div style="color:#68757D; font-size:15px; line-height:2;">Emisiones de metano<br>Agua<br>Erosión del suelo<br>Deforestación<br>Cultivos forrajeros</div>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div style="color:#68757D; font-size:13px; margin-top:12px;">'
        'Los resultados se calculan mediante el modelo de investigación MY NET ZERO.'
        '</div>',
        unsafe_allow_html=True
    )
    
    # =========================
    # MENSAJE NACIONAL CLAVE
    # =========================

    national_message = selected_row["Key national message"]

    st.markdown(
        '<div style="height:30px;"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#2F765D; font-size:14px; font-weight:700; '
        'letter-spacing:2px;">MENSAJE NACIONAL CLAVE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div style="color:#123047; font-size:20px; line-height:1.7; '
        f'margin-top:12px; margin-bottom:20px;">{national_message}</div>',
        unsafe_allow_html=True
    )



st.markdown(
    '<div class="world-title">NET ZERO MUNDIAL</div>',
    unsafe_allow_html=True
)


# =========================
# NET ZERO FORMULAS
# =========================
col1, col2 = st.columns(2)

with col1:

    st.markdown(
        '<div class="small-title">'
        'Net Zero convencional'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="formula">'
        '1 − 1 = 0'
        '</div>',
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        '<div class="small-title">'
        'Brecha real hacia el Net Zero'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div style="
            color:#123047;
            font-size:34px;
            font-weight:600;
            margin-top:10px;
            line-height:1.25;
            white-space:nowrap;
        ">
            Net Zero = 1 − (0.25 − 11.87)
        </div>

        <div style="
            color:#123047;
            font-size:58px;
            font-weight:750;
            letter-spacing:-2px;
            margin-top:12px;
            margin-bottom:25px;
        ">
            = 12.62
        </div>
        ''',
        unsafe_allow_html=True
    )

  


# =========================
# WHY
# =========================
with st.expander("¿POR QUÉ?"):

    st.image(
        "net_zero_gap.png.png",
        caption="Figura 1.1. Medición de la distancia desde el presente hasta el éxito climático.",
        use_container_width=True
    )

    st.markdown("""
### LA BRECHA HACIA EL NET ZERO

**Brecha de CO₂ atmosférico**

426 ppm − 350 ppm ≈ **76 ppm**

**Equivalente de CO₂**

76 ppm × 7.81 GtCO₂/ppm ≈ **593 GtCO₂**

**Años equivalentes de emisiones globales**

593 GtCO₂ ÷ 50 GtCO₂/year ≈ **11.87 years**

**Modelo MY NET ZERO**

1 − (0.25 − 11.87) ≈ **12.62**

*Base de conversión: Poljak (2023), donde cada ppm de CO₂ atmosférico ≈ 7,81 GtCO₂.*
""")

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)


# =========================
# TRANSICIÓN ALIMENTARIA
# =========================
st.markdown(
    '<div class="diet-title">TRANSICIÓN ALIMENTARIA</div>',
    unsafe_allow_html=True
)


diet_shift = st.slider(
    "Transición alimentaria",
    0,
    100,
    0,
    1,
    label_visibility="collapsed"
)


# =========================
# CALCULATION
# =========================

MAX_CO2 = 643.0

START_PPM = 426.0
TARGET_PPM = 350.0

co2_reduced = MAX_CO2 * diet_shift / 100

co2_remaining = MAX_CO2 - co2_reduced

current_ppm = (
    START_PPM
    - (START_PPM - TARGET_PPM)
    * diet_shift / 100
)

ppm_reduced = START_PPM - current_ppm


# =========================
# RESULTS
# =========================
col3, col4 = st.columns(2)

with col3:

    st.markdown(
        '<div class="number-title">'
        'CO₂ REDUCIDO'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="big-number">'
        f'{co2_reduced:.1f} GtCO₂'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="small-number">'
        f'{co2_remaining:.1f} GtCO₂ restantes'
        f'</div>',
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        '<div class="number-title">'
        'CO₂ ATMOSFÉRICO'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="big-number">'
        f'{current_ppm:.1f} ppm'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="small-number">'
        f'426 → {current_ppm:.1f} ppm'
        f'</div>',
        unsafe_allow_html=True
    )


# =========================
# CHART DATA
# =========================

x = np.arange(0, 101)

carbon_curve = MAX_CO2 * (1 - x / 100)

ppm_curve = (
    START_PPM
    - (START_PPM - TARGET_PPM)
    * x / 100
)


# =========================
# CHART 1
# =========================

chart1, chart2 = st.columns(2)


with chart1:

    fig1 = go.Figure()

    fig1.add_trace(
        go.Scatter(
            x=x,
            y=carbon_curve,
            mode="lines",
            line=dict(
                color="#123047",
                width=4
            )
        )
    )

    fig1.add_trace(
        go.Scatter(
            x=[diet_shift],
            y=[co2_remaining],
            mode="markers",
            marker=dict(
                size=13,
                color="#2F765D"
            )
        )
    )

    fig1.update_layout(
        title="BRECHA DE CO₂",
        height=330,
        showlegend=False,
        paper_bgcolor="#FAFAF7",
        plot_bgcolor="#FAFAF7",
        xaxis_title="Transición alimentaria (%)",
        yaxis_title="GtCO₂ restantes",
        margin=dict(
            l=20,
            r=20,
            t=55,
            b=30
        )
    )

    st.plotly_chart(
        fig1,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )


# =========================
# CHART 2
# =========================

with chart2:

    fig2 = go.Figure()

    fig2.add_trace(
        go.Scatter(
            x=x,
            y=ppm_curve,
            mode="lines",
            line=dict(
                color="#2F765D",
                width=4
            )
        )
    )

    fig2.add_trace(
        go.Scatter(
            x=[diet_shift],
            y=[current_ppm],
            mode="markers",
            marker=dict(
                size=13,
                color="#123047"
            )
        )
    )

    fig2.update_layout(
        title="CO₂ ATMOSFÉRICO",
        height=330,
        showlegend=False,
        paper_bgcolor="#FAFAF7",
        plot_bgcolor="#FAFAF7",
        xaxis_title="Transición alimentaria (%)",
        yaxis_title="ppm",
        margin=dict(
            l=20,
            r=20,
            t=55,
            b=30
        )
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )

# =========================
# KEY IMPACTS
# =========================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)

impact1, impact2, impact3 = st.columns(3)

with impact1:
    st.markdown(
        '<div class="number-title">TIERRAS LIBERADAS</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:12px; white-space:nowrap;">37 millones de km²</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="small-number">78 % de las tierras agrícolas mundiales</div>',
        unsafe_allow_html=True
    )

with impact2:
    st.markdown(
        '<div class="number-title">REDUCCIÓN DE GEI</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:12px;">166%</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="small-number">de los GEI mundiales de 2020</div>',
        unsafe_allow_html=True
    )

with impact3:
    st.markdown(
        '<div class="number-title">REDUCCIÓN DE COSTOS ECONÓMICOS</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:12px;">163%</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="small-number">del PIB mundial de 2020</div>',
        unsafe_allow_html=True
    )

# =========================
# SECOND WHY
# =========================

with st.expander(
    "¿POR QUÉ LA TRANSICIÓN ALIMENTARIA CAMBIA EL CO₂?"
):

    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-bottom:15px;">MODELO DE DATOS</div>',
        unsafe_allow_html=True
    )

    st.image(
        "data model.png",
        caption="Modelo de datos de investigación MY NET ZERO",
        use_container_width=True
    )


    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-top:35px; margin-bottom:15px;">'
        'ESTRUCTURA DE LA INVESTIGACIÓN'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
**CAPÍTULO 3 — DATOS Y METODOLOGÍA**  
Marco de investigación · Datos · Variables · Ecuaciones · Modelo de restauración de la naturaleza

**CAPÍTULO 4 — EMISIONES Y ABSORCIÓN NATURAL DE CO₂**  
Validez del modelo · Pronósticos · Análisis de sensibilidad · Escenarios climáticos

**CAPÍTULO 5 — COSTOS EXTERNOS DE LOS COMBUSTIBLES FÓSILES Y LA GANADERÍA**  
Externalidades de la ganadería · Energía · Costos económicos

**CAPÍTULO 6 — RESPONSABILIDAD DE CO₂ DE LOS COMBUSTIBLES FÓSILES Y LA GANADERÍA**  
Emisiones · Pérdida de eliminación de CO₂ · Consumo de energía · Análisis de sensibilidad de tierras y bosques · Responsabilidad ajustada

**CAPÍTULO 7 — APLICACIÓN Y MODELO DE RESTAURACIÓN DE LA NATURALEZA**  
EE. UU. · China · Política climática mundial · Restauración de la naturaleza
        """
    )

    st.caption(
        "Detailed methodology, calculations, sensitivity analyses and "
        "underlying data are documented in the full research."
    )



    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-top:40px; margin-bottom:15px;">'
        'BASE DE CÁLCULO'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
**ENERGÍA — 41 %**

**DATOS FUENTE**  
Consumo mundial de carne por tipo · Requisitos energéticos por tipo de carne · Población mundial · Consumo mundial de electricidad

**CÁLCULO MY NET ZERO**  
Consumo de carne × requisito energético por tipo de carne × población mundial  
→ consumo mundial estimado de electricidad de la industria cárnica  
→ comparado con el consumo mundial total de electricidad

**RESULTADO**  
Consumo estimado de electricidad de la industria cárnica = **41 % del consumo mundial de electricidad**
        """
    )

    st.caption(
        "Derived indicator calculated by the MY NET ZERO research model "
        "from underlying source data."
    )

    st.markdown(
        """
**METANO — 31 %**

**DATOS FUENTE**  
Población bovina · Emisiones anuales de metano por vaca

**SUPUESTO DEL MODELO MY NET ZERO**  
Metano = **100× equivalente de CO₂** para representar su fuerte impacto de calentamiento a corto plazo

**CÁLCULO MY NET ZERO**  
Población bovina × emisiones de metano por vaca × 100 equivalente de CO₂  
→ aproximadamente **15,2 GtCO₂-equivalente**

**RESULTADO**  
15,2 GtCO₂-eq. ÷ 50 GtCO₂-eq. de emisiones globales anuales  
→ **≈ 31 %**
        """
    )

    st.caption(
        "The 100× methane factor is a MY NET ZERO model assumption. "
        "It is not the conventional 100-year GWP factor."
    )
 
    st.markdown(
        """
**TIERRA — 11 %**

**DATOS FUENTE**  
Uso de tierras para la ganadería = **37 millones de km²**

**CÁLCULO MY NET ZERO**  
37 millones de km² × capacidad estimada de absorción de CO₂ de las tierras liberadas  
→ aproximadamente **5,17 GtCO₂ por año**

**RESULTADO**  
5,17 GtCO₂ ÷ 50 GtCO₂ de emisiones globales anuales  
→ **≈ 11 %**
        """
    )

    st.caption(
        "The 37 millones de km² livestock land-use estimate is source data. "
        "The 11% indicator is derived by the MY NET ZERO research model."
    )

    st.markdown(
        """
**BOSQUE — 91 %**

**LÍMITE DEL MODELO**  
Estimación conservadora que utiliza el ganado de **países amazónicos y un país de la cuenca del Congo**, en lugar de la población bovina mundial

**CÁLCULO MY NET ZERO**  
Población bovina en las regiones de bosque tropical seleccionadas × impacto sobre la superficie forestal × capacidad estimada de absorción de CO₂ del bosque tropical  
→ aproximadamente **45,34 GtCO₂ por año**

**RESULTADO**  
45,34 GtCO₂ ÷ 50 GtCO₂ de emisiones globales anuales  
→ **≈ 91 %**
        """
    )

    st.caption(
        "The forest estimate uses a deliberately restricted tropical-forest "
        "boundary to avoid applying one CO₂ absorption rate to forests "
        "across different climatic regions."
    )

    st.markdown(
        """
**RESPONSABILIDAD TOTAL DE CO₂ DE LA GANADERÍA — 166 %**

**REASIGNACIÓN DE ENERGÍA**  
Uso energético de la industria cárnica = **41 %** de la electricidad mundial  
Aplicado a la **línea base del 78 % de combustibles fósiles**  
→ 78 % × 41 % ≈ **32 %**

**CÁLCULO INTEGRADO MY NET ZERO**  
Metano **31 %** + Tierra **11 %** + Bosque **91 %** + Energía **32 %**

**RESULTADO**  
31 % + 11 % + 91 % + 32 % ≈ **166 %**
        """
    )

    st.caption(
        "The 166% result is an integrated MY NET ZERO research-model "
        "estimate relative to the 50 GtCO₂-eq. annual global emissions baseline."
    )


    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-top:40px; margin-bottom:15px;">'
        'SOURCES'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
**FUENTES DE DATOS PRINCIPALES**

**FAO / UNFAO**  
Datos sobre ganadería, consumo de alimentos y uso de tierras agrícolas

**Energypedia**  
Requisitos energéticos en las cadenas de valor alimentarias y agrícolas

**U.S. Energy Information Administration (EIA)**  
Datos mundiales de energía y electricidad

**IPCC**  
Marco convencional de contabilidad de gases de efecto invernadero y evaluación climática
        """
    )

    st.caption(
        "Source data are used as inputs. Calculations, integration and "
        "derived indicators are produced by the MY NET ZERO research model."
    )
    st.markdown(
        """
**VER FUENTES ORIGINALES**

[FAO / FAOSTAT — Datos mundiales de alimentación y agricultura](https://www.fao.org/faostat/)

[Energypedia — Energía en las cadenas de valor alimentarias y agrícolas](https://energypedia.info/wiki/Energy_within_Food_and_Agricultural_Value_Chains)

[U.S. Energy Information Administration (EIA) — Datos de electricidad](https://www.eia.gov/electricity/data.php)

[Gatti et al. (2021), Nature — La Amazonia como fuente de carbono vinculada a la deforestación y el cambio climático](https://www.nature.com/articles/s41586-021-03629-6)
        """
    )
