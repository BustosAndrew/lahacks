import google.generativeai as genai

genai.configure(api_key="AIzaSyDNOIh-OOaMZb0GG1iNqiTuTAKlejdkL9U")

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 0.95,
    "top_k": 32,
    "max_output_tokens": 1024,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


def generate_recipe(req: dict):
    prompt_parts = [
        "Provide a healthier recipe consistent with the provided ingredients, along with the steps to make them. Provide nutritional info where possible. Add a name for the recipe and categorize the details as either healthy or unhealthy. Ignore ingredients with quantity 0.",
        "Ingredients: " + req["ingredients"],
    ]
    response = model.generate_content(prompt_parts)
    return response.text
