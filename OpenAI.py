import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def generate_response(prompt):
  
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can experiment with different engines
        prompt=prompt,
        max_tokens=150,  # Adjust as needed
        temperature=0.7,  # Adjust as needed (higher values for more randomness)
        stop=None  # You can customize stop conditions if needed
    )
    return response.choices[0].text.strip()

def main():
    # Example prompt
    user_input = input("Customer: ")
    
    while user_input.lower() != 'exit':
       
        response = generate_response(f"Customer: {user_input}\nSupport Agent:")

        # Display the generated response
        print(f"Support Agent: {response}")

        # Get the next user input
        user_input = input("Customer: ")

if __name__ == "__main__":
    main()
