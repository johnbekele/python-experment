import os
from dotenv import load_dotenv
import requests
from openai import OpenAI
load_dotenv()




client=OpenAI(
   api_key=os.getenv("GPT")  
)




url = "https://api.openai.com/v1/responses"






def chat_with_ai(payload):
    response=client.responses.create(
        **payload
    )
    return response



def main():
    while True:
        user_text=input("chat with ai :)")
        payload = {
        "model": "gpt-4o-mini",  # valid model
        "input": user_text,
}    
        if(user_text):
            response=chat_with_ai(payload)
            print(response.output_text)
        else:
            print("please let me know what you want to ask ")
    



if __name__== "__main__":
    main()

    