缓存的三种算法     
- LRU    
    - Least Recently Used，最近最久未使用算法，在很多分布式缓存系统（Redis, Memcached）中广泛使用      
    - 如果一个数据在最近一段时间没有被访问到，那么可以认为在将来它被访问的可能性也很小。因此，当空间满时，**最久没有访问的数据**最先被置换（淘汰）
  
  - 算法描述：
    设计一种数据结构，构造时确定大小，假设大小为k，有两个功能：
    - set(key, value)：将记录 (key, value) 插入该结构，缓存满时，将最久未使用的数据淘汰掉
    - get(key)：返回key 对应的value值
  - 实现

- LFU     
    - Least Frequently Used ，最近最少使用算法   
    - 如果一个数据在最近一段时间没有被访问到，那么可以认为在将来它被访问的可能性也很小。因此，当空间满时，**最小频率的没有被访问的数据**最先被置换（淘汰）   
  
  - 算法描述：
    设计一种数据结构，构造时确定大小，假设大小为k，有两个功能：
    - set(key, value)：将记录 (key, value) 插入该结构，缓存满时，将访问频率最低的数据淘汰掉
    - get(key)：返回key 对应的value值

- FIFO     
    First In First Out，先进先出的队列


