class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.isLeaf = False
        self.assoc =[]

class PointDatabase():
 def __init__(self,pointlist):
     self.dtree=self.ConstructRangeTree2d(sorted(pointlist),True)
 def searchNearby(self,q,d):
     return self.SearchRangeTree2d(self.dtree,q[0]-d,q[0]+d,q[1]-d,q[1]+d,2)
     
 def ConstructRangeTree2d1(self,data, enable=True):
    if not data:
        return None
    if len(data) == 1:
        node = Node(data[0])
        node.isLeaf = True
    else:
        mid_val = len(data)//2
        node = Node(data[mid_val])
        node.left = self.ConstructRangeTree2d1(data[:mid_val], enable)
        node.right = self.ConstructRangeTree2d1(data[mid_val+1:], enable)
    return node
 def ConstructRangeTree2d(self,data,enable):
    datatree=self.ConstructRangeTree2d1(data,True)
    self.concatdata(datatree)
    return datatree
 def merge(self,test_list1,test_list2):
    size_1 = len(test_list1)
    size_2 = len(test_list2)
    res = []
    i, j = 0, 0
  
    while i < size_1 and j < size_2:
     if test_list1[i][1] < test_list2[j][1]:
      res.append(test_list1[i])
      i += 1
  
     else:
      res.append(test_list2[j])
      j += 1
  
    res = res + test_list1[i:] + test_list2[j:]
    return res   
 def concatdata(self,treeroot):
    if treeroot==None:
        return []
    if treeroot.isLeaf:
        treeroot.assoc=[treeroot.value]
        return treeroot.assoc
    else:
        a=self.concatdata(treeroot.left)
        b=self.concatdata(treeroot.right)
        treeroot.assoc=self.merge(a,b)
        treeroot.assoc.insert(self.find1(treeroot.assoc,treeroot.value),treeroot.value)
        return treeroot.assoc
    

 def withinRange(self,point, rangev , check):
    if check == 1:
        x = point
        if (x >= rangev[0][0]  and x <= rangev[0][1] ) :
            return True
        else:
            return False
    elif check == 2:
        x = point[0]
        y = point[1]

        if (x >= rangev[0][0]   and x <= rangev[0][1]  and y >= rangev[1][0]  and y <= rangev[1][1] ) :
            return True
        else:
            return False

 def getValue (self,point, enable, dim ):
    if dim == 1:
        value = point.value
    elif dim == 2:
        if enable:
            value = point.value[0]
        else:
            value = point.value[1]
    return value

 def FindSplitNode(self,root, p_min , p_max, dim, enable ):
    splitnode = root
    while splitnode != None:
        node = self.getValue(splitnode, enable, dim)
        if p_max < node:
            splitnode = splitnode.left
        elif p_min > node:
            splitnode = splitnode.right
        elif p_min <= node <= p_max :
            break
    return splitnode
 def find(self,arr,K):
     start = 0
     end =len(arr)-1
     while start<= end:
        mid =(start + end)//2
        if arr[mid][1] == K:
            return mid
        elif arr[mid][1] < K:
            start = mid + 1
        else:
            end = mid-1
     return end + 1
 def find1(self,arr,K):
     start = 0
     end =len(arr)-1
     while start<= end:
        mid =(start + end)//2
        if arr[mid][1] == K[1]:
            return mid
        elif arr[mid][1] < K[1]:
            start = mid + 1
        else:
            end = mid-1
     return end + 1   
 def SearchRangeTree1d (self,data, p1, p2):
    a=self.find(data,p1)
    b=self.find(data,p2)
    if b<len(data) and data[b][1]<=p2:
        return data[a:b+1]
    else:
        return data[a:b]

 def SearchRangeTree2d (self,tree, x1, x2, y1, y2, dim ):
    results = []
    splitnode = self.FindSplitNode(tree, x1, x2, 2, True)
    if (splitnode == None):
        return results
    elif splitnode.isLeaf:
        if self.withinRange(splitnode.value, [(x1, x2), (y1, y2)], 2):
          results.append(splitnode.value)      
    
    else:
        if self.withinRange(splitnode.value, [(x1, x2), (y1, y2)], 2):
          results.append(splitnode.value) 
        if splitnode.left!=None:
         v=splitnode.left
         while True:
            if x1<=v.value[0]:
                if self.withinRange(v.value, [(x1, x2), (y1, y2)], 2):
                      results.append(v.value) 
                if v.right!=None:
                  results+=self.SearchRangeTree1d(v.right.assoc,y1,y2)
                if v.left!=None: 
                  v=v.left
                else:
                    break
            else:
                if v.right!=None:
                 v=v.right
                else:
                    break
                
                
        if splitnode.right!=None:        
         v=splitnode.right
         while True: 
            if v.value[0]<=x2:
                if self.withinRange(v.value, [(x1, x2), (y1, y2)], 2):
                      results.append(v.value)
                if v.left!=None:      
                   results+=self.SearchRangeTree1d(v.left.assoc,y1,y2)
                if v.right!=None:   
                  v=v.right
                else:
                    break
            else:
                if v.left!=None:
                    v=v.left
                else:
                    break
    return results        
