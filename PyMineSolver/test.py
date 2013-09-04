#coding=utf-8
'''
Created on 2013-5-29

@author: SnowOnion
'''
from mat import circumIjIndexList


# @well 
def matrixForm(mat, width):
    '''现在只能是整数 matrix 啦。
    '''
    from os import linesep
    rst = ''
    for line in mat:
        for ele in line:
            newnew = str(ele)
            rst = rst + ('%' + str(width) + 's') % (newnew)
        rst += linesep
    return rst

# @well
def printMatrix(mat, width=3):
    print matrixForm(mat, width),
    
# @quite well    
def tolog(str, filePath="log.txt"):
    f = file(filePath, 'w')
    f.write(str)
    f.close
    
# </UTIL>




def lianxufuhao():
    x=-2
    if -3<x<-1:
        print 'true'
    else:
        print 'false'
    
def ttt():
    print circumIjIndexList(0, 0, 3, 3)
    print circumIjIndexList(0, 1, 3, 3)
    print circumIjIndexList(0, 2, 3, 3)
    print circumIjIndexList(1, 0, 3, 3)
    print circumIjIndexList(1, 1, 3, 3)
    print circumIjIndexList(1, 2, 3, 3)
    print circumIjIndexList(2, 0, 3, 3)
    print circumIjIndexList(2, 1, 3, 3)
    print circumIjIndexList(2, 2, 3, 3)
    
# @well
def addPre(lst, alphabet):
    newlst = []
    for alpha in alphabet:
        for ele in lst:
            alst = [alpha]
            alst.extend(ele)
            newlst.append(alst)
    return newlst

# @well
def dicOrder(length=1, alphabet=[0, 1]):
    lst = [[]]
    for i in range(length):
        lst = addPre(lst, alphabet)
    return lst

# print dicOrder(81) #Don't watch an anime named boku!



def list2mat(lst,col):
    mat=[]
    for i in range(len(lst)/col):
        mat.append(lst[i*col:(i+1)*col])
    if len(lst)%col!=0:
        print 'warn: 列数不整除元素数.'
        mat.append(lst[(len(lst)/col)*col:])
    return mat
        
for i in range(1,10):
    printMatrix(list2mat(range(i), 3))
#     print list2mat(range(i),3)


