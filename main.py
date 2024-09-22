import streamlit as st
import streamlit.components as stc
import asyncio
from ml_inference import run_ml
from homepage import Home
import warnings
warnings.filterwarnings('ignore')

async def main():
    menu = ['Home', 'Discovrio Final Project']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        await Home()
    elif choice == 'Discovrio Final Project':
        await run_ml()

if __name__ == '__main__':
    asyncio.run(main())