from openai import OpenAI

client = OpenAI()


def text2img(prompt):
    print(prompt)
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    return response.data[0].url
