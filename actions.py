# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
import requests
from rasa_sdk.events import SlotSet
import random
from typing import Text, List, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionShowMenu(Action):
    def name(self):
        return "action_show_menu"

    def run(self, dispatcher, tracker, domain):
        menu_items = ["Pizza", "Burger", "Salad", "Souvlaki", "Pasta", "Steak", "Sushi", "Sandwich", "Bagel"]
        dispatcher.utter_message(text=f"Our menu includes: {', '.join(menu_items)}.")
        return []
    
class ActionGetWeather(Action):
    def name(self):
        return "action_get_weather"

    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot("city")

        if not city:
            dispatcher.utter_message(text="Please provide a city to check the weather.")
            return []

        api_key = "your_key_here"  
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url).json()

        if response.get("main"):
            temperature = response["main"]["temp"]
            description = response["weather"][0]["description"]

            food_list = []
            drink_list = []

            if temperature < 15:
                food_list = ["warm soup", "chili con carne", "hot dog", "mac and cheese"]
                drink_list = ["hot chocolate", "coffee", "tea", "mulled wine", "cappuccino"]
            elif 15 <= temperature < 20:
                food_list = ["pizza", "pasta", "grilled cheese", "quiche", "salmon", "sandwiches"]
                drink_list = ["lemonade", "soda", "beer"]
            elif 20 <= temperature < 30:
                food_list = ["salad", "sushi", "grilled vegetables", "tacos", "poke bowl", "fish"]
                drink_list = ["iced coffee", "smoothie", "watermelon juice", "cold lemonade", "iced tea"]
            else:
                food_list = ["smoothie bowl", "fruit salad", "tomato salad", "ice cream"]
                drink_list = ["smoothie", "iced lemonade", "cold brew coffee", "frozen margarita"]

            selected_food = random.choice(food_list)
            selected_drink = random.choice(drink_list)

            dispatcher.utter_message(
                text=f"The current temperature in {city} is {temperature}°C with {description}. How about ordering {selected_food} with a nice {selected_drink}?"
            )

            dispatcher.utter_message(text="Would you like to place an order for this meal?")

            return [SlotSet("food_type", selected_food), SlotSet("drink", selected_drink)]

        else:
            dispatcher.utter_message(text=f"Sorry, I couldn't fetch the weather for {city}. Please try again.")
            return []

SPOONACULAR_API_KEY = "your_key_here" 

class ActionGetRecipe(Action):
    def name(self) -> Text:
        return "action_get_recipe"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ingredients = tracker.get_slot("recipe_ingredients")
        
        if not ingredients:
            dispatcher.utter_message(text="Please provide an ingredient to find a recipe.")
            return []
        
        url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=1&apiKey={SPOONACULAR_API_KEY}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data:
                recipe = data[0]
                recipe_title = recipe.get("title", "Unknown recipe")
                recipe_id = recipe.get("id", "")
                recipe_url = f"https://spoonacular.com/recipes/{recipe_title.replace(' ', '-')}-{recipe_id}"
                dispatcher.utter_message(text=f"Found this recipe for you: {recipe_title}. You can see it here: {recipe_url}")
            else:
                dispatcher.utter_message(text="Couldn't find recipes with these ingredients. Try something else.")
        else:
            dispatcher.utter_message(text="There is a problem. Please try again later.")
        
        return [SlotSet("recipe_ingredients", None)]

