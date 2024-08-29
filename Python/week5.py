# def any_lowercase1(s):
#      for c in s:
#           if c.islower():
#                return True
#           else:
#                return False
# print(any_lowercase1("banana"))
# print(any_lowercase1("Banana"))
# print(any_lowercase1("baNana"))

# 2

# def any_lowercase2(s):
#      for c in s:
#           if 'c'.islower():
#                return 'True'
#           else:
#                return 'False'
# print(any_lowercase2("BANANA"))
# print(any_lowercase2("banana"))


# def any_lowercase3(s):
#      for c in s:
#           flag = c.islower()
#      return flag
# print(any_lowercase3("banana"))
# print(any_lowercase3("bananA"))

# def any_lowercase4(s):
#      flag = False
#      for c in s:
#           flag = flag or c.islower()
#      return flag
# print(any_lowercase4("banana"))
# print(any_lowercase4("bANANa"))
# print(any_lowercase4("BANANA"))



def any_lowercase5(s):
     for c in s:
          if not c.islower(): # if this detect an upper case,
               return False # this will return Flase
     return True
print(any_lowercase5("banana"))
print(any_lowercase5("banaNa"))