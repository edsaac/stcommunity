import streamlit as st

st.set_page_config(layout="wide")

build_badges = st.session_state.build_badges

"# ✅ `streamlit-vis-timeline`"

with st.sidebar:
    "## Clicky stuff"
    st.markdown(
        build_badges(
            repo="https://github.com/giswqs/streamlit-timeline",
            stcloud="https://timeline.streamlit.app/",
            pypi="streamlit-vis-timeline"), 
            unsafe_allow_html=True)

with st.echo(code_location="below"):
    from streamlit_timeline import st_timeline

    items = [
    {"id": 1, "content": "2022-10-20", "start": "2022-10-20"},
    {"id": 2, "content": "2022-10-09", "start": "2022-10-09"},
    {"id": 3, "content": "2022-10-18", "start": "2022-10-18"},
    {"id": 4, "content": "2022-10-16", "start": "2022-10-16"},
    {"id": 5, "content": "2022-10-25", "start": "2022-10-25"},
    {"id": 6, "content": "2022-10-27", "start": "2022-10-27"},
    ]

    timeline = st_timeline(items, groups=[], options={}, height="300px")
    
    "**Selected item:**"
    st.write(timeline)
    "*****"

