#Write a function that takes a list value as an argument
#and returns a string with all the items separated by a comma
#and a space, with 'and' inserted before the last item.
#For example, if spam=['apples', 'bananas', 'tofu', 'cats']
#the function would return 'apples, bananas, tofu, and cats'.
#But your function should be able to work with any
#list value passed to it. Be sure to test the case where
#an empty list [] is passed to your function.

spam = []
typed = ()
print('Type all the elements you want in the list.\
      \nIf you are done, type "quit".')

while True :
    typed = input('Element to be in the list: ')
    if 'quit' == typed :
        break
    elif '' == typed :
        print('Sorry, you have to enter a value or "quit".')
        continue
    spam.append(typed)

# def l2s(listita) :
#     stringA = ''
#     if 1 < len(listita) :
#            for i in range(len(listita) - 2) :
#                stringA += listita[i] + ', '
#            stringA += listita[len(listita) - 2] + ' and '\
#                + listita[len(listita) - 1]
#     elif 1 == len(listita):
#         stringA = listita[0]
#     elif 0 == len(listita):
#         stringA = 'No value was entered.'
#     return stringA

# print('The resulting string is: ' + l2s(spam))

def l2s(listita) :
    stringA = ''
    largo = len(listita)
    if 1 < largo :
           for i in range(largo - 2) :
               stringA += listita[i] + ', '
           stringA += listita[largo - 2] + ' and '\
               + listita[largo - 1]
    elif 1 == largo:
        stringA = listita[0]
    elif 0 == largo:
        stringA = 'No value was entered.'
    return stringA

print('The resulting string is: ' + l2s(spam))