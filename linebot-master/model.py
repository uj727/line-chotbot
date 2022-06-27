import os
import openai
# from linebot import (LineBotApi, WebhookHandler)
# from linebot.exceptions import (InvalidSignatureError)
# from linebot.models import *
openai.api_key = "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"


def ask(question): 
    print(question)
    response = openai.Completion.create(
    model="curie:ft--2022-06-07-04-56-51",
    prompt=question,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0 ,
    stop=["END"]
    )
    story = response['choices'][0]['text'] 
   # return str(story) 
    print( str(story) )
#ask("what are the symptom of heartdisease") 