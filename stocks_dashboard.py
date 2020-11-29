import streamlit as st
import pandas as pd
import plotly_express as px

@st.cache
def load_data():
    """Utility function"""
    df = pd.read_csv("all_stocks_5yr.csv", index_col='date')

    numeric_df = df.select_dtypes(['float', 'int'])
    numeric_cols = numeric_df.columns

    text_df = df.select_dtypes(['object'])
    text_columns = text_df.columns

    stock_column = df['Name']

    unique_stocks = stock_column.unique()

    return  df, numeric_cols, text_columns, unique_stocks


df, numeric_cols, text_columns, unique_stocks = load_data()


st.title("Stocks Dashboard")


# add a checkbox to sidebar
check_box = st.sidebar.checkbox(label="Display the Dataset")

print(check_box)

if check_box:
    st.write(df)


# title for side bar
st.sidebar.title("Settings")
# add a subheader
st.sidebar.subheader("Timeseries settings")

# multiselect
feature_selection = st.sidebar.multiselect(label="Features to plot",
                                           options=numeric_cols)

# add a select box for stock tickers
stock_ticker =st.sidebar.selectbox(label="Stock Ticker ", options=unique_stocks)

print(feature_selection)

print(stock_ticker)

# index the dataframe based on the selected stock ticker
stock_df = df[df['Name']==stock_ticker]

try:
    # plotly express line chart
    plotly_figure = px.line(
        data_frame=stock_df,
        x=stock_df.index,
        y=feature_selection,
        title="Timeline of " + str(stock_ticker) + "prices."
    )

    # visualize the chart
    st.plotly_chart(plotly_figure)

except Exception as e :
    print(e)