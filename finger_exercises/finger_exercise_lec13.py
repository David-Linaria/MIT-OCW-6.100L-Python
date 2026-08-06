# def sum_str_lengths(L):
#     """
#     L is a non-empty list containing either:
#     * string elements or
#     * a non-empty sublist of string elements
#     Returns the sum of the length of all strings in L and
#     lengths of strings in the sublists of L. If L contains an
#     element that is not a string or a list, or L's sublists
#     contain an element that is not a string, raise a ValueError.
#     """
#     # Your code here
#     assert len(L) > 0, 'Empty List Input.'
#
#     total_length = 0
#     for ele in L:
#         if not(type(ele) == list or type(ele) == str):
#             raise ValueError('Elements in List Error.')
#         elif type(ele) == list:
#             for ele2 in ele:
#                 if type(ele2) != str:
#                     raise ValueError('Elements in List Error.')
#                 else:
#                     total_length += len(ele2)
#         else:
#             total_length += len(ele)
#     return total_length
#
# # print(type([1,2]) == list)
# # print(type('abc'))
# # print(type(type(1)))
#
# # Examples:
# print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
# print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
# print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError



def sum_str_lengths(L):
    """
    L is a non-empty list containing either:
    * string elements or
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and
    lengths of strings in the sublists of L. If L contains an
    element that is not a string or a list, or L's sublists
    contain an element that is not a string, raise a ValueError.
    """
    # Your code here
    assert len(L) > 0, 'Empty List Input.'

    total_length = 0
    for ele in L:
        if not(type(ele) == list or type(ele) == str):
            raise ValueError('Elements in List Error.')
        elif type(ele) == list:
            for ele2 in ele:
                try:
                    total_length += len(ele2)
                except:
                    raise ValueError('Elements in List Error.')
        else:
            total_length += len(ele)
    return total_length

# print(type([1,2]) == list)
# print(type('abc'))
# print(type(type(1)))

# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError