import streamlit as st
import datetime
import requests

'''
#       🚕 TaxiFareModel front 🚕
'''


st.markdown('Balance les infos sur ta course en tacos !!!')
date = st.date_input('Indicate pick up date')
time = st.time_input('Indicate pick up time')

pickupdatetime = datetime.datetime.combine(date,time)
st.markdown(pickupdatetime)

pickuplong = st.number_input('Indicate pickup longitude')
pickuplat = st.number_input('Indicate pickup latitude')
dropofflong = st.number_input('Indicate dropoff longitude')
dropofflat = st.number_input('Indicate dropoff latitude')
passcount = st.slider('Passenger Count', min_value=1, max_value=8, value=5, step=1)

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

if pred>10:
    st.image(gif2)
    st.write(f'💰💸💰💸💰💸💰 CA VA TE COUTER {pred}$$ 🤑💵🤑💵🤑💵🤑 !!!!')

if pred < 10:
    st.balloons()
    st.image(gif1)
    st.write(f'💰💸💰💸💰💸💰 CA VA TE COUTER {pred}$$ 🤑💵🤑💵🤑💵🤑 !!!!')


#<iframe src="https://giphy.com/embed/l41Ys1fQky5raqvMQ" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/angrybirds-angry-birds-leonard-movie-l41Ys1fQky5raqvMQ">via GIPHY</a></p>

#if isnum
