# simple_monitoring_system/Publisher
簡易モニタリングシステムのpublisher
cloneしたリポジトリのPublisherディレクトリをお使いください。

## Overview
pythonライブラリのpaho-mqttを利用したデータのpublishのサンプル
今回は簡単に定期的なデータを取得するために/proc/statからのcpuの情報をとってみようかなと思ったけど、ちょっとめんどくさそう。。。
メモリの使用率でとりあえずのサンプルを作ります。

## Settings
1. .envファイルの作成
2. 

## errors
publishしてすぐにpythonファイルの実行が終わると、publishが終わらずに修了してしまう？
0.1秒のsleepだけで安定してpublishできた。