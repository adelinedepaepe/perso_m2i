
import pandas as pd
import numpy as np
from datetime import datetime
import seaborn as sns

import matplotlib.pyplot as plt


#Display options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)

file_encoding = 'cp1252'        # set file_encoding to the file encoding (utf8, latin1, etc.)

path = 'C:/Users/a_khl/PycharmProjects/elections_us/venv/Data/'
trump_file = 'hashtag_donaldtrump.csv'
biden_file = 'hashtag_joebiden.csv'


# Creation des dataframes
trump_input_fd = open(f"{path}{trump_file}", encoding=file_encoding, errors = 'backslashreplace')
biden_input_fd = open(f"{path}{biden_file}", encoding=file_encoding, errors = 'backslashreplace')



trump_df = pd.read_csv(trump_input_fd, delimiter=",", encoding = file_encoding, parse_dates=['created_at'])
biden_df = pd.read_csv(biden_input_fd, delimiter=",", encoding = file_encoding, parse_dates=['created_at'])

#Delete rows with NaN values
trump_df.dropna(axis=0, how='all', inplace=True)
biden_df.dropna(axis=0, how='all', inplace=True)


#Delete duplicates
trump_df.drop_duplicates(keep='first', inplace=True)
biden_df.drop_duplicates(keep='first', inplace=True)

#Clean date column
trump_df = trump_df[trump_df['created_at'].str.startswith('2020')]
biden_df = biden_df[biden_df['created_at'].str.startswith('2020')]

#Convert date column to date
trump_df['created_at'] = pd.to_datetime(trump_df['created_at'])
biden_df['created_at'] = pd.to_datetime(biden_df['created_at'])

#Convert like column to integer
trump_df['likes'].fillna(0, inplace=True)
biden_df['likes'].fillna(0, inplace=True)

trump_df['likes'] = trump_df['likes'].astype(str).astype(float)
biden_df['likes'] = biden_df['likes'].astype(str).astype(float)

#Create month column to group-by
trump_df.insert(1, 'month', trump_df['created_at'].dt.to_period('M'))
biden_df.insert(1, 'month', biden_df['created_at'].dt.to_period('M'))

#Group by month
trump_df_month = trump_df.groupby('month')
biden_df_month = biden_df.groupby('month')

#sum
print('Trump: ')
print('-' * len('Trump: '))
# print('\n' * 1)

print('Number of tweets: ')
print('-' * len('Number of tweets: '))
print(trump_df_month['tweet'].count())          #Number of tweets

print('\n' * 1)
print('Number of retweet: ')
print('-' * len('Number of retweet: '))
print(trump_df_month['retweet_count'].sum())    #Number of retweets

print('\n' * 1)
print('Number of likes: ')
print('-' * len('Number of likes: '))
print(trump_df_month['likes'].sum())    #Number of likes

print('\n' * 2)
print('Joebiden: ')
print('-' * len('Joebiden: '))
# print('\n' * 1)

print('Number of tweets: ')
print('-' * len('Number of tweets: '))
print(biden_df_month['tweet'].count())          #Number of tweets
print('\n' * 1)
print('Number of retweet: ')
print('-' * len('Number of retweet: '))
print(biden_df_month['retweet_count'].sum())    #Number of retweets

print('\n' * 1)
print('Number of likes: ')
print('-' * len('Number of likes: '))
print(biden_df_month['likes'].sum())    #Number of likes


print(trump_df.info())
print(trump_df.head(10))
print(trump_df_month.head(10))



print(biden_df.info())
print(biden_df.head(10))
print(biden_df_month.head(10))


#Seaborn

#Trump
trump_tweets = (trump_df_month['month'], trump_df_month['tweet'].count())
trump_retweets = (trump_df_month['month'], trump_df_month['retweet_count'].sum())
trump_likes = (trump_df_month['month'], trump_df_month['likes'].count())

#Joebiden
Biden_tweets = (biden_df_month['month'], biden_df_month['tweet'].count())
Biden_retweets = (biden_df_month['month'], biden_df_month['retweet_count'].sum())
Biden_likes = (biden_df_month['month'], biden_df_month['likes'].count())

# data_list = []
# for month in biden_df_month['month']:
#     data_list.append(month, trump_df_month['tweet'].count())
#
#
#
# g = sns.PairGrid(data_list, hue='total_rooms')
# g.map(sns.scatterplot)
# plt.show()


nombre_mots = trump_df[['tweet', 'likes']]


print(nombre_mots.head(10))