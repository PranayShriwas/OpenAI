 Day 5: Designing a prompt to stimulate responses from the OpenAI model.

 # Documentation:
"""
This script generates a short story using OpenAI's GPT-3 models.

Usage:
1. Set up your OpenAI API key by assigning it to the `api_key` variable.
2. Define the prompt for the story in the `prompt` variable.
3. The script iterates over a list of engines to try generating the story using each engine.
4. If a response is successfully generated, it prints the generated story.
5. If no response is generated using any available engine, it prints an error message.

Dependencies:
- This script requires the `openai` Python library.
- Install the library using `pip install openai`.

Issue:
I have done what is required to send a prompt and get response using openAi model but there is an issue which is "Unable to generate response using any available engine."
All the engines are not Supported in my environment.
