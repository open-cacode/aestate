# 缓存篇

## 缓存策略

- 当内存满足系统运行内存的1/10时,满足最大限度数据内容,保证数据完整性的同时保留数据

- 当单次查询数据大于阈值时,保留数据并不在扩大缓存空间,数据完整保留,但不再清理,直到处于第二缓存空间更多查询数据量再次大于阈值时清理

- 当通过aestate改变数据时记录数据变更信息,并重新将数据写入缓存,移除旧缓存数据,这将意味着非通过aestate修改的数据不可被检测到

- 扩容策略:当前内存>=当前容量1/2时,重新计算查询数据量

- 流量计算方式:当前缓存大小 + (当前缓存大小 / 上次扩容时间至当前时间段内插入的新内容数量) * 2 * 当前缓存大小

- 移除方案:时间段内缓存查询次数最少内存最大优先,当 (A次数-B次数) * 10 <= (A占用内存-B占用内存),优先删除B

# 缓存的优势

在多次查询中能够提升`3-12`倍（测试封顶12倍）以上的速度，对于数据量极其庞大的查询有着明显的提升效果

对于经常CRUD来说缓存系统能够发挥最大的功效，而不是每次都在苦苦等待

# 缓存的劣势

如果你不 是使用`Aestate`自带的方式插入数据时， 那么系统获取不到数据库的实时信息

数据更新不及时，对于分布式应用来讲，缓存并不能提供很大的帮助，甚至还会造成一系列的麻烦

# 解决方案

1.提供内置关闭缓存的开关，使用

```Python
from aestate.work.Cache import SqlCacheManage, CacheStatus

# 关闭缓存
SqlCacheManage.status = CacheStatus.CLOSE
# 开启缓存
SqlCacheManage.status = CacheStatus.OPEN
```

在不需要缓存的地方关闭缓存，结束之后再次开启缓存

2.使用Redis作为缓存
