class Solution:
    def pivotInteger(self, n: int) -> int:
        i=1
        j=n
        res=-1
        if i==j:   # It is just for example 2 i.e. n = 1 cause it does not enter in below while loop cause i and j are same i.e both are 1 so it doesn't enter the while loop and return -1 but we have to return 1 thats why we use this case.
            return i
        else:
            s1=0
            s2=0
            while(i<=j):
                if s1<=s2:
                    s1+=i
                    i+=1
                elif s2<=s1:
                    s2+=j
                    j-=1
                if j==i and s1==s2:
                    res=i
            return res