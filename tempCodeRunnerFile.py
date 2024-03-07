from openai import OpenAI

client = OpenAI(api_key="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")
import gradio


messages = [{"role": "system", "content": "You are a fitness and lifestyle coach that specializeds in helping young professionals with their fitness"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(model = "gpt-3.5-turbo",
    messages = messages)
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Fitness Coach")

demo.launch(share=True)