import openai
import gradio as gr

#api key and finetuned model id
openai.api_key = " " #need key

fine_tuned_model_id ='ft:gpt-3.5-turbo-0125:personal:astrotale:9CXF5nl2'

system_message ='You are Kara. You are a creative Storyteller who writes stories that including astronomy facts. You write very creative and interesting short stories with dialogues that include astronomy facts. Your target audience is preteens'
test_messages = [{"role": "system", "content": system_message}]

def get_assistant_response(user_message):

  test_messages.append({"role": "user", "content": user_message})


  response = openai.ChatCompletion.create(
      model=fine_tuned_model_id,
      messages=test_messages,
      temperature=1,
      max_tokens=1000
  )
  test_messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
  #print(test_messages)

  return response["choices"][0]["message"]["content"]

"""
def forGradio(input_fromUser):
  while True:
    user_message = input(input_fromUser)
    assistant_response = get_assistant_response(user_message)
    return assistant_response

"""
  #print("Assistant:", assistant_response)

import time

with gr.Blocks() as demo:
    gr.Markdown("AstroTales")
    chatbot = gr.Chatbot(label='Kara:')
    msg = gr.Textbox(label='Your Message:')
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = get_assistant_response(message)
        chat_history.append((message, bot_message))
        time.sleep(2)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()

	