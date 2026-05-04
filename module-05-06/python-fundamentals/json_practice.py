import json

person = {
    "name": "Wasir",
    "age": 23,
    "skills": ["Python", "Django", "React"],
    "active": True
}

p1 = json.dumps(person, indent=2)
print(p1)
p2 = json.loads(p1)
print(p2["name"])

with open("person.json", "w") as f:
    json.dump(person, f, indent=2)

with open("person.json", "r") as f:
    data = json.load(f)
    print(data["skills"])
