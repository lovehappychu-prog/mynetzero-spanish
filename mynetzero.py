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
    'Global Nature & Plant-based Transición alimentaria Agency'
    '</div>',
    unsafe_allow_html=True
)

# =========================
# ACERCA DE GNPA
# =========================

with st.expander("ACERCA DE GNPA"):
    st.markdown(
        """
**Global Nature & Plant-based Transición alimentaria Agency (GNPA)**  
**Agencia Global para la Naturaleza y la Transición hacia una Alimentación Vegetal**

GNPA es una iniciativa centrada en la investigación que explora la relación entre
los sistemas alimentarios, la restauración de la naturaleza, el cambio climático
y la trayectoria hacia el Net Zero.

**MY NET ZERO** transforma esta investigación en una plataforma interactiva,
permitiendo que individuos, países y públicos de todo el mundo exploren cómo
la transición alimentaria y la restauración de la naturaleza pueden influir en los resultados climáticos.

La plataforma está diseñada para conectar la investigación científica con la
comprensión pública y el debate sobre políticas.
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
        contact_email = st.text_input("Correo electrónico")
        contact_message = st.text_area("Pregunta / Mensaje")

        contact_submit = st.form_submit_button("ENVIAR")

    if contact_submit:

        if not contact_name or not contact_email or not contact_message:
            st.warning(
                "Complete su nombre, correo electrónico y pregunta/mensaje."
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
                        "No se pudo enviar su mensaje. Inténtelo de nuevo."
                    )

            except requests.RequestException:
                st.error(
                    "No se pudo enviar su mensaje. Inténtelo de nuevo."
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
        'Changing an unsustainable system is not about giving up the future.<br>'
        'It is about unlocking a future more abundant, more advanced, '
        'and more exciting than we imagined.'
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
        'letter-spacing:2px; margin-top:25px;">MY NET ZERO INDEX</div>',
        unsafe_allow_html=True
    )

    if "diet_choice" not in st.session_state:
        st.session_state.diet_choice = "DE ORIGEN ANIMAL"

    if st.session_state.diet_choice == "VEGETAL":
        my_net_zero_index = -6
    else:
        my_net_zero_index = 10

    st.markdown(
        f'<div style="font-size:64px; font-weight:750; color:#123047; '
        f'margin-top:5px; margin-bottom:30px;">{my_net_zero_index}</div>',
        unsafe_allow_html=True
    )
    
    st.markdown(
        '<div style="font-size:14px; line-height:1.6; color:#68757D; '
        'max-width:760px; margin-top:-15px; margin-bottom:25px;">'
        '<b>ACERCA DE ESTE ÍNDICE</b><br>'
        'MY NET ZERO INDEX is a standardized research indicator based on an '
        '<b>Earth-system accounting framework</b>. Unlike conventional carbon-footprint '
        'approaches that focus primarily on anthropogenic emissions, this model also '
        'accounts for the loss and recovery of natural CO₂-removal capacity across '
        'forests, land and oceans.'
        '</div>',
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

    with st.expander("¿CÓMO SE CALCULA EL ÍNDICE?"):
        st.markdown(
            """
El **MY NET ZERO INDEX** es un indicador de investigación estandarizado.  
No es una calculadora convencional de huella de carbono personal.

**VIDA COTIDIANA = 2**  
La energía, el transporte, la cocina y los electrodomésticos representan aproximadamente el **20 %**
de la carga climática estandarizada en este modelo de investigación.

**ALIMENTACIÓN Y NATURALEZA = 8**  
El **80 %** restante representa la atribución del modelo de investigación de la carga climática
relacionada con la ganadería, incluido el uso de energía del sistema alimentario,
la presión sobre la tierra y la pérdida de capacidad natural de remoción de CO₂.

**DIETA DE ORIGEN ANIMAL**

**2 + 8 = 10**

Por lo tanto, la línea base de dieta de origen animal produce un MY NET ZERO INDEX de **10**.

**DIETA VEGETAL**

**2 − 8 = −6**

En el modelo, la transición alimentaria reduce la presión relacionada con la ganadería
y permite la recuperación de los sumideros naturales de carbono. El valor negativo representa
la contribución de la remoción natural de CO₂ restaurada al equilibrio del sistema Tierra,
no una afirmación de que una persona produzca directamente emisiones negativas.
            """
        )
    st.markdown(
        '<div style="color:#2F765D; font-size:15px; font-weight:700; '
        'letter-spacing:2px;">SU DIETA</div>',
        unsafe_allow_html=True
    )

    diet1, diet2 = st.columns(2)

    if "diet_choice" not in st.session_state:
        st.session_state.diet_choice = "DE ORIGEN ANIMAL"

    with diet1:
        plant_based = st.button(
            "VEGETAL",
            use_container_width=True
        )

        if plant_based:
            st.session_state.diet_choice = "VEGETAL"
            st.rerun()

    with diet2:
        animal_based = st.button(
            "DE ORIGEN ANIMAL",
            use_container_width=True
        )

        if animal_based:
            st.session_state.diet_choice = "DE ORIGEN ANIMAL"
            st.rerun()

  
    if st.session_state.diet_choice == "VEGETAL":

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
                '<div class="number-title">TIERRA LIBERADA</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">78%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">de la tierra agrícola mundial</div>',
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
                '<div class="small-number">de la deforestación tropical vinculada a la producción de carne de res</div>',
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
            '<div style="color:#123047; font-size:15px; font-weight:700; letter-spacing:1.5px; margin-bottom:18px;">CO₂ IMPACT — BASE DE CÁLCULO</div>'
            '<div style="color:#68757D; font-size:15px; line-height:2;">Methane emissions<br>Grazing land<br>Deforestation<br>Energy use<br>Fossil fuels</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with basis2:
        st.markdown(
            '<div style="border:1px solid #D9DEDB; border-radius:8px; padding:20px 24px; min-height:250px;">'
            '<div style="color:#123047; font-size:15px; font-weight:700; letter-spacing:1.5px; margin-bottom:18px;">GDP IMPACT — BASE DE CÁLCULO</div>'
            '<div style="color:#68757D; font-size:15px; line-height:2;">Methane emissions<br>Water<br>Soil erosion<br>Deforestation<br>Feed crops</div>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div style="color:#68757D; font-size:13px; margin-top:12px;">'
        'Los resultados se calculan utilizando el modelo de investigación MY NET ZERO.'
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

st.markdown(
    """
### DOS FORMAS DE CONTABILIZAR EL NET ZERO

El **Net Zero convencional** pregunta principalmente cuántas emisiones antropogénicas deben reducirse o removerse para equilibrar las emisiones causadas por los seres humanos.

**MY NET ZERO** amplía el límite de contabilidad al sistema Tierra: también pregunta cuánta capacidad natural de remoción de CO₂ puede restaurarse cuando disminuye la presión sobre los bosques, la tierra y los océanos.

La diferencia no es simplemente otra estimación de emisiones: es un **límite de contabilidad diferente**.
    """
)
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
        'Brecha real de Net Zero'
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
        caption="Figure 1.1. Measurement of the distance from the present to climate success.",
        use_container_width=True
    )

    st.markdown("""
### THE NET ZERO GAP

**Atmospheric CO₂ gap**

426 ppm − 350 ppm ≈ **76 ppm**

**CO₂ equivalent**

76 ppm × 7.81 GtCO₂/ppm ≈ **593 GtCO₂**

**Equivalent years of global emissions**

593 GtCO₂ ÷ 50 GtCO₂/year ≈ **11.87 years**

**MY NET ZERO model**

1 − (0.25 − 11.87) ≈ **12.62**

*Conversion basis: Poljak (2023), where each atmospheric CO₂ ppm ≈ 7.81 GtCO₂.*
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

co2_restantes = MAX_CO2 - co2_reduced

current_ppm = (
    START_PPM
    - (START_PPM - TARGET_PPM)
    * diet_shift / 100
)

ppm_reduced = START_PPM - current_ppm


# =========================
# RESULTADOS
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
        f'{co2_restantes:.1f} GtCO₂ restantes'
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
            y=[co2_restantes],
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
        '<div class="number-title">TIERRA LIBERADA</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:12px; white-space:nowrap;">37 million km²</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="small-number">78% de la tierra agrícola mundial</div>',
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
        '<div class="number-title">REDUCCIÓN DEL COSTO ECONÓMICO</div>',
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
**CHAPTER 3 — DATA AND METHODOLOGY**  
Research framework · Data · Variables · Equations · Nature Restoration Model

**CHAPTER 4 — EMISSIONS AND NATURE'S CO₂ ABSORPTION**  
Model validity · Forecasting · Sensitivity analysis · Climate scenarios

**CHAPTER 5 — EXTERNAL COSTS OF FOSSIL FUELS AND LIVESTOCK**  
Livestock externalities · Energy · Economic costs

**CHAPTER 6 — CO₂ RESPONSIBILITY OF FOSSIL FUELS AND LIVESTOCK**  
Emissions · CO₂ removal loss · Energy consumption · Land and forest sensitivity analysis · Adjusted responsibility

**CHAPTER 7 — APPLICATION AND NATURE RESTORATION MODEL**  
U.S. · China · Global climate policy · Nature restoration
        """
    )

    st.caption(
        "Detailed methodology, calculations, sensitivity analyses and "
        "underlying data are documented in the full research."
    )

# =========================
# RESEARCH BRIEF
# =========================

st.markdown(
    """
### INFORME DE INVESTIGACIÓN

**Contabilidad del sistema Tierra para el Net Zero**

Un resumen de una página del marco de investigación MY NET ZERO, que incluye el límite de contabilidad, la atribución de la carga climática y la vía desde la transición alimentaria hasta la recuperación de la capacidad natural de remoción de CO₂.
    """
)

with st.expander("VER INFORME DE INVESTIGACIÓN"):
    st.image(
        "research_brief.png",
        use_container_width=True
    )

with open("Net_Zero_Research_Summary_QR_FIXED.pdf", "rb") as pdf_file:
    st.download_button(
        label="DESCARGAR INFORME DE INVESTIGACIÓN (PDF)",
        data=pdf_file,
        file_name="MY_NET_ZERO_Research_Brief.pdf",
        mime="application/pdf",
        use_container_width=True
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
**ENERGÍA — 41%**

**DATOS FUENTE**  
Global meat consumption by meat type · Energy requirements by meat type · Global population · Global electricity consumption

**CÁLCULO MY NET ZERO**  
Meat consumption × energy requirement by meat type × global population  
→ estimated global meat-industry electricity consumption  
→ compared with total global electricity consumption

**RESULTADO**  
Estimated meat-industry electricity consumption = **41% of global electricity consumption**
        """
    )

    st.caption(
        "Derived indicator calculated by the MY NET ZERO research model "
        "from underlying source data."
    )

    st.markdown(
        """
**METANO — 31%**

**DATOS FUENTE**  
Cattle population · Annual methane emissions per cow

**MY NET ZERO MODEL ASSUMPTION**  
Methane = **100× CO₂-equivalent** to represent its strong near-term warming impact

**CÁLCULO MY NET ZERO**  
Cattle population × methane emissions per cow × 100 CO₂-equivalent  
→ approximately **15.2 GtCO₂-equivalent**

**RESULTADO**  
15.2 GtCO₂-eq. ÷ 50 GtCO₂-eq. global annual emissions  
→ **≈ 31%**
        """
    )

    st.caption(
        "The 100× methane factor is a MY NET ZERO model assumption. "
        "It is not the conventional 100-year GWP factor."
    )
 
    st.markdown(
        """
**TIERRA — 11%**

**DATOS FUENTE**  
Livestock land use = **37 million km²**

**CÁLCULO MY NET ZERO**  
37 million km² × estimated CO₂ absorption capacity of released land  
→ approximately **5.17 GtCO₂ per year**

**RESULTADO**  
5.17 GtCO₂ ÷ 50 GtCO₂ global annual emissions  
→ **≈ 11%**
        """
    )

    st.caption(
        "The 37 million km² livestock land-use estimate is source data. "
        "The 11% indicator is derived by the MY NET ZERO research model."
    )

    st.markdown(
        """
**BOSQUE — 91%**

**LÍMITE DEL MODELO**  
Conservative estimate using cattle in **Amazon nations and one Congo Basin country**, rather than global cattle populations

**CÁLCULO MY NET ZERO**  
Cattle population in the selected tropical-forest regions × forest area impact × estimated tropical-forest CO₂ absorption capacity  
→ approximately **45.34 GtCO₂ per year**

**RESULTADO**  
45.34 GtCO₂ ÷ 50 GtCO₂ global annual emissions  
→ **≈ 91%**
        """
    )

    st.caption(
        "The forest estimate uses a deliberately restricted tropical-forest "
        "boundary to avoid applying one CO₂ absorption rate to forests "
        "across different climatic regions."
    )

    st.markdown(
        """
**RESPONSABILIDAD TOTAL DE CO₂ DE LA GANADERÍA — 166%**

**REATRIBUCIÓN DE ENERGÍA**  
Meat-industry energy use = **41%** of global electricity  
Applied to the **78% fossil-fuel baseline**  
→ 78% × 41% ≈ **32%**

**CÁLCULO INTEGRADO MY NET ZERO**  
Methane **31%** + Land **11%** + Forest **91%** + Energy **32%**

**RESULTADO**  
31% + 11% + 91% + 32% ≈ **166%**
        """
    )

    st.caption(
        "The 166% result is an integrated MY NET ZERO research-model "
        "estimate relative to the 50 GtCO₂-eq. annual global emissions baseline."
    )


    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-top:40px; margin-bottom:15px;">'
        'FUENTES'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
**FUENTES DE DATOS PRINCIPALES**

**FAO / UNFAO**  
Livestock, food consumption and agricultural land-use data

**Energypedia**  
Energy requirements within food and agricultural value chains

**U.S. Energy Information Administration (EIA)**  
Global energy and electricity data

**IPCC**  
Conventional greenhouse-gas accounting and climate assessment framework
        """
    )

    st.caption(
        "Source data are used as inputs. Calculations, integration and "
        "derived indicators are produced by the MY NET ZERO research model."
    )
    st.markdown(
        """
**VER FUENTES ORIGINALES**

[FAO / FAOSTAT — Global Food & Agriculture Data](https://www.fao.org/faostat/)

[Energypedia — Energy within Food and Agricultural Value Chains](https://energypedia.info/wiki/Energy_within_Food_and_Agricultural_Value_Chains)

[U.S. Energy Information Administration (EIA) — Electricity Data](https://www.eia.gov/electricity/data.php)

[Gatti et al. (2021), Nature — Amazonia as a carbon source linked to deforestation and climate change](https://www.nature.com/articles/s41586-021-03629-6)
        """
    )
