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

    # greenhouse ~ 컬럼은 단위가 2개만 존재하므로 2개만 보여준다.
    if selected1 == 'Greenhouse gas emissions' :
        selected2 = st.sidebar.radio('Metric', metric_list[1:])

    else :
        selected2 = st.sidebar.radio('Metric', metric_list)

    # 사이드바에서 사용자가 확인하고 싶은 환경적 영향과 단위를 선택하면
    # 해당 문자열을 포함하는 컬럼을 저장한다.
    df_impact = df.loc[ :, (df.columns.str.contains(selected1)) & (df.columns.str.contains(selected2))]
    
    # 식품 이름도 추가해준다.
    df_impact.insert(0, 'Food product', df['Food product'])

    st.markdown('#### 선택한 환경에 가장 많은 영향을 주는 음식 TOP12')
    st.markdown('\n')
    
    # 환경 컬럼의 데이터를 내림차순으로 정렬한 후, 12개만 보여준다.
    df_impact = df_impact.sort_values(df_impact.columns[1], ascending=False).head(12)
    st.dataframe(df_impact)

    
    # x는 수치, y는 식품명
    df_impact = df_impact.sort_values(df_impact.columns[1]).head(12)
    fig = px.bar(df_impact, x= df_impact.columns[1], y=df_impact.columns[0])
    st.plotly_chart(fig)

     
    st.markdown('#### 선택한 환경에 따른 음식의 단위별 영향')
    df_env = df.loc[:,df.columns.str.contains(selected1)]
    df_env.insert(0, 'Food product', df['Food product'])
    st.dataframe(df_env)
    fig_test = plt.figure()
    fig_test = px.bar(df_env, x= df_env.columns[1:], y=df_env.columns[0])
    st.plotly_chart(fig_test)


    st.markdown('#### 온실가스 배출량 원인 비율')
    with st.expander('📌 확인하기'):
        
        fig2 = plt.figure()
        df_chart = df.iloc[:,1:8].sum()
        plt.pie(df_chart.values, labels=df_chart.index, autopct='%.1f%%')
        
        st.pyplot(fig2)


