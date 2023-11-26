number_of_pieces = int(input())
pianist_dict = {}
for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    if piece not in pianist_dict:
        pianist_dict[piece] = {"Composer": composer, "Key": key}
commands = input()

while commands != "Stop":
    current_command = commands.split("|")
    if current_command[0] == "Add":
        piece, composer, key = current_command[1], current_command[2], current_command[3]
        if piece in pianist_dict:
            print(f"{piece} is already in the collection!")
        else:
            pianist_dict[piece] = {"Composer": composer, "Key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif current_command[0] == "Remove":
        piece = current_command[1]
        if piece in pianist_dict:
            pianist_dict.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif current_command[0] == "ChangeKey":
        piece, new_key = current_command[1], current_command[2]
        if piece in pianist_dict:
            pianist_dict[piece]["Key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    commands = input()

for piece, info in pianist_dict.items():
    print(f"{piece} -> Composer: {info['Composer']}, Key: {info['Key']}")
