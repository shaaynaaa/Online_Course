

#PRACTICE QUES 
#for mid 3 characters
food= input("whats your favourite food? ")
mid= len(food)//2
print(food[mid-1:mid+2])
#find length of input divide by 2 for center value median
#double // to remove any 0.5 and make it integer like 2 or -3 since indexing take only integers

#for last2 characters use negative indexing
print(food[-2:-1])

#PRACTICE
line= input('gimme a line ')
print(line.lower().replace(' ','_'))