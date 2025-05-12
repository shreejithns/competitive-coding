class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        my_list = []
        permu = permutations(digits,3)

        three_digit_numbers = [100*a + 10*b + c for a, b, c in permu if a != 0]

        three_digit_numbers = set(three_digit_numbers)

        for i in three_digit_numbers:
            if i % 2 == 0:
                my_list.append(i)

        my_list.sort()

        return my_list
        