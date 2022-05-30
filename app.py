import streamlit as st

from app_home import run_home
from app_search import run_search



def main() :

    st.header('식품 생산의 환경 영향 🌏')
    st.markdown('---')

    select_list = ['Home', 'Search']
    page = st.sidebar.selectbox('페이지를 선택해주세요', select_list)
    
    st.sidebar.markdown('\n')
    st.sidebar.markdown('\n')

    if page == select_list[0] :
        run_home()
    
    elif page == select_list[1] :
        run_search()


if __name__ == '__main__' :
    main()