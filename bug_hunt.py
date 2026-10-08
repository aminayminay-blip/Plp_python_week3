count = 1
total = 0

while count < 5:
    total = total + count
    count = count + 1

print("Sum of 1 to 5 is: " + str(total))

count = 1
total = 0

# BUG: Added a colon because a while statement must end with a colon.
# BUG: Changed < to <= so the loop includes 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Used an f-string because total is an integer.
print(f"Sum of 1 to 5 is: {total}")
