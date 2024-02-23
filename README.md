Day 5: Designing a prompt to stimulate responses from the OpenAI model.

#Documentation For OpenAI model:

Usage:
1. Set up your OpenAI API key by assigning it to the `api_key` variable.
2. Define the prompt for the story in the `prompt` variable.
3. The script iterates over a list of engines to try generating the story using each engine.
4. If a response is successfully generated, it prints the generated story.
5. If no response is generated using any available engine, it prints an error message.

Dependencies And How To Run:
1. Make sure you have Python installed on your system.
2. Install the `openai` library using pip. Open a command prompt or terminal and run the following command:
   pip install openai
3. Copy the script to a Python file (e.g., `generate_story.py`) on your local machine.
4. Open a command prompt or terminal, navigate to the directory where the script is located, and run the script using Python. For example:
   python generate_story.py
5. The script will execute and attempt to generate a short story using OpenAI's GPT-3 models. If successful, it will print the generated story. If none of the models are available or deprecated, it will print an error message.

Issue:
I have done what is required to send a prompt and get response using openAi model but there is an issue which is "Unable to generate response using any available engine."
All the engines are not Supported in my environment.

Free Engine:-
text-davinci-003: Another variant of the text-davinci model, which may have different training data or fine-tuning.
text-curie: This model is designed to balance quality and speed, making it suitable for applications that require quick responses without sacrificing too much on quality.
text-babbage: This model is optimized for speed and efficiency, making it ideal for scenarios where response time is critical, such as chatbots or real-time applications.
text-gpt-3.5-turbo: A variant of the GPT-3.5 model optimized for speed and efficiency, providing fast responses while maintaining high-quality text generation.
text-gpt-3.5: The standard GPT-3.5 model, offering a balance between speed and quality for various natural language processing tasks

