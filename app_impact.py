import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def run_impact() :
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

    st.markdown('#### 선택한 환경에 가장 많은 영향을 주는 음식 TOP12')
    st.markdown('\n')
    
    df_impact = df_impact.sort_values(df_impact.columns[1], ascending=False).head(12)
    st.dataframe(df_impact)

    
    df_impact = df_impact.sort_values(df_impact.columns[1]).head(12)
    fig = px.bar(df_impact, x= df_impact.columns[1], y=df_impact.columns[0])
    st.plotly_chart(fig)


    st.markdown('#### 온실가스 배출량 원인 비율')
    with st.expander('📌 확인하기'):
        
        fig2 = plt.figure()
        df_chart = df.iloc[:,1:8].sum()
        plt.pie(df_chart.values, labels=df_chart.index, autopct='%.1f%%')
        
        st.pyplot(fig2)