import sys

def read_items(filename, max_items):
    items = []
    file = open(filename, 'r')
    lines = file.readlines()
    
    # Processing file in groups of 3 lines: name, weight, value.
    i = 0
    count = 0
    while i + 2 < len(lines) and count < max_items:
        name = lines[i].strip()
        weight = float(lines[i+1].strip())
        value = float(lines[i+2].strip())
        items.append({
            'name': name,
            'weight': weight,
            'value': value,
            'index': count
        })
        i += 3
        count += 1
    return items

def get_value(item):
    return item['value']
def get_ratio(item):
    return item['value']/item['weight']

def greedy_knapsack(items, capacity, heuristic):
    # Select the key function based on the heuristic.
    if heuristic == "by_value":
        sorted_items = sorted(items, key=get_value, reverse=True)
    elif heuristic == "value_to_weight": 
        sorted_items = sorted(items, key=get_ratio, reverse=True)   
    remaining = capacity
    chosen = [False] * len(items)
    total_weight = 0
    total_value = 0

    # Iterate over the sorted items; add an item if it fits.
    for item in sorted_items:
        if item['weight'] <= remaining:
            # Mark the chosen item in its original order.            
            chosen[item['index']] = True  
            remaining -= item['weight']
            total_weight += item['weight']
            total_value += item['value']
             
    return chosen, total_weight, total_value

def main():
    # Check for correct number of command line arguments.
    if len(sys.argv) != 5:
        print("Usage: python3 greedy_knapsack.py max_items weight_limit heuristic_name input_file_name")
        sys.exit(1)

    try:
        max_items = int(sys.argv[1])
        capacity = float(sys.argv[2])
    except ValueError:
        print("Error: max_items and weight_limit must be numeric.")
        sys.exit(1)

    heuristic = sys.argv[3]
    input_file = sys.argv[4]

    # Read items from file.
    items = read_items(input_file, max_items)
    
    # Solve the knapsack using the greedy heuristic.
    chosen, total_weight, total_value = greedy_knapsack(items, capacity, heuristic)
    
    # Create binary string in the order of input items.
    binary_str = ''.join('1' if flag else '0' for flag in chosen)
    
    # printing the solution
    # First line: binary string, second line: total weight, third line: total value
    print(binary_str)
    print(total_weight)
    print(total_value)

if __name__ == "__main__":
    main()
