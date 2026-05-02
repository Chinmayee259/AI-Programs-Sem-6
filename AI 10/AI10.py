def chatbot():
    print("Chatbot: Hello! Welcome to Customer Support 😊")
    print("Type 'exit' to end the chat.\n")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Chatbot: Thank you! Have a nice day 😊")
            break

        elif "hello" in user or "hi" in user:
            print("Chatbot: Hi! How can I help you?")

        elif "price" in user or "cost" in user:
            print("Chatbot: Our products start from ₹500.")

        elif "delivery" in user or "time" in user:
            print("Chatbot: Delivery takes 3-5 working days.")

        elif "return" in user or "refund" in user:
            print("Chatbot: You can return the product within 7 days.")

        elif "payment" in user or "pay" in user or "money" in user:
            print("Chatbot: We accept UPI, cards, and cash on delivery.")

        else:
            print("Chatbot: Sorry, I didn't understand that. Please try again.")

chatbot()


# ------------ OUTPUT -----------------
# Chatbot: Hello! Welcome to Customer Support 😊
# Type 'exit' to end the chat.

# You: hi
# Chatbot: Hi! How can I help you?
# You: What is the price?
# Chatbot: Our products start from ₹500.
# You:  How much does it cost?
# Chatbot: Our products start from ₹500.
# You: How long is delivery?
# Chatbot: Delivery takes 3-5 working days.
# You: Can I get refund?
# Chatbot: You can return the product within 7 days.
# You: How can I pay?
# Chatbot: We accept UPI, cards, and cash on delivery.
# You: exit
# Chatbot: Thank you! Have a nice day 😊