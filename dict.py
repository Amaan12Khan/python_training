# 1.WAP to create and print a dictionary which stores your information
dic={}
name=input("Enter your name:")
age=int(input("Enter your age:"))
gender=input("Enter your gender(m/M or f/F):")
dic["Name"]=name
dic["Age"]=age
dic["Gender"]=gender
print(dic)


# 2.WAP to access the items of a dictionary by referring to its key name
dic={"Name":"Alice","Age":25,"Gender":"F"}
print(dic["Name"])
print(dic["Age"])
print(dic["Gender"])

# 3.WAP to get a list of the values from a dictionary
dic={"Name":"Bob","Age":30,"Gender":"M"}
list_values=list(dic.values())
print(list_values)

# 4.WAP to change the value of a specific item by referring to its key name
dic={"Name":"Charlie","Age":28,"Gender":"M"}
print("Before changing:",dic)
dic["Age"]=40
print("After changing:",dic)

#5. WAP to print all key names in the dictionary,one by one
dic={"Name":"Diana","Age":22,"Gender":"F"}
for key in dic.keys():
    print(key)


#6.WAP to create a dictionary that contains three dictionaries.(nested)
family={
    "child1":{"Name":"Eve","Age":5},
    "child2":{"Name":"Frank","Age":8},
    "child3":{"Name":"Grace","Age":3}
}
print(family)


#7.WAP to to create three dictionaries,then create one dictionary that will contain the other three dictionarieschild1={"Name":"Hannah","Age":6}
child2={"Name":"Ian","Age":9}
child3={"Name":"Jack","Age":4}
family={"Child1":child1,"Child2":child2,"Child3":child3}
print(family)


#8.WAP to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value
list1=["Name","Age","Gender"]
list2=["Kate",27,"F"]
for i in range(0,len(list1)):
    dic={}
    dic[list1[i]]=list2[i]
    print(dic)


#9.WAP to merge two python dictionaries into one dictionary
dic1={"Name":"Liam","Age":35}
dic2={"Gender":"M","City":"New York"}
dic1.update(dic2)
print(dic1)


'''10.Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85}'''
sample_dict = {'C': 92,'Java': 66,'Python': 85}
min_key = min(sample_dict, key=sample_dict.get)
print("Key with the lowest value:", min_key)