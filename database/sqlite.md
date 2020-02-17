## SQLite 体系结构
sqlite 可以划分为3个子系统的8个独立模块组成。这些模块将查询过程划分为几个独立的任务，流水线工作pipline。在体系结构栈的顶部编译查询语句，在中部执行，在底部处理存储并于操作系统交互。
### 接口
接口位于栈的顶端，由SQLite C API 组成。
### 编译器
编译过程从词法分析器(Tokenizer)和语法分析器(Parser)开始。
SQLite语法分析器时手动编码实现的，由SQLite特定的语法分析生成器Lemon产生的。
### 虚拟机
架构栈的中心部分是虚拟机，即虚拟数据库引擎(Virtual DataBase Engine, VDBE)。VDBE是基于寄存器的VM，在字节码上工作，独立于顶层操作系统、CPU和系统体系结构。
### 后端
后端由B-tree、页缓存(page cache)以及操作系统接口组成。B-tree和pager一起作为信息代理。
B-tree的职责就是排序。它维护多个页之间的复杂关系，用来保证快速定位并找到一切有联系的数据。B-tree将页面组织成树状结构，页面就是树的叶子。pager(SQLite的一种数据结构)帮助B-tree管理页面。
OS接口会根据系统指定如何调用底层系统实现。所有的必须解决的OS问题在OS接口API中以文档的形式记录了。
### 工具和测试代码
工具中包含如内存分配、字符串比较、Unicode转换之类的公共服务。
测试模块中包含了回归测试用例，用来检查数据库代码的每个细节。

### 查询数据
``` sql
sqlite> select * from foods where name='Cinnamon Bobka';
sqlite> select last_insert_rowid();
``` 
### 修改数据
#### 插入记录
``` sql
sqlite> insert into foods (name, type_id) values('Cinnaomon Bobka', 1);
sqlite> insert into foods (NULL, 1, 'Blueberry Bobka');

sqlite> insert into foods
        values(null,
              (select id from food_types where name='Bakery'),
              'Blackberry Bobka');

sqlite> insert into foods
        select last_insert_rowid()+1, type_id, name 
        from foods
        where name='Chocolate Bobka';
```
#### 插入多行数据
``` sql
sqlite> create table foods2(id int, type_id int, name text);
sqlite> insert into foods2 select * from foods;
sqlite> select count(*) from foods2;
``` 
直接指定从select语句中创建表。
``` sql
sqlite> create table foods2 as select * from foods;
``` 
create table 与从foods表选择数据插入表两步并未一步，对于创建临时表特别有用。
``` sql
sqlite> create temp table list as
        select f.name food, t.name name,
               (select count(episode_id)
                from foods_episodes where food_id=f.id) episodes
        from foods f, food_types t
        where f.type_id=t.id;
``` 


#### 更新记录
``` sql
sqlite> update table set update_list where predicate;
``` 
#### 
``` sql
sqlite> delete from table where predicate;
``` 


### 数据完整性
数据完整性用于定义和保护表内部或表之间的数据关系。
一般有四种完整性：
域完整性、实体完整性、引用完整性和用户自定义完整性。
域完整性设计控制字段内的值。实体完整性设计表中的行。
引用完整性设计表之间的行，即外键关系。用户自定义完整新可以包罗万象。

数据完整性是通过约束实现的。约束就是对字段存储值的一种限制措施。数据库会对字段中的存储值进行完整性约束强制实施。
SQLite中，约束还包括对冲突解决的支持。

``` sql
sqlite> create table contacts (
        id integer primary key,
        name text not null collate nacase,
        phone text not null default 'UNKNOWN',
        unique (name,phone));
```
字段级的约束包括not null, unique, primary key, foreign key, check和collate。
表一级约束包括primary key, unique以及check。

#### 主键约束
在SQLite中,不管有没有定义主键,都会有一个字段,rowid,64-bit整性字段,还有两个别名_rowid_和oid, 默认取值按照增序自动生成。
























