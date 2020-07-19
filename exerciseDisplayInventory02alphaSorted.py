# You are creating a fantasy video game. The data structure
# to model the player’s inventory will be a dictionary where
# the keys are string values describing the item in the inventory
# and the value is an integer value detailing how many of
# that item the player has. For example, the dictionary
# value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1,
#        'arrow': 12} means the player has 1 rope, 6 torches,
# 42 gold coins, and so on.
# Write a function named displayInventory() that would take
# any possible “inventory” and display it like a vertical list
# ordered alphabetically by item name,
# starting with the quantity and then the item´s name.
# It has a tittle (Inventory:) and ends with a total count
# (Total number of items: 62).


# Some inventories to test function.
treasure1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
treasure2 = {'rope': 1}
treasure3 = {'rope': 10, 'torch': 60, 'gold coin': 420, 'dagger': 10, 'arrow': 120}
treasure4 = {'rope': 0, 'torch': 0, 'gold coin': 1}

# Some inventories with incorrect datatype values.
treasure5 = {1: 0, 'torch': 0, 'gold coin': 1}
treasure6 = {'rope': 'a', 'torch': 0, 'gold coin': 1}

# An incorrect argument since it is not a dictionary:
treasure7 = ['sdf', 'sdf']
treasure8 = 10
treasure9 = ()



def displayInventoryAlpha(myThings):
    orderedItems = []
    tupleItem = ()
    totalItems = 0
    
    # End function if argument not a dictionary data type.  
    if type(myThings) != dict :
        print('The argument is not a dictionary.\nThis function works only on dictionary data types.\n')
        return
 
    for k, v in myThings.items() :
        # Find incorrect data type in keys or values and halt.
        if type(k) == str and type(v) == int:
            tupleItem = v, k
            orderedItems.append(tupleItem)
            totalItems += v
        else:
            print('Item´s name is not a string,\nor item´s value is not an integer.', end='\n\n')
            return
        
    # Order alphabetically the list derived from the dict.
    def custom_sort(t):
        return t[1]
    orderedItems.sort(key=custom_sort)
    
    # Print the inventory
    print('Inventory:')

    for i in range(0,len(orderedItems)) :
        print(orderedItems[i][0], orderedItems[i][1], end='\n')
    
    print('Total number of items:', totalItems, end='\n\n')
    
    
    
    
# Testing.
# print('******treasure1******'); displayInventoryAlpha(treasure1)
# print('******treasure2******'); displayInventoryAlpha(treasure2)
# print('******treasure3******'); displayInventoryAlpha(treasure3)
# print('******treasure4******'); displayInventoryAlpha(treasure4)
# print('******treasure5******'); displayInventoryAlpha(treasure5)
# print('******treasure6******'); displayInventoryAlpha(treasure6)
# print('******treasure7******'); displayInventoryAlpha(treasure7)
# print('******treasure8******'); displayInventoryAlpha(treasure8)
# print('******treasure9******'); displayInventoryAlpha(treasure9)
