import datetime
today=datetime.datetime.now()
print(today)
list_tohoku=[5349.0,5478.0,5344.0,4644.0,4968.0,6259.0]
list_shikoku=[3148.0,2991.0,2966.0,2457.0]
avg_tohoku=0
for val in list_tohoku:
    avg_tohoku +=val
avg_tohoku /=len(list_tohoku)
print(avg_tohoku)
dict_tohoku={'aomori':5349.0,'akita':4644.0,'sendai':5344.0,'Yamagata':4968.0,'fukushima':6259.0,'morioka':5478.0}
for val in dict_tohoku:
    print(val)
    avg_tohoku/=dict_tohoku[val]
    avg_tohoku/=len(dict_tohoku)

test_file=open('test.txt','w')
test_file.write('Hello!')
test_file.flush()
test_file.close()
'''
test_file=open('test.txt','r')
read_str=test_file.readline()
test_file.close()
print(read_str)'''
test_file=open('test2.txt','w')
test_file.write('Hello!\nPython')
test_file.close()
test_file=open('test2.txt','r')
lines=test_file.readlines()
print(lines)
test_file.close()
print(lines[0])
print(lines[0].strip())
data=['1,2,3\n','4,5,6\n','7,8,9\n']
test_file=open('test3.txt','w')
test_file.writelines(data)
test_file.flush()
test_file.close()

#'-'.join(['a','b','c'])
test_file=open('test3.txt','r')
for line in test_file:
    print(line.strip())
test_file.close()
    
test_file=open('test3.txt','r')
for line in test_file:
    temp_list=line.strip().split(',')
    output_line='\t'.join(temp_list)
    print(output_line)
test_file.close()
