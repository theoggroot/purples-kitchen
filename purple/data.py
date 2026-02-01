import requests
import random

# 1. EXTENSIVE INGREDIENT LIST
def get_all_ingredients_flat():
    return sorted([
        "Chicken", "Salmon", "Beef", "Pork", "Bacon", "Potato", "Onion", "Tomato", "Garlic", "Ginger", 
        "Spinach", "Avocado", "Cheese", "Butter", "Cream", "Milk", "Eggs", "Rice", "Pasta", "Noodles",
        "Bread", "Flour", "Sugar", "Honey", "Soy Sauce", "Lemon", "Chili", "Mushrooms", "Carrot", 
        "Broccoli", "Cauliflower", "Peas", "Corn", "Beans", "Lentils", "Chickpeas", "Tofu", "Paneer",
        "Cumin", "Turmeric", "Coriander", "Garam Masala", "Yogurt", "Ghee", "Basmati Rice", "Lamb"
    ])

# 2. FETCH RANDOM GLOBAL RECIPE
def get_random_recipe_from_api():
    try:
        url = "https://www.themealdb.com/api/json/v1/1/random.php"
        response = requests.get(url)
        data = response.json()
        if data['meals']:
            return format_meal_data(data['meals'][0])
    except Exception:
        return None

# 3. FETCH UNIQUE INDIAN RECIPE (With Image Fix)
def get_random_indian_recipe(seen_ids=[]):
    try:
        # A. Get list of all Indian IDs
        url_list = "https://www.themealdb.com/api/json/v1/1/filter.php?a=Indian"
        response = requests.get(url_list)
        data = response.json()
        
        if data['meals']:
            all_meals = data['meals']
            
            # Filter seen IDs
            available_meals = [m for m in all_meals if m['idMeal'] not in seen_ids]
            if not available_meals:
                available_meals = all_meals # Reset if all seen
            
            # B. Pick Random Summary
            summary = random.choice(available_meals)
            meal_id = summary['idMeal']
            backup_image = summary.get('strMealThumb') # <--- CAPTURE IMAGE HERE
            
            # C. Get Details
            url_details = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
            response_d = requests.get(url_details)
            data_d = response_d.json()
            
            if data_d['meals']:
                meal_data = format_meal_data(data_d['meals'][0])
                
                # Force image if missing in details
                if not meal_data['image'] and backup_image:
                    meal_data['image'] = backup_image
                    
                meal_data['id'] = meal_id 
                return meal_data
                
    except Exception as e:
        print(f"API Error: {e}")
        return None
    return None

# 4. SEARCH BY INGREDIENT
def find_recipes_smart(category, preference, user_ingredients):
    if not user_ingredients: return []
    
    main_ingredient = user_ingredients[0]
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={main_ingredient}"
    
    matches = []
    try:
        response = requests.get(url)
        data = response.json()
        if data['meals']:
            for item in data['meals'][:5]: 
                # Capture summary image
                thumb = item.get('strMealThumb')
                
                details_url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={item['idMeal']}"
                det_resp = requests.get(details_url)
                det_data = det_resp.json()
                if det_data['meals']:
                    formatted = format_meal_data(det_data['meals'][0])
                    
                    # Force image
                    if not formatted['image']: formatted['image'] = thumb
                    
                    # Veg Check
                    api_cat = formatted['tags'][0]
                    if preference == "Veg" and api_cat not in ["Vegetarian", "Vegan", "Pasta", "Side", "Dessert"]:
                        continue 
                    matches.append({"data": formatted, "name": formatted['name']})
    except Exception: pass
    return matches

# 5. DATA FORMATTER
def format_meal_data(meal):
    ingredients = []
    for i in range(1, 21):
        ing = meal.get(f"strIngredient{i}")
        measure = meal.get(f"strMeasure{i}")
        if ing and ing.strip():
            ingredients.append(f"{ing} ({measure})")
    
    instructions = meal.get('strInstructions', '').split('.')
    instructions = [step.strip() for step in instructions if len(step) > 5]

    return {
        "name": meal.get('strMeal'),
        "time": "30-45 mins",
        "diff": "Medium",
        "tags": [meal.get('strCategory', 'General'), meal.get('strArea', 'International')],
        "ingredients_needed": ingredients,
        "steps": instructions,
        "image": meal.get('strMealThumb') # Primary source
    }