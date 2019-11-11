#Its spooky october #
cats=['garfield','kitty','mittens','hobbes']
dogs=['spot','lassie','shenzie']
#lists are not commutative#
pets=[]
pets+=cats
pets+=dogs


#nested lists, lists INSIDE of lists oo
nested_pets=[cats,dogs]

#we have max and min, can take of lists, python has duck typing

#extend is for lists
pets3=[]
pets3.extend(cats)
pets3.extend(dogs)

#append is not for lists 
dogs.append('chester')


def filter_odd(lst):
    '''
return list with odd elements removed
'''
    result=[]
    for item in lst:
        if item %2 == 0:
            result.append(item)
    return result
