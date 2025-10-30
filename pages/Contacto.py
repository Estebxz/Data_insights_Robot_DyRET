import streamlit as st
from components.UI.star_github import footer_component

equipo = [
    {
        "nombre": "Kevin Ángel",
        "cargo": "Analista de datos",
        "descripcion": "Analista de datos, tengo experiencia en Python, SQL y visualización de datos. Me encanta transformar datos complicados en información sencilla y útil para facilitar la toma de decisiones en el ámbito empresarial.",
        "imagen": "public/images/team_kevin_angel.jpg",
        "linkedin": "https://www.linkedin.com/in/kevin-%C3%A1ngel-12ba44349?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
        "github": "https://github.com/kevin69Angel"
    },
    {
        "nombre": "Maria Paula Iglesias",
        "cargo": "Ingeniera mecatronica",
        "descripcion": "Ingeniera en mecatrónica con experiencia en electrónica, robótica, programación y automatización. Desarrollo soluciones innovadoras y contribuyo a equipos colaborativos y multidisciplinarios, aportando un sólido liderazgo, eficiencia organizativa y habilidades para la resolución de problemas.",
        "imagen": "public/images/team_maria_paula.jpg",
        "linkedin": "https://www.linkedin.com/in/maria-paula-iglesias-gonz%C3%A1lez?utm_source",
    },
    {
        "nombre": "Maria Cristina Her.",
        "cargo": "Jefa de Producto",
        "descripcion": "Profesional en administración de empresas, experiencia en la gestión de productos, el desarrollo de estrategias de mercado y el liderazgo de equipos diversos. Desarrollo de soluciones innovadoras con las expectativas de los clientes y que, al mismo tiempo, generen valor para la empresa.",
        "imagen": "public/images/team_maria_cristina.jpg",
        "linkedin": "https://www.linkedin.com/in/cristina-hernandez-bb160a362/",
    },
    {
        "nombre": "Joan Esteban Mendéz",
        "cargo": "Desarrollador Frontend",
        "descripcion": "Desarrollador web frontend con experiencia en React, JavaScript, HTML y CSS. Creacion de interfaces de usuario atractivas y funcionales, con un enfoque en la experiencia del usuario y el diseño responsivo.",
        "imagen": "public/images/team_joan_esteban.jpg",
        "linkedin": "https://www.linkedin.com/in/martinez-esteban/",
        "github": "https://github.com/Estebxz"
    },
]

st.title("CONTACTOS")

for i in range(0, len(equipo), 2):
    col1, col2 = st.columns([1, 1])
    
    for col, miembro in zip([col1, col2], equipo[i:i+2]):
        with col:
            with st.container(border=True): 
                st.image(miembro['imagen'], width="content", output_format="JPEG")
                st.subheader(f"{miembro['nombre']}")
                st.markdown(
                    f"""
                    <div style='display: flex; justify-content: left; align-items: left;'>
                    <span style='color:#5865F2; text-transform:capitalize; font-weight:600; font-size:18.5px;'>{miembro['cargo']}
                        </span>
                    </div>""",
                    unsafe_allow_html=True)     
                st.markdown(
                    f"""
                    <div style='min-height: 50px; margin-bottom: 1rem;'>
                        <p style='display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; text-overflow: ellipsis;'>
                            {miembro['descripcion']}
                        </p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                col_btn1, col_btn2 = st.columns([1, 1.6], vertical_alignment="top", gap="small")
                with col_btn1:
                    st.link_button(
                        label="💼 Linkedin",
                        url=miembro['linkedin'],
                        type="secondary",
                        help="Visitar perfil de LinkedIn"
                    )
                with col_btn2:
                    if 'github' in miembro and miembro['github']:
                        st.link_button(
                            label="🔗 GitHub",
                            url=miembro['github'],
                            type="secondary",
                            help="Visitar perfil de GitHub"
                        )
footer_component()