# travelApp

> <アプリの説明を追加>

## セットアップ手順

エラーやわからないことがあれば、島川に連絡

1. プロジェクトを保存するフォルダの場所を指定
   コマンドプロンプト(mac)、PowerShell(windows)のアプリケーションを開く
   フォルダを作成するファイルの場所へ移動する
   ・使用するコマンド

   `ls` ... 今いるフォルダの中身を表示

   `cd <フォルダ名>` ... 特定のフォルダへ移動

   `cd ..` ... ルート（最も階層の低い）のフォルダへ移動

2. プロジェクトをクローンする

   ```
   $ git clone https://github.com/NorisukeShadow/travelApp.git
   $ cd travelApp
   ```

3. python で仮想環境を作成
   myvenv という名前の仮想環境を作成し、作成した仮想環境を起動する

   ```
   $ python3 -m venv myvenv
   $ source myvenv/bin/activate
   ```

   `(myvenv)`という表記が出ていたら成功

4. django のインストール

   ```
   $ pip3 install django==4.2.5
   ```

5. アプリケーションをローカルで起動
   ```
   $ python3 manage.py startapp travel
   ```
   成功すると、http から始まる URL が表示される. URL を開くと django のアプリケーションが表示される.

## 2 回目以降の起動

```
$ cd プロジェクトへのパス
$ source myvenv/bin/activate
$ python manage.py runserver
```

## pip ライブラリ

`pip list`でライブラリを確認

```
Package            Version
------------------ -------
asgiref            3.7.2
backports.zoneinfo 0.2.1
Django             4.2.5
pip                23.2.1
setuptools         41.2.0
sqlparse           0.4.4
typing_extensions  4.7.1
```
