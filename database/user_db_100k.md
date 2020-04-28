# һ�����ݿ�100K�����ƽ��������
## 1. ��ϵͳ��sysinf������ֶ� 'record_num'�� ������¼�򿨱�ļ�¼������
```sql
insert into sysinfo (key,value) VALUES('record_num',0);
```
## 2. ����2����������ά�� record_num ��������ʵ������ƥ�䣺
### A: ��¼ɾ��ʱ record_num ��һ
```sql
CREATE TRIGGER checkin_del_log after delete on checkin
BEGIN
	update sysinfo set value=(select value from sysinfo where key='record_num')-1 where key='record_num';
END
```
### B: ��¼����ʱ record_num ��һ
```sql
CREATE TRIGGER checkin_ins_log after insert on checkin
BEGIN
	update sysinfo set value=(select value from sysinfo where key='record_num')+1 where key='record_num';
END
```
## 3. �ڸ��� record_numʱ�ж��Ƿ񳬹���������������ƽ���ɾ����ɵļ�¼(����500ֻ��ʾ�⣩
```sql
CREATE TRIGGER checkin_max_a after update on sysinfo
WHEN
	new.key='record_num' AND new.value>500
BEGIN
	delete from checkin where check_in_time in (select check_in_time from checkin order by check_in_time limit 500,1);
END
```
�˴�Ӧ��checkin���check_in_time�����������Լӿ������ٶȡ�
```sql
CREATE INDEX checkin_500 on checkin (check_in_time);
```

## 4. ���Խ���¼��ɾ�����̱��������� ���ڵ��ԡ�
### A:������
```sql
CREATE TABLE del_record_log
        (id integer PRIMARY key, userid not null,
        timestamp not null ,
        del_time not null default (datetime(CURRENT_TIMESTAMP,'localtime')))
```
### B:����������
```sql
CREATE TRIGGER checkin_del_backup after delete on checkin
BEGIN
	insert into del_record_log (userid, timestamp) VALUES(old.userid, old.check_in_time);
END
```

## P.S.
��Ҫ��checkin������������ϳ���ӿ���ң���������Ϊ(userid, check_in_time)
```sql
CREATE UNIQUE INDEX checkin_query on checkin (userid, check_in_time);
```

# ���� ����
�����ݿ�ִ�����½ű�
## ��Ҫ�ű�

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
## ���ӽű�
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
# ��¼5K������
## ��ϵͳ����ά�������ļ�¼
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
## ʹ�ô��������Ա�ļ�¼������������
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
1. ��������������ʱ����¼�������һ��ҪΪINTERGER�����ΪTEXT������δ֪����
2. һ��Ҫע�� LIMIT�Ӿ���﷨�� [LIMIT cnt offset|LIMIT offset,cnt].
