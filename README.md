# LAB_MODULES_PACKAGES

## Restaurant

In this exercise, you'll create a Python package named `restaurant` that
contains a module named `chef`. The `chef` module includes functions for
managing dishes in a restaurant system without using classes.

In this exercise, you'll create a Python package named restaurant that contains a module named chef. The chef module should include functions for managing dishes in a restaurant system without using classes.

Follow these steps to complete the exercise:

1- Create a folder named restaurant in your working directory.

2- Inside the restaurant folder, create a file named __init__.py. This file is required for Python to treat the directory as a package.

3- Create a new file named chef.py inside the restaurant folder. In this file, define the following functions:

- add_dish(menu, name, price) – takes a dictionary (menu), a dish name (string), and a price (float or int) as input, and adds a new dish to the menu as a dictionary with the keys 'name', 'price', and 'available'. The 'available' key should have a boolean value, initially set to True. If the dish already exists in the menu, print an appropriate message.

- remove_dish(menu, name) – takes a dictionary (menu) and a dish name (string) as input, and removes the dish from the menu. If the dish does not exist in the menu, print an appropriate message.

- update_price(menu, name, new_price) – takes a dictionary (menu), a dish name (string), and a new price (float or int), and updates the price of the dish. If the dish does not exist, print an appropriate message.

- place_order(menu, name) – takes a dictionary (menu) and a dish name (string) as input, and sets the 'available' key of the dish to False to indicate it’s being prepared. If the dish does not exist or is not available, print an appropriate message.

- display_menu(menu) – takes a dictionary (menu) as input and prints all the dishes in the menu in a formatted way.

4 - Write a script named main.py in your working directory (outside the restaurant folder) that imports and uses the chef module from the restaurant package to manage a simple restaurant menu.

5- Use the functions from chef to add dishes, remove a dish, update a price, place an order, and display the menu.


### File Tree

    .
    ├── README.md            
    ├── main.py
    └── restaurant/
        ├── __init__.py
        └── chef.py

------------------------------------------------------------------------

## Sample Output

When you run `python main.py`, you should see:

    Pizza - $12.99 - Available
    Pasta - $9.99 - Available
    Salad - $6.99 - Available

    Pizza - $12.99 - Ordered
    Pasta - $9.99 - Available
    Salad - $6.99 - Available

    Pizza - $13.99 - Available
    Pasta - $9.99 - Available
    Salad - $6.99 - Available

------------------------------------------------------------------------
