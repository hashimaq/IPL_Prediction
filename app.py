import streamlit as st
import pickle
import pandas as pd

cities=['Chennai', 'Hyderabad', 'Visakhapatnam', 'Chandigarh', 'Durban',
       'Centurion', 'Abu Dhabi', 'Delhi', 'Kolkata', 'Jaipur', 'Guwahati',
       'Ahmedabad', 'Mumbai', 'Kimberley', 'Mohali', 'Bangalore',
       'Johannesburg', 'Navi Mumbai', 'Dharamsala', 'Port Elizabeth',
       'Pune', 'Bengaluru', 'Bloemfontein', 'Dubai', 'Indore', 'Raipur',
       'Cape Town', 'Nagpur', 'Cuttack', 'Lucknow', 'Sharjah', 'Ranchi',
       'East London']

teams=['Royal Challengers Bengaluru',
 'Punjab Kings',
 'Sunrisers Hyderabad',
 'Mumbai Indians',
 'Kolkata Knight Riders',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals',
 'Lucknow Super Giants',
 'Gujarat Titans']

pipe=pickle.load(open('pipe.pkl','rb'))


st.title('IPL Win Predictor')

col1, col2 = st.columns(2)


with col1:
       batting_team=st.selectbox('Select the batting team',sorted(teams))
with col2:
       bolling_team=st.selectbox('Select the bolling team',sorted(teams))

selected_city=st.selectbox('Select the hosted City',sorted(cities))

target=st.number_input('Target')

col3,col4,col5=st.columns(3)

with col3:
    score=st.number_input('Score')
with col4:
    overs=st.number_input('Overs Completed')
with col5:
    wickets=st.number_input('Wickets out')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs *6)
    remaing_wickets = 10 - wickets
    current_run_rate= score / overs
    required_run_rate = (runs_left * 6) / balls_left

    inputs=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bolling_team],'city':[selected_city],
                  'target_runs':[target],'current_score':[score],'runs_left':[runs_left],'balls_left':[balls_left],
                  'remaing_wickets':[remaing_wickets],'current_run_rate':[current_run_rate],
                  'required_run_rate':[required_run_rate]})
    st.table(inputs)
    result=pipe.predict_proba(inputs)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + '-' + str(round(win * 100)) + '%')
    st.header(bolling_team + '-' + str(round(loss * 100)) + '%')