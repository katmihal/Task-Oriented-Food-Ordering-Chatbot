# Task-Oriented-Food-Ordering-Chatbot
A Rasa-powered chatbot for food and drink ordering, weather-based meal suggestions, and recipe recommendations.

## 📖 ABOUT 

This chatbot is designed to assist users in ordering food, checking the weather and recomment corresponding food, and finding recipes based on ingredients. 
It integrates real-world APIs to provide dynamic responses, enhancing the user experience.

## 💡 Motivation

The food industry is rapidly adopting AI-driven solutions for customer interactions. This chatbot aims to:

- Simplify food ordering with a natural conversation flow.
- Provide weather-based meal recommendations.
- Offer instant recipe suggestions for users interested in cooking at home.
- Showcase the power of task-oriented dialog systems using Rasa.

## Implemented Scenarios

### 3 Distinct Interaction Scenarios

1. Ordering Food
2. Ordering Drink
3. Cancel order 

Example 1 of Conversation:
> **User:** I want to order food.  
> **Bot:** What food would you like to order? (Pizza, Burger, Salad, etc.)  
> **User:** Pizza  
> **Bot:** Would you like a drink with your meal? (Water, Soda, Cola etc.)  
> **User:** Yes, a Cola.  
> **Bot:** Your Pizza with Cola is being prepared!

Example 2 of Conversation
> **User:** I want to order food.  
> **Bot:** What food would you like to order? (Pizza, Burger, Salad, etc.)  
> **User:** I would like a Burger  
> **Bot:** Would you like a drink with your meal? (Water, Soda, Cola etc.)  
> **User:** No, thank you.  
> **Bot:** Your burger is being prepared!

Example 3 of Conversation
> **User:** Cancel my order.  
> **Bot:** Your order has been cancelled let me know if you need anything else.

### Simulated Task Execution with Mock Up Action

User can ask for the menu and bot shows the available dishes.

Example of Conversation
> **User:** Show me the menu.  
> **Bot:** Our menu includes: Pizza, Burger, Salad, Souvlaki, Pasta, Steak, Sushi, Sandwich, Bagel.

### Tasks with Real-world Data Sources

1. Users can ask about the weather, and the chatbot suggests meals accordingly.
2. Users can ask for a recipe based on available ingredients.

Example 1 of Conversation
> **User:** What's the weather in Athens?  
> **Bot:** The current temperature in Athens is 5°C with clouds. How about ordering warm soup with a nice mulled wine? Would you like to place an order for this meal?  
> **User:** Yes sure.  
> **Bot:** Your warm soup with mulled wine is being prepared.  

Example 2 of Conversation
> **User:** What's the weather in Athens?  
> **Bot:** The current temperature in Athens is 5°C with clouds. How about ordering warm soup with a nice mulled wine? Would you like to place an order for this meal?  
> **User:** No.  
> **Bot:** No problem! Here’s the menu for you to choose from. Our menu includes: Pizza, Burger, Salad, Souvlaki, Pasta, Steak, Sushi, Sandwich, Bagel.  

Example 3 of Conversation
> **User:** Find me a recipe with tomato.  
> **Bot:**  Found this recipe for you: {recipe_title}. You can see it here: {recipe_url}
  
## 🔗 Integrated Data Sources

1. OpenWeather API (for weather-based meal suggestions)  
Why? Provides real-time weather data to help suggest suitable meals.  
Endpoint: https://openweathermap.org/api

2. Spoonacular API (for recipe recommendations)  
Why? Enables searching for recipes based on user-provided ingredients.  
Endpoint: https://spoonacular.com/food-api

## ⚠️ Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| Handling missing user input (e.g., missing food type) | Added slot handling and prompts to request missing details. |
| API failures (e.g., weather API down) | Implemented error handling with fallback messages. |
| No information in API (e.g., no weather info for a specific city) | An error message is returned. |
| Ensuring natural conversation flow | Used Rasa's rules and stories to guide interactions smoothly. |


## 🔑 Setup Instructions

1. Clone the Repository
$ git clone $ git clone https://github.com/katmihal/Task-Oriented-Food-Ordering-Chatbot.git   
$ cd Task-Oriented-Food-Ordering-Chatbot  

2. Install Dependencies
$ pip install rasa    
$ pip install requests

3. Set Up API Keys
Create an .env file and add:  
OPENWEATHER_API_KEY=your_api_key_here  
SPOONACULAR_API_KEY=your_api_key_here  

4. Train the Model  
$ rasa train  

5. Run the chatbot  
$ rasa run actions  
$ rasa shell

## Dialog Policy Experimentation (Bonus)

### Modifications & Rationale
- Added rules for greeting responses to ensure the bot always acknowledges the user before and after a task.  
- Modified action to handle weather in 4 different cases to dynamically suggest meals based on weather.  
Cold weather (<15°C): Suggests warm food and hot drinks.  
Mild weather (15-20°C): Suggests comfort food and refreshing drinks.  
Warm weather (20-30°C): Suggests light food and cold drinks.  
Hot weather (>30°C): Suggests cooling food and frozen drinks.  
- Added new food order phrases: Various phrases like "I need food," "I am starving," "I want to order food," etc. were added to recognize the user's intent to order food. 

### Observed Results & Insights
- More engaging interactions with personalized recommendations.  
- Users appreciated the answer to "Thank you" sentences, such as "Happy to help".  
- Variety of food order phrases: The bot now recognizes several different ways users ask for food, such as:  
"I need food"  
"I am starving"  
"I want to order food" etc.
Users are no longer limited to just one phrase to request food, which enhances the natural flow of conversation and improves user experience.  

## 📢 Future Improvements
1. Adding payment processing for food orders.
2. Expanding recipe database for nutrient information (e.g. calories, proteins, fat etc.).
3. Adding expected preparation time of the meal.

## 📌 Conclusion

This chatbot successfully demonstrates a task-oriented dialog system with real-world data integrations. 
It enhances user experience by dynamically responding to food orders, weather inquiries, and recipe searches.

