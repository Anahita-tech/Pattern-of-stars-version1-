a=0
n=int(input('Enter the number of lines:')) # Take a number from the user as the maximum number of stars in a line
while a<n :
    a+=1 # Because we want to increase the number of stars in each line, so we add a number to a loop
    print(' * ' * a) # it is a command with which the number 'a' star can be printed.
for i in range(n) :
    a-=1 # in this step we want to do the opposite of the above operation, so in each loop substract 1 from a
    print(' * ' * a) # to make the shape look more beatiful, we leave a space on both of sides of the star.
