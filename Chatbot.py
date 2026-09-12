def chatbot():
    print("================================")
    print("       RULE-BASED CHATBOT")
    print("================================")
    print("Bot: Hello! I am your chatbot.")
    print("Bot: Type 'hello', 'how are you', 'what is your name', or 'bye'.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi! Nice to meet you!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Bot: My name is CodeBot.")

        elif user_input == "what can you do":
            print("Bot: I can respond to simple predefined questions.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()