import streamlit as st

from components.mapa import mapa_interactivo
from components.plano import plano_tridimensional
from components.tabla_superficies import tabla_superficies
from components.UI.boton_flotante import Boton_flotante

st.title("DyRET LEGGED ROBOT TERRAIN CLASSIFICATION DATASET")
mapa_interactivo()

st.markdown("""
**Tema:** Recopilación de mediciones en diferentes superficies en Brisbane, Australia, durante noviembre de 2019. Se utilizó el robot cuadrúpedo **DyRET** equipado con dos tipos de sensores, probándolo sobre **6 superficies** distintas y a **6 velocidades** diferentes.
""")

st.divider()

col1, col2 = st.columns(2)
with col1:
    container = st.container(border=True, height=567)
    container.subheader("Sensores")
    container.markdown("""
    * **Raw:** Sensor de 3 ejes en cada pata (*Optoforce OMD-20-SH-80N*).
    * **IMU:** Giroscopio, acelerómetro y magnetómetro de 3 ejes (*Xsens MTI-30*).
    """)
    container.subheader("Uso del Dataset")
    container.markdown("""
    * Validación de modelos cinemáticos/dinámicos.
    * Clasificación de terreno mediante señales de contacto.
    """)
    container.subheader("Metadatos")
    container.markdown("""
    * **Licencia:** Creative Commons 4.0.
    * **Actualizaciones:** No.
    * **Recolección:** 10 pruebas por archivo, 8 pasos cada una (total: **2880 pasos**).
    """)
    container.subheader("Proposito")
    container.markdown(
        "Evaluar el rendimiento del robot DyRET según la fuerza aplicada por cada pata durante la marcha."
    )

with col2:
    st.subheader("Velocidades y Pasos")
    st.markdown("""
    | Rango de Prueba | Velocidad (Hz) | Longitud de Paso (mm) |
    | :---: | :---: | :---: |
    | **0 - 1** | $0.125$ | $80$ |
    | **2 - 3** | $0.1875$ | $120$ |
    | **4 - 5** | $0.25$ | $80$ |
    """)
    st.subheader("Superficie")
    tabla_superficies()

st.divider()
plano_tridimensional()

st.header("Ejes del sensor RAW")
st.markdown("""
Los **robots cuadrúpedos bioinspirados** representan un campo de rápido desarrollo en la robótica, destacando por su capacidad para adaptarse a terrenos complejos y realizar tareas en ambientes desafiantes.

---

Uno de los componentes clave es el **sensor RAW**, instalado en el extremo de cada una de sus cuatro patas. Este sensor puede detectar las fuerzas que actúan en **tres direcciones**, llamadas **ejes X, Y y Z**:

* **Eje X:** Mide los movimientos **hacia adelante y hacia atrás** (Fuerza Longitudinal).
* **Eje Y:** Mide los desplazamientos **hacia los lados** (Fuerza Lateral).
* **Eje Z:** Mide las fuerzas **verticales**, es decir, hacia arriba y hacia abajo (Fuerza Normal).

Gracias a esta información, el robot puede determinar la presión que ejerce cada pata al tocar el suelo, lo que es fundamental para mejorar su **equilibrio y estabilidad** al caminar.
""")

col3, col4 = st.columns(2, gap="small") 

with col3:
    container_hito2 = st.container(border=True) 
    
    container_hito2.markdown("#### Exploración Inicial de Datos en Python")
    container_hito2.markdown("""
    Esta fase se centra en asegurar la **calidad** del dataset y realizar un Análisis Exploratorio (EDA) para identificar patrones y anomalías.
    """)
    container_hito2.link_button(
        label="Haz clic",
        url="https://colab.research.google.com/drive/1uczDqJNx-5RfNXIooJ5xJSgQ4Cw2fzrs",
        type="primary", 
        help="Haz clic para abrir el Hito 2"
    )
    
with col4:
    container_hito3 = st.container(border=True) 
    
    container_hito3.markdown("#### Limpieza y Exploración de Datos")
    container_hito3.markdown("""
    Esta etapa profundiza en el manejo de datos faltantes, normalización y visualización avanzada para validar hipótesis.
    """)
    
    container_hito3.link_button(
        label="Haz clic",
        url="https://colab.research.google.com/drive/1qRZ1FP8FBRl9PFz39juQCs_E4Itvn2lQ",
        type="primary", 
        help="Haz clic para abrir el Hito 3"
    )

Boton_flotante()