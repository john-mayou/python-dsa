# Very deep inheritance hierarchies are generally hard to understand because they have poor
# "locality of behavior". The idea is: to understand a simple method 5 classes down,
# you have to understand 5 different class across 5 different files with 100s of methods
# that might be overriden at any level. Also, good luck changing anything and having test isolation.
# TLDR: inheritence is the root of all evil.