import streamlit as st
from streamlit_custom_toggle import st_custom_toggle

build_badges = st.session_state.build_badges

"# ⛔ `streamlit-custom-toggle`"

with st.sidebar:
    "## Clicky stuff"
    st.markdown(
        build_badges(
            repo="https://github.com/ShruAgarwal/streamlit-custom-toggle",
            post="https://discuss.streamlit.io/t/streamlit-custom-toggle-a-custom-component-to-load-heart-shaped-toggle-switch-widget/32499",
            pypi="streamlit-custom-toggle"), 
            unsafe_allow_html=True)

with st.echo(code_location="below"):

    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        calm = st_custom_toggle(
            'Calm', 
            active_track_fill="#EAE4E4", 
            active_thumb_color="#EAE4E4", 
            value="true", 
            key="toggle1")  # Disabled toggle switch

    with col2:
        fun = st_custom_toggle(
            'Fun', 
            active_track_fill="#57FD6E", 
            active_thumb_color="#EAE4E4", 
            key="toggle2")

    with col3:
        rock = st_custom_toggle(
            'Rock', 
            active_track_fill="#FF5733", 
            active_thumb_color="#900C3F")

    # "👇 Component is not returning its state ⛔⛔"
    st.code(f"Calm = {calm}, Fun = {fun}, Rock = {rock}")
    "****"