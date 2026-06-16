from datetime import datetime

print("AI Assistant Started")
print("Type 'exit' to stop\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "your name" in user:
        print("Bot: I am an AI Assistant created for internship project.")

    elif "time" in user:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif "date" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif "python" in user:
        print("Bot: Python is a powerful programming language used in AI, ML and Data Science.")

    elif "ai" in user or "artificial intelligence" in user:
        print("Bot: Artificial Intelligence helps machines think and make decisions like humans.")

    elif "machine learning" in user:
        print("Bot: Machine Learning is a branch of AI where systems learn from data.")

    elif "motivate me" in user:
        print("Bot: Success comes from consistency and hard work.")

    elif "joke" in user:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs.")

    elif "calculate" in user:
        expression = input("Enter expression: ")
        try:
            result = eval(expression)
            print("Bot: Result =", result)
        except:
            print("Bot: Invalid expression")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")