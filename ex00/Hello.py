# You need to modify the string of each data object to display the following greetings:
# "Hello World", "Hello «country of your campus»", "Hello «city of your campus»", "Hello
# «name of your campus»"
# ft_list = ["Hello", "tata!"]
# ft_tuple = ("Hello", "toto!")
# ft_set = {"Hello", "tutu!"}
# ft_dict = {"Hello" : "titi!"}
# #your code here
# print(ft_list)
# print(ft_tuple)
# print(ft_set)
# print(ft_dict)
# Expected output:
# $>python Hello.py | cat -e
# ['Hello'
# ,
# 'World!']$
# ('Hello'
# ,
# 'France!')$
# {'Hello'
# ,
# 'Paris!'}$
# {'Hello': '42Paris!'}$
# $>




ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

## Start my code
ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")
ft_set.remove("tutu!")
ft_set.add("Paris!")
ft_dict["Hello"] = "42Paris!"
## End My code

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)


