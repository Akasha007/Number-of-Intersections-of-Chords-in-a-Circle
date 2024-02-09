def count_intersections(radians, identifiers):
    # Create a dictionary that maps identifiers to radians
    rad_dict = dict(zip(identifiers, radians))

    # Pair up the starting and ending radians using the identifiers and sort by starting radians
    chords = sorted([[rad_dict['s_' + str(i)], rad_dict['e_' + str(i)]] for i in range(1, len(radians) // 2 + 1)])
    print(chords)

    intersection_count = 0

    # Iterate over each pair of chords to check for intersections
    for i in range(len(chords)):
        for j in range(i + 1, len(chords)):
            # Sort the start and end radians of each chord
            chord1 = sorted(chords[i])
            chord2 = sorted(chords[j])

            # Check for intersection conditions
            if chord1[0] < chord2[0] < chord1[1] < chord2[1] or chord2[0] < chord1[0] < chord2[1] < chord1[1]:
                intersection_count += 1

    return intersection_count

print(count_intersections([0.9, 1.3, 1.70, 2.92],["s_1", "e_1", "s_2", "e_2"])) #Output 0
print(count_intersections([0.78, 1.47, 1.77, 3.92],["s_1", "s_2", "e_1", "e_2"])) #Output 2
