# ハピネスチャージャー
[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2020/09/JPHACKS2020_ogp.jpg)](https://www.youtube.com/watch?v=G5rULR53uMk)
## 製品概要
### 背景(製品開発のきっかけ、課題等)
COVID-19の影響で、自宅での生活が増えました。その影響により、鬱気味になったりストレスが溜まりやすくなったりしたという声を聞きます。また、ストレスを発散せずに、頑張りすぎるのが日本人の性質としてあります。そこで、私たちは、手軽にストレスを解消してもらうために,ストレス度合いに応じて,ご褒美を提案するアプリを開発しました。
### 製品説明(具体的な製品の説明)
### 特長
1. **普段たまっているストレスを可視化!**
 イライラしている時には、何かものに当たりたくなりませんか?そんな時には、心が落ち着くまで、ボタンを連打しまくってください!押したボタンの回数に応じて、ストレス判定を行います!
2. **さらに.Twitterから隠れストレスを分析!**
 イライラする以外にもストレスは、溜まります.Twitter連携をすると、呟きから隠れているストレスを炙り出しますよ!
3. **疲れているそんなあなたに,最適なご褒美を提案!**
押したボタンの回数、Twitterからの隠れストレスを分析して、あなたに最適なご褒美を提案します!
### 解決出来ること
ストレス発散をしにくいという課題を、ストレス度合いに応じてご褒美を提案することで、解決します。
### 今後の展望
- 複数のユーザー及び鍵垢でも収集できるようにする。
### 注力したこと(こだわり等)
- ご褒美を数段階に分けて、ストレス度によってサジェストを分ける
- ミライ小町ちゃんの表情
- Tweetから隠れストレスを分析及びレポートとして表示
## 開発技術
### 活用した技術
#### API・データ
- 感情判定アダプター
- ミライ小町ちゃんの3Dモデル
#### フレームワーク・ライブラリ・モジュール
- Backend
  - Azure
  - python
  - Tweepy
  - Pytorch
 
- Fronted
  - Unity
  - VroidSDK
  - ミライ小町VRM
#### デバイス
- iOS/Androidのスマートフォン
### 独自技術
#### ハッカソンで開発した独自機能・技術
- Web API
  - カウンターを記録する API
  - ツイートを集計して、感情判定する API
  - 感情判定されたツイートからレポート情報を作成する API
