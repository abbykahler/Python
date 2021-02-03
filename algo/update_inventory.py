
# Given a list of dictionaries to represent new inventory,
# and a list of dictionaries to represent current inventory,
# update the quantities of the current inventory

# if the item doesn't exist in current inventory, add it to the inventory
# return the current inventory after updating it.

# new_inv = [
#   { "name": "Grain of Rice", "quantity": 9000 },
#   { "name": "Peanut Butter", "quantity": 50 },
#   { "name": " Royal Jelly", "quantity": 20 },
# ]
# curr_inv = [
#   { "name": "Peanut Butter", "quantity": 20 },
#   { "name": "Grain of Rice", "quantity": 1 },
# ]

# expected = [
#   { "name": "Peanut Butter", "quantity": 70 },
#   { "name": "Grain of Rice", "quantity": 9001 },
#   { "name": "Royal Jelly", "quantity": 20 },
# ]

def update_inventory(new_inv, curr_inv):
    for i in range(len(new_inv)):
        exists = False
        for j in range(len(curr_inv)):
            if new_inv[i]['name'] == curr_inv[j]['name']:
                curr_inv[j]['quantity'] += new_inv[i]['quantity']
                exists = True
                break
        if exists == False:
            curr_inv.append(new_inv[i])
    return curr_inv

bag1 = [
    { "name": "Grain of Rice", "quantity": 9000 },
    { "name": "Peanut Butter", "quantity": 50 },
    { "name": " Royal Jelly", "quantity": 20 },
]
bag2 = [
    { "name": "Peanut Butter", "quantity": 20 },
    { "name": "Grain of Rice", "quantity": 1 },
]

print(update_inventory(bag1,bag2))