def flatten_array(nested_list):
    """
    Flattens a deeply nested list into a single-level list.
    
    Args:
        nested_list (list): A list that can contain nested lists at any depth.
        
    Returns:
        list: A single-level, flattened list with all elements from the input nested_list.
        
    Example:
        Input: [1, [2, [3, [4, 5]], 6], 7]
        Output: [1, 2, 3, 4, 5, 6, 7]
    """

    # Resultant flattened list to store the single-level elements
    flattened = []

    # Inner function to perform recursive flattening
    def flatten(item):
        """
        Recursively flattens the nested lists.
        
        Args:
            item (list or any type): The current item, which may be a list or an element.
        """
        # If item is a list, we iterate over each element and apply flatten
        if isinstance(item, list):
            for element in item:
                flatten(element)  # Recursively call flatten on each element
        else:
            # If the item is not a list, it's a base element we want to keep
            flattened.append(item)

    # Start the flattening process
    flatten(nested_list)

    # Return the fully flattened list
    return flattened

# Example usage
input_array = [1, [2, [3, [4, 5]], 6], 7]
output_array = flatten_array(input_array)
print("Flattened array:", output_array)

