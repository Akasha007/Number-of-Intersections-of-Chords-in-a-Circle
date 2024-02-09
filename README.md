
# Number-of-Intersections-of-Chords-in-a-Circle

This repository contains the code to find the number of intersections of chords in $$O(n \log n)$$ time where $$n$$ is the number of Chords.

## Task

Given a list of chords in a circle, count the number of intersections, if any. For simplicity's sake, assume all starting and ending points are unique.

## Inputs

Two parallel lists: The first contains the radian measure of the start or end. The second contains the identifiers of the chords. The identifiers are denoted 's_x' and 'e_x', where 's' is the starting point of the chord, 'e' is the ending point of the chord, and s_x < e_x. The radian measures are sorted in ascending order (May not be sorted as well).

## Brute Force Approach

For two lines to intersect with each other, the starting or ending point of one line must be between the starting and ending points of the other line. Using this logic, we can check this condition for each of the chords with the rest of the chords and count the number of intersections. The code for that implementation is below:

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

Although this gives us the right output, this takes $$O(n^2)$$ time. This is not an efficient approach. 

# Optimized Approach

Let us go over the optimized approach which runs in **O(nlogn)** time. 

To start with, I found it easier to name the starting and the ending points to a single number, that is "s_1" and "e_1" will be named 1 and 1. This gives us a list of length 2n with every number being twice in it. In this case, coded_identifiers will contain 2n identifiers. 

The idea is to scan this list with 2n identifiers once and follow this approach. When we encounter an identifier (let’s call it i) for the first time, we consider it as the start of an interval. This interval remains open until we encounter i again. When i is seen the second time, we close its interval and count how many other intervals were opened but not yet closed after i’s interval was first opened. Each of these counts represents an intersection between the chord represented by i and another chord.

For example, consider the sequence 1 2 1 2:

- We first see 1, so we open an interval for 1.
- Next, we see 2 and open an interval for 2.
- We see 1 again, so we close the interval for 1. Since 2’s interval was opened after 1’s and is still open, we count one intersection.
- Finally, we see 2 again and close its interval. There are no other open intervals at this point, so we don’t count any additional intersections. So, for the sequence 1 2 1 2, there is one intersection.

## Final Algorithm:

- **sort_lists function:**

   Combine the `radians` and `identifiers` lists into a list of tuples.
   
   Sort the combined list based on the radian values.
   
   Separate the sorted, combined list back into two lists: `sorted_radians` and `sorted_identifiers`.

- **code_identifiers function:**

   Initialize an empty list `coded_identifiers`.
   
   For each identifier in the identifiers list:

   - Split the identifier on the underscore character (‘_’) and take the second part (which is a string representation of a number).
   
   - Convert this number to an integer and append it to coded_identifiers.

- **count_intersections function:**

   Initialize intersections to 0, seen to a list of False values, `E` to a list of zeros, and `S` to an empty list.
   
   For each index i in the range from 0 to 2n:

   - Let j be the i-th element of u.
   
   - If j has not been seen before:

      Mark j as seen.
      
      Store i in E[j - 1].
      
      Insert i into S in a way that S remains sorted.

   - Otherwise:

      Increase intersections by the number of elements in S that are greater than E[j - 1].
      
      Mark j as not seen.
      
      Remove E[j - 1] from S.

- **Main part of the code:**

  -  Define the `radians` and `identifiers` lists.

  -  Call `sort_lists` with `radians` and `identifiers` as arguments and unpack its return value into `sorted_radians` and `sorted_identifiers`.

  -  Call `code_identifiers` with `sorted_identifiers` as an argument and assign its return value to `coded_identifiers`.

  -  Call `count_intersections` with `coded_identifiers` as an argument and assign its return value to intersections.

  -  Print `coded_identifiers` and `intersections`.

## Code Analysis

The code consists of three main functions: `sort_lists`, `code_identifiers`, and `count_intersections`.

1. **sort_lists function**: This function takes two lists as input: `radians` and `identifiers`. It combines these two lists into a list of tuples, sorts this list (based on the radian values), and then separates it back into two lists. The time complexity of this function is dominated by the sort operation, which is $$O(n \log n)$$, where $$n$$ is the length of the input lists.

2. **code_identifiers function**: This function takes a list of identifiers as input. It iterates over this list, extracts a number from each identifier, and appends it to a new list. Since it processes each identifier once, its time complexity is $$O(n)$$.

3. **count_intersections function**: This function takes a list of coded identifiers as input and counts the number of intersections. It does this by maintaining a sorted list `S` of open intervals. For each identifier, it either opens a new interval (when the identifier is seen for the first time) or closes an existing interval (when the identifier is seen for the second time) and counts the number of intersections. The key operations in this function are inserting an element into `S` and finding the insertion point for an element in `S`, both of which are performed using binary search and take $$O(\log n)$$ time. Therefore, the time complexity of this function is $$O(n \log n)$$.

So, considering all these functions, the overall time complexity of the code is $$O(n \log n)$$, which is dominated by the `sort_lists` and `count_intersections` functions. This makes the code efficient for large inputs.
