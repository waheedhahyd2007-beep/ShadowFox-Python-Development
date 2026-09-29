import random

# Exercise 1: Dice rolling simulation

count_six = 0
count_one = 0
consecutive_sixes = 0
previous_roll = 0

for i in range(20):
    roll = random.randint(1, 6)
    print("Roll", i + 1, ":", roll)

    if roll == 6:
        count_six += 1

    if roll == 1:
        count_one += 1

    if roll == 6 and previous_roll == 6:
        consecutive_sixes += 1

    previous_roll = roll

print("\nTotal number of 6s:", count_six)
print("Total number of 1s:", count_one)
print("Consecutive pairs of 6s:", consecutive_sixes)

print("----------------------------------------")
# Exercise 2: Jumping jacks workout

total_jumping_jacks = 0

for i in range(10):
    print("\nSet", i + 1)
    print("Do 10 jumping jacks!")

    total_jumping_jacks += 10

    if total_jumping_jacks == 100:
        print("Congratulations! You completed the workout!")
        break

    tired = input("Are you tired? (yes/no): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()

        if skip == "yes" or skip == "y":
            print("You completed a total of",
                  total_jumping_jacks, "jumping jacks.")
            break
        else:
            print("You have",
                  100 - total_jumping_jacks,
                  "jumping jacks remaining.")
    else:
        print("You have",
              100 - total_jumping_jacks,
              "jumping jacks remaining.")
