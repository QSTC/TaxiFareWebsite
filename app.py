import streamlit as st
import datetime
import requests
import folium
from streamlit_folium import folium_static

st.markdown("<h1 style='text-align: center; color: red;'>🚕 TAXI PAS CHER 🚕</h1>",
            unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 6, 1])

### Side menu for data input

button_status=st.sidebar.button('🎰 calcul hyper compliqué 🎰')

st.sidebar.markdown('Balance les infos sur ta course en tacos 🌮')
date = st.sidebar.date_input('Indicate pick up date')
time = st.sidebar.time_input('Indicate pick up time')

pickupdatetime = datetime.datetime.combine(date,time)
st.sidebar.markdown(pickupdatetime)

pickuplong = st.sidebar.number_input('Indicate pickup longitude')
pickuplat = st.sidebar.number_input('Indicate pickup latitude')
dropofflong = st.sidebar.number_input('Indicate dropoff longitude')
dropofflat = st.sidebar.number_input('Indicate dropoff latitude')
passcount = st.sidebar.slider('Passenger Count',
                              min_value=1,
                              max_value=8,
                              value=5,
                              step=1)

# center on Liberty Bell
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)

# add marker for Liberty Bell
tooltip = "Liberty Bell"
folium.Marker(
        [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
    ).add_to(m)

# call to render Folium map in Streamlit
folium_static(m)


## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

##1. Let's ask for:
#- date and time
#- pickup longitude
#- pickup latitude
#- dropoff longitude
#- dropoff latitude
#- passenger count

## Once we have these, let's call our API in order to retrieve a prediction

#See ? No need to load a `model.joblib` file in this app,
#we do not even need to know anything about Data Science in order to retrieve a prediction...
#🤔 How could we call our API ? Off course... The `requests` package 💡


url = 'https://taxifare.lewagon.ai/predict'

#2. Let's build a dictionary containing the parameters for our API...

api_params=dict(pickup_datetime=pickupdatetime,
                pickup_longitude=pickuplong,
                pickup_latitude=pickuplat,
                dropoff_longitude=dropofflong,
                dropoff_latitude=dropofflat,
                passenger_count=passcount)


##3. Let's call our API using the `requests` package...


response=requests.get(url,params=api_params)
pred=round(response.json()['prediction'],2)

##4. Let's retrieve the prediction from the **JSON** returned by the API...
## Finally, we can display the prediction to the user

gif1 = 'https://media3.giphy.com/media/l41Ys1fQky5raqvMQ/giphy.gif?cid=790b761118d3d817bc8d97e06a3409200d7253a334bbad87&rid=giphy.gif&ct=g'
gif2 = 'https://media4.giphy.com/media/3ohze3kG5qO9DcTUbe/giphy.gif?cid=ecf05e4736bb926c6883196942a0e7e83f978d433646fe06&rid=giphy.gif&ct=g'
#<iframe src="https://giphy.com/embed/3ohze3kG5qO9DcTUbe" width="480" height="333" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/foxhomeent-3ohze3kG5qO9DcTUbe">via GIPHY</a></p>

with col2:
    if button_status:
        if pred > 10:
            st.image(gif2)
            st.write(f'😱🥶😱🥶😱 {pred}$$ C TROP REUCH !!!')


        if pred < 10:
            st.balloons()
            st.image(gif1)
            st.write(f'💰💸💰💸💰💸💰 CA VA TE COUTER {pred}$$ 🤑💵🤑💵🤑💵🤑 !!!!')










#<iframe src="https://giphy.com/embed/l41Ys1fQky5raqvMQ" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/angrybirds-angry-birds-leonard-movie-l41Ys1fQky5raqvMQ">via GIPHY</a></p>

#if isnum
