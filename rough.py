lst = [1,2,3]
my_str = "learning mlops"
my_int = 155

#print(type(my_str))

# lst.clear()
#print(lst)

#my_str = my_str.capitalize()
#print(my_str)

#lst.capitalize()
#print(lst)

from oopsproj import chatbook

#user1 = chatbook()


lst = [1,2,3]

#Function vs method

# calling a function
#a1 = len(lst) # we can call a function directly.
#print(a1)

# calling a method
#user1 = chatbook()
#user1.sendmsg() # for calling a method, we need to pick the object and then call the method.

# Encapsulation
# print(user1._chatbook__name)

# Getter and Setter
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())

user1 = chatbook()
print(user1.id)

chatbook.set_id(10) # Static method can be called from the class itself.
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)