# Lists are mutable sequences
# https://docs.python.org/3/library/stdtypes.html#lists

# 1 print list, len, access
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses)
# print(len(courses))
# print(courses[0])
# print(courses[1])
# print(courses[-2])
# print(courses[-1])

# 2 slicing:
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses[:2])
# print(courses[2:])
# print(courses[1:3])

# 3 list append, insert
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses_2 = ["Dance","Poetry"]
# print(courses)
# courses.append(courses_2)
# print(courses)

# courses.insert(2,"Music")
# print(courses)


# 4 list remove , pop
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses)
# courses.remove("History")
# print(courses)
#
# pop_value = courses.pop()
# print(courses)
# print(pop_value)
# pop_value = courses.pop(0)
# print(pop_value)
# print(courses)

# 5 list reverse, sort
# courses = ['History', 'Math', 'Physics', 'CompSci']
# nums = [1,5,2,8,4,6]
# print(courses)
# courses.reverse()
# print(courses)

# courses.sort()
# print(courses)
# courses.sort(reverse=True)
# print(courses)

# print(sorted(nums))
# print(nums)


# list min, max, sum
# nums = [1,5,2,8,4,6]
# print(max(nums))
# print(min(nums))
# print(sum(nums))


# 6 list index
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses.index("CompSci"))

# in operator
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print('Math' in courses)
# print('Art' in courses)
#
# for item in courses:
#     print(item)

# for index, course in enumerate(courses, start=1):
#     print(index, course)

# 7 join, split
# courses = ['History', 'Math', 'Physics', 'CompSci']
# course_str = ', '.join(courses)
# print(course_str)
#
# new_list = course_str.split(', ')
# print(new_list)

### Tuples immutable sequence types ###############
# Mutable
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1
#
# print(list_1)
# print(list_2)
#
# list_1[0] = 'Art'
#
# print(list_1)
# print(list_2)


# Immutable can't append remove etc but rest same as list
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
#
# print(tuple_1)
# print(tuple_2)
#
# tuple_1[0] = 'Art'
#
# print(tuple_1)
# print(tuple_2)

### Sets unordered and have no duplicates sequences ###############
# Sets optimazed for in
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# print(cs_courses)
# print('Math' in cs_courses) # optimazed for sets !

# art_courses = {'History', 'Math', 'Art', 'Design'}
# print(cs_courses.intersection(art_courses)) # both in sets
# print(cs_courses.difference(art_courses)) # differnets between two
# print(cs_courses.union(art_courses)) # union of both

# empty initialitation
# Empty Lists
# empty_list = []
# empty_list = list()
#
# # Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()
#
# # Empty Sets
# empty_set = {} # This isn't right! It's a dict
# empty_set = set()

