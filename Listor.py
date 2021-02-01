import random
NameMale = [
    "James",
    "John",
    "Robert",
    "Michael",
    "William",
    "David",
    "Richard",
    "Joseph",
    "Thomas",
    "Charles"
]
NameFemale = [
    "Mary",
    "Patricia",
    "Jennifer",
    "Linda",
    "Elizabeth",
    "Barbara",
    "Susan",
    "Jessica",
    "Sarah",
    "Karen"
]

while True:
    begin = input("Press ENTER to generate a random male and female name and a love precentage: ")
    for i in range(0, 1):
        RandomMale = random.randint(0, len(NameMale)-1)
        RandomFemale = random.randint(0, len(NameFemale)-1)
        Love = random.randint(0, 100)
        print(f"\n\t{NameMale[RandomMale]} and {NameFemale[RandomFemale]} are {Love}% in love ❤")