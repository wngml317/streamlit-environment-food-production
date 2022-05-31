import streamlit as st
import pandas as pd
import plotly.express as px

def run_food() :

    st.subheader('선택한 음식의 환경적 영향 확인하기')
    st.write('')

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

    food_list = st.multiselect('음식을 선택하세요', df['Food product'])
    st.write('')

    if food_list != [] :
        for i in range(len(food_list)) :
            if i == 0 :
                df_food = df.loc[df['Food product'] == food_list[i]]
            else :
                df_food = df_food.append(df.loc[df['Food product'] == food_list[i]])
        
        
        
        st.write('')
        st.markdown('##### 전체 데이터 확인')
        st.dataframe(df_food)
        st.write('')


        df_impact = df_food.loc[ :, (df_food.columns.str.contains(selected1)) & (df_food.columns.str.contains(selected2))]
        
        df_impact.insert(0, 'Food product', df_food['Food product'])
        st.write('')
        st.markdown('##### 환경적 영향 데이터 확인')
        st.dataframe(df_impact)
        
        
        fig = px.bar(df_impact, x= df_impact.columns[1], y=df_impact.columns[0])
        st.plotly_chart(fig)

    

    


    