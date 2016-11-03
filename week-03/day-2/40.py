students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]
# create a function that takes a list of students,
# then returns how many candies are own by students
# under 10

def candycrush(val):
    candies = 0
    slist = []
    
    for i in val:
        slist += [i['name']]
        if i['age'] < 10:
            candies += i['candies']
            
    print("Students names are:", slist)
    # print("Candies owned by age 10< :",candies)

    return candies
    
print(candycrush(students))