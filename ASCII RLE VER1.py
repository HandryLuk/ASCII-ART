def encode():
    file_name=input('Please enter the name of the text file that contains the ASCII art: ')
    file_name=file_name+'.txt'#get file name
    line_list=[]
    word=0
    with open((file_name),'r') as f:#open file
      total_lines=len(f.readlines())#get amount of lines in the file
      f=f.readlines()
    count=0
    for i in range(0,int(total_lines)):
        f=open(file_name)
        f=f.readlines()
        data=(f[count])#get the x line according to the for loop
        data_list=[]
        frequency=1
        word=word+(int(len(data)))#count the amount of character in line x for compare the difference between ascii and rle
        for j in range(0,int(len(data))):#for loop according the length of the xth line
          if int(len(data))>(j+1):#ensure the amount of loop doesnt excess the amount of characters
            if data[j]==data[j+1]:# if the first character == the second character:
               frequency+=1#add the frequence by 1
               character=data[j]#get what is the character
            else:#if the first character != second character
               character=data[j]#get what is the character
               output_data=(str(frequency).rjust(2,'0'))#add '0' infront of the frequency
               output_data=output_data+character#join the frequency and the character
               data_list.append(output_data)#put the rle of the xth line to a list
               frequency=1#revalue the frequency
        data_list=(''.join(data_list))#join the list
        line_list.append(data_list)#put the rle of the xth line in a new list
        line_list.append('\n')#skip a line
        count+=1
    print('The RLE code of the ASCII art is:')
    print(''.join(line_list))#print the item in a list
    word=(len(''.join(line_list)))-word#find the difference of characters between ascii and rle
    if word>0:
        print('The ascii code have',word,'less characters than the RLE code.')
    elif word<0:
        word=word*-1
        print('The ascii code have',word,'more characters than the RLE code.')
    else:
        print('The ascii code have the same amount of characters as the RLE code.')
        
        
  
def RLE():
    lines=int(input("Enter the total number of line."))
    line_list=[]
    while lines<=2:
        lines=int(input('This need to be more than 2 lines.'))
    for i in range(0,lines):
        data_list=[]
        data=input('Please enter a line of RLC code.')
        count=0
        frequency=0
        for j in range(0,int((len(data)/3))):#make sure 'list out of range' error will not occur
            frequency= data[count:count+2]#get the first two characters as frequency
            frequency= int(frequency)#turn it from str to int
            character= data[count+2]#get the third characters as character
            character= (character*frequency)#output the characters by frequency times
            count+= 3
            data_list.append(character)# put the rle of the x line to a list
        data_list=(''.join(data_list))#join the items of the list
        line_list.append(data_list)#put the line of rle to a new list
        line_list.append('\n')#skip a line
    print(''.join(line_list))#print the joined list until all of the lines are decoded
def display_ASCII():
    file_name=input('Please enter the name of the text file that contains the ASCII art: ')
    file_name=file_name+'.txt'#get the name of the file
    f=open((file_name),'r')#read the file
    print(f.read())#print the file
def convert_ASCII():
    file_name=input('Please enter the name of the text file that contains the RLE code: ')
    file_name=file_name+'.txt'#get the na,e of the file
    line_list=[]
    word=0
    with open((file_name),'r') as f:
      total_lines=len(f.readlines())#find the amount of lines in the file
      f=f.readlines()
    count=0
    for i in range(0,int(total_lines)):
      with open((file_name),'r') as f:
        f=f.readlines()
        data=(f[i])#get the xth line in the file
        data_list=[]
      data_list=[]
      count=0
      frequency=0
      for j in range(0,int((len(data)/3))):
            frequency= data[count:count+2]#get the first two character of the line
            frequency= int(frequency)#then convert it to int for frequency
            character= data[count+2]#get the third character as character
            character= (character*frequency)#get the character as frequency times character
            count+= 3#get to the forth character for the loop
            data_list.append(character)#put the characters into a list
      data_list=(''.join(data_list))#join the items in the list
      line_list.append(data_list)# put the xth line of ascii code in a new list
      line_list.append('\n')#input \n in the list for new line
    print(''.join(line_list)) #print the final ascii art
        
def menu(select):#open the sutible subroutine according to the selection
    if select=='1':
        RLE()
    if select=='2':
        display_ASCII()
    if select=='3':
        convert_ASCII()
    if select=='4':
        encode()
    select=input('Enter 1 for enter RLE, enter 2 for display ASCII art, enter 3 for convert to ASCII art, enter 4 to convert to RLE, enter 5 to quit: ')
    if select!='5':
       menu(select)
#The code starts here
select=input('Enter 1 for enter RLE, enter 2 for display ASCII art, enter 3 for convert to ASCII art, enter 4 to convert to RLE, enter 5 to quit:')
if select!='5':
    menu(select)
print("See you next time, bye!")
