import json

with open("person.json", "r") as file:
    person = json.load(file)

print(person)
print(person["name"])
#
# import json
#
# person = {
#     "name": "Sara",
#     "age": 24,
#     "city": "Pune"
# }
#
# with open("person.json", "w") as file:
#     json.dump(person, file, indent=4)
#
# print("Data saved successfully")

# import json
#
# person = {
#     "name": "Sara",
#     "age": 24,
#     "city": "Pune"
# }
#
# with open("person.json", "w") as file:
#     json.dump(person, file, indent=4)
#
# print("Data saved successfully")


# Code	Meaning
# os.getcwd()	Get the current folder path
# os.listdir()	List files and folders
# os.path.exists(path)	Check whether a path exists
# os.path.isfile(path)	Check whether a path is a file
# os.path.isdir(path)	Check whether a path is a folder
# os.makedirs(path, exist_ok=True)	Create a folder if needed