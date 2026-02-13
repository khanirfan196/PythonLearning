
names = ["michael", "christ", "daniel", "sarah", "bob"]

emails = ["michael@email.com", "christ@email.com", "daniel@email.com", "sarah@email.com", "bob@email.com"]

zipped = zip(names, emails)

print(zipped) # is not iterable and is a class

print(dict(zipped)) # converting that object to dictionary

data_list = []

for name, email in zip(names, emails):
    data_list.append((name, email))

print(data_list)
