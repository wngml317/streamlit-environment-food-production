import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def run_metric() :
    df = pd.read_csv('data/Food_Production.csv')

    environment_list = ['Eutrophying emissions', 'Freshwater withdrawals', 'Land use',
                        'Greenhouse gas emissions', 'Scarcity-weighted water use']
            
    selected1 = st.sidebar.selectbox('환경적 영향', environment_list)
    st.sidebar.write('')
     
    st.markdown('#### 선택한 환경에 따른 음식의 단위별 영향')

    # 'Land use' 컬럼은 온실가스 배출량 원인 컬럼도 존재하므로
    # 단위를 포함하는 컬럼만 출력해주도록 한다.
    if selected1 == 'Land use' : 
        df_env = df.loc[:,(df.columns.str.contains(selected1)) & (df.columns.str.contains('per'))]
    else :
        df_env = df.loc[:,df.columns.str.contains(selected1)]
    
    df_env.insert(0, 'Food product', df['Food product'])
    st.dataframe(df_env)
    
    fig = px.bar(df_env, x= df_env.columns[1:], y=df_env.columns[0], width=900)
    st.plotly_chart(fig)
