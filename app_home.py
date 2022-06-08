import streamlit as st
import pandas as pd
import plotly.express as px

def run_home() :
    st.markdown('#### 데이터 설명')
    with st.expander('📌 확인하기') :
        st.markdown('- Food product : 식품 종류')
        st.markdown('- 온실가스 배출량\n'
                    '  - Land use change : 토지 사용\n'
                    '  - Animal Feed : 동물 사료\n'
                    '  - Farm : 농장\n'
                    '  - Processing : 가공\n'
                    '  - Transport : 운송\n'
                    '  - Packing : 포장\n'
                    '  - Retail : 소매\n'
                    '  - Total_emissions : 총배출량')
        st.markdown('- Eutrophying emissions : 부영양화 배출(수질 오염)')
        st.markdown('- Freshwater withdrawals : 담수 취수량')
        st.markdown('- Greenhouse gas emissions : 온실가스 배출')
        st.markdown('- Land use : 거주 가능한 토지의 사용')
        st.markdown('- Scarcity-weighted water use : 희소성이 가중된 물의 사용')
    


    df = pd.read_csv('data/Food_Production.csv')
    
    st.markdown('\n')
    st.markdown('#### 데이터')
    st.dataframe(df)

    st.write('')

    st.markdown('#### 온실가스 배출량 원인 비율')
    with st.expander('📌 확인하기'):
    
        emissions = df.iloc[:,1:8].sum()
        df_emissions = pd.DataFrame({'cause' : emissions.index, 'ratio' : emissions.values})
        
        fig2 = px.pie(df_emissions, values = 'ratio', names = 'cause', width=650)
        st.plotly_chart(fig2)
