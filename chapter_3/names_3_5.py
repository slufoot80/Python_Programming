#List and messages set to variables
fname = ['paula','frank','lisa','gabe','gena','sammy','tony','daddy','lynne']
length = len(fname)
print("The length of my list is " + str(length))
msg0 = ", Please come to dinner"
msg1 = ", Can't make it for dinner tonight!"
msg2 = ", Can make it for dinner tonight!\n\n"
# Print Statements
print(fname[0].title() + msg0)
print(fname[1].title() + msg0)
print(fname[2].title() + msg0)
print(fname[3].title() + msg0)
print(fname[4].title() + msg0)
print(fname[5].title() + msg0)
print(fname[6].title() + msg0)

print("\nSorry, " + fname[1].title() + msg1)
del(fname[1])
fname.insert(1, 'papa')
print("Although, " + fname[1].title() + msg2)
