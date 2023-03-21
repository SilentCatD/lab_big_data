---
title: "Lab 01: A Gentle Introduction to Hadoop"
author: ["nhom 1"]
date: "2023-03-20"
subtitle: "CSC14114 Big Data Application 19KHMT"
lang: "en"
titlepage: true
titlepage-color: "0B1887"
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "FFFFFF"
titlepage-rule-height: 2
book: true
classoption: oneside
code-block-font-size: \scriptsize
---

# Work schedule table

|Number|Section|Progress
|:--:|:----:|:----:
|1|UBCF algorithm|100%
|2|IBCF algorithm|100%
|3|Evalation metric| 100%
|4|Recommender Syster: MovieLens 1M Dataset|100%

# Lab 01:  Building Recommendation Systems

## K-Nearest Neighbors Recommendation

### UBCF: Q

According to the slide and theory taught in class, there are 4 step to compute UBCF:
1. Calculating the average rating of all users, using function **calc_average_rating**..
2. Calculating the similarity score of each user to other user, using function **calc_user_sim** and store all scores on 2-d array.
3. For each user and similarity score, sort list similar users order by decreasing similarity scores.
4. Based on K (top K), compute the prediction score of items by users that existed on test dataset, using **ubcf_predict_rating**

To fulfill the requirement, we output 2 matrices:
- *raing_predicted*: conpute prediction scores in test dataset, based on *test_mask*
- *top_sims*: top user with the decreasing similarity scores for each user.

### IBCF: P

### Evaluation Metrics

#### RMSE : P

#### NDCG :
To compute NDCG score, first we sort the predicted items list and the idea items by the decreasing prediction score. And we implement this metric evaluation with 2 version: 
+ In the first version, we calculate the NDCG score of each user based on the score of the training dataset combining the score of the test dataset with the score of the training dataset combining the prediction score.
+ The second version, we compute the NDCG score of each user based on just the score of test dataset and the prediction score.

## MovieLens 1M Dataset: P

## References
