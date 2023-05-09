# simple_monitoring_system/Subscriber
簡易モニタリングシステムのsubscriber<br>
cloneしたリポジトリのSubscriberディレクトリをお使いください。

## Overview
pythonライブラリのpaho-mqttを利用したデータのsubscribeのサンプル。<br>
PublisherからBrokerに送信されたデータをsubscribeするので、今回はPublisherのサンプルコードにあわせてメモリ使用率とハードウェア温度をsubscribeします。<br>
subscribe後はデータベースにデータを追加します。<br>

## Settings

## データベース
テーブル構造はこんな感じで。センサーの種類ごとにテーブル分けするのが一番いいんかな？
data_valueのデータ型が違うと困るしね。

|Field|Type|Null|Key|Default|Extra|
|--|--|--|--|--|--|
|ID|int|NO|PRI|NULL|auto_increment|
|data_topic|varchar(50)|YES| |NULL||
|data_value|float|YES| |NULL||
|data_time|datetime|NO| |NULL||

テーブル作成のコマンド等は[Database/README.md](../Database/README.md)を参照

## Sample code Description
```python

```





## Reference
- hoge
- huga

## Author
[sudo-roa](https://github.com/sudo-roa)
