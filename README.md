# sword-to-offer
1.顺序二维数组中的查找：二叉搜索树
将数组逆时针旋转45°
“根节点” 对应的是矩阵的 “左下角” 和 “右上角” 元素，本文称之为 标志数 ，以 matrix 中的 左下角元素 为标志数 flag ，则有:

若 flag > target ，则 target 一定在 flag 所在 行的上方 ，即 flag 所在行可被消去。
若 flag < target ，则 target 一定在 flag 所在 列的右方 ，即 flag 所在列可被消去。

rows = len(matrix) # Height行数
columns = len(matrix[0]) # Width列数

2.排序数组中的搜索问题，首先想到 二分法 解决。

3.二分函数：注意内置函数参数名！！！不要写成了外函数的变量名。

4. a =set() #创建集合
a.add() #集合添加数据
a.remove(2) #删除数字2
a.discard("mei") #删除, 即使这个元素不存在，也不会报错
a.pop() #随机删除一个元素

a= {} #创建字典
a["wohnen"]="stauffenberg" #字典添加数据
del a["name"] #删除某个键及其对应的数据

5.数组重新排序，并倒序：
newlist = sorted(nums, reverse=True) 构造新序列
nums.sort(reverse =True) 原序列直接排序

A.sort(reverse=True)
for i in range(len(A)-2):
if A[i]<A[i+1]+A[i+2]:
return A[i]+A[i+1]+A[i+2]
return 0

6.<< 左移 *      # 3 <<4 就是3* 2^4

>> 右移 /        # 3>>4 就是 3/ (2^4)

按位与运算符（&）
定义：参加运算的两个数据，按二进制位进行"与"运算。

运算规则：

0&0=0 0&1=0 1&0=0 1&1=1
总结：两位同时为1，结果才为1，否则结果为0。

例如：3&5 即 0000 0011& 0000 0101 = 0000 0001，因此 3&5 的值得1。

注意：负数按补码形式参加按位与运算。

7.str.join(sequence)
例如：
s= ("we", "a", "e")
“-”.join(s) #we-a-e

"".join(s) #weae

s.replace(" ", "%20") #替换

8.深拷贝 deepcopy()

浅拷贝 =

9.哈希表： 复制复杂链表
class Solution:
def copyRandomList(self, head: 'Node') -> 'Node':
if not head: return
dic = {}
# 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
cur = head
while cur:
dic[cur] = Node(cur.val)
cur = cur.next
cur = head
# 4. 构建新节点的 next 和 random 指向
while cur:
dic[cur].next = dic.get(cur.next)
dic[cur].random = dic.get(cur.random)
cur = cur.next
# 5. 返回新链表的头节点
return dic[head]

10.list[::-1] 逆序打印列表

list = [1,2,3,4,5,6]

list[3::-1] #[4,3,2,1]
