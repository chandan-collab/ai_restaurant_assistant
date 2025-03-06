MENU_ITEMS = {
    "NON-VEG":"",
    "chicken": "Creamy tomato-based chicken curry - 320",
    "biryani": "Aromatic basmati rice with chicken - 350",
    "mutton": "Spicy mutton in rich gravy - 400",
    "fishFry": "Crispy fried fish - 300",
    "egg": "Boiled eggs in masala curry - 180",
    "roll": "Stuffed chicken wrap - 150",

    "Desserts":"",
    "gulab jamun": "Deep-fried sweet - 120",
    "rasmalai": "Soft paneer soaked in saffron milk - 140",
    "jalebi": "Crispy deep-fried sugar spirals - 100",
    "kheer": "Rice pudding with dry fruits - 130",
    "gajar halwa": "Sweet carrot dessert - 150"
}

def get_menu():
    
    menu_text = "Our menu specializes in:\n"
    for item, description in MENU_ITEMS.items():
        menu_text += f"- {item.capitalize()}: {description}\n"
    menu_text += "\nType 'order  <items>' to place an order."
    return menu_text

def menu_keys():
    key_list=[]
    for i in MENU_ITEMS.keys():
        key_list.append(i)
    return key_list
