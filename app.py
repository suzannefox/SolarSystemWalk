import streamlit as st

# .\venv\Scripts\activate



st.title("Exploring Saturn")
st.write("This is a simple Streamlit app to learn about the planet Saturn.")

st.image("https://upload.wikimedia.org/wikipedia/commons/c/c7/Saturn_during_Equinox.jpg",
         caption="Saturn", use_column_width=True)
st.markdown("""
## Facts about Saturn
- It is the sixth planet from the Sun.
- Saturn has a ring system composed mainly of ice particles and rocky debris.
- There are 57 moons.
- It is a gas giant, like Jupiter.
""")
