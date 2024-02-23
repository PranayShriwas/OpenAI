import openai

# Set up your OpenAI API key
api_key = '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'
openai.api_key = api_key

# Define your prompt
prompt = "Write a short story about a detective solving a mystery in a small town."

# List of engines to try
engines = ["davinci-codex", "davinci-instruct-beta", "text-davinci-003"]

# Flag to track if a response is generated successfully
response_generated = False

for engine in engines:
    try:
        # Generate a response using the current engine
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=150  # Adjust the length of the generated response as needed
        )

        # Print the generated response
        print("Generated Response:")
        print(response.choices[0].text.strip())

        # Set the flag to indicate a successful response
        response_generated = True

        # Break out of the loop since a successful response is obtained
        break

    except openai.error.InvalidRequestError as e:
        # Print error message if the engine is deprecated
        print(f"The model {engine} has been deprecated:", e)

if not response_generated:
    print("Unable to generate response using any available engine.")
