from database.db import get_db_connection
from core.menu import menu_keys,get_menu
import re


def place_order(user, order_details):
    """Inserts a new order into the database."""
    menu_items=menu_keys()
    print(f'this is my menu items {menu_items}')

    order_items=re.split(r'[,\s]+',order_details)   #order_details.split() #split items from incomming msg /// may be here a problem due to default split by space if user is using comma ','
    print(f'this is my menu keys {type(order_items)}')
    valid_items=[]
    invalid_items=[]

    for i in order_items:
        item=i
        print(f'this is my order item {item}')
        if item in menu_items:
            valid_items.append(item) #append present items 
        else:
            invalid_items.append(item)   

    print(f'order {valid_items}, not valid{invalid_items}')      

    if not valid_items:  #if no valid item from menu
        return f"None of this items are present in our menu.\n{(get_menu())}"


    order_summary = ", ".join(valid_items)  # Create a readable list of valid items using ','

    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO orders (user, order_details) VALUES (?, ?)", (user, order_summary))
            conn.commit()

        response = f"Order received: {order_summary}\nType 'confirm' to proceed."
        if invalid_items:
            response += f"\n\n(Note: We do not have {', '.join(invalid_items)} in our menu.)" #note for invalid items
        
        return response

    except Exception as e:
        return "Error saving order. Please try again."



    # try:
    #         with get_db_connection() as conn:
    #             cursor = conn.cursor()
    #             cursor.execute("INSERT INTO orders (user, order_details) VALUES (?, ?)", (user, order_details))
    #             conn.commit()
    #         return f"Order received: {order_details}\n-Type 'confirm' to proceed."
    # except Exception as e:
    #         return "Error saving order. Please try again."

def confirm_order(user):
    """Updates the order status to confirmed."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE orders SET status = 'confirmed' WHERE user = ?", (user,))   
            conn.commit()
        return "Your order is confirmed! We will prepare your fresh salad shortly."
    except Exception as e:
        return "Error confirming order. Please try again."
