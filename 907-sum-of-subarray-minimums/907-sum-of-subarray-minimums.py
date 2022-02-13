class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        """
        Returns the sum of the minimums over all of the contiguous subarrays of the
        list A.
        """
        # The -inf at the beginning makes sure that the stack is never empty. The
        # -inf at the end makes sure that every element in the original A gets
        # popped from the stack eventually.
        A = [float('-inf')] + A + [float('-inf')]
        stack = [0]
        result = 0

        for i in range(1, len(A)):
            while A[stack[-1]] > A[i]:
                # The index i is the first, greater than j whose value is less than
                # the value at j. If there were some smaller i, it would have caused
                # j to be popped before.
                j = stack.pop()

                # The index k is the largest, less than j whose value is less than
                # the value at j.
                k = stack[-1]

                # A[j] will be the minimum of (i - j) * (j - k) different contiguous
                # subarrays.
                result += A[j] * (i - j) * (j - k)
                result %= 10 ** 9 + 7

            stack.append(i)

        return result