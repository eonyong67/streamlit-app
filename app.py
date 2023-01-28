import streamlit as st
import pandas as pd
view = [100,150,30]
st.write('# 김언용 Streamlit 연습')
st.write('## raw')
view
st.bar_chart(view)
sview = pd.Series(view)
sview