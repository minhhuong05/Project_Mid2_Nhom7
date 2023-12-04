import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie

def app():
    st.markdown("""<h1 style='text-align: center; font-family: Candara; font-size: 40px'>
                    USED CAR SEARCH AND ANALYSIS TOOL
                    </h1>""", unsafe_allow_html=True)
    st.write('---')
    
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

    st.balloons()

    st.markdown("""<h1 style='text-align: center; font-family: Candara; font-size: 30px'>
                            Our Member
                            </h1>""", unsafe_allow_html=True)
    mem_1, mem_2, mem_3, mem_4 = st.columns(4)
    with mem_1:
        st.image("img/lqc.jpeg", caption="Luong Quynh Chi")

    with mem_2:
        st.image("img/nmh.jpeg", caption="Nguyen Minh Huong")

    with mem_3:
        st.image("img/ttq.jpeg", caption="Tran Truc Quynh")

    with mem_4:
        st.image("img/nvn.jpeg", caption="Tran Van Ngoc")


    st.write('---')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<h1 style='text-align: center; font-family: Candara; font-size: 25px'>
                            About The Project
                            </h1>""", unsafe_allow_html=True)
        st.markdown("""<p style='text-align: justify;'>
                This app will help you find your wanted car easily by navigating and filtering through a diverse range of used cars based on brand, year of manufacture, \
                and price range. But it don't stop there, our tool could offering you a market trend analysis feature. Gain valuable insights into pricing trends, popular \
                brands, and market dynamics to stay ahead of the curve. Welcome to a smarter way to find, evaluate, and analyze used cars.
                </p>""", unsafe_allow_html=True)
    with col2:
        lottie = load_lottiefile("img/intro_img.json")
        st_lottie(lottie, speed=1, reverse=False, loop=True, quality="high", height=None, width=None, key=None)
