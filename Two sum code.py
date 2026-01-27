def two_sum(num,target):
    x=0
    l=len(num)
    while x<l:
        z=x+1
        while z<l:
            if num[x]+num[z]==target:
                return [x,z]
            z+=1
        x+=1
    return []    
list1=[2,7,12,15]
target=9
print(two_sum(list1,target))

def twosum(nums,target):
    index=0
    m={}
    for val in nums:
        res=target-val
        if res in m:
            return [m[res],index]
        m[val]=index
        index+=1
    return []
list1=[2,7,12,15]
target=9
print(twosum(list1,target))
+';l89`     `'