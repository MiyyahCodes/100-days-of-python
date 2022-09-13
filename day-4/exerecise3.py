row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

first_num = int(position[0])
second_num = int(position[1])

map[second_num - 1][first_num - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
