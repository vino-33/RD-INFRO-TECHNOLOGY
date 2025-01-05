# Simple chatbot with predefined rules

def chatbot():
    print("Hello! I am your friendly customer support assistant.")
    print("You can ask me about store hours, product availability, or just say goodbye.")
    
    while True:
        user_input = input("\nYou: ").lower()  # Taking user input and converting to lowercase for easier matching
        
        # Respond based on predefined rules
        if 'store hours' in user_input:
            print("Chatbot: Our store is open from 9 AM to 6 PM, Monday to Saturday.")
        elif 'product' in user_input and 'available' in user_input:
            print("Chatbot: We have a wide variety of products in stock. Please specify which product you are interested in!")
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello there! How can I assist you today?")
        elif 'thank you' in user_input:
            print("Chatbot: You're welcome! Let me know if you need anything else.")
        elif 'goodbye' in user_input or 'bye' in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break  # End the chat loop
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you please rephrase?")

# Start the chatbot
chatbot()
