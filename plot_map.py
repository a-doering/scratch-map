import pandas as pd
import altair as alt
import streamlit as st
from vega_datasets import data


# Data generators for the background
sphere = alt.sphere()
graticule = alt.graticule()

# Source of land data
source = alt.topo_feature(data.world_110m.url, "countries")

# Layering and configuring the components
layers = alt.layer(
    alt.Chart(sphere).mark_geoshape(fill="lightblue"),
    alt.Chart(graticule).mark_geoshape(stroke="white", strokeWidth=0.5),
    alt.Chart(source).mark_geoshape(
        fill="ForestGreen", stroke="black", strokeWidth=0.15
    ),
).project("naturalEarth1")

st.altair_chart(layers.interactive(), use_container_width=True)
