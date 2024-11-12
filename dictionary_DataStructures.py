""" -dictionary
	-type constraints for keys & values
	-add item
	-access key
	-update value
	-in
	-pop
	-iterate
	-keys
	-values
	-convert list of tuples to dictionary
	-convert list of lists to dictionary
	-update
	-collections(counter, defaultdict)"""
"""
 dictionary -> {}, mutable, unordered, unique
--> cannot use mutable data types as key in dictionary
--> keys can be any data types
--> duplicates are not allowed
"""
details = {}
details["name"] = "suresh"
details[1001] = "id" 
details[("city",)] = "nyk"
details[frozenset({"city", "state"})] = ["USA", "nyk"]
# print(details[1001])
# for key in details:
#     print(f"{key} -> {details[key]}") 

# print()

# for key, value in details.items():
#     print(f"{key} -> {value}")

details.pop("name")
print(details)
"""-------"""
data = {"name":"hari"}
data.update({"age":"hari"})
print(data)
"""-----"""
temp1 = [("name1", "nick"), ("course1", "python")] # list of tuples
temp2 = [["course2", "python"]] # list of tuples
temp3 = [{"name3", "nick"}, {"course3", "python"}] # working, but not suggestable
print(dict(temp1))
print(dict(temp2))
print(dict(temp3))

