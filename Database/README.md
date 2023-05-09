# simple_monitoring_system/Database
簡易モニタリングシステムのdatabaseについて

## Table example
mysqlでログインして、以下のコマンド

```
> use DB_NAME;
> create table mem_use_rate(
    id int auto_increment not null, 
    data_topic varchar(50), 
    data_value float, 
    data_time datetime not null, 
    primary key(id));

> desc mem_use_rate;
    +------------+-------------+------+-----+---------+----------------+
    | Field      | Type        | Null | Key | Default | Extra          |
    +------------+-------------+------+-----+---------+----------------+
    | id         | int         | NO   | PRI | NULL    | auto_increment |
    | data_topic | varchar(50) | YES  |     | NULL    |                |
    | data_value | float       | YES  |     | NULL    |                |
    | data_time  | datetime    | NO   |     | NULL    |                |
    +------------+-------------+------+-----+---------+----------------+
```

## Settings
環境によってはrootを使って問題ないが、、、
ユーザーの作成(パスワード周りがなかなか厄介)、GRANT、外部からの接続ができるようにbind-addressの変更も必要
環境によって設定ファイルの位置が変わるかもしれないが、
自分の環境では/etc/mysql/mysql.conf.d/mysqld.cnf


## Author
[sudo-roa](https://github.com/sudo-roa)