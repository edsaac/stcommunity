import streamlit as st
from mytools import build_badges

if "build_badges" not in st.session_state:
    st.session_state.build_badges = build_badges