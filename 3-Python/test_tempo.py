# with open ('C:\\Users\\Administrateur\\PycharmProjects\\Adeline\\perso_m2i\\3-Python\\tempo.csv', encoding='UTF-8') as f:
#     lines = f.readlines()
#     # print(lines)
#
#     columns = ['created_at', 'tweet_id', 'tweet', 'likes', 'retweet_count', 'source', 'user_id', 'user_name',
#                'user_screen_name', 'user_description', 'user_join_date', 'user_followers_count', 'user_location', 'lat',
#                'long', 'city', 'country', 'continent', 'state', 'state_code', 'collected_at']

    # data = {j: [line.replace('\n','').split ( ',' )[i] for line in lines if 'created_at' not in line] for i, j in enumerate ( columns )}
    # for line in lines:
    #     print(len(line.split(',')))
    # print(lines[4].split(','))
    # for line in lines:
    #     print(len(line.split(',')))
    # data={}
    # for i,j in enumerate(columns):
    #     data[j]=list()
    #     for line in lines:
    #         if len(line.split(','))<10:
    #             data[j].append('')
    #         if 'created_at' not in line and len(line.split(','))>20:
    #             print(len(line.split(',')))
    #             data[j].append(line.split(',')[i])
        # for i,j in enumerate(columns):
        #     try:
        #         data[j].append(line.split(',')[i])
        #     except:
        #         continue
    # print(data)
import pandas as pd

f = pd.read_csv('C:\\Users\\Administrateur\\PycharmProjects\\Adeline\\perso_m2i\\3-Python\\tempo.csv', encoding='UTF-8')
#print(f)
df = pd.DataFrame(f)
df = df[pd.notnull(df['collected_at'])]
print(df)
print(df['created_at'].count())