import pandas as pd
import altair as alt
import streamlit as st
from vega_datasets import data


# Data generators for the background
sphere = alt.sphere()
graticule = alt.graticule()

# Source of land data
source = alt.topo_feature(data.world_110m.url, "countries")

hover = alt.selection_single(on="mouseover", empty="none")

# Layering and configuring the components
background = (
    alt.layer(
        alt.Chart(sphere).mark_geoshape(fill="lightblue"),
        alt.Chart(graticule).mark_geoshape(stroke="white", strokeWidth=0.5),
        alt.Chart(source)
        .mark_geoshape(
            # fill="white",
            stroke="black",
            strokeWidth=0.15,
        )
        .encode(
            tooltip=[
                alt.Tooltip("id:N", title="Country"),
            ],
            color=alt.condition(hover, alt.value("firebrick"), alt.value("white")),
        )
        # TODO: transform country ISO id to name
        # .transform_lookup(
        #     lookup="id",
        #     from_=alt.LookupData(source, "geometries/id", ["my_id"]),
        # )
    )
    .add_selection(hover)
    .project("naturalEarth1")
    .properties(width=1200, height=800)
)

# foreground = (
#     alt.Chart(source)
#     .mark_geoshape()
#     .encode(
#         color=alt.condition(hover, alt.value("firebrick"), alt.value("white"))
#     )
#     .add_selection(hover)
# )


st.altair_chart(
    background.interactive(),
    # (background + foreground).interactive(),
    use_container_width=False,
)
