#تمرین 1-1

def BFS(graph , start):
    queue = [start]
    visited = {start}
    while queue:
        vertex = queue.pop(0)
        for ne in graph[vertex]:
            visited.add(ne)
            queue.append(ne)


    return visited

def DFS(graph , start , visited):
    visited[start] = True
    for ne in graph[start]:
        if not visited[ne]:
            DFS(graph , ne , visited)

def sort1(A):
    B = [] *len(A)
    for i in range(len(A)):
        for j in range(1 , len(A)):
            if A[j] < min:
                min = A[j]
                k = j
        B[i] = min
        A[k] = float("inf")
    return B 

def Bubble(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1] , A[j]  


#تمرین 1-2


class Tree_Node :
    def __init__(self , x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None
#تابع بازگشتی بنویسید که تعداد برگ های درخت باینری روت را محاسبه کند
def Count_leaves(root):
    if root is None:
        return 0
    if 2 :
#       if root.Lchild is None :
#           and root.Rchild is not None:
#       if root.Rchild is None:
#           and root.Lchild is not None:                
        return 1
    return Count_leaves(root.Lchild) + Count_leaves(root.Rchild)

#تابع بازگشتی بنویسید که گره های درجه یک ، درخت باینری را محاسبه کند
def Count_1Deg(root):
    if root is None:
        return 0
    if root.Lchild:
        return 1
    if root.Rchild:
        return 1
    return Count_1Deg(root.Lchild) + Count_1Deg(root.Rchild)   

def Count_2Deg (root):
    if root is None:
        return 0
    if root.Lchild:
        return Count_2Deg(root.Lchild)
    if root.Rchild:
        return Count_2Deg(root.Rchild)
    return Count_2Deg(root.Lchild) + Count_2Deg(root.Rchild)

#تابعی بازگشتی بنویسید که حاصل جمع تمامی داده های یک درخت دودویی را بازگرداند
def sum_Tree(root):
    if root is None:
        return 0
    if root.Lchild:
        return sum_Tree(root.Lchild) + root.Data
    if root.Rchild:
        return sum_Tree(root.Rchild) + root.Data
    return sum_Tree(root.Lchild) + sum_Tree(root.Rchild) + root.Data

#تابعی بازگشتی بنوبسید که تعداد نود های یک درخت باینری را بازگرداند
def Count(root):
    if root is None:
        return 0
    return 1+ Count(root.Lchild) + Count(root.Rchild)





def pre(root):
    if root is None:
        return
    print(root.Data)
    print(root.Lchild)
    print(root.Rchild)       

#تابعی بازگشتی بنویسید که مقدار تارگت را در یک درخت جستجو کند
def search(root , t):
    if root is None:
        return False
    if root.Data == t:
        return True
    return search(root.Lchild) or search(root.Rchild)      

#تابعی بازگشتی بنویسید که مقدار حداکثر یک درخت را بازگرداند
def max_t(root):
    if root is None:
        return float("inf")
    return max(max_t(root.Lchild) , max_t(root.Rchild) , root.Data)
    










def count(root):
    if root is None:
        return 0
    return 1+ count(root.left) + count(root.right)


#تمرین 1-3

#fib(n)
1,1,2,3,5,8,13,
#fib(n) = fib(n-1) + fib(n-2)
#shart bazgasht :
#if (n = 1) or (n = 2) :
#meqdar bazgasht :
#1
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)




    for i in range (n):
        for j in range(n):
            for k in range(n):
                c[i,k] = c[i,k] + a[i,j] *[j.k]


def test(a,b):
    if a>b :
        return a*b
    return test(a , b-2) + test(a-1 , b-3) +6
test(3,7)


#تمرین 1-4




class dnode():
    def __init__(self , x):
        self.Data = x
        self.next = None
        self.back = None


class dlinked_list :
    def __init__(self):
        self.head = None
    def del_after(self , x):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c:
            if c.Data == x:
                if c.next :
                    a = c.next
                    c.next = a.next
                    if a.next:
                        a.next.back = c
                    del a
                    return
                print("error 1")
                return
            c = c.next
            print("not found")
    def del_x(self , x):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c:
            if c.Data == x:
                if c.next is None:
                    self.del_last()
                    return
                c.back.next = c.next
                c.next.back = c.back
                del c
                return
            c = c.next
            print("not found")


#تمرین 1-5


class dnode():
    def __init__(self , x):
        self.Data = x
        self.next = None
        self.back = None


class dlinked_list :
    def __init__(self):
        self.head = None

    def ins_frist(self , x):
        if self.head is None:
            self.head = dnode(x)
        a = dnode(x)
        a.next = self.head
        self.head = a
        a.next.back = a
    def ins_last(self , x):
        if self.head is None:
            self.ins_frist(x)
            return
        c = self.head
        while c.next:
            c = c.next
        a = dnode(x)
        c.next = a
        a.back = c
    def ins_after(self , x ,y):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c :
            if c.Data == x:
                if c.next is None:
                    self.ins_last(y)
                    return
                a = dnode(y)
                a.next = c.next
                c.next = a
                a.next.back = a
                a.back = c
                return
            c = c.next
            print("not found")
    def ins_befor(self , x , y):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c:
            if c.Data == x:
                if c.back is None:
                    self.ins_frist(y)
                    return
                a = dnode(y)
                a.next = c
                c.back.next = a
                a.back = c.back
                c.back = a
                return
            c = c.next
            print("not found")
    def del_first(self):
        if self.head is None:
            print("error")
            return
        c = self.head
        self.head = c.next
        del c
        if self.head:
            self.head.back = None
    def del_last(self):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c.next:
            c = c.next
        if c.back is None:
            self.del_first()
            return
        c.back.next = None
        del c
    def del_befor(self , x):
        if self.head is None:
            print("error")
            return
        if self.head.Data == x:
            print("error")
            return
        c = self.head
        while c :
            if c.Data == x:
                a = c.back
                c.back = a.back
                if a.back:
                    a.back.next = c
                del a
                return
            c = c.next
            print("x not found")


#تمرین 1-6

#node گره
class node :
    def __init__(self , d):
        self.Data = d
        self.next = None




class linked_list :
    def __init__(self):
        self.head = None
    def insert_frist(self , x):
        if self.head == None:
            self.head = node(x)
        else:
            a = node(x)
            a.next = self.head
            self.head = a     
    def insert_last(self , x):
        if self.head is None:
            self.head = node(x)
        else:
            a = node(x)
            c = self.head
            while c.next:
                c = c.next 
            c.next = a
    def insert_after(self , x, y):
        if self.head is None:
            print("list is empty")
        else:
            c = self.head
            while c:
                if c.Data == x:
                    a = node(y)
                    a.next = c.next
                    c.next = a
                c = c.next
            print("not found")
#رفع ایراد
#    def insert_after(self , x, y):
#        if self.head is None:
#            print("list is empty")
#        else:
#            f = True
#            c = self.head
#            while c:
#                if c.Data == x:
#                    a = node(y)
#                    a.next = c.next
#                    c.next = a
#                    f = False
#                c = c.next
#            if flag:
#                print("not found")
    def insert_after(self , x, y):
        if self.head is None:
            print("list is empty")
        else:
            c = self.head
            while c:
                if c.Data == x:
                    a = node(y)
                    a.next = c.next
                    c.next = a
                    return
                c = c.next
            print("not found")    

    def insert_after(self , x, y):
        if self.head is None:
            print("list is empty")
            return
        if self.head.Data == x:
            self.insert_frist(y)
            return
        c = self.head
        while c.next:
                if c.next.Data == x:
                    a = node(y)
                    a.next = c.next
                    c.next = a
                    return
                c = c.next
                print("not found")                      

    def insert_befor(self , x, y):
        if self.head is None:
            print("list is empty")
            return
        if self.head.Data == x:
            self.insert_frist(y)
            return
        while c.next:
            if c.next.Data == x:
                a = node(y)
                a.next = c.next
                c.next = a
                return
            c = c.next
        print("not found")


#تمرین 1-7

class C_Queue:
    def __init__(self, max = 100):
        self.list = [] * max
        self.front = -1
        self.rear = -1
    def  insert(self , x):
        if (self.rear +1) % len(self.list) == self.front:
            print("Queue is full")
            return
        if  self.front == -1:
            self.front = 0
            self.rear = 0
            self.list[0] = x
            return
        self.rear=(self.rear +1) % len(self.list)
        self.list[self.rear] = x
    def delete(self):
        if self.front == -1:
            print("Queue is empty")
            return
        if self.front == self.rear:
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k
        k = self.list[self.front]
        self.front = (self.front +1) % len (self.list)
        return k
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear +1) % len (self.list) == self.front
    
    def show_valid(self):
        if self.rear >= self.front:
            for i in range(self.front , self.rear+1 , 1):
                print(self.list[i])
        else:
            for i in range(self.front , len(self.list) , 1):
                print(self.list[i])
            for i in range(self.rear +1):
                print(self.list[i])

    def show_invalid(self):
        if self.front == -1:
            for i in range(len(self.list)):
                print(self[i])
                return
            i = (self.rear+1) % len (self.list)
            while i != self.front:
                print(self.list[i])
                i = (i +1) % len (self.list)

    def Find(self , x):
        if self.is_empty():
            return
        i = self.front
        if self.list[i] == x:
            return i
        while i != self.rear:
            i = (i +1) % len(self.list)
            if self.list[i] == x:
                return i
            
    def raplace(self , x , y):
        if self.is_empty():
            return
        i = self.front
        if self.list[i] == x:
            self.list[i] = y
        while i != self.rear:
            i = (i +1) % len (self.list)
            if self.list[i] == x:
                self.list[i] = y 


#تمرین 1-8

class Queue:
    def __init__(self ,max = 100):
        self.list=[None]* max
        self.front = -1
        self.rear = -1
    def insert(self,x):
        if self.rear >= len(self.list) -1 :
            print("Queue is Full")
            return
        if  self.front == -1 :
            self.front+= 1 
            self.rear+= 1
            self.list[list.rear] = x
            return
        self.rear+= 1 
        self.list[self.rear] = x
    def Del(self):
        if self.front == -1 :
            print("Queue is empty")
            return     
        if  self.front == self.rear :
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k
        k = self.list[self.front]
        self.front+= 1
        return k
    


test = Queue(3)
test.insert(57)
test.insert(32)
test.insert(44)
test.insert(39) #Queue is Full
test.Del()
test.insert(39) #Queue is Full





class C_Queue:
    def __init__(self, max):
        self.list = [] * max
        self.front = -1
        self.rear = -1
    def  insert(self , x):
        if (self.rear +1) % len(self.list) == self.front:
            print("Queue is full")
            return
        if  self.front == -1:
            self.front = 0
            self.rear = 0
            self.list[0] = x
            return
        self.rear=(self.rear +1) % len(self.list)
        self.list[self.rear] = x
    def delete(self):
        if self.front == -1:
            print("Queue is empty")
            return
        if self.front == self.rear:
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k
        k = self.list[self.front]
        self.front = (self.front +1) % len (self.list)
        return k
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear +1) % len (self.list) == self.front
    


#تمرین 1-9

class stack : 
    def __init__(self , limit = 1000):
        self.st=[]
        self.lim = limit
    def push(self , x):
        if len(self.st) >= self.lim:
           print("stack is full")
           return -1
        self.st.append(x)
    def pop(self):
        if len(self.st) == 0 :
            print("stack is empty")
            return -1
        return self.st.pop()
    def peek(self):
        if len(self.st) == 0 :
            print("stack is empty")
            return -1
        return self.st[-1]
         





test = stack(10)
test.push(57)
test.push(126)
test.push(-10)
k=test.peek()




#"ایندکس(x) های درون پشته را برگرداند."
def find(self,x):
    for i in range(len(self.st)):
        if self.st[i] == x :
           print(i)


#"اولین شامل  (x) را برگرداند"
def find1(self,x):
    for i in range(len(self.st)):
        if self.st[i] == x :
           print(i)
           return


#"اخرین ایندکس شامل (x) را چاپ کند"
def find2(self,x):
    for i in range(len(self.st)-1,-1,-1) :
        if self.st[i] == x :
            print(i)
            return
def find2_n(self,x):
    for i in range(len(self.st)):
        if self.st[i] == x :
            p=i
    print(p)                



def find2_n(self,x):
    list=[]
    for i in range(len(self.st)):
        if self.st[i] == x :
            list.append(i)
    print(list[2])




def replace(self,x,y):
    for i in range(len(self.st)):
        if self.st[i] == x :
            self.st[i]=y


#تمرین 1-10

"تابع پیچیدگی زمانی الگوریتم زیر را محاسبه کنید"
a = 5
for i in range (n):
    p=t
    t=l+6
l = 2 + l

F(n) = 2 n + 2
