import os

path = 'E:\Python_Code\list'
path_lists = os.listdir(path)
print(path_lists)

for list_name in path_lists:
 
     with open(path + '\\' + list_name, 'r+', encoding='utf-8') as file_object,open(list_name, 'w', encoding='utf-8',errors = 'ignore') as f2:
        contents = file_object.readlines()
        print(contents)
        for i in range(0,len(contents)) :
            if len(contents[i]) >= 8 :
                if contents[i][7] == 'H' :
                     contents[i]= contents[i][:7] + 'I' + contents[i][8:]
                     #print(contents[i]+'success!')
            f2.write(contents[i])
#os.rename(list_name,list_name)
        
    #else with open(path + '\\' + list_name, 'r+', encoding='utf-8') as file_object:
    #    contents = file_object.readlines()
     #   print(len(contents))
