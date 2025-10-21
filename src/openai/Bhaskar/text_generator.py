from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Get user input
user_prompt = input("Enter the beginning of your story: ")

# Generate response from OpenAI
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=user_prompt,
    max_tokens=100,
    temperature=0.7
)

# Print the generated text
print(response.choices[0].text.strip())