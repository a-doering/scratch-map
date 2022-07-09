import pandas as pd
import altair as alt
import streamlit as st
from vega_datasets import data


# Data generators for the background
sphere = alt.sphere()
graticule = alt.graticule()

# Source of land data
source = alt.topo_feature(data.world_110m.url, "countries")

highlight = alt.selection_single(on="mouseover", fields=["id"], empty="none")

# Layering and configuring the components
layers = alt.layer(
    alt.Chart(sphere).mark_geoshape(fill="lightblue"),
    alt.Chart(graticule).mark_geoshape(stroke="white", strokeWidth=0.5),
    alt.Chart(source)
    .mark_geoshape(
        fill="ForestGreen",
        # TODO: change color on mouseover
        # color=alt.condition(highlight, alt.value("red"), alt.value("beige")),
        stroke="black",
        strokeWidth=0.15,
    )
    .encode(
        tooltip=[
            alt.Tooltip("id:N", title="Country"),
        ]
    )
    .add_selection(highlight)
    # TODO: transform country ISO id to name
    # .transform_lookup(
    #     lookup="id",
    #     from_=alt.LookupData(source, "geometries/id", ["my_id"]),
    # )
).project("naturalEarth1")

st.altair_chart(layers.interactive(), use_container_width=False)
