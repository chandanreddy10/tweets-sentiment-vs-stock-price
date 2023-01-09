import pandas as pd
import regex as re

#merge everyday tweet to one.
def data_reading(df,company):
    df['Date'] = pd.to_datetime(df['Date'])

    companies = df.groupby(by='Company Name')

    #Tesla, Inc.
    result = companies.get_group(company).copy()
    result['date'] = result['Date'].dt.date
    result.drop(columns='Date',inplace=True)
    result['date'] = pd.to_datetime(result['date'])

    return result

#---------------------------- concat tweets based on date
def __get_tweets(df):
    
    tweets = df['Tweet'].sum()

    pattern = re.compile(r'[a-zA-z\s]+')
    matches = pattern.findall(tweets)
    cleaned_tweets = ''
    for match in matches:
        cleaned_tweets = cleaned_tweets+match

    cleaned_tweets = cleaned_tweets.strip(' ').replace('\n',' ')
    return cleaned_tweets
    

def merge_tweets(df):
    
    tweets_date_group = df.groupby(by='date')

    tweets_list = []
    for date in df.date.unique():
        helper = tweets_date_group.get_group(date)
        tweets = __get_tweets(helper)
        tweets_list.append(tweets)

    return tweets_list
#------------------------------------------ ends here
  

