import json
from pathlib import Path

import pandas as pd
import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Orbit Intelligence",
    page_icon="🤖",
    layout="wide",
)


# =========================================================
# CONSTANTS
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent

ENTITIES_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "entities.json"
)

RELATIONSHIPS_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "relationships.json"
)


# =========================================================
# LOAD JSON DATA
# =========================================================

@st.cache_data
def load_json(file_path):

    if not file_path.exists():
        return []

    try:
        with file_path.open(
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except Exception as error:
        st.error(
            f"Could not read {file_path}: {error}"
        )
        return []


entities = load_json(
    ENTITIES_FILE
)

relationships = load_json(
    RELATIONSHIPS_FILE
)


# =========================================================
# HEADER
# =========================================================

st.title(
    "🤖 AI Orbit Intelligence Platform"
)

st.markdown(
    """
    ### Multi-Source AI Ecosystem Intelligence

    Explore AI **companies, models, repositories, news,
    MCP servers, and tools** collected and processed
    through the AI Orbit data pipeline.
    """
)


# =========================================================
# DATA AVAILABILITY CHECK
# =========================================================

if not ENTITIES_FILE.exists():

    st.error(
        "entities.json was not found."
    )

    st.code(
        str(ENTITIES_FILE)
    )

    st.stop()


if not entities:

    st.warning(
        "No entity data is available."
    )

    st.stop()


# =========================================================
# DATAFRAME
# =========================================================

entity_df = pd.DataFrame(
    entities
)


# =========================================================
# NORMALIZE COLUMNS
# =========================================================

required_columns = [
    "id",
    "entity_type",
    "name",
    "description",
    "url",
    "categories",
    "source",
]


for column in required_columns:

    if column not in entity_df.columns:

        entity_df[column] = None


# Convert source object into readable source name

def get_source_name(source):

    if isinstance(source, dict):
        return source.get(
            "name",
            ""
        )

    return ""


entity_df["source_name"] = (
    entity_df["source"]
    .apply(get_source_name)
)


# Convert categories into text

def get_categories(value):

    if isinstance(value, list):
        return ", ".join(
            str(item)
            for item in value
        )

    if value is None:
        return ""

    return str(value)


entity_df["categories_text"] = (
    entity_df["categories"]
    .apply(get_categories)
)


# =========================================================
# STATISTICS
# =========================================================

total_entities = len(
    entity_df
)

total_relationships = len(
    relationships
)

total_entity_types = (
    entity_df["entity_type"]
    .nunique()
)


total_sources = (
    entity_df["source_name"]
    .replace("", pd.NA)
    .dropna()
    .nunique()
)


# =========================================================
# TOP METRICS
# =========================================================

col1, col2, col3, col4 = st.columns(
    4
)

with col1:

    st.metric(
        "Total Entities",
        total_entities
    )


with col2:

    st.metric(
        "Relationships",
        total_relationships
    )


with col3:

    st.metric(
        "Entity Types",
        total_entity_types
    )


with col4:

    st.metric(
        "Data Sources",
        total_sources
    )


st.divider()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title(
    "🔎 Explore AI Ecosystem"
)


search_text = st.sidebar.text_input(
    "Search entities",
    placeholder=(
        "Search OpenAI, AI model, MCP..."
    )
)


available_types = sorted(
    entity_df[
        "entity_type"
    ]
    .dropna()
    .unique()
    .tolist()
)


selected_types = st.sidebar.multiselect(
    "Entity Type",
    available_types,
    default=available_types
)


available_sources = sorted(
    entity_df[
        "source_name"
    ]
    .replace("", pd.NA)
    .dropna()
    .unique()
    .tolist()
)


selected_sources = st.sidebar.multiselect(
    "Source",
    available_sources,
    default=available_sources
)


# =========================================================
# FILTER DATA
# =========================================================

filtered_df = entity_df.copy()


# Entity type filter

if selected_types:

    filtered_df = filtered_df[
        filtered_df[
            "entity_type"
        ].isin(
            selected_types
        )
    ]


# Source filter

if selected_sources:

    filtered_df = filtered_df[
        filtered_df[
            "source_name"
        ].isin(
            selected_sources
        )
    ]


# Search filter

if search_text:

    search = (
        search_text
        .strip()
        .lower()
    )

    name_match = (
        filtered_df["name"]
        .fillna("")
        .astype(str)
        .str.lower()
        .str.contains(
            search,
            na=False
        )
    )

    description_match = (
        filtered_df["description"]
        .fillna("")
        .astype(str)
        .str.lower()
        .str.contains(
            search,
            na=False
        )
    )

    category_match = (
        filtered_df[
            "categories_text"
        ]
        .fillna("")
        .astype(str)
        .str.lower()
        .str.contains(
            search,
            na=False
        )
    )

    filtered_df = filtered_df[
        name_match
        | description_match
        | category_match
    ]


# =========================================================
# FILTER RESULT
# =========================================================

st.subheader(
    "🔍 Search Results"
)

st.write(
    f"Showing **{len(filtered_df)}** "
    f"of **{total_entities}** entities."
)


# =========================================================
# ENTITY DISTRIBUTION
# =========================================================

st.subheader(
    "📊 Entity Distribution"
)


if not filtered_df.empty:

    distribution = (
        filtered_df[
            "entity_type"
        ]
        .value_counts()
    )

    st.bar_chart(
        distribution
    )

else:

    st.info(
        "No data available for the "
        "selected filters."
    )


# =========================================================
# ENTITY TABLE
# =========================================================

st.subheader(
    "📋 Entity Explorer"
)


if not filtered_df.empty:

    table_df = filtered_df[
        [
            "entity_type",
            "name",
            "description",
            "url",
            "source_name",
            "categories_text",
        ]
    ].copy()

    table_df.columns = [
        "Type",
        "Name",
        "Description",
        "URL",
        "Source",
        "Categories",
    ]

    st.dataframe(
        table_df,
        use_container_width=True,
        hide_index=True,
    )

else:

    st.warning(
        "No entities match your search."
    )


# =========================================================
# ENTITY DETAILS
# =========================================================

st.divider()

st.subheader(
    "📄 Entity Details"
)


if not filtered_df.empty:

    entity_names = (
        filtered_df["name"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_entity_name = st.selectbox(
        "Select an entity",
        entity_names
    )

    selected_rows = filtered_df[
        filtered_df["name"].astype(str)
        == selected_entity_name
    ]

    if not selected_rows.empty:

        entity = (
            selected_rows
            .iloc[0]
            .to_dict()
        )

        col1, col2 = st.columns(
            2
        )

        with col1:

            st.markdown(
                "**Entity Type**"
            )

            st.write(
                entity.get(
                    "entity_type",
                    ""
                )
            )

            st.markdown(
                "**Name**"
            )

            st.write(
                entity.get(
                    "name",
                    ""
                )
            )

            st.markdown(
                "**Description**"
            )

            st.write(
                entity.get(
                    "description",
                    ""
                )
                or "No description available."
            )

        with col2:

            st.markdown(
                "**Source**"
            )

            st.write(
                entity.get(
                    "source_name",
                    ""
                )
            )

            st.markdown(
                "**Categories**"
            )

            st.write(
                entity.get(
                    "categories_text",
                    ""
                )
                or "No categories available."
            )

            url = entity.get(
                "url"
            )

            if (
                url
                and str(url) != "nan"
            ):

                st.markdown(
                    f"[🔗 Open Entity Source]({url})"
                )


# =========================================================
# RELATIONSHIPS
# =========================================================

st.divider()

st.subheader(
    "🔗 Relationship Explorer"
)


if relationships:

    relationship_df = pd.DataFrame(
        relationships
    )

    relationship_types = sorted(
        relationship_df[
            "relationship"
        ]
        .dropna()
        .unique()
        .tolist()
    )

    selected_relationship = st.selectbox(
        "Relationship Type",
        ["All"]
        + relationship_types
    )

    filtered_relationships = (
        relationship_df.copy()
    )

    if (
        selected_relationship
        != "All"
    ):

        filtered_relationships = (
            filtered_relationships[
                filtered_relationships[
                    "relationship"
                ]
                == selected_relationship
            ]
        )

    st.write(
        f"Showing "
        f"**{len(filtered_relationships)}** "
        f"relationships."
    )

    st.dataframe(
        filtered_relationships,
        use_container_width=True,
        hide_index=True,
    )

else:

    st.info(
        "No evidence-backed relationships "
        "are available yet."
    )


# =========================================================
# DATA QUALITY SUMMARY
# =========================================================

st.divider()

st.subheader(
    "✅ Data Quality"
)


missing_names = int(
    entity_df[
        "name"
    ]
    .fillna("")
    .astype(str)
    .str.strip()
    .eq("")
    .sum()
)


missing_sources = int(
    entity_df[
        "source_name"
    ]
    .fillna("")
    .astype(str)
    .str.strip()
    .eq("")
    .sum()
)


duplicate_ids = int(
    entity_df["id"]
    .duplicated()
    .sum()
)


quality_col1, quality_col2, quality_col3 = (
    st.columns(3)
)


with quality_col1:

    st.metric(
        "Missing Names",
        missing_names
    )


with quality_col2:

    st.metric(
        "Missing Sources",
        missing_sources
    )


with quality_col3:

    st.metric(
        "Duplicate IDs",
        duplicate_ids
    )


if (
    missing_names == 0
    and missing_sources == 0
    and duplicate_ids == 0
):

    st.success(
        "Dataset quality checks passed."
    )

else:

    st.warning(
        "Some data quality issues require review."
    )


# =========================================================
# DOWNLOAD SECTION
# =========================================================

st.divider()

st.subheader(
    "⬇️ Download Dataset"
)


download_col1, download_col2 = (
    st.columns(2)
)


with download_col1:

    json_data = json.dumps(
        entities,
        indent=2,
        ensure_ascii=False
    )

    st.download_button(
        label="⬇️ Download Entities JSON",
        data=json_data,
        file_name="entities.json",
        mime="application/json",
    )


with download_col2:

    csv_df = entity_df[
        [
            "id",
            "entity_type",
            "name",
            "description",
            "url",
            "source_name",
            "categories_text",
        ]
    ].copy()

    csv_data = csv_df.to_csv(
        index=False
    )

    st.download_button(
        label="⬇️ Download Entities CSV",
        data=csv_data,
        file_name="entities.csv",
        mime="text/csv",
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "AI Orbit Intelligence Platform | "
    "Multi-source AI ecosystem discovery, "
    "entity resolution and relationship analysis"
)