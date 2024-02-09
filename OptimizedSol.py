import bisect

# This function sorts two lists together based on the values in the first list
def sort_lists(radians, identifiers):
    # Combine the two lists into a list of tuples
    combined = list(zip(radians, identifiers))
    
    # Sort the combined list based on the first element of each tuple
    combined.sort()
    
    # Unzip the sorted, combined list back into two separate lists
    sorted_radians, sorted_identifiers = zip(*combined)
    
    # Return the sorted lists
    return list(sorted_radians), list(sorted_identifiers)

# This function converts identifiers of the form 's_i' or 'e_i' to integers i
def code_identifiers(identifiers):
    # Create a list to store the coded identifiers
    coded_identifiers = []
    
    # Iterate over the identifiers
    for identifier in identifiers:
        # Extract the number from the identifier and convert it to an integer
        number = int(identifier.split('_')[1])
        
        # Add the coded number to the list
        coded_identifiers.append(number)
    
    # Return the list of coded identifiers
    return coded_identifiers

# This function counts the number of intersections in a list of coded identifiers
def count_intersections(u):
    n = len(u) // 2
    intersections = 0
    seen = [False] * (n + 1)
    E = [0] * n
    S = []

    # Iterate over the list of coded identifiers
    for i in range(2 * n):
        j = u[i]
        if not seen[j]:
            # If this is the first occurrence of the identifier, open an interval for it
            seen[j] = True
            E[j - 1] = i
            bisect.insort(S, i)
        else:
            # If this is the second occurrence of the identifier, close the interval and count the intersections
            intersections += len(S) - bisect.bisect_right(S, E[j - 1])
            seen[j] = False
            S.remove(E[j - 1])

    # Return the total number of intersections
    return intersections

# Test the functions with your example
radians = [0.78, 1.47, 1.77, 3.92]
identifiers = ["s_1", "s_2", "e_1", "e_2"]

# Sort the radians and identifiers together
sorted_radians, sorted_identifiers = sort_lists(radians, identifiers)

# Convert the sorted identifiers to coded identifiers
coded_identifiers = code_identifiers(sorted_identifiers)

# Count the number of intersections in the coded identifiers
intersections = count_intersections(coded_identifiers)

# Print the results
print("Coded Identifiers: ", coded_identifiers)
print("Number of Intersections: ", intersections)
