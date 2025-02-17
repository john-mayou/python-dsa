# formula for number of elements in the range:
#   max(0, (stop − start + step − 1) // step)
#
# 1. The number of elements can never be less than 0, to we clamp to 0
# 2. The number of elements can never be a floating point value, thus integer division `//`
# 3.
#   start = 0
#   stop  = 10
#   step  = 3
# 
# By just calculating (stop - start) // step = (10 - 0) // 3 = 10 // 3 = 3 although its
# actually 4 elements: 0, 3, 6, 9. `//` rounds down, but we actually want to round up, since
# we want to include all numbers that are landed on. We can think of this like going from 0 to 3
# but with a step of 2. What we want is [0, 2] or 2 elements, but (3 - 0) // 2 = 3 // 2 = 1. We
# can round up by adding step - 1 to the numerator: (3 + 2 - 1) // 2 = 4 // 2 = 2.
#
# Examples:
#   start = 0
#   stop  = 10
#   steps:
#     (1) = (10 - 0 + 1 - 1) // 1
#         = 10 // 1
#         = 10
#     (2) = (10 - 0 + 2 - 1) // 2
#         = 11 // 2
#         = 5
#     (3) = (10 - 0 + 3 - 1) // 3
#         = 12 // 3
#         = 4
#     (4) = (10 - 0 + 4 - 1) // 4
#         = 13 // 4
#         = 3
#     (5) = (10 - 0 + 5 - 1) // 5
#         = 14 // 5
#         = 2