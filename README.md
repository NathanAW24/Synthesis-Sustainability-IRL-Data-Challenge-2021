# Synthesis_SustainabilityDataChallenge_2021

Contributors:
- Nathan Aldrich Wiryawan (@NathanAW24)
- Sean Phay Wei Xiang (@Sean2309)

Link to Challenge:
https://www.sustainabilityirl.synthesis.partners/

As part of the Data Science Challenge conducted by synthesis, we were given two main datasets which relates to sustainability. We chose a problem statement, "Perceptions of surplus food and barriers to consumption", and were tasked to tackle it using the data that was given to us. This repository contains what we did to the data and how we extract insights from it.

We divided the challenge to three main parts:
1. Initial Filtering
   - Conducting EDA to get the overall picture of the data.
   - Finding hashtags that are significant using important keyword(s) filtering.
2. SQL Filtering
   - Filtered the initial data on the whole table based on the hashtags obtained previously to get a more unbiased result.
   - As SQL is faster than python, this process is important because it optmizes the required computation time.
3. Data Extraction and Sentiment Analysis
   - Using the filtered SQL query on python to get the top data.
   - Apply sentiment analysis to get the polarity and subjectivity of each rows.
   - Plotting the distribution of both metrics as a histogram to get the general consensus on this problem.
