import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run_search() :
    df = pd.read_csv('data/Food_Production.csv')

    environment_list = ['Eutrophying emissions', 'Freshwater withdrawals', 'Land use',
                        'Greenhouse gas emissions', 'Scarcity-weighted water use']
        
    metric_list = ['per kilogram', 'per 100g protein', 'per 1000kcal']

    selected1 = st.sidebar.selectbox('환경적 영향', environment_list)
    st.sidebar.write('')

    if selected1 == 'Greenhouse gas emissions' :
        selected2 = st.sidebar.radio('Metric', metric_list[1:])

    else :
        selected2 = st.sidebar.radio('Metric', metric_list)

    df_impact = df.loc[ :, (df.columns.str.contains(selected1)) & (df.columns.str.contains(selected2))]
    df_impact.insert(0, 'Food product', df['Food product'])

    st.markdown('#### 선택한 환경에 가장 많은 영향을 주는 음식')
    # st.dataframe(sorted(df_impact.values, reverse=True))
    
    df_impact = df_impact.sort_values(df_impact.columns[1], ascending=False)
    st.dataframe(df_impact)

    df_impact = df_impact.sort_values(df_impact.columns[1]).head(12)
    fig = px.bar(df_impact, x= df_impact.columns[1], y=df_impact.columns[0])
    st.plotly_chart(fig)

    # 음식 검색
    st.sidebar.markdown('\n')
    st.sidebar.markdown('\n')
    search_food = st.sidebar.text_input('음식 검색', placeholder='영어로 음식을 입력하세요.')
    if len(search_food) != 0 :
        search_df = df.loc[df['Food product'].str.lower().str.contains(search_food), ]
        st.dataframe(search_df)