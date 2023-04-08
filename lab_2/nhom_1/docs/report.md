---
title: "Lab 02: Building a Sentiment Analysis Benchmark"
author: ["nhom 1"]
date: "2023-04-14"
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

Task | Completed
------------------|----------------------------------------
Data collection      | **Percent**: 100
Data preprocess and labeling     | **Percent**: 100
Feature extraction | Percent: 100
Classification models     | **Percent**: 100


# Lab 02: Building a Sentiment Analysis Benchmark

## Data collection

## Data labeling

Using collected data from IMDb, we proceeded with the preprocessing and labeling steps in the following order:

1.  Tokenization: We separated each review into sentences and considered each sentence as a separate review. The entire dataset was created by splitting all the sentences in the raw dataset.
2.  Special Symbol Removal: We removed special symbols from each sentence to clean the text data and ensure consistency.
3.  POS Tagging: POS tagging was conducted to identify the part-of-speech of each word in the sentences. This information was needed for lemmatization.
4.  Lemmatization: Lemmatization was performed on each POS-tagged sentence to reduce words to their base or dictionary form, which helps in grouping similar words together.
5.  Sentiment Rule-Based Tagging: Following tutorials and research, we used the `sentiwordnet` submodule of the `nltk` library for the labeling process. `sentiwordnet` provides polarity scores for individual words, not entire sentences. We used these scores to compute the polarity of each lemmatized sentence.

The core idea behind the labeling process is to count and summarize the polarity scores of each word in the lemmatized sentences (after preprocessing). The resulting label can be one of four cases: `positive`, `negative`, `neutral`, or `None`, depending on the overall polarity score of the sentence.

## Benchmarking

## Reflection


## References
- https://stackoverflow.com/questions/35722185/to-find-the-opinion-of-a-sentence-as-positive-or-negative
- https://stackoverflow.com/questions/30829713/how-to-get-synsets-using-sentiwordnet-and-calculate-their-sentiment-score
- https://srish6.medium.com/sentiment-analysis-using-the-sentiwordnet-lexicon-1a3d8d856a10
- https://stackoverflow.com/questions/38263039/sentiwordnet-scoring-with-python
- https://www.analyticsvidhya.com/blog/2021/06/rule-based-sentiment-analysis-in-python/#:~:text=This%20is%20a%20practical%20approach,is%20called%20Lexicon%20based%20approach
- Slides
