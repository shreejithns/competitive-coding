class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        two_baskets = [-1, -1]
        two_b_fre = [0, 0]
        ans = 0

        j = 0

        for i in range(len(fruits)):
            if two_baskets[0] == -1:
                two_baskets[0] = fruits[i]
                two_b_fre[0] += 1
            elif two_baskets[0] == fruits[i]:
                two_b_fre[0] += 1
            elif two_baskets[1] == -1:
                two_baskets[1] = fruits[i]
                two_b_fre[1] += 1
            elif two_baskets[1] == fruits[i]:
                two_b_fre[1] += 1
            else:
                ans = max(ans, sum(two_b_fre))
                while j < i and (two_b_fre[0] != 0 and two_b_fre[1] != 0):
                    if fruits[j] == two_baskets[0]:
                        two_b_fre[0] -= 1
                        if two_b_fre[0] == 0:
                            two_baskets[0] = -1
                    elif fruits[j] == two_baskets[1]:
                        two_b_fre[1] -= 1
                        if two_b_fre[1] == 0:
                            two_baskets[1] = -1
                    j+=1
                if two_baskets[0] == -1:
                    two_baskets[0] = fruits[i]
                    two_b_fre[0] = 1
                else:
                    two_baskets[1] = fruits[i]
                    two_b_fre[1] = 1

        ans = max(ans, sum(two_b_fre))

        return ans 

        