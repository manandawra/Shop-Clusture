import json  
import os  
  
def register_shop():  
    shop_details = {  
        "shop_name": input("Enter the shop name: "),  
        "owner_name": input("Enter the owner's name: "),  
        "address": input("Enter the shop address: "),  
        "products": []  
    }  
      
    while True:  
        product = {}  
        product["product_name"] = input("Enter product name: ")  
        product["price"] = float(input("Enter product price: "))  
        product["quantity"] = int(input("Enter product quantity: "))  
        print(product)
        shop_details["products"].append(product)  
  
        add_another = input("Would you like to add another product? (yes/no): ").lower()  
        if add_another != "yes":  
            break  
  
    return shop_details  
  
def save_shop_details(shop_details):  
    all_shops = []  
  
    # Check if the file exists  
    if os.path.exists("shop_details.json"):  
        # Read the existing data  
        try:  
            with open("shop_details.json", "r") as file:  
                all_shops = json.load(file)  
                # Ensure that all_shops is a list  
                if not isinstance(all_shops, list):  
                    all_shops = [all_shops]  
        except json.JSONDecodeError:  
            # If JSON is not in the correct format, initialize as an empty list  
            all_shops = []  
  
    # Append the new shop details  
    all_shops.append(shop_details)  
      
    # Save the updated list of shops back to the file  
    with open("shop_details.json", "w") as file:  
        json.dump(all_shops, file, indent=4)  
  
# Rest of your code remains the same    
  
def main():  
    print("Welcome to Shop Registration")  
    shop_details = register_shop()  
    save_shop_details(shop_details)  
    print("Shop has been registered successfully!")  
  
if __name__ == "__main__":  
    main()  