# DeepMinds

Repo for senior design 2

## Members

- [Matthew Munoz](https://www.github.com/MattMunoz) - Team Leader
- [Matthew Nieves](https://www.github.com/Nieves350) - System Savvy
- [Tajwar Rahman](https://www.github.com/thetajwar2003) - Tech Smith

## Demo
https://drive.google.com/file/d/1p81cDjszGQDgT5P8ahCzOeH5bOGJ5Pin/view?usp=sharing

## Timeline for Project (Subject to Change)

[Schedule](https://docs.google.com/spreadsheets/d/1_CTNEVaTbUeiSTDD4i7zU3mf360-n2xHzTq5874sA4o/edit?gid=2016187939#gid=2016187939)

## Project Description

- Recipe App

  - The ML aspect of the project will be implemented alongside a recipe app. The recipe app will work much the same way other recipe apps work. The full details of it can be found [here](https://github.com/thetajwar2003/khuda-lagche)

- Senior Design Project

  1. The main aspect of the project will be a recommendation system that creates personalized recommendations for each app user. The users will obtain this personalization based on past preferences, whether like or dislike, compared to what other similar app users prefer. For example, if two users have similar tastes in recipes and are more closely related, we can assume that they will like a similar recipe in the future, so if one of them likes a recipe the other one has not tried, we can recommend the said recipe to the other user.

  2. If time permits, the project will also attempt to implement a function within the app that allows the user to upload a picture of a dish they tried and would like to know how to make. The app will then identify the dish in the image and provide a recipe to make that dish. Specifically, if a user uploads a picture of a margarita pizza, they can upload a picture of the pizza they like, and the app will provide a recipe.

## Monthly Updates

### Septemeber

- [Data analysis](https://docs.google.com/presentation/d/1evxd-9ThpiSafHGqG9SWblSGBWH8p6MRBY8j7teP6Z8/edit#slide=id.p) with a thorough understanding of the various datasets needed for image recognition and recommendation systems.
- Implemented preprocessing techniques like normalization, resizing images, and removing incorrect or mislabeled entries to ensure data quality.
  
### October

- Selection and creation of the models to be used with a deep neural network for image recognition and cosine similarity for the recommendation system.
- Performed iterative testing on both models to ensure baseline performance, identifying areas for improvement and exploring methods to enhance performance. A more thorough update is found [here](https://docs.google.com/presentation/d/1j-zSWSOCYNckjP9O2TLLutKJe3B4m4ZwDKZLs8ZG9i8/edit#slide=id.p) along with the [midterm update](https://docs.google.com/presentation/d/1hpQh4t4M3lrK75eTXjqawNI2oM0_PV_bo9ysY-2bQNY/edit#slide=id.g30b8e1912aa_2_0).

### November

- Used primarily for implementation and testing with a working image recognition and recommendation model.
- Analysis of performance metrics such as precision, recall, and F1-score by food class, identifying factors contributing to class performance, and exploring correlations between similar classes that may have led to misclassifications. In addition, [API documentation](https://github.com/thetajwar2003/khuda-lagche/tree/master/backend) was created.
