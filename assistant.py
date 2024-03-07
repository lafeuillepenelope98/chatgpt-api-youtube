from openai import OpenAI

client = OpenAI(api_key="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")


messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=messages)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")