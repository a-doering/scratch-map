import pandas as pd
import altair as alt
import streamlit as st
from vega_datasets import data


@st.cache
def get_iso_names(url: str) -> pd.DataFrame:
    return pd.read_csv(url)


# Data generators for the background
sphere = alt.sphere()
graticule = alt.graticule()

# Source of land data
source = alt.topo_feature(data.world_110m.url, "countries")
iso_name_url = "https://raw.githubusercontent.com/stefangabos/world_countries/master/data/countries/en/world.csv"
country_names = get_iso_names(iso_name_url)

hover = alt.selection_single(on="mouseover", empty="none")

# Layering and configuring the components
background = (
    alt.layer(
        alt.Chart(sphere).mark_geoshape(fill="lightblue"),
        alt.Chart(graticule).mark_geoshape(stroke="white", strokeWidth=0.5),
        alt.Chart(source)
        .mark_geoshape(
            stroke="black",
            strokeWidth=0.15,
        )
        .encode(
            tooltip=[
                alt.Tooltip("name:N", title="Country"),
            ],
            color=alt.condition(hover, alt.value("firebrick"), alt.value("white")),
        )
        .transform_lookup(
            lookup="id",
            from_=alt.LookupData(country_names, "id", ["name"]),
        ),
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
