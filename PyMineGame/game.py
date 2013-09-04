# coding=utf-8
'''
Created on 2013-5-3

@author: snowonion
'''
import platform

if platform.system()=='Linux':
    print 'this is linux'
    from curses.ascii import TAB
    #不知道干嘛的。很可能源于某一次错误的联想导致的自动import。
elif platform.system()=='Windows':
    print 'this is windows'
    pass
    

class Grid:
    '''
    isMine: bool，是雷否
    num: int，周8格雷数；是雷则-1
    status: int, sage=0,flag=-1,open=1
    display: str，进行时显示出来的东西
    '''
    SAGE=0
    FLAG=-1
    OPEN=1
    def __init__(self, oneIfIsmineElseZero):
        self.isMine = (oneIfIsmineElseZero == 1)
        self.num = -1 if self.isMine else 0  # calc then, in Board class's method
        self.status = Grid.SAGE
        self.display = '#'
    

class Board:
    '''
    table: Grid类型，2-dimension list，雷盘局势
    m: int，剩余雷数
    rows: int, = len(table)
    cols: int, = len(table[0])
    '''
    def fail(self):
        self.printData()
        print 'Game Over'
    
    def open(self, row, col):
        '''
        return 0 if touch mine
        return 1 if safe
        '''
        self.table[row][col]
        if self.table[row][col].isMine:
            self.fail()
            return 0
        else:
            def op(i, j):
                if self.table[i][j].status!=Grid.SAGE:
                    return
                else:
                    self.table[i][j].status = Grid.OPEN
                    self.table[i][j].display='%2d'%(self.table[i][j].num)
                    
                if self.table[i][j].num == 0:
                    # Fuck my life!!!!!!!!!!!!!!!!!!!!!!!!!!
                    up = (i == 0)
                    down = (i == self.rows - 1) 
                    left = (j == 0) 
                    right = (j == self.cols - 1)
                    if up and left:
                        op(i, j + 1)
                        op(i + 1, j)
                        op(i + 1, j + 1)
                    if up and not left and not right:
                        op(i, j - 1)
                        op(i, j + 1)
                        op(i + 1, j - 1)
                        op(i + 1, j)
                        op(i + 1, j + 1)
                    if up and right:
                        op(i, j - 1)
                        op(i + 1, j - 1)
                        op(i + 1, j)
                    if right and not up and not down:
                        op(i - 1, j - 1)
                        op(i - 1, j)
                        op(i, j - 1)
                        op(i + 1, j - 1)
                        op(i + 1, j)
                    if right and down:
                        op(i - 1, j - 1)
                        op(i - 1, j)
                        op(i, j - 1)
                    if down and not right and not left:
                        op(i - 1, j - 1)
                        op(i - 1, j)
                        op(i - 1, j + 1)
                        op(i, j - 1)
                        op(i, j + 1)
                    if down and left:
                        op(i - 1, j)
                        op(i - 1, j + 1)
                        op(i, j + 1)
                    if left and not up and not down:
                        op(i - 1, j)
                        op(i - 1, j + 1)
                        op(i, j + 1)
                        op(i + 1, j)
                        op(i + 1, j + 1)
                    if not left and not right and not up and not down:
                        op(i - 1, j - 1)
                        op(i - 1, j)
                        op(i - 1, j + 1)
                        op(i, j - 1)
                        op(i, j + 1)
                        op(i + 1, j - 1)
                        op(i + 1, j)
                        op(i + 1, j + 1)                
            # end op()
            
            op(row, col)
            
    def flag(self, row, col):
        if self.table[row][col].status==Grid.OPEN:
            return
        elif self.table[row][col].status==Grid.SAGE:
            self.table[row][col].status=Grid.FLAG
            self.table[row][col].display=' f'
            self.m-=1
        elif self.table[row][col].status==Grid.FLAG:
            self.table[row][col].status=Grid.SAGE
            self.table[row][col].display=' #'
            self.m+=1
    
    def control(self, cmd):
        cmd = cmd.split(' ')
        if len(cmd)<3:
            print 'command contains too few arguments'
        elif cmd[0] == 'f' or cmd[0] == 'F' or cmd[0] == 'flag':
            self.flag(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'o' or cmd[0] == 'O' or cmd[0] == 'open':
            self.open(int(cmd[1]), int(cmd[2]))
        else:
            print 'invalid command'
        
    
    def __init__(self, filePath):
        def readFromFile(filePath):
            '''return int[][] OneIfMineElseZero'''
            fp = file(filePath, 'rU')
            rst = fp.readlines()       
            fp.close()
            rst = [line.split(' ') for line in rst]
            rst = [[int(ele) for ele in line]for line in rst]
            return rst

        def calcNum():
            self.rows = len(self.table)
            self.cols = len(self.table[0])
            for i in range(self.rows):
                for j in range (self.cols):
                    if not self.table[i][j].isMine:
                        # Fuck my life!!!!!!!!!!!!!!!!!!!!!!!!!!
                        up = (i == 0)
                        down = (i == self.rows - 1) 
                        left = (j == 0) 
                        right = (j == self.cols - 1)
                        if up and left:
                            self.table[i][j].num = [self.table[i][j + 1].isMine, self.table[i + 1][j].isMine, self.table[i + 1][j + 1].isMine].count(True)
                        if up and not left and not right:
                            self.table[i][j].num = [self.table[i][j - 1].isMine, self.table[i ][j + 1].isMine, self.table[i + 1][j - 1].isMine, self.table[i + 1][j ].isMine, self.table[i + 1][j + 1].isMine].count(True)
                        if up and right:
                            self.table[i][j].num = [self.table[i][j - 1].isMine, self.table[i + 1][j - 1].isMine, self.table[i + 1][j].isMine].count(True)
                        if right and not up and not down:
                            self.table[i][j].num = [self.table[i - 1][j - 1].isMine, self.table[i - 1][j].isMine, self.table[i][j - 1].isMine, self.table[i + 1][j - 1].isMine, self.table[i + 1][j].isMine].count(True)
                        if right and down:
                            self.table[i][j].num = [self.table[i - 1][j - 1].isMine, self.table[i - 1][j].isMine, self.table[i][j - 1].isMine].count(True)
                        if down and not right and not left:
                            self.table[i][j].num = [self.table[i - 1][j - 1].isMine, self.table[i - 1][j].isMine, self.table[i - 1][j + 1].isMine, self.table[i][j - 1].isMine, self.table[i][j + 1].isMine].count(True)
                        if down and left:
                            self.table[i][j].num = [self.table[i - 1][j].isMine, self.table[i - 1][j + 1].isMine, self.table[i][j + 1].isMine].count(True)
                        if left and not up and not down:
                            self.table[i][j].num = [self.table[i - 1][j].isMine, self.table[i - 1][j + 1].isMine, self.table[i][j + 1].isMine, self.table[i + 1][j].isMine, self.table[i + 1][j + 1].isMine].count(True)
                        if not left and not right and not up and not down:
                            self.table[i][j].num = [self.table[i - 1][j - 1].isMine, self.table[i - 1][j].isMine, self.table[i - 1][j + 1].isMine, self.table[i ][j - 1].isMine, self.table[i][j + 1].isMine, self.table[i + 1][j - 1].isMine, self.table[i + 1][j].isMine, self.table[i + 1][j + 1].isMine].count(True)
        
        mineTable = readFromFile(filePath)
        self.table = [[Grid(ele) for ele in line]for line in mineTable]
        self.m = sum([sum(line) for line in mineTable])
        calcNum()
        for line in self.table:
            for ele in line:
                ele.display = ' #'
            
    def printCUI(self):
        print '~' * 30
        print ' ' * 2,
        for j in range(30):
            print '%2d' % (j),
        print
        for row in self.table:
            print '%2d' % (self.table.index(row)),
            for ele in row:
                print ele.display,
            print 
        print 'M=%d' % (self.m)
        
    def printData(self):
        print '~' * 30
        print ' ' * 2,
        for j in range(30):
            print '%2d' % (j),
        print
        for row in self.table:
            print '%2d' % (self.table.index(row)),
            for ele in row:
                print '%2d' % (ele.num),
            print 
        print 'M=%d' % (self.m)
        
import os
# os.system('clear')  #eclipse 里会报TERM environment variable not set.，终端里正常

if __name__ == '__main__':
    theMine = Board('mine.txt')
    liveFlag=True
    while liveFlag:
        theMine.printCUI()
        theMine.control(raw_input('>'))
