"""
Al says he can prove that all sheep in a flock are the same color:
Base case: One sheep. It is clearly the same color as itself.
Induction step: A flock of n sheep. Take a sheep, a, out. The remaining
n-1 are all the same color by induction. Now put sheep a back in and
take out a different sheep, b. By induction, the n-1 sheep (now with a)
are all the same color. Therefore, all the sheep in the flock are the same
color. What is wrong with Al's “justification”?

This approach does not prove that the step from n to n+1 holds. There
is nothing linking one sheep to the rest of the pack.
"""