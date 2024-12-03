from groq import Groq

client = Groq(api_key="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")

def ask_question(message):
    chat_completion = client.chat.completions.create(

        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Please give a one line answer to this question:" + message,
            }
        ],
        model="llama3-8b-8192",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )

    # Print the completion returned by the LLM.
    return chat_completion.choices[0].message.content


# def ask_question(message, sys_message="You are a helpful agent.",
#          model="groq:llama-3.2-3b-preview"):
#     # Initialize the AI client for accessing the language model
#     client = ai.Client(provider_configs)
#     # Construct the messages list for the chat
#     messages = [
#         {"role": "system", "content": sys_message},
#         {"role": "user", "content": "Please give a one line answer to this question:" + message }
#     ]

#     # Send the messages to the model and get the response
#     response = client.chat.completions.create(model=model, messages=messages)

#     # Return the content of the model's response
#     return response.choices[0].message.content

# def ask_question(message, sys_message="You are a helpful agent.",
#          model="groq:llama-3.2-3b-preview"):

#          client = Groq(
#              api_key=groq_api_key,
#          )
         
#          chat_completion = client.chat.completions.create(
#                 messages = [
#                           {"role": "system", "content": sys_message},
#                           {"role": "user", "content": "Please give a one line answer to this question:" + message }
#                       ],
#              model=model,
#          )
#          response = chat_completion.choices[0].message.content

#     # Return the content of the model's response
#     return response



# import aisuite as ai
# import os
# from dotenv import load_dotenv
# load_dotenv()
# os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

# # client = ai.Client()

# # messages = [
# #     {"role": "system", "content": "You are a helpful agent, who answers with brevity."},
# #     {"role": "user", "content": 'Hi'},
# # ]

# # # Request a response from the model
# # response = client.chat.completions.create(model="groq:llama-3.2-3b-preview", messages=messages)

# def ask_question(message, sys_message="You are a helpful agent.",
#          model="groq:llama-3.2-3b-preview"):
    
#     client = ai.Client()
    
#     messages = [
#         {"role": "system", "content": sys_message},
#         {"role": "user", "content": "Please give a one line answer to this question:" + message }
#     ]

#     # Send the messages to the model and get the response
#     response = client.chat.completions.create(model=model, messages=messages)

#     # Return the content of the model's response
#     return response.choices[0].message.content

