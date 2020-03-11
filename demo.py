namelist= ['David','Mike','John']
print(namelist[0]+', '+namelist[1]+', '+namelist[2]+' are invited.')
print(namelist[0]+' cannot attend our ceremony.')
namelist[0]='Chen'
print("We've gotten a larger table. Let's have more people invited!")
namelist.append('Jenny')
namelist.insert(0,'Mary')
namelist.insert(2,'Dick')
print(namelist)
print('Sad to know that our new table cannot be delivered in time.')
people_del=namelist.pop()
print(people_del+', sorry to inform you that you cannot attend our ceremony.')
people_del=namelist.pop()
print(people_del+', sorry to inform you that you cannot attend our ceremony.')
people_del=namelist.pop()
print(people_del+', sorry to inform you that you cannot attend our ceremony.')
people_del=namelist.pop()
print(people_del+', sorry to inform you that you cannot attend our ceremony.')
print(namelist[0]+' and '+namelist[1]+", glad to invite.")
del namelist[0]
del namelist[0]
print(namelist)

