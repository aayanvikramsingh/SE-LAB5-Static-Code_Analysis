"""
Lab 5: Inventory System
A simple command-line inventory management script.
"""

import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Adds a quantity of an item to the inventory.
    Initializes a new log list if one isn't provided.
    """
    if not item:
        return

    if logs is None:
        logs = []

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")


def remove_item(item, qty):
    """Removes a quantity of an item from the inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        # Item not in stock, do nothing.
        pass


def get_qty(item):
    """Gets the current quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Loads the inventory data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            loaded_data = json.loads(f.read())
            stock_data.clear()
            stock_data.update(loaded_data)
    except FileNotFoundError:
        print(f"Warning: {file} not found. Starting with empty inventory.")
        stock_data.clear()
    except json.JSONDecodeError:
        print(f"Error: Could not decode {file}. Starting with empty inventory.")
        stock_data.clear()


def save_data(file="inventory.json"):
    """Saves the current inventory data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data, indent=4))


def print_data():
    """Prints a report of all items and their quantities."""
    print("Items Report")
    print("--------------")
    for item, quantity in stock_data.items():
        print(f"  {item} -> {quantity}")
    print("--------------")


def check_low_items(threshold=5):
    """Returns a list of items below a given quantity threshold."""
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """Main function to demonstrate inventory operations."""
    load_data()
    add_item("apple", 10)
    add_item("banana", -2)
    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    print_data()


if __name__ == "__main__":
    main()
