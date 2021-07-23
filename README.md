
### Table of Contents

1. [Installation](#installation)
2. [Project Description](#description)
3. [Files in the Repository](#files)
4. [Instructions](#Instructions)
5. [Results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

The list of commands required to install necessary libraries are given in requirements.txt file.  The code should run with no issues using Python versions 3.*. 

## Project Description<a name="description"></a>

<b>Problem Statement</b>: Analyze the interactions that users have with articles on the IBM Watson Studio platform, and make recommendations to them about new articles you think they will like. More details corresponding to each technique is provided in the python notebook.

**I.Exploratory Data Analysis**

Before making recommendations of any kind, one need to explore the data and throw in some statistics to understand it better. It will drive our recommendation systems and will improve our understanding on the behavior for each on of them

**II.Rank Based Recommendations**

Find the most popular articles simply based on the most interactions. Since there are no ratings for any of the articles, it is easy to assume the articles with the most interactions are the most popular. These are then the articles we might recommend to new users (or anyone depending on what we know about them).

**III.User-User Based Collaborative Filtering**

In order to build better recommendations for the users of IBM's platform, we could look at users that are similar in terms of the items they have interacted with. These items could then be recommended to the similar users. This would be a step in the right direction towards more personal recommendations for the users. You will implement this next.

**IV.Content Based Recommendations**

Using Natural Language processing, to group articles based on similarity and then using it to recommend users, articles similar to the ones they have interacted. 

**V.Matrix Factorization**

A machine learning approach to building recommendations. Using the user-item interactions, building out a matrix decomposition that gives an indea on how well we can predict new articles, a user might interact with.

## Files in the Repository<a name="files"></a>

    • data
	|- articles_community.csv #file that contains articles’ data
	|- user-item-interactions.csv #file that contains user article interactions’ data.
    • Recommendations_with_IBM.ipynb #python notebook that has all the codes discussing each technique
    • projects_test.py #file that contains test cases corresponding to cases in notebook
    • custom_transformer.py #file that contains class of a custom transformer based on gensim word2vec model
    • Recommendations_with_IBM.html #html converted file of the notebook
    • top_10.p #pickle file containing top 10 articles
    • top_20.p #pickle file containing top 20 articles
    • top_5.p #pickle file containing top 5 articles
    • user_item_matrix.p #pickle file containing user_item matrix
    • requirements.txt #file that contains list of pre-requisite libraries to be installed
    • README.md


## Instructions <a name="Instructions"></a>


1. Install all the necessary libraries in the requirements.txt file
2. Run the Jupyter notebook Starbucks.ipynb till the end to get the results.

## Observations<a name="results"></a>

The Observations corresponding to each technique is discussed in the notebook.


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

The entire project in partial fulfilment towards completing Udacity's Data Science Nanodegree Program.
The videos and lectures guided me to understand and implemen each technique.

The Custom Transformers and using word2vec model was inspired by various medium posts and other websites, links to some of them are given below.
[Word Embeddings](https://www.shanelynn.ie/word-embeddings-in-python-with-spacy-and-gensim/), 
[Medium Post](https://towardsdatascience.com/how-to-compute-sentence-similarity-using-bert-and-word2vec-ab0663a5d64)




