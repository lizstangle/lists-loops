songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0,2])
print(songs[1:3])
songs[2] = "Killing Me Softly With His Song"
songs.extend(["Fallin'", "By Your Side", "Whatever You Like"])
del songs[0]

animals = ["cat", "dog", 'bird']
animals.append("monkey")
print(animal[2])
del animals[0]
for animal in animals:
    print(animal)