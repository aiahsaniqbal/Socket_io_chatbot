import requests
import json
import pandas as pd
import os


def storing_data(user_id,val1,val2):

    df = pd.DataFrame({'col1': [val1], 'col2': [val2]})

    fname = user_id+'.csv'

    if os.path.isfile(fname):
        df = df.append(pd.read_csv(fname))
    df.to_csv(fname, index=False)


def call_Rasa(user_id,msg):
    url = "http://localhost:5005/webhooks/rest/webhook"

    payload = json.dumps({
        "sender": user_id,
        "message": msg
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response= requests.request("POST", url, headers=headers, data=payload)
    print(response)
    print('*************************************\n','------------Response--------------\n\n', response)
    return response