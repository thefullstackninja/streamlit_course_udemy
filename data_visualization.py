import streamlit as st
import plotly_express as px
import pandas as pd

# add a title
st.title("Data Visualization App")

# add a sub header in the sidebar
st.sidebar.subheader("Visualization Settings")

# add a file uploader
uploaded_file = st.sidebar.file_uploader(
    label="Upload your CSV or Excel file here",
    type=['csv','xlsx']
)

# would you like to display the dataset?
display_data = st.sidebar.checkbox(
    label="Would you like to view the uploaded dataset?")

global df
global numeric_columns
global non_numeric_columns
# account for cases where uploaded file is not None
if uploaded_file is not None:
    # try:
    df = pd.read_csv(uploaded_file)

    uploaded_file.seek(0)

    # except Exception as e:
    #     print(e)
    #     df = pd.read_excel(uploaded_file)

    if display_data:
        st.write(df)

    # extract numeric columns as a list
    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)

    # extract the non numeric columns
    non_numeric_columns = list(df.select_dtypes(['object']).columns)

    # st.write(numeric_columns)
    # st.write(non_numeric_columns)

# add a select widget
chart_select = st.sidebar.selectbox(
    label="Select the Visualization type.",
    options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplots']
)

try:
    if chart_select == 'Scatterplots':
        st.sidebar.subheader("Settings for Scatterplot")
        x_value = st.sidebar.selectbox(label="X axis",
                                       options=numeric_columns)
        y_value = st.sidebar.selectbox(label="Y axis",
                                       options=numeric_columns)

        specify_color = st.sidebar.checkbox(
            label="Would you like to specify the color?")

        if specify_color:
            color_value = st.sidebar.selectbox(label="Color",
                                           options=non_numeric_columns)
            plot = px.scatter(data_frame=df, x=x_value,
                              y=y_value, color=color_value)

        else:
            plot = px.scatter(data_frame=df, x=x_value,
                              y=y_value)

        # display chart in streamlit
        st.plotly_chart(plot)

    if chart_select == 'Histogram':
        st.sidebar.subheader("Settings for Histogram")
        x = st.sidebar.selectbox(label="Feature",
                                       options=numeric_columns)
        bin_size = st.sidebar.slider(label="Number of bins",
                                     min_value=10,
                                     max_value=100,
                                     value=50)
        plot = px.histogram(data_frame=df, x=x, nbins=bin_size)
        st.plotly_chart(plot)

    if chart_select=='Lineplots':
        st.sidebar.subheader("Settings for Line plots.")
        x_value =st.sidebar.selectbox(label='X axis', options=numeric_columns)
        y_value = st.sidebar.selectbox(label='Y axis', options=numeric_columns)

        plot = px.line(data_frame=df, x=x_value, y=y_value)

        # display the chart
        st.plotly_chart(plot)





except Exception as e:
    print(e)








