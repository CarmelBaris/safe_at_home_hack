from classify_violence import classify_violence_type

# Example user inputs
user_inputs = {
    "verbal": "My spouse insulted me in front of the kids.",
    "physical": "My spouse slapped me.",
    "financial": "My partner is denying me access to my bank account.",
    "social": "He has isolated me from everyone.",
    "spiritual": "My partner said that God wants us to be together and that we cannot deny the will of God.",
    "intimate": "He convinced me to sleep with him even after I told him I was not in the mood.",
    "else": "He keeps causing me so much pain.",
    "none": "He is so annoying, maybe I should break up with him."
}


# Process user inputs and print results
for user_input in user_inputs:
    violence_type = classify_violence_type(user_input)
    print(f"User Input: {user_inputs.index(user_input)}\nViolence Type: {violence_type}\n")