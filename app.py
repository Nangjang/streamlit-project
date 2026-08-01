import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------- Page Configuration --------------------
st.set_page_config(layout="wide", page_title="Startup Analysis")

# -------------------- Load Data --------------------
funding_df = pd.read_csv("startup_cleaned.csv")

funding_df["date"] = pd.to_datetime(funding_df["date"], errors="coerce")
funding_df["month"] = funding_df["date"].dt.month
funding_df["year"] = funding_df["date"].dt.year


# ==========================================================
# Overall Analysis
# ==========================================================
def show_overall_analysis():

    st.title("Overall Analysis")

    # Metrics
    total_funding = round(funding_df["amount"].sum())

    highest_single_funding = (
        funding_df.groupby("startup")["amount"]
        .max()
        .sort_values(ascending=False)
        .iloc[0]
    )

    average_startup_funding = (
        funding_df.groupby("startup")["amount"]
        .sum()
        .mean()
    )

    total_startups = funding_df["startup"].nunique()

    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

    with metric_col1:
        st.metric("Total", f"{total_funding} Cr")

    with metric_col2:
        st.metric("Max", f"{highest_single_funding} Cr")

    with metric_col3:
        st.metric("Average", f"{round(average_startup_funding)} Cr")

    with metric_col4:
        st.metric("Funded Startups", total_startups)

    # -------------------- Month-on-Month Graph --------------------
    st.header("Month-on-Month Analysis")

    graph_type = st.selectbox("Select Type", ["Total", "Count"])

    if graph_type == "Total":
        monthly_df = (
            funding_df.groupby(["year", "month"])["amount"]
            .sum()
            .reset_index()
        )
    else:
        monthly_df = (
            funding_df.groupby(["year", "month"])["amount"]
            .count()
            .reset_index()
        )

    monthly_df["x_axis"] = (
        monthly_df["month"].astype(str)
        + "-"
        + monthly_df["year"].astype(str)
    )

    mom_fig, mom_ax = plt.subplots()
    mom_ax.plot(monthly_df["x_axis"], monthly_df["amount"])

    st.pyplot(mom_fig)


# ==========================================================
# Investor Analysis
# ==========================================================
def show_investor_analysis(investor_name):

    st.title(investor_name)

    # Recent investments
    recent_investments_df = (
        funding_df[funding_df["investors"].str.contains(investor_name)]
        .head()[["date", "startup", "vertical", "city", "round", "amount"]]
    )

    st.subheader("Most Recent Investments")
    st.dataframe(recent_investments_df)

    left_col, right_col = st.columns(2)

    # Biggest investments
    with left_col:

        top_startups_series = (
            funding_df[funding_df["investors"].str.contains(investor_name)]
            .groupby("startup")["amount"]
            .sum()
            .sort_values(ascending=False)
            .head()
        )

        st.subheader("Biggest Investments")

        bar_fig, bar_ax = plt.subplots()
        bar_ax.bar(top_startups_series.index, top_startups_series.values)

        st.pyplot(bar_fig)

    # Sector-wise investment
    with right_col:

        sector_series = (
            funding_df[funding_df["investors"].str.contains(investor_name)]
            .groupby("vertical")["amount"]
            .sum()
        )

        st.subheader("Sectors Invested In")

        pie_fig, pie_ax = plt.subplots()
        pie_ax.pie(
            sector_series,
            labels=sector_series.index,
            autopct="%0.1f%%",
        )

        st.pyplot(pie_fig)

    # Year-wise investment
    yearly_investment_series = (
        funding_df[funding_df["investors"].str.contains(investor_name)]
        .groupby("year")["amount"]
        .sum()
    )

    st.subheader("Year-on-Year Investment")

    line_fig, line_ax = plt.subplots()
    line_ax.plot(
        yearly_investment_series.index,
        yearly_investment_series.values,
    )

    st.pyplot(line_fig)


# ==========================================================
# Sidebar
# ==========================================================
st.sidebar.title("Startup Funding Analysis")

analysis_type = st.sidebar.selectbox(
    "Select Analysis",
    ["Overall Analysis", "StartUp", "Investor"],
)

if analysis_type == "Overall Analysis":

    show_overall_analysis()

elif analysis_type == "StartUp":

    selected_startup = st.sidebar.selectbox(
        "Select StartUp",
        sorted(funding_df["startup"].unique())
    )

    show_startup_btn = st.sidebar.button("Find StartUp Details")

    st.title("StartUp Analysis")

else:

    investor_name = st.sidebar.selectbox(
        "Select Investor",
        sorted(set(funding_df["investors"].str.split(",").sum()))
    )

    show_investor_btn = st.sidebar.button("Find Investor Details")

    if show_investor_btn:
        show_investor_analysis(investor_name)