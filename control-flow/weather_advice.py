# weather_advice.py

def weather_recommendation():
    """
    Asks the user for the current weather and provides clothing recommendations.
    """
    # 1. Prompt User for Weather Input and convert to lowercase for case-insensitive comparison
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

    # 2. Provide Clothing Recommendations using conditional statements
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        # 3. Handle unexpected input
        print("Sorry, I don't have recommendations for this weather.")

# Execute the function
if __name__ == "__main__":
    weather_recommendation()