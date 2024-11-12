"""data structures
  -list
	-index
	-slicing
	-in, not in
	-len
	-count
	-modify
	-append
	-extend
	-insert
	-pop
	-remove
	-concatenate
	-multiply list with scalar
	-max
	-min
	-sum
	-reverse
	-list conversion
	-unpacking
	-enumerate
	-sort(asc, dec)
	-sorted
	-list comparision
	-copy
	-nested lists
"""
# list [], ordered, mutable
names = []
print(f"After initializing names: {names}\n")

names.append("akash")
print(f"After appending 'akash': {names}\n")

names.append("sri vidhya")
print(f"After appending 'sri vidhya': {names}\n")

names.insert(1, "gayatri")
print(f"After inserting 'gayatri' at index 1: {names}\n")

deleted_name = names.pop()  # you can store popped element
print(f"After popping last element '{deleted_name}': {names}\n")

names.append(deleted_name)
print(f"After appending popped element '{deleted_name}': {names}\n")

names.remove("akash")
print(f"After removing 'akash': {names}\n")


names.insert(2, "mouneesh")
print(f"After inserting 'mouneesh' at index 2: {names}\n")

print(f"Last two elements: {names[-2:]}\n")

print(f"'sudhir' in names: {'sudhir' in names}\n")

names[2] = names[2].upper()
print(f"After converting index 2 to uppercase: {names}\n")

names.extend(["sudhir"])
print(f"After extending with ['sudhir']: {names}\n")

names.append(['srinu', 'anil', 'sudhir'])
print(f"After appending ['srinu', 'anil', 'sudhir']: {names}\n")

req = names[-1]
names.pop()
print(f"After popping the last list: {names}\n")

names = names + req 
print(f"After concatenating names & req: {names}\n")

print(f"List created with [0, 1]*5: {[0, 1]*5}\n")

names.sort(reverse=True)
print(f"Descending Order: {names}\n")

names.sort()
print(f"Ascending Order: {names}\n")

print(f"Sum of [1, 2, 3, 4]: {sum([1, 2, 3, 4])}\n")

name = ("CodeWala",)
print(f"List created from tuple: {list(name)}\n")

bio = ["1001", "steeve", "brooklyn"]
_id, *rest = bio
print(f"Remaining elements after unpacking bio: {rest}")
"""---"""
name = "hello"
for letter in range(len(name)):
    print(name[letter])
print(f"Each letter in 'hello' is printed one by one.\n")

for idx, letter in enumerate(name):
    print(idx, letter)
print(f"Each letter in 'hello' is printed with its index.\n")

nums = [2, 1, 4, 3, 5]
nums.sort(reverse=True)
print(f"List sorted in reverse order without storing : {nums}")

nums = sorted(nums)
print(f"List sorted in ascending order with storing: {nums}\n")

arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
print(f"[{arr1} == {arr2}] -> {arr1 == arr2}")  # --> True
print(f"[{arr1} is {arr2}] -> {arr1 is arr2}")  # --> False (because it will compare id's)

nums1 = [1, 2, 3, 4]
nums2 = nums1 #it is not copying the list, just referencing
nums2.append(5)
print(f"nums1 after appending 5 through nums2: {nums1}")

nums3 = nums1.copy() #it is copying the list
nums3.append(6)
print(f"nums1 after appending 6 to a copy: {nums1}")

arr = [[1, "steeve", 40000], [2, "tony", 30000, [3, "pepper", 10000]]]
print(f"The salary of {arr[1][3][1]} is {arr[1][3][2]}.")