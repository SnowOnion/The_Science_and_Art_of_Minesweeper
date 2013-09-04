#coding=utf-8
'''
Created on 2013-6-2

@author: SnowOnion
'''

class MatUtil(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
    # @well 
    @staticmethod  # static方法, 过程思维(摊手
    def matrixForm(mat, width, floatDigit):
        '''
        '''
        from os import linesep
        rst = ''
        for line in mat:
            for ele in line:
                if type(ele) == type(3.14):  # for float
                    newnew = ('%.' + str(floatDigit) + 'f') % (ele)
                else:
                    newnew = str(ele)
                rst = rst + ('%' + str(width) + 's') % (newnew)
            rst += linesep
        return rst
    
    # @well
    @staticmethod  # static方法, 过程思维(摊手
    def printMatrix(mat, title='iMatrix', width=3, floatDigit=2):
        print'-' * 10, title, '-' * 10
        print MatUtil.matrixForm(mat, width, floatDigit),
        
    # @well
    @staticmethod  # static方法, 过程思维(摊手
    def mat2list(mat):
        lst = []
        for line in mat:
            lst.extend(line)
        return lst
    
    # @well
    @staticmethod  # static方法, 过程思维(摊手
    def list2mat(lst, col):
        mat = []
        for i in range(len(lst) / col):
            mat.append(lst[i * col:(i + 1) * col])
        if len(lst) % col != 0:
            print 'warn: 列数不整除元素数.'
            mat.append(lst[(len(lst) / col) * col:])
        return mat        
    
    # @well
    @staticmethod  # static方法, 过程思维(摊手
    def realIndex(col, i, j):
        return i * col + j
    
    # @well
    @staticmethod  # static方法, 过程思维(摊手
    def ijIndex(col, realInd):
        return (realInd / col, realInd % col)
    
    # 在这里处理越界！！大概暴力地一劳永逸？
    # @ well
    @staticmethod  # static方法, 过程思维(摊手
    def circumIjIndexList(i, j, row, col):
        
        lst = []
        
        up = (i == 0)
        down = (i == row - 1) 
        left = (j == 0) 
        right = (j == col - 1)
         
        if up and left:
            lst.append((i, j + 1))
            lst.append((i + 1, j))
            lst.append((i + 1, j + 1))
             
        if up and not left and not right:        
            lst.append((i, j - 1))
            lst.append((i, j + 1))
            lst.append((i + 1, j - 1))
            lst.append((i + 1, j))
            lst.append((i + 1, j + 1))
             
        if up and right:        
            lst.append((i, j - 1))
            lst.append((i + 1, j - 1))
            lst.append((i + 1, j))
             
        if right and not up and not down:        
            lst.append((i - 1, j - 1))
            lst.append((i - 1, j))
            lst.append((i, j - 1))
            lst.append((i + 1, j - 1))
            lst.append((i + 1, j))
             
        if right and down:        
            lst.append((i - 1, j - 1))
            lst.append((i - 1, j))
            lst.append((i, j - 1))
             
        if down and not right and not left:        
            lst.append((i - 1, j - 1))
            lst.append((i - 1, j))
            lst.append((i - 1, j + 1))
            lst.append((i, j - 1))
            lst.append((i, j + 1))
             
        if down and left:        
            lst.append((i - 1, j))
            lst.append((i - 1, j + 1))
            lst.append((i, j + 1))
             
        if left and not up and not down:        
            lst.append((i - 1, j))
            lst.append((i - 1, j + 1))
            lst.append((i, j + 1))
            lst.append((i + 1, j))
            lst.append((i + 1, j + 1))
             
        if not left and not right and not up and not down:        
            lst.append((i - 1, j - 1))   
            lst.append((i - 1, j))
            lst.append((i - 1, j + 1))
            lst.append((i, j - 1))
            lst.append((i, j + 1))
            lst.append((i + 1, j - 1))
            lst.append((i + 1, j))
            lst.append((i + 1, j + 1))
    
        return lst