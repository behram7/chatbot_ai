import streamlit as st
from streamlit_lottie import st_lottie
import json

def render_lottie_animation(path: str, height=250):
    with open(path, "r") as file:
        lottie_json = json.load(file)
        st_lottie(lottie_json, height=height)
