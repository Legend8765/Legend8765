import random
lower = "abcdefijklmnopqrstuvwxyz"
upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "0123456789"
Symbol = "[]{}#()*;._-"

all=lower + upper + NUMBER + Symbol
length = 9
password = "".join(random.sample(all,length))  # type: ignore
print(" The Password You Generated is :",password)
