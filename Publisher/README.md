# simple_monitoring_system/Publisher
簡易モニタリングシステムのpublisher<br>
cloneしたリポジトリのPublisherディレクトリをお使いください。

## Overview
pythonライブラリのpaho-mqttを利用したデータのpublishのサンプル。<br>
~~今回は簡単に定期的なデータを取得するために/proc/statからのcpuの情報をとってみようかなと思ったけど、ちょっとめんどくさそう。。。~~ <br>
メモリの使用率とPC温度でとりあえずのサンプルを作りました。<br>
ハードウェアとOSの互換性(ドライバの有無等)によってセンサデータを取得できないこともあります。

## Settings
設定は以下の3項目のみ
1. .envファイルの作成
2. .envファイルの記述例
    ```
    MQTT_CLIENT="localhost"
    MQTT_PORT=1883
    ```
3. pub_*.pyファイル内のMQTT_TOPICとDATA_PATHの変更

## Sample code Description
```python
    client = mqtt.Client() #mqttクライアントのインスタンス作成
    client.on_connect = on_connect # 接続時コールバック関数の設定
    client.on_disconnect = on_disconnect # 切断時コールバック関数の設定
    client.on_publish = on_publish # パブリッシュ時コールバック関数の設定

    client.connect(MQTT_CLIENT, MQTT_PORT, 60) # 接続設定(Brokerのホスト名, ポート, キープアライブ)
    client.loop_start() # clientの起動

    while True: # ループ
        client.publish(MQTT_TOPIC, calc_mem_use_rate()) # publish関数(トピック, メッセージ)
        sleep(30) # 30秒間のsleep
```

### Get memory use rate
ubuntu16以降であれば/proc/meminfoの中のMemTotalとMemAvailableを参照すれば計算できる
$$ Memory Use Rate = MemAvailable ÷ MemTotal $$
計算する前の生データを送信するべきなのかどうかという議論はおいておいて...<br>
メモリ使用率はこれで計算できます。

```python
def calc_mem_use_rate():
    with open(DATA_PATH) as f: # meminfoファイルを開く
        for line in f:
            if("MemTotal" in line):
                mem_total = int(line.split()[1])
            if("MemAvailable" in line):
                mem_available = int(line.split()[1])
    return ((mem_total - mem_available) / mem_total)
```


### Get PC temperature
`/sys/class/thermal/thermal_zone`, `/sys/class/hwmon` 等々から温度を引っ張り出して来るといいと思います。
今回は/sys/class/thermal/thermal_zone0/tempを使ってグラフに出力しています。

```python
def get_hw_temp():
    with open(DATA_PATH+"type") as f: # thermal_zone*/typeファイルを開く
        data_type = f.read()
    with open(DATA_PATH+"temp") as f: # thermal_zone*/tempファイルを開く
        data_temp = f.read()
    return (int(data_temp)/1000) # ℃で表せる正しい値に修正
```


## Errors
publishしてすぐにpythonファイルの実行が終わると、publishされないことがある。
publish後すぐにファイルの実行が終わらないようにsleepなんかを入れるといいかも？

## Reference
- [man proc](https://man7.org/linux/man-pages/man5/proc.5.html)
- [sysfs-class-thermal](https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-thermal)


## Author
[sudo-roa](https://github.com/sudo-roa)
