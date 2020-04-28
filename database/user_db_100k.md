# 一、数据库100K条限制解决方案：
## 1. 在系统表sysinf内添加字段 'record_num'， 用来记录打卡表的记录条数；
```sql
insert into sysinfo (key,value) VALUES('record_num',0);
```
## 2. 创建2个触发器来维护 record_num 的数量与实际数量匹配：
### A: 记录删除时 record_num 减一
```sql
CREATE TRIGGER checkin_del_log after delete on checkin
BEGIN
	update sysinfo set value=(select value from sysinfo where key='record_num')-1 where key='record_num';
END
```
### B: 记录插入时 record_num 加一
```sql
CREATE TRIGGER checkin_ins_log after insert on checkin
BEGIN
	update sysinfo set value=(select value from sysinfo where key='record_num')+1 where key='record_num';
END
```
## 3. 在更新 record_num时判断是否超过限制量，如果限制进行删除最旧的记录(这里500只做示意）
```sql
CREATE TRIGGER checkin_max_a after update on sysinfo
WHEN
	new.key='record_num' AND new.value>500
BEGIN
	delete from checkin where check_in_time in (select check_in_time from checkin order by check_in_time limit 500,1);
END
```
此处应对checkin表的check_in_time加上索引，以加快运行速度。
```sql
CREATE INDEX checkin_500 on checkin (check_in_time);
```

## 4. 可以将记录的删除过程保存下来， 便于调试。
### A:创建表
```sql
CREATE TABLE del_record_log
        (id integer PRIMARY key, userid not null,
        timestamp not null ,
        del_time not null default (datetime(CURRENT_TIMESTAMP,'localtime')))
```
### B:建立触发器
```sql
CREATE TRIGGER checkin_del_backup after delete on checkin
BEGIN
	insert into del_record_log (userid, timestamp) VALUES(old.userid, old.check_in_time);
END
```

## P.S.
需要在checkin表建立索引以配合程序加快查找，联合索引为(userid, check_in_time)
```sql
CREATE UNIQUE INDEX checkin_query on checkin (userid, check_in_time);
```

# 二、 方法
对数据库执行以下脚本
## 必要脚本

```sql
insert into sysinfo (key,value) VALUES('record_num',0);
CREATE TRIGGER checkin_del_log after delete on checkin
BEGIN
	update sysinfo set value=(select value from sysinfo where key='record_num')-1 where key='record_num';
END;
CREATE TRIGGER checkin_ins_log after insert on checkin
BEGIN
	update sysinfo set value=(select value from sysinfo where key='record_num')+1 where key='record_num';
END;
CREATE TRIGGER checkin_max_a after update on sysinfo
WHEN
	new.key='record_num' AND new.value>500
BEGIN
	delete from checkin where check_in_time in (select check_in_time from checkin order by check_in_time limit 500,1);
END;
CREATE INDEX checkin_500 on checkin (check_in_time);
```
## 附加脚本
```sql
CREATE TABLE del_record_log
        (id integer PRIMARY key, userid not null,
        timestamp not null ,
        del_time not null default (datetime(CURRENT_TIMESTAMP,'localtime')));
CREATE TRIGGER checkin_del_backup after delete on checkin
BEGIN
	insert into del_record_log (userid, timestamp) VALUES(old.userid, old.check_in_time);
END;
CREATE UNIQUE INDEX checkin_query on checkin (userid, check_in_time);
```
# 记录5K条限制
## 在系统表内维护数量的记录
```sql
CREATE TRIGGER person_del_log after delete on employee
BEGIN
    update sysinfo set value=(select value from sysinfo where key='person_num')-1 where key='person_num';
END;
CREATE TRIGGER person_ins_log after insert on employee
BEGIN
    update sysinfo set value=(select value from sysinfo where key='person_num')+1 where key='person_num';
END;
```
## 使用触发器来对表的记录数量进行限制
```sql
CREATE TRIGGER person_max_5k before insert on employee
BEGIN
    SELECT CASE
	when (select value from sysinfo where key='person_num')>=5
	THEN
	RAISE(ABORT, 'employee 5k')
	end;
END;
```

## important note
1. 建立触发器计数时，记录项的类型一定要为INTERGER，如果为TEXT会引起未知错误。
2. 一定要注意 LIMIT子句的语法， [LIMIT cnt offset|LIMIT offset,cnt].
