
# シリアライザーのインポート
from rest_framework import serializers
# 作ったTaskモデルをインポート
from .models import Task
# ユーザーモデルはDjangoでデフォルトで用意されているものをインポート
from django.contrib.auth.models import User
# トークンを扱うためにrest_frameworkからインポートする
from rest_framework.authtoken.models import Token

# ユーザーモデルに対してシリアラザーを作る
# ()の中に継承するものを記載する
class UserSerializer(serializers.ModelSerializer):
    # Class
    class Meta:
        # Usermodelを割り当てる
        model = User
        # レスポンスで表示する値を記載
        fields = ("id", "username", "password")
        # requiredは必須判定
        # write_onlyはSerializerから値を入れるが、読み出しはしたくない場合の値に設定する（個人情報関連データ）
        # ※入力専用のフィールドかをBooleanで判定
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    #  ユーザーを作る際のメソッドをオーバーライド
    # パスワードをハッシュかして登録するためのメソッドを作る
    def create(self, validated_data):
        # ハッシュしたデータをDBへ登録する
        user = User.objects.create_user(**validated_data)
        # 新規登録する際にトークンを作る
        Token.objects.create(user=user)
        return user

# Taskモデル用のシリアライザー
class TaskSerializer(serializers.HyperlinkedModelSerializer):

    # Djangoのデータタイムをシンプルに表示するためのフォーマット
    created_at = serializers.DateTimeField(format="%Y-%m-%d %h:%M", read_only=True)
    update_at = serializers.DateTimeField(format="%Y-%m-%d %h:%M", read_only=True)

    class Meta:
        # モデルの割り当て
        model = Task
        # 入力する値を指定
        fields = ["id", "title", "created_At", "updated_at"]