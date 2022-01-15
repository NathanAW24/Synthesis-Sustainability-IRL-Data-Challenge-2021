# Synthesis_SustainabilityDataChallenge_2021
## Perceptions of Surplus Food and Barriers to Consumption

Contributors:
- Nathan Aldrich Wiryawan (https://github.com/NathanAW24)
- Sean Phay Wei Xiang (https://github.com/Sean2309)

Link to Challenge:
https://www.sustainabilityirl.synthesis.partners/

Our Result:
https://static1.squarespace.com/static/60754f2bbe89bf2527b7d57c/t/61a868f405e8c4433c163dea/1638426869609/nathan-sean.pdf

As part of the Data Science Challenge conducted by Synthesis, we were given two main datasets which relates to sustainability. We chose a problem statement, "Perceptions of surplus food and barriers to consumption", and were tasked to tackle it using the data that was given to us in parquet format. This repository contains what we did to the data and how we extract insights from it.

We divided the challenge to three main parts:
1. Initial Filtering
   - Conducting EDA to get the overall picture of the data.
   - Finding hashtags that are significant using important keyword(s) filtering.
2. SQL Filtering
   - Filtering the initial data on the whole table based on the hashtags obtained previously to get a more unbiased result.
   - As SQL is faster than python, this process becomes important because it optmizes the required computation time.
3. Data Extraction and Sentiment Analysis
   - Using the filtered SQL query on python to get the top data.
   - Applying sentiment analysis to get the polarity and subjectivity of each rows.
   - Plotting the distribution of both metrics as a histogram to get the general consensus on this problem.
