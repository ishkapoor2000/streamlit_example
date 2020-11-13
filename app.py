import streamlit as st
import pandas as pd
import numpy as np


line_graph = 'Line Graph'
bar_graph = 'Bar Graph'
option = st.sidebar.selectbox('Graph type', [line_graph, bar_graph])

if option == line_graph:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

if option == bar_graph:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.area_chart(chart_data)
