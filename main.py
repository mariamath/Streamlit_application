import streamlit as st
import pandas as pd
import plotly_express as px
import seaborn as sns
from matplotlib import pyplot as plt

df = st.cache_data(pd.read_csv)("df_new.csv")
cat_names=["GENDER", "SOCSTATUS_WORK_FL", "SOCSTATUS_PENS_FL", "TARGET"]
for name in cat_names:
    df[name]=df[name].astype("object")

what_to_display = st.sidebar.selectbox("Choose a data to display", ["Main characteristics", "Show histogram", "Heatmap", "Pairwise plots", "Dependence of target on a current feature"])



if what_to_display in ["Main characteristics", "Show histogram"]:
    col = st.sidebar.selectbox("Choose a column", df.columns[2:])
    if what_to_display == "Main characteristics":
        st.write(df[col].describe())
    elif what_to_display == "Show histogram":
        fig = px.histogram(df, x=col)
        fig.update_layout(bargap=0.1)
        st.plotly_chart(fig)
df1=df.iloc[:, 2:]
if what_to_display == "Heatmap":
    fig, ax = plt.subplots()
    sns.heatmap(df1.select_dtypes(include="number").corr(), annot=True, vmin=-1, vmax=1, center=0, ax=ax)
    st.pyplot(fig)

if what_to_display == "Pairwise plots":
    col_1 = st.sidebar.selectbox("Choose first ax", df.columns[2:])
    col_2 = st.sidebar.selectbox("Choose second column", df.columns[2:])
    fig = px.scatter(df, x = col_1, y=col_2)
    st.plotly_chart(fig)

if what_to_display == "Dependence of target on a current feature":
    col_3 = st.sidebar.selectbox("Choose a current feature", df.drop("TARGET", axis=1).columns[2:])
    fig, ax = plt.subplots()
    sns.violinplot(data=df, x=col_3, y="TARGET", hue="TARGET", orient="h", ax=ax)
    st.pyplot(fig)
