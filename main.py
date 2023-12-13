import model
import inference_mamdani
import fuzzy_operators
import streamlit as st
import numpy as np
import pandas as pd
import mymodel

crisp = []
transportation = "Walk"
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        height = int(st.text_input(f"Distance", "0"))
        distance = int(st.text_input(f"Height Gain", "0"))
        crisp.append(distance)
        crisp.append(height)
        pass
    with col2:

        road_quality = int(st.text_input(f"Road Quality", "0"))
        crisp.append(road_quality)
        transportation = st.selectbox(
            "Transportation Type", ("Walk", "Ride")
        )
        pass

print(transportation)
inference_mamdani.preprocessing(
        mymodel.input_lvs[transportation], mymodel.output_lv[transportation]
    )

num, val = inference_mamdani.process(
    mymodel.input_lvs[transportation],
    mymodel.output_lv[transportation],
    mymodel.rule_base,
    crisp,
)

print(num, val)

st.text("Road points: " + str(num))
st.text("Road appealing: " + str(val))








