class Heap(): 
 def parent(self, j):
  return (j-1)// 2

 def left(self, j):
  return 2*j+1

 def right(self, j):
  return 2*j+2

 def _has_left(self, j):
  return self.left(j)<len(self._data) 

 def _has_right(self, j):
  return self.right(j)<len(self._data)

 def _swap(self, i, j):
  self._data[i], self._data[j] = self._data[j], self._data[i]

 def _upheap(self, j):
  parent = self. parent(j)
  if j > 0 and self._data[j] < self._data[parent]:
   self._swap(j, parent)
   self._upheap(parent) 

 def _downheap(self, j):
  if self. _has_left(j):
   left = self.left(j)
   small_child = left 
   if self._has_right(j):
    right = self.right(j)
    if self._data[right] < self._data[left]:
     small_child = right
   if self._data[small_child] < self._data[j]:
    self._swap(j, small_child)
    self._downheap(small_child)
 def __init__ (self):
   self. _data = []

 def __len__ (self):
   return len(self._data)

 def heappush(self,value):
   self._data.append(value)
   self._upheap(len(self._data)-1)

 def heappop(self):
  self._swap(0, len(self._data)-1)
  item = self._data.pop() 
  self._downheap(0) 
  return (item)   

 def is_empty(self):
     return self._data==[]

def operator(l,m):
    if m[2]-l[2]>=0:
        return -1
    else:
        if l[3]==m[3]:
            return (l[3]+(m[1]-l[1])/(l[2]-m[2]))
        elif l[3]>m[3]:
            return(operator(l,[m[0],m[1]+m[2]*(l[3]-m[3]),m[2],l[3]]))
        else:
            return(operator([l[0],l[1]+(m[3]-l[3])*l[2],l[2],m[3]],m))

def collider(t,i,L):
    l,m=L[i],L[i+1]
    if l[3]==m[3]:
        r1=(l[0]-m[0])/(l[0]+m[0])
        r2=m[0]/(l[0]+m[0])
        r3=l[0]/(l[0]+m[0])
        v1=r1*l[2]+2*r2*m[2]
        v2=2*r3*l[2]-r1*m[2]
        l[1]=l[1]+(t-l[3])*l[2]
        m[1]=m[1]+(t-m[3])*m[2]
        l[2]=v1
        m[2]=v2
        m[3]=l[3]=t
        return(round(t,4),i,round(l[1],4))
    elif l[3]>m[3]:
            L[i+1]=[m[0],m[1]+m[2]*(l[3]-m[3]),m[2],l[3]]
            return collider(t,i,L)
            
    else:
            L[i]=[l[0],l[1]+(m[3]-l[3])*l[2],l[2],m[3]]
            return collider(t,i,L)
        
def listCollisions(M,x,v,m,T):
    op=Heap()
    lis=[]
    maintainer=[-1]*(len(M)-1)
    for i in range(len(M)):
        lis.append([M[i],x[i],v[i],0])
    count=1    
    for i in range(len(M)-1):
        h=operator(lis[i],lis[i+1])
        if h!=-1:
          op.heappush((h,i,count))
          maintainer[i]=(h,count)
          count+=1
    f=0
    ans=[]
    t=0
    while f<m:
        if op.is_empty():
            break
        k1=op.heappop()
        t=k1[0]
        if t>T:
            break
        if maintainer[k1[1]]!=-1:
            if k1[2]==maintainer[k1[1]][1]:
                h=collider(k1[0],k1[1],lis)
                maintainer[k1[1]]=-1
                ans.append(h)
                f+=1
            else:
                continue
        else:
                continue       
        if k1[1]>=1:
            r1=operator(lis[k1[1]-1],lis[k1[1]])
            if r1!=-1 :
               rx1=(r1,k1[1]-1,count) 
               op.heappush(rx1)
               maintainer[rx1[1]]=(rx1[0],rx1[2])               
               count+=1
            else:
                maintainer[k1[1]-1]=-1
        if k1[1]<=len(lis)-3:
         r2=operator(lis[k1[1]+1],lis[k1[1]+2])
         if r2!=-1 :
              rx2=(r2,k1[1]+1,count)
              op.heappush(rx2)
              maintainer[rx2[1]]=(rx2[0],rx2[2])
              count+=1
         else:
             maintainer[k1[1]+1]=-1
    return(ans)    
