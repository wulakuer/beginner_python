man=[]
other=[]

try:
    data=open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            line_spoken=line_spoken.strip()
            if role=='Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
except IOError:
    print('The file is missing')

print(man)
print(other)
try:
    
    '''man_file=open('man_data.txt','w')
    other_file=open('other_data.txt','w')'''
    with open('man_data.txt','w') as man_file:
        print(man,file=man_file)        
    with open('other_data.txt','w') as other_file:
        print(other,file=other_file)
    
except IOError as err:
      print('File Error:'+ str(err))
      
'''finally:
    if 'man_file' in locals():
        man_file.close()
    if 'other_file' in locals():
        other_file.close()'''
            
