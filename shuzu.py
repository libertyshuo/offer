# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------
# 面试题3 二维数组中的查找
# 行列均排好序的二维数组找某个数字
# class Solution:
#     # array 二维列表
#     def Find(target, array):
#         if(len(array[0])<1):
#             return False;
#         found = False;
#         line = len(array)-1;
#         line_min = 0;
#         row_min = 0;
#         row = len(array[0])-1;
#         right = array[0][row];
#         print line,row;
#         while((row>0)and(line_min<line)):
#             if(target<right):
#                 row = row - 1;
#                 right = array[line_min][row];
#                 print "<<<<<<<<<<<<<<<",row,right;
#             if(target>right):
#                 line_min = line_min + 1;
#                 right = array[line_min][row];
#                 print ">>>>>>>>>>>>>>>>",line_min,right;
#             if(target==right):
#                 print True;
#                 return True;
#         print target,right;
#         print found
#         return False;
#         # write code here
#     Find(16,[[]])   #列表[[]]，len(array)为1，len(array[0])为0；列表[[1]]，都为1

# -----------------------------------------------------------------------
# 面试题5 替换空格
# 字符串中的空格替换为 %20
# class Solution:
#     # s 源字符串
#     def replaceSpace( s):
#         print s.replace(' ','%20')
#         # write code here
#     replaceSpace('w er t y eerw aaa')

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# ------------------------------------------------------------------------
# 面试题6 从尾到头打印链表
# 实现链表结构：每个Node分为两部分。一部分含有链表的元素，可以称为数据域；另一部分为一指针，指向下一个Node。
# class Node(object):
#     def __init__(self,initdata):
#         self.data = initdata;
#         self.next = None

#     def getdata(self):
#         return self.data

#     def setdata(self,newData):
#         self.data = newData

#     def getNext(self):
#         return self.next

#     def setNext(self,nextNode):
#         self.next = nextNode

# class UnorderedList:
#     def __init__(self):
#         self.head = None

#     def isEmpty(self):
#         return self.head == None
#     # 在链表头部添加数据    
#     def add(self,item):
#         temp = Node(item)
#         temp.setNext(self.head)
#         self.head = temp

#     def size(self):
#         current = self.head
#         count = 0
#         while current != None:
#             count = count + 1
#             self.head = current.getNext()
        
#         return count

#     def search(self,item):
#         current = self.head
#         found = False
#         while current != None and not found:
#             if current.getdata() == item:
#                 found = True
#             else:
#                 current = current.getNext()

#         return found

#     def remove(self,item):
#         current = self.head
#         previous = None
#         found = False
#         while not found:
#             if current.getdata() == item:
#                 found = True
#             else:
#                 previous = current
#                 current = current.getNext()

#         if previous == None:
#             self.head = current.getNext()
#         else:
#             previous.setNext(current.getNext())

# 实现栈结构：后入后出;用list直接实现栈
# class Stack(object):
#     # 初始化栈为空列表
#     def __init__(self):
#         self.items = []

#     # 判断栈是否为空，返回布尔值
#     def isEmpty(self):
#         return self.items == []

#     # 返回栈顶元素
#     def peek(self):
#         return self.items[len(items)-1]

#     # 返回栈的大小
#     def size(self):
#         return len(self.items)

#     # 把新的元素堆在栈里面，入栈
#     def push(self,item):
#         self.items.append(item)

#     # 出栈
#     def pop(self):
#         return self.items.pop()     #python的list结构有pop函数

# class Solution:
#     def printListFromTailToHead(self,listNode):
#         result = []
#         if listNode == None:
#             print result
#             return result
#         current = listNode
#         stackkk = Stack()
#         while current != None:
#             stackkk.push(current.val)
#             current = current.next
#         while not stackkk.isEmpty():
#             print stackkk.pop()

# -----------------------------------------------------------------------
# 重建二叉树
"""输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     # 返回构造的TreeNode根节点
#     def reConstructBinaryTree(self, pre, tin):
#         print pre,tin
#         pre_list = list(pre)
#         tin_list = list(tin)
#         if pre_list==[] or tin_list==[] or len(pre_list)!=len(tin_list):
#             return None
#         root = TreeNode(pre_list[0])
#         # root.val = pre_list[0]
#         # if pre_list[0] not in tin_list:
#             # return None
#         if len(pre_list)==1:
#             return root
#         else:
#             for i in range(0,len(tin_list)):
#                 if tin_list[i] == pre_list[0]:
#                     break
#             root.left = self.reConstructBinaryTree(pre_list[1:i+1],tin_list[:i])
#             root.right = self.reConstructBinaryTree(pre_list[i+1:],tin_list[i+1:])
#         return root

# -------------------------------------------------------------------------------------
# 面试题8 二叉树的下一个节点：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
# class Solution:
#     def GetNext(self, pNode):
#         # write code here
#         Node = TreeLinkNode(pNode)
#         if Node == None:
#             return Node
#         elif Node.right != None:
#             Node = Node.right
#             while Node.left != None:
#                 Node = Node.left
#             return Node
#         Next = Node.next
#         while Next != None:
#             if Node != Next.left:
#                 Node = Node.next
#                 Next = Next.next
#             return Node.next
#         return None

"""
# 面试题11 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，
输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
# -*- coding:utf-8 -*-
# class Solution:
#     def minNumberInRotateArray(self, rotateArray):
#         if len(rotateArray)==0:
#             return 0
#         if len(rotateArray)==1:
#             return rotateArray[0]
#         index1 = 0
#         index2 = len(rotateArray)-1
#         while (rotateArray[index1] >= rotateArray[index2]):
#             if index2-index1 == 1:
#                 return rotateArray[index2]
#             indexMid = (index2+index1)/2
#             print indexMid
#             if rotateArray[indexMid]>=rotateArray[index1]:
#                 index1 = indexMid
#             elif rotateArray[indexMid]<=rotateArray[index2]:
#                 index2 = indexMid
#             print index2,index1
#         return rotateArray[index2]
# if __name__ == '__main__':
#     a = Solution()
#     print a.minNumberInRotateArray([6,7,8,1,2,3])

# ---------------------------------------------------------------------------------
# 快速排序
# -*- coding:utf-8 -*-
# class Solution:
#     def quickSort(self,array,l,r):
#         if len(array) == 0 or len(array)==1 or l>=r:
#             return array
#         # print array
#         index1 = l
#         index2 = r
#         # print "initial",index1,index2
#         init = array[index1]
#         while index1!=index2:
#             if index2<index1:
#                 print 'error'
#                 return 0
#             if index2>index1:
#                 while array[index2]>=init and index2>index1:
#                     index2 = index2-1
#                 if index2!=index1:
#                     array[index1] = array[index2]
#                 # print "circle",index2,array[index1]
#                 while array[index1]<=init and index2>index1:
#                     index1 = index1+1
#                 if index2!=index1:
#                     array[index2]=array[index1]
#         if index1==index2:
#             array[index1]=init
#         # print "-----------------"
#         # print index1,index2
#         # print array
#         self.quickSort(array,l,index1-1)
#         self.quickSort(array,index1+1,r)
#         return array
# if __name__ == '__main__':
#     a = Solution()
#     print a.quickSort([2,4,5,1],0,3)

# ---------------------------------------------------------------------------------------
# 矩阵中的路径
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.lable=[]
        self.r=[]
        self.c=[]

    def hasPath(self, matrix, rows, cols, path):
        if len(matrix)==0 or rows==0 or cols==0 or len(path)==0 or len(matrix)!=rows*cols:
            return False
        array = [[0]*cols for i in range(rows)]
        self.r = self.c = [None]*len(path)
        for i in range(0,rows):
            for j in range(0,cols):
                array[i][j]=matrix[cols*i+j]
        return self.arr(array, path,-1,-1)
    def arr(self,array, path,row,col):
        rows,cols=len(array),len(array[0])
        for i in range(0,rows):
            for j in range(0,cols):
                if array[i][j]==path[0] and i>row and j>col:
                    label = [[0]*cols for i in range(rows)]     #做标记
                    label[i][j]=1
                    self.r[0]=i
                    self.c[0]=j
                    print i,j,array[i][j],path[0],self.r,self.c,label
                    self.core(i,j,array,path,1,self.r,self.c,label)
        return False
    def core(self,row,col,array,path,pi,r,c,label):
        if pi == len(path):
            return True
        elif row>0 and pi>=0 and pi<len(path):
            if array[row-1][col]==path[pi] and label[row-1][col]!=1:
                label[row-1][col]=1
                r[pi],c[pi]=row-1,col
                return self.core(row-1,col,array,path,pi+1,r,c,label)
        elif row<len(array)-1 and pi>=0 and pi<len(path):
            if array[row+1][col]==path[pi] and label[row+1][col]!=1:
                label[row+1][col]=1
                r[pi],c[pi]=row+1,col
                return self.core(row+1,col,array,path,pi+1,r,c,label)
        elif col>0 and pi>=0 and pi<len(path):
            if array[row,col-1]==path[pi] and label[row,col-1]!=1:
                label[row,col-1]=1
                r[pi],c[pi]=row,col-1
                return self.core(row,col-1,array,path,pi+1,r,c,label)
        elif col<len(array[0])-1 and pi>=0 and pi<len(path):
            if array[row][col+1]==path[pi] and label[row][col+1]!=1:
                label[row][col+1]=1
                r[pi],c[pi]=row,col+1
                return self.core(row,col+1,array,path,pi+1,r,c,label)
        elif pi==1:
            return self.arr(array, path,row,col)
        else:
            label[r[pi]][c[pi]]=0
            return self.core(r[pi-1],c[pi-1],array,path,pi-1,r,c,label)
if __name__ == '__main__':
    a = Solution()
    print a.hasPath(['e','s','f','e','s','g','j','o'],4,2,'es')