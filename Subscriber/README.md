# simple_monitoring_system/Subscriber
簡易モニタリングシステムのsubscriber<br>
cloneしたリポジトリのSubscriberディレクトリをお使いください。

## Overview
pythonライブラリのpaho-mqttを利用したデータのsubscribeのサンプル。<br>
PublisherからBrokerに送信されたデータをsubscribeするので、今回はPublisherのサンプルコードにあわせてメモリ使用率とハードウェア温度をsubscribeします。<br>
subscribe後はデータベースにデータを追加します。<br>

## Settings
設定は以下の3項目のみ
1. .envファイルの作成
2. .envファイルの記述例
    ```
    # MQTT
    MQTT_BROKER="localhost"
    MQTT_PORT="1883"
    # MySQL
    SQL_HOST="ホスト名"
    SQL_USER="ユーザ名"
    SQL_PASSWORD="パスワード"
    SQL_DB="データベース名"
    ```

## Database
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
... 

# publishと違いsubsucribeするトピック名を登録する必要がある
def on_connect(client, userdata, flag, rc):
  print("Connected with result code " + str(rc))
  client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
  # mqttのメッセージはmsgの中にtopicとpayloadとして格納されている
  topic = msg.topic # topic名
  raw_data = str(msg.payload) # メッセージ本体
  data = raw_data.replace("b","").replace("'","") # 必要部分の切り出し
  print("[", topic, "]", data)
  set_mysql(topic, data) # メッセージを受け取るごとにデータベースへデータをinsert

def set_mysql(topic, data):
  connection = pymysql.connect(host = SQL_HOST, user = SQL_USER, password = SQL_PASSWORD, db = SQL_DB, charset='utf8', cursorclass=pymysql.cursors.DictCursor) # データベースへの接続
  with connection.cursor() as cursor:
    sql = "INSERT INTO `hw_temp`(data_topic, data_value, data_time) VALUES (%s, %s, %s)"
    r = cursor.execute(sql, (topic, float(data), datetime.now().strftime( '%Y-%m-%d %H:%M:%S' )))
    connection.commit()


# publishとほとんど同じだけど、subscribeはloop_forever()のみ。
def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message # メッセージ受信時コールバック関数の設定
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever() # clientの起動

...
```

## Author
[sudo-roa](https://github.com/sudo-roa)
