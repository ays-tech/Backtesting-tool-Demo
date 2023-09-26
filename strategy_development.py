# File: strategy_development.py

import openai

# Set up your OpenAI API key
api_key = "YOUR_OPENAI_API_KEY"
openai.api_key = api_key

# Function to generate trading strategy ideas using a language model
def generate_strategy(currency_pair, strategy_description):
    try:
        # Define the user prompt for the language model
        prompt = f"Generate a trading strategy for {currency_pair} based on the following description: {strategy_description}"

        # Call the language model to generate a strategy idea
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )

        # Extract and return the generated strategy from the response
        generated_strategy = response.choices[0].text.strip()
        return generated_strategy
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    currency_pair = "EUR/USD"
    strategy_description = "A trend-following strategy based on moving averages."
    generated_strategy = generate_strategy(currency_pair, strategy_description)
    if generated_strategy is not None:
        print("Generated Strategy:")
        print(generated_strategy)
