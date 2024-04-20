import requests

# Replace these values with your Gemini API credentials
API_KEY = "AIzaSyBD85VX9F60wicPXBO4IDXI5shLW6aaKlY"
SECRET_KEY = "YOUR_SECRET_KEY"

def recognize_dish(image_url):
    endpoint = "https://api.gemini.ai/v1/recognize/dish"
    headers = {
        "Content-Type": "application/json",
        "Api-Key": API_KEY,
        "Api-Secret": SECRET_KEY
    }
    data = {
        "image_url": image_url
    }
    try:
        response = requests.post(endpoint, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            print("Error:", response.text)
            return None
    except Exception as e:
        print("Error:", e)
        return None

def display_results(result):
    if result and 'success' in result and result['success']:
        dish_name = result['data']['name']
        recipe_steps = result['data']['recipe_steps']
        print("Dish:", dish_name)
        print("Recipe Steps:")
        for step in recipe_steps:
            print(step)
    else:
        print("Recognition failed.")

def main():
    image_url = input("Enter the URL of the dish image: ")
    result = recognize_dish(image_url)
    display_results(result)

if __name__ == "__main__":
    main()
