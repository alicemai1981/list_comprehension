inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for group in inventory:
    inv_string = (group,)
    print("the store has {1} {0}, each for{2}USD".format(*inv_string))

