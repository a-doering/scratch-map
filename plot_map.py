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
background = (
    alt.layer(
        alt.Chart(sphere).mark_geoshape(fill="lightblue"),
        alt.Chart(graticule).mark_geoshape(stroke="white", strokeWidth=0.5),
        alt.Chart(source)
        .mark_geoshape(
            fill="white",
            stroke="black",
            strokeWidth=0.15,
        )
        .encode(
            tooltip=[
                alt.Tooltip("id:N", title="Country"),
            ],
        )
        # TODO: transform country ISO id to name
        # .transform_lookup(
        #     lookup="id",
        #     from_=alt.LookupData(source, "geometries/id", ["my_id"]),
        # )
    )
    .project("naturalEarth1")
    .properties(width=1200, height=800)
    .interactive()
)


# TODO: change color on mouseover
# color=alt.condition(highlight, alt.value("red"), alt.value("beige")),
# .add_selection(highlight)

foreground = (
    alt.Chart(source)
    .mark_geoshape()
    .encode(color=alt.condition(highlight, "id", alt.value("white")))
    .add_selection(highlight)
    .interactive()
)


st.altair_chart(
    background,
    # (background + foreground),
    use_container_width=False,
)
