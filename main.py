import streamlit as st
from ml_inference import run_ml
from homepage import Home
import warnings
warnings.filterwarnings('ignore')

async def main():
    menu = ['Home', 'Discovrio Final Project']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        Home()
    elif choice == 'Discovrio Final Project':
        run_ml()

if __name__ == '__main__':
    asyncio.run(main())