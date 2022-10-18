# Databricks notebook source
pip install flask


# COMMAND ----------

import requests

# COMMAND ----------

response = requests.get('https://randomuser.me/api')
##print(response.status_code)
##print(response.json())

gender = response.json()['results'][0]['gender']


title = response.json()['results'][0]['name']['title']

first_name = response.json()['results'][0]['name']['first']

last_name = response.json()['results'][0]['name']['last']

Date_Birth = response.json()['results'][0]['dob']['date']

age = response.json()['results'][0]['dob']['age']
print (gender)
print(f'{title}. {first_name} {last_name}')
print (f'Age:{age}')
print(f'DOB:{Date_Birth}')

# COMMAND ----------

###Extracting Tweet from twitter Account 
##import variables 
import requests
import os
import json
import pandas
import csv
import datetime
import time 
import dateutil.parser
import unicodedata

# COMMAND ----------

os.environ['Token'] = '<value erased>'

# COMMAND ----------

def auth ():
  return os.getenv('Token')

# COMMAND ----------

def create_headers(bearer_token):
  headers = {"Authorization": "Bearer {}".format(bearer_token)}
  
  return headers
print (create_headers)

# COMMAND ----------

def create_url(keyword, start_date, end_date, max_results = 10):
  Base_url = "https://api.twitter.com/2/tweets/search/all"
  query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
  return (Base_url, query_params)

# COMMAND ----------

def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

# COMMAND ----------

#Inputs for the request
bearer_token = auth()
headers = 'create_headers(bearer_token)'
keyword = "(church) or (bigot)"
start_time = "2021-03-01T00:00:00.000Z"
end_time = "2021-09-31T00:00:00.000Z"
max_results = 15

# COMMAND ----------

url = create_url(keyword, start_time,end_time, max_results)
json_response = connect_to_endpoint(url[0], headers, url[1])
