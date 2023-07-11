import xgboost as xgb
import streamlit as st
from PIL import Image
import pandas as pd
import base64
# Loading up the Regression model we created
model = xgb.XGBRegressor ()
model.load_model ('C:/Users/khanh/OneDrive/CN8 SUMMER2023/DBM301/Project/app/models/xgb_model1000pro.bin')

# Caching the model for faster loading
@st.cache_resource


def predict ( carat , cut , color , clarity , depth , table , x , y , z ):
 # Predicting the price of the carat
 if cut == 'Fair ':
   cut = 0
 elif cut == 'Good ':
    cut = 1
 elif cut == 'Very Good ':
    cut = 2
 elif cut == 'Premium ':
    cut = 3
 elif cut == 'Ideal ':
    cut = 4

 if color == 'J':
    color = 0
 elif color == 'I':
    color = 1
 elif color == 'H':
    color = 2
 elif color == 'G':
    color = 3
 elif color == 'F':
    color = 4
 elif color == 'E':
    color = 5
 elif color == 'D':
    color = 6

 if clarity == 'I1 ':
    clarity = 0
 elif clarity == 'SI2 ':
    clarity = 1
 elif clarity == 'SI1 ':
    clarity = 2
 elif clarity == 'VS2 ':
    clarity = 3
 elif clarity == 'VS1 ':
    clarity = 4
 elif clarity == 'VVS2 ':
    clarity = 5
 elif clarity == 'VVS1 ':
    clarity = 6
 elif clarity == 'IF ':
    clarity = 7

 prediction = model.predict ( pd.DataFrame ([[ carat , cut , color , clarity , depth ,table , x , y , z ]] , 
                                            columns =[ 'carat ', 'cut ', 'color ', 'clarity ', 'depth ', 'table ', 'x', 'y', 'z']) )
 return prediction


st.title ('Thần tài đã đến')
image = Image.open('C:/Users/khanh/OneDrive/CN8 SUMMER2023/DBM301/Project/app/utils/imgs/kim_cuong.jpeg')
st.image (image)
st.header ('Vui lòng nhập thông tin kim cương cần mua:')
carat = st.number_input ('Carat Weight :', min_value =0.1 , max_value =10.0 , value =1.0)

cut = st.selectbox ('Cut Rating :', ['Fair ', 'Good ', 'Very Good ', 'Premium ', 'Ideal '])
color = st.selectbox ('Color Rating :', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
clarity = st.selectbox ('Clarity Rating :', ['I1 ', 'SI2 ', 'SI1 ', 'VS2 ', 'VS1 ', 'VVS2 ','VVS1 ', 'IF '])
depth = st.number_input ('Diamond Depth Percentage :', min_value =0.1 , max_value =100.0 ,value =1.0)
table = st.number_input ('Diamond Table Percentage :', min_value =0.1 , max_value =100.0 ,value =1.0)
x = st.number_input ('Diamond Length (X) in mm:', min_value =0.1 , max_value =100.0 ,value =1.0)
y = st.number_input ('Diamond Width (Y) in mm:', min_value =0.1 , max_value =100.0 ,value =1.0)
z = st.number_input ('Diamond Height (Z) in mm:', min_value =0.1 , max_value =100.0 ,value =1.0)


def autoplay_audio ( file_path : str ):
   with open ( file_path, "rb" ) as f:
      data = f.read()
      b64 = base64.b64encode(data).decode()
      md = f"""
      <audio autoplay="true">
      <source src = "data:audio/mp3; base64, {b64}"type ="audio/mp3">
      </audio>
      """
      st.markdown(md, unsafe_allow_html = True,)

autoplay_audio ("C:/Users/khanh/OneDrive/CN8 SUMMER2023/DBM301/Project/app/utils/audios/background_music.mp3")

if st.button ('Predict Price '):
                price = predict ( carat , cut , color , clarity , depth , table , x , y , z)
                st.success (f'Giá đoán của kim cương: ${ price [0]:.2f} USD ')