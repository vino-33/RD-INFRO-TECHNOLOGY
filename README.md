RD INFRO TECHNOLOGY Internship - Task 1

Chatbot with Rule-Based Responses

This repository contains the solution for Task 1 ,of the RD INFRO TECHNOLOGY internship: a simple chatbot that responds to user inputs based on predefined rules. The chatbot is implemented using Python and focuses on providing interactive and meaningful responses through basic `if-else` logic.


Features
- A rule-based chatbot that provides responses based on predefined keywords.
- Interactive conversation flow.
- Easy to customize or extend for additional scenarios.

How to Use
1. Clone this repository to your local machine or download the ZIP file.
2. Ensure you have Python installed on your system. You can check by running:
   ```bash
   python --version
   ```
3. Run the chatbot script:
   ```bash
   python chatbot.py
   ```
4. Follow the chatbot's prompts and enter your responses to interact.
   
Files in the Repository
- `chatbot.py`: The Python script for the chatbot.

Steps to Set Up and Submit
1. **Create the chatbot:** Write a Python script (`chatbot.py`) using predefined rules.
2. **Push the code to GitHub:**
   - Initialize a Git repository.
   - Add the chatbot file and other relevant files.
   - Commit the changes with a descriptive message.
   - Push the changes to the GitHub repository.
3. **Verify the code:**
   - # Simple chatbot with predefined rules

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

Start the chatbot
chatbot()

4. Repository link:(https://github.com/vino-33/RD-INFRO-TECHNOLOGY)


Contributors
- Name: Vinoliyaa
- GitHub Username: [vino-33](https://github.com/vino-33)
- Email: vinoliyaanancy003@gmail.com


Acknowledgments
- This project is part of the RD INFRO TECHNOLOGY internship program.
- It was a valuable learning experience in Artificial Intelligence and Git/GitHub.

---
