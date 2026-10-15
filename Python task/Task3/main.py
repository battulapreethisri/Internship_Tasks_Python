from solutions import *
def main():
    print("Q1.Find the Frequency of Each Word in a Sentence:",frequency("python is easy and python is powerful"))
    print("Q2.Find the Frequency of Each Character in a Word:",frequent("banana"))
    print("Q3. Find the First Non-Repeating Character in a Word:", least("swiss"))
    print("Q4. Check Whether Two Strings Are Anagrams:", anagrams("listen","silent"))
    print("Q5. Find the First Repeating Character in a String:", frequent("programming"))
    print("Q6. Move All Zeros to the End of a List:", move_zero([0, 3, 0, 1, 2, 0, 4],0))
    print("Q7. Find the Second Highest Distinct Number in a List:", second_highest([10, 20, 40, 30, 40, 20]))
    print("Q8. Remove Duplicates Without Changing the Original Order:", duplicates( [4, 2, 4, 5, 2, 7, 5]))
    print("Q9. Find the Missing Number from 1 to N:", missing([1, 2, 4, 5, 6],6))
    print("Q10. Find Two Numbers Whose Sum Equals a Target:", sum_two([2, 7, 11, 15], 9))
    print("Q11. Find the Number Closest to Zero:", close_zero([-8, -3, 2, 5, -2]))
    print("Q12. Find Common Elements Between Two Lists:", common([1, 2, 3, 4, 5],[3, 4, 5, 6, 7]))
    print("Q13. Rotate a List to the Right by K Positions:", rotate_right( [1, 2, 3, 4, 5], 2))
    print("Q14. Find the Maximum Sum of Two Consecutive Elements:", max_sum_of_consecutive( [4, 7, 2, 9, 5]))
    print("Q15. Find All Pairs of Numbers Whose Sum Equals a Target:", all_pairs_sum([2, 4, 3, 5, 7, 8, 1], 9))

if __name__=="__main__":
    main()