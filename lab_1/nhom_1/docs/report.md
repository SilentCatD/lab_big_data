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
This implementation algorithm has 3 function.
+ The main function **ubcf** return 2 variables *rating_predicted* and *top_sims* with the 2-d array type. *rating_predicted* store the prediction score of items, which are samples of test dataset. And *top_sims* is the list of similar users order by similarity score decreasingly. 
+ We compute similarity score between each user by function **calc_user_sim**, and store all similiraity score on 2-d matrix. After that, we sort each user's simlilarity scores and return as a *top_sims* variable. 
+ We use the function **ubcf_predict_rating** to compute predction scores existed in test dataset. We store these scores on 2-d matrix *rating_predicted* variable. This variable has the same mask data as test dataset.
### IBCF: P

### Evaluation Metrics

#### RMSE : P

#### NDCG :
To compute NDCG score, first we sort the predicted items list and the idea items by the decreasing prediction score. And we implement this metric evaluation with 2 version: 
+ In the first version, we calculate the NDCG score of each user based on the score of the training dataset combining the score of the test dataset with the score of the training dataset combining the prediction score.
+ The second version, we compute the NDCG score of each user based on just the score of test dataset and the prediction score.

## MovieLens 1M Dataset: P

## References
