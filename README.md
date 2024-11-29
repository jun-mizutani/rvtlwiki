# RvtlWiki ver.2.06

  2024/11/28  Jun Mizutani & Toshio Moritake

RvtlWikiは結城 浩 氏が公開されている YukiWiki (http://www.hyuki.com)
の機能と文法を参考に rvtl (http://www.mztn.org/) という
TinyBasic系の言語で作成した Wiki Engineの一種です。

Linux で動作しますが、CPUの種類でパッケージが異なります。

|   RvtlWiki     |   CPU   |     rvtl          |
|:---------------|:--------|:------------------|
|  rvtlwiki      |  x86    | rvtl-x86-3.05     |
|  rvtlwiki      |  arm    | rvtl-arm-3.05     |
|  rvtlwiki64    |  x86_64 | rvtl-amd64-4.01   |
|  rvtlwiki64    |  arm64  | rvtl-arm64-4.01   |
|  rvtlwiki64    |  risc-v | rvtl-riscv64-4.00 |


## RvtlWiki 2.06 の変更点
- 表示ページの右上に、そのページが属するページ分類を表示。ページ分類に所属するページリストへのリンクとなっている。

### RvtlWiki 2.05
- ビデオ用のタグ挿入
- 最大ページサイズのデフォルトを 1MB/1万行 に拡張
- 編集領域のデフォルトを広げた

### RvtlWiki 2.04 欠番

### RvtlWiki 2.03
- フッターにページトップへのリンクを配置
- 見出しにページトップへのリンクを配置
- rvtlwiki.css にページトップへのリンク用の設定を追加
- EUC版を廃止

### RvtlWiki 2.02
- ページ一覧に表示されるページ分類にリンクを追加

### RvtlWiki 2.01
- 追記メニュー内でシングルクォートの抜けを修正

### RvtlWiki 2.00
- 出力タグを HTML5対応に修正
- rvtl コードと html データの文字コードを utf-8 に変更
- 見出し文字列の指定に、行頭に以下の日本語記号も使用可能

    ★    &lt;h1&gt;
    ■    &lt;h2&gt;
    ●    &lt;h3&gt;
    ◆    &lt;h4&gt;
    ▲    &lt;h5&gt;
    ☆    &lt;h6&gt;

- シングルクォートを使った文字属性の指定が増えました。
- 行頭から3文字以上の空白がある場合は整形済み(pre)となります。
- 空行が2つ連続すると &lt;br /&gt; に変換されます。

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
- 強制改行「&lt;br&gt;」が 「--.」で挿入できます。
- テーブルの rowspan が可能です。
- 文字飾りは2種類ですが、スタイルシートで形式を変更できます。
- 見出しは4段階あります。
- 整形済みのフォーマット指定は4種類あります。
- 画像挿入の指定方法が異なります。
- 行頭はスペースでも整形済み(&lt;pre&gt;)になりません。
- &gt; による引用文はありません。
- Wikiのページ名へのリンクは[[ページ名]]ではかけません。
- 大文字小文字を混ぜた英文字列はWikiのページ名としてリンクになりません。
- テーブル中にコンマ(,)を書くことはできません。
- コメントフォームは設置できません。
- ページ差分をとることはできません。
- 検索機能がありません。

## バージョンアップ手順

以下のファイルを上書きコピーしてください。

- rvtlwiki.cgi と render.cgi
- data ディレクトリのrvtlwiki.css と rvtlwiki.dat

pages ディレクトリは変更する必要はありません。

## インストール手順

RvtlWiki を動作させるためには rvtl (http://www.mztn.org/) が必要です。 rvtl-x86-3.05.tar.gz または rvtl-amd64-4.01.tar.gz (PC)、rvtl-3.03.1ppc.tar.gz(玄箱)、rvtl-arm-3.05.tar.gz (Raspberry Pi) 、rvtl-arm64-4.01.tar.gz (Dragonboard410C) 中の rvtl または rvtl64 を /usr/bin/にコピーしてください。

rvtl または rvtl64 を rvtlw というファイル名で /usr/bin/ 以下にシンボリックリンクを作成するか、

    cd /usr/bin
    ln -s rvtl rvtlw

    cd /usr/bin
    ln -s rvtl64 rvtlw

rvtl または rvtl64 を rvtlw というファイル名でコピーしてください。

    cd /usr/bin
    cp rvtl rvtlw

    cd /usr/bin
    cp rvtl64 rvtlw

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

    10180 :-------------------------------------------------------------
    10190 : ユーザ設定
    10200 :-------------------------------------------------------------
    10210    u=U                : 変更不可
    10220    u*="./data/"       : dataディレクトリのパス名 U[0]
    10230    u=U+64             : 変更不可
    10240    u*="./pages/"      : pagesディレクトリのパス名 U[16]
    10250    u=U+128            : 変更不可
    10260    u*="http://www.example.com/rvtlwiki/" : URL U[32]
    10270    u=U+768            : 変更不可
    10280    u*="RvtlWiki"      : フロントページのタイトル
    10290    u=U+512            : 変更不可
    10300    u*="RvtlWiki New"  : RSSタイトル
    10310    u=U+640            : 変更不可
    10320    u*="RvtlWiki RSS"  : RSS description
    10330    U['N']=1024*1024   : 最大ページサイズ
    10340    U['W']=120         : 編集領域の桁数
    10350    U['H']=50          : 編集領域の行数
    10360    U['R']=80          : 更新履歴表示件数

また、最大ページサイズを変更した場合は render.cgi の以下の部分も変更します。

    10100 :------------------------------------------------------------
    10110    M=1024             : 最大ページサイズ(KB)

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

