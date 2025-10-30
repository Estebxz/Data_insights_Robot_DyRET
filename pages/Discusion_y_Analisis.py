import streamlit as st
import pandas as pd

from components.UI.boton_flotante import Boton_flotante

st.title("DISCUSIÓN Y ANÁLISIS")
st.header("Hallazgos Principales")

data = {
    "Terreno": ["Arena", "Concreto", "Césped", "Mulch", "Grava", "Tierra"],
    "Fuerzas netas delanteras (N)": ["15-21", "25-35", "18-26", "17-25", "18-25", "18-26"],
    "Fuerzas netas traseras (N)": ["70-75", "72-80", "78-88", "74-82", "78-86", "76-83"],
    "Estabilidad": ["Baja", "Muy alta", "Media", "Baja - Media", "Media - Alta", "Media - Alta"]
}

df = pd.DataFrame(data)

def color_estabilidad(val):
    val_lower = val.lower()
    
    if "muy alta" in val_lower:
        bg = "#23362A"
        fg = "#0FA145"
    elif "alta" in val_lower:
        bg = "#23362A"
        fg = "#0FA145"
    elif "media" in val_lower:
        bg = "#3A3423"
        fg = "#DE960F"
    elif "baja" in val_lower:
        bg = "#330000"
        fg = "#FF3037"
    else:
        bg = "white"
        fg = "black"
    return f"background-color: {bg}; color: {fg};"

st.dataframe(
    df.style.map(color_estabilidad, subset=["Estabilidad"]),
    width="stretch",
    )

st.markdown("""
    El robot concentra mayor fuerza en las **patas traseras** (≈70–85 N), especialmente la derecha, indicando que la **tracción principal** proviene de la parte posterior.  
    Las **patas delanteras** (≈15–35 N) actúan más en **dirección y estabilización**.
    """)

etapas = [
    ("Arena:", "Superficie blanda y poco compacta; fuerzas delanteras irregulares y dispersas, traseras elevadas (≈70–75 N). El robot redistribuye carga hacia atrás para compensar la pérdida de apoyo. Concreto: Terreno rígido y estable; fuerzas limpias y constantes (delanteras ≈25–35 N, traseras ≈72–80 N). Locomoción más eficiente y equilibrada."),
    ("Concreto:", "Superficie dura, homogénea y tiene una mínima deformación. La fuerza en las patas delanteras es mucho más estable y mayor (≈25–35 N), la fuerza en las patas traseras mantiene valores similares (≈72–80 N) con oscilaciones periódicas muy regulares. Además, tiene señales o valores mucho más limpios y con una amplitud constante lo que puede ser debido a que el robot cuenta con una mayor adherencia y realiza un tracción uniforme."),
    ("Césped:", "Superficie semiblanda; fuerzas delanteras moderadas (≈18–26 N) y traseras más altas (≈78–88 N). Buen desempeño con ligera pérdida de eficiencia por compresibilidad."),
    ("Mulch (mantillo orgánico):", " Terreno fibroso e inestable; fuerzas delanteras irregulares (≈17–25 N) y traseras fluctuantes (≈74–82 N). Se presentan deslizamientos intermitentes y mayor esfuerzo de corrección."),
    ("Grava:", "Terreno granular con buena fricción; fuerzas delanteras cíclicas (≈18–25 N) y traseras regulares (≈78–86 N). Buena tracción con microajustes para estabilidad."),
    ("Tierra:", "Superficie semiblanda y bien compactada; fuerzas equilibradas (delanteras ≈18–26 N, traseras ≈76–83 N) y patrón estable. Ofrece equilibrio entre adherencia y absorción.")
]

for titulo, descripcion in etapas:
    col1, col2 = st.columns([1.3, 2.7])
    with col1:
        st.markdown(f"<h4 style='margin-top:5px; color:#58A6FF';>{titulo}</h4>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<p style='text-align: justify; margin-top:10px;'>{descripcion}</p>", unsafe_allow_html=True)
    st.divider()
    
st.markdown("""El estudio muestra cómo se mueven y se comportan las fuerzas en las patas del robot DyRET cuando camina sobre diferentes tipos de terreno""")

st.subheader("Como camina el robot")
st.write("""
Las fuerzas cambian de forma constante y repetitiva, lo que indica que el robot tiene un **movimiento bien coordinado**.  
Se puede ver que las patas se mueven en **pares diagonales**, como muchos animales cuando trotan, con una pata delantera y la trasera opuesta trabajando en conjunto.
""")

st.markdown("""
- 🦵 **Pata trasera derecha:** soporta más peso y empuja con más fuerza, siendo fundamental para mantener el equilibrio.  
- 🦶 **Pata delantera izquierda:** ayuda principalmente a mantener la **estabilidad** y adaptarse al terreno.  
- 🦿 **Otras dos patas:** colaboran para completar el ciclo del movimiento.
""")

st.info("""
En general, el robot camina con un **patrón de trote estable**, alternando las patas diagonales.  
Este tipo de marcha le brinda **buena estabilidad** y un **ahorro de energía notable**.
""")

st.divider()

st.subheader("Cómo cambian las fuerzas según el terreno")
st.markdown("""
Las fuerzas **cambian de forma constante y repetitiva**, lo que indica que el robot tiene un 
**movimiento bien coordinado**.  
Se observa que las patas se mueven en **pares diagonales**, como muchos animales cuando trotan, 
trabajando juntas una pata delantera y la trasera opuesta.
""")


st.markdown("""
- 🦵 **Pata trasera derecha:** soporta más peso y empuja con mayor fuerza, siendo esencial para el **equilibrio** del robot.  
- 🦶 **Pata delantera izquierda:** se encarga de **mantener la estabilidad** y adaptarse a las irregularidades del terreno.  
- ⚙️ **Pares diagonales:** las otras dos patas completan el ciclo de la marcha, coordinadas con el primer par.
""")
st.info("""
En conjunto, el robot camina con un **patrón de trote estable**, alternando patas diagonales.  
Este tipo de marcha mejora la **estabilidad dinámica** y permite un **uso más eficiente de la energía**.
""")

st.divider()

st.subheader("Diferencias entre patas")
st.markdown("""
Las **patas traseras** son las que aportan **mayor fuerza**, 
siendo las principales responsables de **sostener y empujar** al robot hacia adelante.  

Por otro lado, las **patas delanteras** realizan **ajustes más finos** en la fuerza lateral y longitudinal, 
lo que les permite **mantener el equilibrio** y **dirigir el movimiento** con precisión.
""")

st.info("""
En conjunto, cada par de patas cumple una función específica:  
las traseras impulsan, y las delanteras estabilizan y controlan la dirección.
""")

st.divider()

st.subheader("En resumen")
st.markdown("""
El robot **ajusta su forma de caminar** según el tipo de superficie que enfrenta.  
Los sensores registran con gran detalle **cómo interactúan las patas con el terreno**, 
y esta información es clave para **mejorar su locomoción** y **adaptarse a distintos entornos**.
""")

st.info("""
Estos resultados permiten optimizar el **control, equilibrio y eficiencia del movimiento**, 
haciendo que el robot responda de manera más inteligente a cada tipo de terreno.
""")

Boton_flotante()