# writing into file
# fp=open('text.txt','w')
# fp.write("hi varun")
# fp.close()



# # reading the file
# fp=open('text.txt',"r")
# x=fp.readline() # to display line bt line
# print(x)
# x=fp.readline()
# print(x)
# fp.close()




# # read all the lines in the file
# fp=open("text.txt","r")
# import time
# for line in fp:
#     print(line)
#     time.sleep(1)
# fp.close()
 
#   # or

# fp=open("text.txt","r")
# import time
# for line in fp.readlines():
#     print(line)
    
# fp.close()

# seeK()
# tell()
# f=open("text.txt","r")
# f.seek(11) # read from 11 th character
# print(f.tell()) # tells cursor postion
# print(f.read())

# f.close()


# longest_line=""
# long_length=0
# f=open("text.txt","r")
# for line in f:
   
#     if len(line)>long_length:
#         long_length=len(line)
#         longest_line=line
# f.close()
# print("longest line:",longest_line)
# print("length of logest line:",long_length)
