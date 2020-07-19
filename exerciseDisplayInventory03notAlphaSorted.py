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

print('\n')
def displayInventory(myThings, zeroListed = ''):
    '''
    Parameters
    ----------
    myThings : Dictionary data type with format items:qtty.
    zeroListed : Flag to avoid listing zero qtty items
                 Use 'n'.
    Returns
    -------
    None.
    '''
    
    totalItems = 0
    notAstring = ''
    
    # End function if argument not a dictionary data type.  
    if type(myThings) != dict :
        print('The argument is not a dictionary.\nThis function works only on dictionary data types.\n')
        return
    
    # Print inventory.
    print('Inventory:')
        
    for k, v in myThings.items() :  
        # Find incorrect data type in keys or values.  
        if type(k) == str and type(v) == int :
            # Check if zeroListed flag is present.
            if 'n' == str(zeroListed) and v > 0:
                print(myThings[k], k)
                totalItems += v
                notAstring = '\033[1;30;43m(Note: some items were not printed\nbecause quantity was not an integer > 0.)\033[0m'
            elif 'n' != str(zeroListed) :
                print(myThings[k], k)
                totalItems += v                
        else:
            notAstring = '\033[2;30;41m(Note: some items were not printed\nbecause names were not strings,\nor quantity was not an integer.)\033[0m'

    print('Total number of items:', totalItems)
    if notAstring != '' :
        print(notAstring)
    print('\n')
    
    
    
# CRED = '\033[2;30;41m'
# CEND = '\033[0m'

# Testing.
# help(displayInventory)
# print('******treasure1******'); displayInventory(treasure1)
# print('******treasure2******'); displayInventory(treasure2)
# print('******treasure3******'); displayInventory(treasure3)
# print('******treasure4 avoiding zero qtty. items.******'); displayInventory(treasure4, 'n')
# print('******treasure4 listing zero qtty. items.******'); displayInventory(treasure4)
# print('******treasure5******'); displayInventory(treasure5)
# print('******treasure6******'); displayInventory(treasure6)
# print('******treasure7******'); displayInventory(treasure7)
# print('******treasure8******'); displayInventory(treasure8)
# print('******treasure9******'); displayInventory(treasure9)
