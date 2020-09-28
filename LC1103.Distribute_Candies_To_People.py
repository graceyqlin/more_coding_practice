#LC1103.Distribute_Candies_To_People.py

#Topic: Math

# We distribute some number of candies, to a row of n = num_people people in the following way:

# We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

# Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

# This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

# Return an array (of length num_people and sum candies) that represents the final distribution of candies.

# Example 1:

# Input: candies = 7, num_people = 4
# Output: [1,2,3,1]
# Explanation:
# On the first turn, ans[0] += 1, and the array is [1,0,0,0].
# On the second turn, ans[1] += 2, and the array is [1,2,0,0].
# On the third turn, ans[2] += 3, and the array is [1,2,3,0].
# On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        temp = [0] * num_people
        cur_num = 1
        i = 0
        
        while candies > 0:
            temp[i%num_people] += min(cur_num, candies)
            candies -= cur_num
            cur_num += 1
            i += 1

        return temp

        #time complexity: O(square_root(candies)) (number_of_times * number_of_times+1)/2 = candies
        #space complexity:O(num_people)