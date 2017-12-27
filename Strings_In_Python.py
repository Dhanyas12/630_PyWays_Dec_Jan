
    #012345678910111213141516171819202122 -- Left to Right
    #-22............-2,-1  -- Right to Left
str1='Welcome to Python Worl'

print("String Special operators i.e. Concatination + :",str1)
print(len(str1))

print("Left to Right Indexing",str1[0]) #slicing i.e. Slice- ginves the character from given index

print("Right to Left Indexing",str1[-22]) #slicing i.e. Slice- ginves the character from given index

print("Range Slicing",str1[0:7]) # End-1=7-1=6 till 6th index it will print

print("",str1[:7]) #End-1 i.e. 7-1=6 l ; Fronm 0th index to 6th index

str2='102030405060708090'
print("zero based indexing",str2[0::4])

print("updating string",str1[:8]+ "planet")

str3="Guido"
print("",str3 * 3)
print("", str1,"",str2, "" , str3)
