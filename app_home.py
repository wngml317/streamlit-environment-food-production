import streamlit


import streamlit as st
import pandas as pd

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
    
    st.markdown('#### 데이터')
    with st.expander('📌 확인하기') :
        st.dataframe(df)
