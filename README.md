# Djangoのdjangorestframeworkを使ってAPIを作成

# 初期設定
##ツールの導入
anaconda,pyCharmをインストール

## anacondaナビゲーターで仮想環境を作る
Environmentsを選択,createで新規仮想環境を作成

Openterminalでターミナルを立ち上げ
pip install Django
pip install djangorestframework

## プロジェクトを作成
フォルダを作成する
pyCharmから作成したフォルダをオープン

## pycharmから仮想環境を紐付けする
pyCharm > Preferences > project/python interpreter
歯車マーク(add) > Existing の...をクリック
users/user名/opt/Anaconda3/envs/仮想環境名/din/pythonを選択

## 仮想環境に入っているか確認
ターミナルを開いて、(仮想環境名)が表示されていればOK

# Djangoプロジェクトを作っていく
ターミナルで「django-admin startproject プロジェクト名 .」を実行

## アプリケーションの作成
今回はAPIを作成する<br>
django-admin startapp api<br>
フォルダに作成したプロジェクトとアプリケーションのファイルが作成される

## ローカル環境立ち上げ
manage.pyファイルを実行すると右上にmanageが追加される
右上にあるmanageをクリックしてEdit Configuraionsを選択し
parameters箇所へ「runserver」と記載し
▶️をクリックし、ローカルホストへアクセス
ストップ時は■をおす

## プロジェクトの設定
api/drfapi/settings.pyを編集する<br>
INSTALLED＿APPSへ必要パッケージを記載
'rest_framework',<br>
'rest_framework.authtoken',　登録用　<br>
'api.apps.ApiConfig',       自作API<br>
.で繋いでパスを指定している
api/apps/ApiConfigを指定している

### タイムゾーンの変更
settings.pyのTimeZoneをAsia/Tokyo
へ変更

### モデルの作成
api/modelsへ記載
モデルを作成したらadmin.pyへモデルをインポートする

### DB作成
ターミナルで以下を実行し、マイグレーションファイルを作成する<br>
python manage.py makemigrations <br>
マイグレーション実行「python manage.py migrate」

### superユーザーの作成
python manage.py createsuperuser
user名を決める
Emailはblankでも問題ない
パスワードを設定する（簡単なものだと警告がでる、ローカルの場合それでも問題なし）
今回はadminuser

### admin画面へアクセス
djangoのローカル環境のURLに/adminでアクセスすると
ログイン画面へアクセスできる
そこで設定したsuperユーザーでアクセスすると作成したDBが確認できる

## シリアライザー
#### 役割
パスワードをハッシュ化したり  
DBのモデル値を適正な物で返すことができる

