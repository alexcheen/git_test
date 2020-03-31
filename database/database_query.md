#数据库查询
与数据一起工作是SQL数据操作语言(DML)的工作。
DML的核心是select命令。select的很多操作都来源于关系代数，并且包含了关系代数的很多内容。

## 关系操作
以某种概念的方式思考select做什么以及为什么是有用的。大部分SQL实现中，包括SQLite，select语句提供混合、比较和过滤数据的"关系操作"。
  1. 基本操作
   - Restriction限制
   - Projection投影
   - Cartesian Product笛卡尔积
   - Union联合
   - Different差
   - Rename重命名
  2. 附加操作
   - Intersection交叉
   - Natural Join 自然连接
   - Assign 赋值
  3. 扩展操作
   - Generalized Projection广义投影
   - Left Outer Join 左外连接
   - Right Outer Join 右外连接
   - Full Outer Join 全外连接

## select命令与管道操作
```sql
SELECT [DISTINCT] heading FROM tables WHERE predicate GROUP BY columns HAVING predicate ORDER BY columns LIMIT count,offset;
```
