# For an integer N find the number of trailing zeroes in N!.

# Solution: the trailing is created due to combination of 5*2, which we can find by dividing the number by 5 and 2 and taking the
# integer value of it.Then take the min of quotient from both divisions as answer

# we can avoid counting 2 and # of 5's are always lesser then 2's
# we need to use floor function instead of int() as we want to get the actual number of divisors of 5

# Numbers like 25, 125, etc have more than one 5. For example, if we consider 28! we get one extra 5 and the number of 0s becomes 6.
# Handling this is simple, first, divide n by 5 and remove all single 5s, then divide by 25 to remove extra 5s, and so on.


n = 25
count = 0
while(n >= 5):
    n = n//5
    count += n


print("number of zeros are", count)