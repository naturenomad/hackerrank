# LISTS

# Action user input commands on a list

#### Internal call code :

def listeval():        
    n = int(input())
    l = list()
    cmds = list()
    arr = list()
    
    for i in range(n):
        l = list(input().split())
        cmds.append(l)
    
    for j in cmds:
        cmd = j[0]
        args = j[1:]
        if cmd == 'print':
            print(arr)
        else:
            cmd += '(' + ','.join(args) + ')'
            eval('arr.' + cmd)       


# External call code
if __name__ == '__main__':
    n = int(input())
    l = list()
    cmds = list()
    arr = list()
    
    for i in range(n):
        l = list(input().split())
        cmds.append(l)
    
    for j in cmds:
        cmd = j[0]
        args = j[1:]
        if cmd == 'print':
            print(arr)
        else:
            cmd += '(' + ','.join(args) + ')'
            eval('arr.' + cmd)

'''
# Sample commands
listeval()
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
# Expect the following output
#[6, 5, 10]
#[1, 5, 9, 10]
#[9, 5, 1]
'''
