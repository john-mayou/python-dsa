"""
An evil king has n bottles of wine, and a spy has just poisoned one of
them. Unfortunately, they do not know which one it is. The poison is very
deadly; just one drop diluted even a billion to one will still kill. Even so,
it takes a full month for the poison to take effect. Design a scheme for
determining exactly which one of the wine bottles was poisoned in just
one month's time while expending O(log(n)) taste testers.

We can encode each bottle with a binary representation where each bit space is
dedicated to a tester. Therefore after a month, we can a unique binary number
based on the specific people who died and did not die, locating the bottle.
"""