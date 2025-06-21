IPL Win Predictor
This project predicts the winning probability of IPL teams in a live T20 match scenario using machine learning. The user inputs match details (teams, city, current score, overs, wickets, target), and the model returns the real-time probability of winning for both teams.

📌 Project Overview
Cricket is not just a sport—it's a game of uncertainty and numbers. This application uses match statistics and machine learning to predict the probability of the batting and bowling team winning the match at any point during the second innings of an IPL match.

⚙️ Features
Select batting and bowling teams
Choose the city (match venue)
Enter current score, wickets fallen, overs completed, and target score
Get real-time win/loss probability
Easy-to-use Streamlit interface
🧠 Machine Learning
The model is trained on historical IPL match data using Logistic Regression. Features include:

Batting and bowling teams
Match location (city)
Target runs, current score
Balls left, wickets left
Current and required run rate
The model uses ColumnTransformer for categorical encoding and is wrapped in a Pipeline along with a logistic regression classifier.
