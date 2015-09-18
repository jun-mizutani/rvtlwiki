# RvtlWiki ver.2.00

  2015/09/18  Jun Mizutani & Toshio Moritake

RvtlWikiは結城 浩 氏が公開されている YukiWiki (http://www.hyuki.com)
の機能と文法を参考に rvtl (http://www.mztn.org/) という
TinyBasic系の言語で作成した Wiki Engineの一種です。

Linux で動作しますが、CPUの種類でパッケージが異なります。

   ---------------+----------+---------------
    RvtlWiki          CPU          rvtl
   ---------------+----------+---------------
    rvtlwiki         x86       rvtl-x86-3.05
    rvtlwiki         arm       rvtl-arm-3.05
    rvtlwiki64       x86_64    rvtl-amd64-4.01
    rvtlwiki64       arm64     rvtl-arm64-4.01
    rvtlwiki_euc     PowePC    rvtl-3.03.1ppc


## RvtlWiki 2.00 の変更点

### RvtlWiki 1.05 から

- 出力タグを HTML5対応に修正
- rvtl コードと html データの文字コードを utf-8 に変更
- 見出し文字列の指定に、行頭に以下の日本語記号も使用可能
   ★    <h1>
   ■    <h2>
   ●    <h3>
   ◆    <h4>
   ▲    <h5>
   ☆    <h6>

- シングルクォートを使った文字属性の指定が増えました。
- 行頭から3文字以上の空白がある場合は整形済み(pre)となります。
- 空行が2つ連続すると <br /> に変換されます。

### RvtlWiki 1.03 から 1.05

- RSS機能を追加
- ページのデザインを少し修正
- 出力タグを XHTML1.0対応に修正

### RvtlWiki 1.02 から 1.03

- プレビューの編集エリアが「[EFAULT] Bad address 」となる点を修正

### RvtlWiki 1.01 から1.02

- 空行が段落として認識されないのを修正
- 行頭が空白の場合に段落にならない部分を修正

### RvtlWiki 1.00 から 1.01

- 追記機能により、どのページにも簡単に追記が可能。
- コメントフォーム(YukiWikiとは異なり位置は先頭に固定)からページ最上部または最下部に追加が可能。
- 定義形式リストのタイトル部分をボールドに変更。
- 水平線がハイフン5つであったのを4つに修正。
- 編集を保存すると直接ページが表示されるように変更。
- pages ディレクトリの内容を変更する必要はありません。

## YukiWikiとの違い

- ページタイトルの変更ができます。
- ページをグループに分類することができます。
- 強制改行「<br>」が 「--.」で挿入できます。
- テーブルの rowspan が可能です。
- 文字飾りは2種類ですが、スタイルシートで形式を変更できます。
- 見出しは4段階あります。
- 整形済みのフォーマット指定は4種類あります。
- 画像挿入の指定方法が異なります。
- 行頭はスペースでも整形済み(<pre>)になりません。
- > による引用文はありません。
- Wikiのページ名へのリンクは[[ページ名]]ではかけません。
- 大文字小文字を混ぜた英文字列はWikiのページ名としてリンクになりません。
- テーブル中にコンマ(,)を書くことはできません。
- コメントフォームは設置できません。
- ページ差分をとることはできません。
- 検索機能がありません。

## バージョンアップ手順

RvtlWiki 2.00 は文字コードが UTF-8 になっています。文字コードが EUC の
RvtlWiki 1.0x からバージョンアップする場合は rvtlwiki-200euc.tar.gz
を使って下さい。 以下のファイルを上書きコピーしてください。

- rvtlwiki.cgi と render.cgi
- data ディレクトリのrvtlwiki.css と rvtlwiki.dat

pages ディレクトリは変更する必要はありません。

## インストール手順

RvtlWiki を動作させるためには rvtl (http://www.mztn.org/) が
必要です。rvtl-3.05.tar.gz (PC)、rvtl-3.03.1ppc.tar.gz(玄箱)、
rvtl-3.05arm.tar.gz (Linux Zaurus) 中の rvtl を /usr/bin/
にコピーしてください。

また rvtl を rvtlw というファイル名で /usr/bin/ 以下にシンボリックリンク
を作成するか、

    cd /usr/bin
    ln -s rvtl rvtlw

または rvtl を rvtlw というファイル名でコピーしてください。

    cd /usr/bin
    cp rvtl rvtlw

RvtlWikiは複数のファイルで構成されています。rvtlwiki.cgiには実行可能
属性(755)、その他は読みだし可能(644)である必要があります。
また、pages ディレクトリは CGI が読み書き(755)します。

httpサーバが nobody 等のユーザとして動作していて、suEXEC の設定に
なっていない場合は、pages ディレクトリの権限は 777(読み書き検索可)、
その下にある pages.txt、groups.txt の権限は 666(読み書き可) として
ください。

    cd rvtlwiki
    chmod 755 *.cgi
    chmod 755 data
    chmod 644 data/*
    chmod 777 pages
    chmod 666 pages/*


    --+-- rvtlwiki.cgi   RvtlWiki の本体CGI
      |
      +-- render.cgi     テキストからHTMLへのレンダリングCGI
      |
      +-- .htaccess      Apache用の設定ファイル
      |
      +-- readme.txt     このファイル。実行には不要です。
      |
      +-- data -+-- rvtlwiki.png   RvtlWiki のロゴ
      |         |
      |         +-- rvtlwiki.dat   Wikiの使用法の表示データ
      |         |
      |         +-- rvtlwiki.css   RvtlWiki のスタイルシート
      |         |
      |         +-- frontpage.dat  表紙の表示データ
      |
      +--pages -+-- pages.txt  ページ管理用ファイル
                |
                +-- groups.txt グループ管理用ファイル
                :
                +-- 各Wikiページのファイル
                :

必要ならrvtlwiki.cgiのはじめの方にある、U['W']、U['H']などの値を修正して下さい。

    10100 :-------------------------------------------------------------
    10110 : ユーザ設定
    10120 :-------------------------------------------------------------
    10130    u=U                : 変更不可
    10140    u*="./data/"       : dataディレクトリのパス名 U[0]
    10150    u=U+64             : 変更不可
    10160    u*="./pages/"      : pagesディレクトリのパス名 U[16]
    10170    u=U+128            : 変更不可
    10180    u*="http://www.example.com/rvtlwiki/" : URL U[32]
    10190    u=U+768            : 変更不可
    10200    u*="RvtlWiki"      : フロントページのタイトル
    10210    u=U+512            : 変更不可
    10220    u*="RvtlWiki New"  : RSSタイトル
    10230    u=U+640            : 変更不可
    10240    u*="RvtlWiki RSS"  : RSS description
    10250    U['N']=256*1024     : 最大ページサイズ
    10260    U['W']=80          : 編集領域の桁数
    10270    U['H']=30          : 編集領域の行数
    10280    U['R']=40          : 更新履歴表示件数

また、最大ページサイズを変更した場合は render.cgi の以下の部分も変更します。

    10070 :------------------------------------------------------------
    10080    M=256              : 最大ページサイズ(KB)


dataディレクトリ中のfrontpage.datはhtml形式のファイルです。
必要に応じて書き換えてください。本文部分(<body></body>の内側)のみ
を書きます。

ファイル一覧にあるファイルをサーバに転送します。転送モードやパーミッションを環境にあわせ適切に設定して下さい。

ブラウザでサーバ上の rvtlwiki.cgi の URL にアクセスします。

メニューの「新規ページ分類」からページ分類名を設定します。

メニューの「新規ページ」から新しいページを作成します。


## 最新情報

この文書以外の情報やサンプルプログラム、rvtlの最新情報は
http://www.mztn.org/ を参照して下さい。

rvtl を使ってプログラムを作成された方は mizutani.jun@nifty.ne.jp まで
お知らせください。http://www.mztn.org/ で紹介させて頂きます。


## ライセンス

このソフトはフリーソフトウェアです. GNU General Pulic Licenceにしたがって
自由に使用，配布，改変して頂いてかまいません。

著作権は 水谷 純<mizutani.jun@nifty.ne.jp> http://www.mztn.org/ と
森竹 俊夫 Toshio Moritake <odinsroom@gmail.com> http://www.odin.hyork.net/
が保有しています。
本ソフトウェアによって生じた損害について著作者は責任を負いません。
また、著作者はバージョンアップの義務を負いません。

