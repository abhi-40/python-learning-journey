# open and read


# f=open("abhi.txt","r")
# content=f.read()
# print(content)
# f.close()

# write

# f=open("john.txt","w")
# string='''
# John doe is a nice guy 
# he live in NYC
# he is coder
# '''
# f.write(string)
# f.close()

# Append to exist file

# f=open("john.txt","a")
# string='''
# he is graduated from cambridge univ
# with an avg cgpa of 7.5
# '''
# f.write(string)
# f.close()
# print("Task done")

# read line by line

# f=open("abhi.txt","r")

# for line in f:
#     print(line)

# f.close()

# with open method

with open ("abhi.txt","r") as f:
    content=f.read()
    print(content)