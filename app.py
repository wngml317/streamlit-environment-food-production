import streamlit as st

from app_home import run_home
from app_impact import run_impact
from app_food import run_food
from app_metric import run_metric


def main() :

    st.header('π³ μν μμ°μ νκ²½ μν₯')
    st.markdown('---')

    select_list = ['Home', 'Environment Impact', 'Food Production Impact', 'Metric Impact']
    page = st.sidebar.selectbox('νμ΄μ§λ₯Ό μ νν΄μ£ΌμΈμ', select_list)
    
    st.sidebar.markdown('\n')
    st.sidebar.markdown('\n')

    if page == select_list[0] :
        run_home()
    
    elif page == select_list[1] :
        run_impact()

    elif page == select_list[2] :
        run_food()
    
    elif page == select_list[3] :
        run_metric()


if __name__ == '__main__' :
    main()