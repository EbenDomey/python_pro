# question 1
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
new_dict = dict()
for key in keys:
    for value in values:
        if keys.index(key) == values.index(value):
            new_dict[key] = value
print(new_dict)

# question2

dict1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
dict2 = {"Thirty": 30, "Fourty": 40, "Fifty": 50}
dict3 = dict()

for key1 in dict1:
    dict3[key1] = dict1[key1]
    for key2 in dict2:
        dict3[key2] = dict2[key2]
print(dict3)

# question3

sampleDict = {
    "class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}
}

print(sampleDict["class"]["student"]["marks"]["history"])


# question4

employees = ["Kelly", "Emma"]
defaults = {"designation": "Developer", "salary": 8000}
composite = dict()

for employee in employees:
    for default_keys in defaults:
        composite[employee] = defaults
print(composite)

# question5
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
extracted_dict = dict()

# question6 same preamble as question5

for description in sample_dict:
    for key in keys:
        if description == key:
            extracted_dict[key] = sample_dict[description]
print(extracted_dict)

# Keys to remove
keys = ["name", "salary"]
remnant_dict = dict()
for description in sample_dict:
    if description not in keys:
        remnant_dict[description] = sample_dict[description]
print(remnant_dict)

# question7

sample_dict2 = {"a": 100, "b": 200, "c": 300}
result = 0
for key in sample_dict2:
    if sample_dict2[key] == 200:
        result = sample_dict2[key]
print(f"{result} is found")

# question8

rep_dict = dict()
rep_value = ""
new_description = "location"
for content in sample_dict:
    if content == "city":
        rep_value = sample_dict[content]
        rep_dict[new_description] = rep_value
    rep_dict[content] = sample_dict[content]
rep_dict.pop("city")
print(rep_dict)

# question9

sample_dict2 = {"Physics": 82, "Math": 65, "history": 75}
sample_list2 = list(sample_dict2.values())
minimum = min(sample_list2)

for key in sample_dict2:
    if sample_dict2[key] == minimum:
        print(key)

# question10

sample_dict3 = {
    "emp1": {"name": "John", "salary": 7500},
    "emp2": {"name": "Emma", "salary": 8000},
    "emp3": {"name": "Brad", "salary": 500},
}
sample_dict3["emp3"]["salary"] = 8500

print(sample_dict3)
