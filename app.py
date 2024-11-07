import streamlit as st

# .\venv\Scripts\activate
# streamlit run app.py
# git add x.x
# git add .
# git commit -m "text"
# git push origin main

# https://www.markdownguide.org/basic-syntax/

import streamlit as st
st.set_page_config(layout="wide")

# Add custom CSS for breadcrumb-style buttons

st.markdown(
    """
    <style>
    .breadcrumb-container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 5px;
    }
    .breadcrumb {
        font-size: 1.2em;
        color: #005E87;
        background-color: #ffffff;
        border: 1px solid #005E87;
        padding: 2px 2px;
        border-radius: 2px;
        text-decoration: none;
    }
    .breadcrumb:hover {
        background-color: #005E87;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Breadcrumb buttons container
st.markdown(
    """
    <div class="breadcrumb-container">
        <a href="#" class="breadcrumb">← Jupiter</a>
        <a href="#" class="breadcrumb">Uranus →</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .title {
        font-size: 2.5em;
        text-align: left;
        color: #005E87; 
        background-color: white; 
        padding: 5px;
        margin-top: -5px;
    }
    .subtitle {
        font-size: 1.2em;
        text-align: left;
        color: #005E87;
        background-color: white;
        padding: 5px;
        margin-top: -15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and subtitle text
st.markdown('<div class="title"><b>Ewell Astronomical Society</b></div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Nonsuch Park Solar System Walk</div>', unsafe_allow_html=True)

# col1, col2 = st.columns(2)
col1, colblank, col2 = st.columns([1, 0.1, 1])

with col1.container():
    sub_col1, sub_col2 = st.columns(2)  # Inner layout with two columns

    # Content in the nested container's columns
    sub_col1.image('Saturn.png', caption="Saturn (Image from NASA)")
    sub_col2.write("""
        Saturn is the 6th planet from the Sun, 1.4 billion km away from it - 10 times the Earth’s distance. It has a \
        squashed shape, with a diameter of 120,536 km at the equator but only 108,728 km at the poles. The Earth's \
        diameter is 12,756 km, so Astronomers usually use an average, and estimate Saturn is about 9 times wider than Earth.
    """)

# col1.image('Saturn.png', caption = "Saturn (Image from NASA)", width=250)
# col1.html("Saturn has a squashed shape, it's diameter is 120,536 kilometers at the equator \
#           and 108,728 kilometers at the poles, so it's shaped more like a rugby ball than a football. \
#           The Earth is also squashed, but only by a little. At the equator our diameter is \
#           12,756 kilometers, at the poles it's 12,725, so not even the distance of a marathon. \
#           Astronomers usual estimate that Saturn is 9 times wider than the Earth.")
col1.html("Saturn is well knowm for it's icy rings, which extend to 280,000 km. The rings are up to 9 meters thick. \
          Even through a small telescope Saturn is an amazing sight. The rings were first observed over 400 years \
          ago soon after the invention of the telescope. Although the other giant planets also have ring systems, \
          they are not easily seen and were all discovered within the last 50 years.")

# Basic facts
# Diameter (1) kms (2) Earth radii
# Mass – Earth masses
# Distance from the Sun
# Year
# Day
# Number of moons')

# Example image and text with HTML and CSS for text wrapping
st.markdown(
    """
    <style>
    .image-wrap {
        float: left; /* Float image to the left to allow text wrapping */
        margin: 0 15px 10px 0; /* Adds space around the image */
        width: 200px; /* Set image width */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# # Display the image with wrapping text
# col2.html(
#     """
#     <div>
#         <img src="FunFact.png" class="image-wrap">
#         <p>
#             This is a sample paragraph that will flow around the image. The CSS float property allows the text to wrap around the image seamlessly. 
#             You can add as much text as needed here, and it will naturally fill the space to the right of the image. This setup is ideal for adding descriptions 
#             or explanations alongside images in a visually appealing format.
#         </p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

col2.html("Saturn currently over 145 known moons, of which, Titan is the largest.  \
          At over 5,000 kilometres in diameter Titan is larger than the planet Mercury and is only \
          just beaten by Jupiter’s moon Ganymede to the title of the solar system’s largest moon.  \
          Titan is also the most distant object that man has landed a spacecraft on – the \
          European Space Agency’s Huygens probe in 2005.  \
          Titan has a thick atmosphere mostly made of nitrogen, like the Earth.  \
          However, although Titan also has liquid on its surface, it is not liquid water, \
          but liquid methane and ethane.")
col2.image('FunFact.png', width=350)  # Adjust the width as needed
