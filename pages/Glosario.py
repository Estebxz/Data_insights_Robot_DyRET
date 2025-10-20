import streamlit as st

st.title("GLOSARIO")

etapas = [
    ("Sensor RAW", "Datos sin procesar obtenidos directamente de los sensores del robot (en este caso, mediciones de fuerza y posición)."),
    ("IMU (Unidad de Medición Inercial)", "Dispositivo (Xsens MTI-30) que integra un giroscopio, un acelerómetro y un magnetómetro, permitiendo medir velocidades angulares, aceleraciones lineales y orientación respecto al campo magnético terrestre."),
    ("Fx, Fy, Fz", "Componentes de la fuerza medida por cada pata en los ejes X (horizontal), Y (lateral) y Z (vertical)."),
    ("Velocidad de marcha", "Frecuencia de paso o ritmo al que el robot avanza; puede estar asociada a una frecuencia en Hz."),
    ("Superficie o terreno", "Material sobre el que se desplaza el robot (por ejemplo: arena, pasto, concreto)."),
    ("Datos atípicos (outliers)", "Valores que se alejan considerablemente del comportamiento general de los datos, posiblemente por errores o condiciones especiales."),
    ("Correlación", "Relación estadística entre dos variables que indica cómo una cambia respecto a la otra."),
    ("F_L", "Pata delantera izquierda."),
    ("F_R", "Pata delantera derecha."),
    ("B_L", "Pata trasera izquierda."),
    ("B_R", "Pata trasera derecha."),
    ("Locomoción adaptable", "Capacidad del robot para ajustar su forma o manera de caminar dependiendo del terreno, buscando mantener equilibrio y eficiencia."),
    ("Estabilidad:", "Capacidad del robot para mantenerse equilibrado sin caer o perder apoyo al caminar."),
    ("Tracción", "Grado de agarre o fuerza de contacto que tiene el robot con el suelo. Una buena tracción mejora el desplazamiento y evita resbalones."),
    ("Datos cinemáticos:", "Información relacionada con el movimiento, como la posición, la velocidad o los ángulos de las patas del robot."),
    ("Ruido en los datos:", "Variaciones o errores que aparecen en las mediciones debido a interferencias o imprecisiones en los sensores."),
    ("Morfología del robot", "Hace referencia a la estructura física o forma del robot (por ejemplo, el largo de sus patas). Dyret puede modificar su morfología para adaptarse mejor."),
]

for titulo, descripcion in etapas:
    col1, col2 = st.columns([1.3, 2.7])
    with col1:
        st.markdown(f"<h4 style='margin-top:10px; color:#58A6FF';>{titulo}</h4>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<p style='text-align: justify; margin-top:10px;'>{descripcion}</p>", unsafe_allow_html=True)
    st.divider()