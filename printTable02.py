# Write a function named printTable() that takes a list
# of lists of strings and displays it in a well-organized
# table with each column right-justified. Assume that all
# the inner lists will contain the same number of strings.
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#               ['Alice', 'Bob', 'Carol', 'David'],
#               ['dogs', 'cats', 'moose', 'goose']]
#
# Your printTable() function would print the following:
#
#     apples Alice  dogs
#    oranges   Bob  cats
#   cherries Carol moose
#     banana David goose
 
def printTable(tableData) :
    
    # Validate data given.
    if type(tableData) != list :
        print('Argument for printTable() must be a list.')
        return
    
    for sublist in range(len(tableData)) :
        if type(tableData[sublist]) != list :
            print('Each element in the list must also be a list.')
            return
    
    colWidths = [0] * len(tableData)  
    
    # Measure longest str in each column.
    for sublist in range(len(tableData)) :  
        for element in range(len(tableData[sublist])) :
            if len(tableData[sublist][element]) > colWidths[sublist] :
                colWidths[sublist] = len(tableData[sublist][element])

    # Print well organized table.
    for element in range(len(tableData[0])) :
        for sublist in range(len(tableData)) :
            print(str(tableData[sublist][element]).rjust(colWidths[sublist]), end=' ')
        print()
    print()   
        
# Test
Data1 = [['apples', 'oranges', 'cherries', 'banana'],
         ['Alice', 'Bob', 'Carol', 'David'],
         ['dogs', 'cats', 'moose', 'goose']]

Data2 = [['123', '1234', '12345'],
         ['1', '22', '333'],
         ['11', '222', '3333']]

                  
printTable(Data1)
printTable(Data2)