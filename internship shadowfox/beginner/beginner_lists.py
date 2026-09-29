# Task 3: Lists - Justice League

justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

# 1. Count the number of members
print("1. Number of members:", len(justice_league))
print("Justice League:", justice_league)
print("--------------------------------------------------")

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")

print("2. After adding new members:")
print(justice_league)
print("--------------------------------------------------")

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("3. Wonder Woman is now the leader:")
print(justice_league)
print("--------------------------------------------------")

# 4. Separate Aquaman and Flash
# Move Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")

print("4. After separating Aquaman and Flash:")
print(justice_league)
print("--------------------------------------------------")

# 5. Replace the list with new members
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]

print("5. New Justice League:")
print(justice_league)
print("--------------------------------------------------")

# 6. Sort the list alphabetically
justice_league.sort()

print("6. Justice League in alphabetical order:")
print(justice_league)

# The hero at index 0 becomes the new leader
new_leader = justice_league[0]
print("New leader:", new_leader)
