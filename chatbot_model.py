from transformers import pipeline

# Load a small pre-trained conversational model
chatbot = pipeline("text-generation", model="gpt2")

def get_bot_response(user_input):
    response = chatbot(user_input, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']
