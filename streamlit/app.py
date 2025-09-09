import streamlit as st
import pandas as pd
import numpy as np


### title of the aplication

st.title("hello from chai")

## display simple text

st.write("hello from chai")


### create data frame

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
# st.dataframe(df)
st.write(df)

## create a line chart 

st.line_chart(df)


