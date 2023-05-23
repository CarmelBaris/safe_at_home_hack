import openai
import configparser

# Load API key from config.ini
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['API_KEYS']['openai']

# Set up OpenAI API
openai.api_key = api_key

# Define the prompt template
PROMPT_TEMPLATE = "Return a full word that describes the relationship violence type based" \
                  "on the provided input." \
                  "\nRelationship violence type classification:\nUser Input: \"{user_input}\"\nViolence Type:"

# Define the violence types
VIOLENCE_TYPES = ["verbal", "physical", "financial", "social", "spiritual", "intimate", "else", "none"]

def classify_violence_type(user_input):
    prompt = PROMPT_TEMPLATE.format(user_input=user_input)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1,
        temperature=0.0,
        n=1
    )

    if len(response.choices) > 0 and 'text' in response.choices[0]:
        return response.choices[0]['text'].strip()
    else:
        return None



