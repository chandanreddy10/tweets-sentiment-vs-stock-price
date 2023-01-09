# Tweets sentiment vs stock price
#### This project is to find out whether the tweets sentiment has any effect on the company's stock price. here, i have considered onlt Tesla.
#### It involves both tweets dataset collected from **KAGGLE** (data between **2021 september to 2022 september**). I have clubbed together the tweets based on a day and not on individuals tweets again this is to find out how collectively the sentiment effects the stock price.
#### Then, i extracted the words from the tweets. Then trained the __Doc2Vec__ model to get the embedding of the tweets. later, labelled data and trained with 2 basic models, SVM and Logistic Regression, both the models achieved accuracy above 85%. Later, i used the data to find the effect on stock price.
# **Findings**<br>## Only about 34.45% of the time the stock has increased when the sentiment was positive.

