from openai import OpenAI

client = OpenAI(
    api_key="KEY",
    base_url="https://api.proxyapi.ru/openai/v1",
)


def chat_with_ai():
    messages = []

    print("Type 'exit' to exit")
    print("Start conversation with AI:")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        messages.append({"role": "user", "content": user_input})
        # messages.append({"role": "system", "content": "answer as a funny clown"})

        chat_completion = client.chat.completions.create(
            # model="gpt-3.5-turbo",
            model="gpt-3.5-turbo-1106",
            messages=messages
        )

        ai_response = chat_completion.choices[0].message.content
        print("AI:", ai_response)

        messages.append({"role": "assistant", "content": ai_response})


chat_with_ai()
