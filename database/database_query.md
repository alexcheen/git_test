# SQL 简要语
SQL分为两个部分： 数据操作语言DML 和数据定义语言DDL  
 1.  DML 语言部分
  - SELECT - 从数据库中获取数据
  - UPDATE - 更新数据库表中的数据
  - DELETE - 从数据库中删除数据
  - INSERT INTO - 向数据库中插入数据
 2.  DDL 语言部分 
  - CREATE DATABASE -创建新数据库
  - ALTER DATABASE - 修改数据库
  - CREATE TABLE - 创建表
  - ALTER TABLE - 变更数据库表
  - DROP TABLE - 删除表
  - CREATE INDEX - 创建索引
  - DROP INDEX - 删除索引

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

## LIKE与GLOB操作符
LIKE的作用与相等类似，都是通过一个模式来进行字符串匹配的。
'%'用来匹配任意多个字符，'_'匹配任意单个字符内容。
另一个有用的方式是用NOT来否定某些模式。
```sql
select * from table where name like '%acp%' and name not like'%Sch%;
```


