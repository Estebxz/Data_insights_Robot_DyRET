import streamlit as st
from components.UI.boton_flotante import Boton_flotante

st.title("CONCLUSIONES Y RECOMENDACIONES")
st.subheader("Resumen de hallazgos:")
st.markdown("""
Con esto se puede concluir que en cuanto a la **distribución de fuerzas**, las **patas traseras** son las principales generadoras de empuje, independientemente del terreno. En cuanto a la influencia del terreno, a mayor rigidez y uniformidad del terreno, menor dispersión y mayor eficiencia de la locomoción.  

Además, como se dijo anteriormente, en **terrenos blandos** (arena, mulch) aumenta el esfuerzo y se reduce la estabilidad debido a que posiblemente el robot necesita ajustar su morfología o estrategia de control. En **terrenos intermedios** (césped, tierra, grava) se obtiene un desempeño equilibrado. Y por último, en **terrenos firmes** (concreto) se presenta un patrón más limpio y estable, que puede ser ideal para calibraciones o pruebas de referencia.  

Los resultados sugieren que el **ajuste dinámico de la morfología** (longitud de patas) del DyRET podría optimizar la tracción y estabilidad dependiendo del tipo de superficie detectada.  

Las **patas traseras**, especialmente la derecha, generan las fuerzas más grandes, lo que concuerda con el patrón típico de robots cuadrúpedos donde la parte trasera impulsa y estabiliza la marcha, mientras que las delanteras mantienen el equilibrio y dirección.  

Además, se presenta una **distribución asimétrica de fuerzas**, donde la pata trasera derecha ejerce la mayor carga, lo que podría indicar una ligera descompensación mecánica o una preferencia direccional del sistema de control.  

También se presenta una **marcha coordinada diagonal**, ya que en las gráficas temporales se muestra una sincronía entre patas opuestas diagonales. También se concluye que existe una **fase de apoyo bien definida**, donde las variaciones periódicas de fuerza reflejan una alternancia clara entre apoyo y balanceo, sin irregularidades marcadas.
""")
st.subheader("Recomendaciones para trabajos futuros:")
st.markdown("Teniendo en cuenta esto, se recomienda verificar la **calibración de actuadores traseros**, especialmente el derecho, para evitar sobrecarga a largo plazo y asegurar una distribución más uniforme de las fuerzas.")
st.divider()

Boton_flotante()