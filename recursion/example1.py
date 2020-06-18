# Created by Dmitriy Shin on June 18, 2020

# Look for a key in a pile of boxes
# Using loops
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("Found the key!")


# Using recursion
def look_for_key_recursive(main_box):
    for item in box:
        if item.is_a_box():
            look_for_key_recursive(ote,)
        elif item.is_a_key():
            print("Found the key!")
            return
