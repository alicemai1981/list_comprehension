inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
inv_string =()
for group in inventory:
    # create a list contains elements from string
    inv_string =group.split(",")
    # unpack list to a number of strings, pass strings into format function
    print("the store has {1} {0}, each for{2}USD".format(*inv_string))


