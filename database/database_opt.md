<!--
 * @Author: Alex Cheen
 * @Date: 2020-05-18 17:23:56
 * @LastEditTime: 2020-05-18 17:50:00
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \undefinedd:\git\git_test\database\database_opt.md
--> 
# select子句中尽量避免使用*
1. 取出表中的所有字段，不论该字段的数据对调用的应用程序是否有用.
2. 表的结构在以后发生了改变，那么SELECT * 语句可能会取到不正确的数据甚至是出错。
3. SELECT * 语句将不会使用到覆盖索引，不利于查询的性能优化。
4. 文档角度来看，SELECT * 语句没有列明将要取出哪些字段进行操作

# where子句比较符号左侧避免函数
尽量避免在where条件子句中，比较符号的左侧出现表达式、函数等操作。因为这会导致数据库引擎进行全表扫描，从而增加运行时间。
1. where 成绩 + 5 > 90 （表达式在比较符号的左侧）(ugly)
2. where 成绩 > 90 – 5（表达式在比较符号的右侧）(ok)
   
# 尽量避免使用or
or同样会导致数据库进项全表搜索。

# 使用limit子句限制返回的数据行数
如果前台只需要显示15行数据，而你的查询结果集返回了1万行，那么这适合最好使用limit子句来限制查询返回的数据行数。