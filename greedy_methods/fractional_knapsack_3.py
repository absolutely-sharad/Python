"""
Problem Statement:
------------------
The Fractional Knapsack Problem involves selecting items with given weights and values 
to maximize the total value in a knapsack of limited capacity. Unlike the 0/1 Knapsack 
Problem, here you can take fractions of items.

Approach:
---------
1. Compute the value-to-weight ratio for each item.
2. Sort the items by this ratio in descending order.
3. Add items to the knapsack fully or partially based on the remaining capacity.

Arguments:
----------
1. capacity (int): The maximum weight the knapsack can carry.
2. items (list of Item objects): A list of items where each item has a value and weight.

Returns:
--------
float: The maximum total value that can be carried in the knapsack.

Example:
--------
Input:
    Items = [(Value: 60, Weight: 10), (Value: 100, Weight: 20), (Value: 120, Weight: 30)]
    Capacity = 50
Output:
    Maximum value in Knapsack = 240.00
"""

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Function to calculate the maximum value in the knapsack
def fractional_knapsack(capacity, items):
    """
    Calculate the maximum value that can fit in the knapsack.

    Args:
        capacity (int): The maximum weight the knapsack can carry.
        items (list[Item]): List of items with value and weight.

    Returns:
        float: Maximum total value in the knapsack.
    """
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0.0  # Total value in the knapsack

    for item in items:
        if capacity >= item.weight:
            # If the knapsack can carry the full item
            capacity -= item.weight
            total_value += item.value
        else:
            # If the knapsack can only carry part of the item
            total_value += (item.value / item.weight) * capacity
            break

    return total_value

# Driver code
if __name__ == "__main__":
    # Example input
    items = [
        Item(60, 10),  # Value: 60, Weight: 10
        Item(100, 20),  # Value: 100, Weight: 20
        Item(120, 30)   # Value: 120, Weight: 30
    ]
    capacity = 50

    # Calculate the maximum value that can be carried in the knapsack
    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value in Knapsack = {max_value:.2f}")
