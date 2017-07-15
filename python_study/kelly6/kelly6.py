def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
       
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins,secs)=time_string.split(splitter)
    return (mins+'.'+secs)
def split_coach_data(file_object):
    dict={}
    try:
        with open (file_object) as file:
            for each_line in file:
                a_list=each_line.strip().split(',')
                dict['name']=a_list.pop(0)
                dict['dob']=a_list.pop(0)
                #dict['time']=a_list
                dict['time']=str(sorted(set(sanitize(each) for each in a_list))[0:3])
            return dict
    except IOError as err:
        print(str(err))
        return(None) 

sarah_dict={}
mikey_dict={}
julie_dict={}
james_dict={}
name_list=['james','julie','mikey','sarah']
try:
    #with open('julie.txt') as julie_file, open('james.txt') as james_file, open('sarah.txt') as sarah_file,open('mikey.txt') as mikey_file:
       # name_list[0]=split_coach_data(james_file)
       # name_list[1]=split_coach_data(julie_file)
       # name_list[2]=split_coach_data(mikey_file)
       # name_list[3]=split_coach_data(sarah_file)

        #print(dict['name']+"'s fast time are:"+dict['time'])
        #sarah_dict['name']=name_list[3].pop(0)
        #sarah_dict['dob']=name_list[3].pop(0)
        #sarah_dict['time']=name_list[3]
        #print(sarah_dict['name']+" fast time are:"+str(sorted(set(sanitize(each) for each in name_list[3]))[0:3]))

        james=split_coach_data('james.txt')
        print(james['name']+ "'s fast time are: "+james['time'])
       
        
except IOError as err:
    print(str(err))

