import string
lst = list(string.ascii_lowercase)

def countdown(N):
   for i in range(N):
       yield i


gen = countdown(len(string.ascii_lowercase))
for i in gen:
  print(lst[i])