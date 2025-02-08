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

Bot can greet, say goodbye and answer to thank you. 

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

