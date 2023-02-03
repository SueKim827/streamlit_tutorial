# streamlit run <streamlitapp>.py (--server.address=127.0.0.1 방화벽땜)

import streamlit as st
import pandas as pd

# def main():
    st.title("First_APP")
    df=pd.DataFrame({
        "first_col":[1,2,3,4],
        "second_col":[10,20,30,40]
    })
    st.write(df)

# if __name__== '__main__':  #파일 이름이 메인 나자신
#     main()

