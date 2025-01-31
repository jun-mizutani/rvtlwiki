#!/usr/bin/rvtlw
 
10020 :-------------------------------------------------------------
10030 : RvtlWiki (rvtlwiki.cgi)
10040 : version : 2.07 (32bit) 2025/01/31
10050 : Copyright (C) 2005-2025
10060 :   Jun Mizutani <mizutani.jun@nifty.ne.jp> http://www.mztn.org/
10070 : & Toshio Moritake <odinsroom@gmail.com> http://www.odin.hyork.net/
10080 :     RvtlWiki may be copied under the terms of the
10090 :     GNU General Public License.
10100 :------------------------------------------------------------
10110    |ve
10120    ;=(%>>32)=0 #=^START
10130      "rvtl64 では動作しません。rvtl で起動してください。"
10140      #=-1
10150   ^START
10160    z=&                : heap top
10170    U=z z=z+1024       : ユーザ設定領域
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
10370 :-------------------------------------------------------------
10380 : グローバル変数(配列を除く)
10390 :-------------------------
10400 : C          : ページDB要素数
10410 : I          : リモートIPアドレスを保持
10420 : M          : CGIモード
10430 : N          : buffer size 単位
10440 : O          : グループDB要素数
10450 : S          : ローカル変数として Lockfile名
10460 : z=&        : heap top
10470 :-------------------------
10480 : メモリー確保
10490 :-------------------------
10500    N=U['N']
10510    *=*+(7*N)          : メモリ拡張
10520    B=z z=z+256        : Buffer
10530    Q=z z=z+256        : Post Data Buffer
10540    R=z z=z+256        : Data Buffer
10550    Z=z z=z+256        : rvtlwiki.cgi
10560    J=z z=z+256        : version
10570    :E
10580    F=z z=z+24576      : FileName      (num <1535)
10590    :G
10600    :H
10610    L=z z=z+256        : POSTデータ文字列先頭配列
10620    X=z z=z+8192       : Group管理データワーク
10630    Y=z z=z+8192       : Groupタイトル格納
10640    V=z z=z+4096       : Group管理データ
10650    A=z z=z+N          : ページ管理ファイル
10660    D=z z=z+N          : ページ管理タイトルBuffer
10670    T=z z=z+N          : text
10680    P=z z=z+N          : POST文字列(URLデコード済み)保存
10690    W=z z=z+(N*3)      : work
10700 :
10710    Z*="rvtlwiki.cgi"
10720    |ve ;=%<0 Z*="rvtlwiki.elf.cgi"
10730    J*="Powered by RvtlWiki 2.06(32bit)"
10740    [=0                : 範囲チェックOFF
10750    C=0                : ページDB要素数
10760    O=0                : グループDB要素数
10770    !=^TimerStart
10780 :
10790    :-------------------------
10800    : 動作モードの決定
10810    :-------------------------
10820    !=^REMOTE_ADDR I=r
10830    x=B s=W !=^REQUEST
10840    ;=r='P' x=B !=^RequestPost Mode='Post' #=^Get
10850    ;=r='G' x=B !=^RequestGet  Mode='Get'  #=^Get
10860    "No REQUEST_METHOD"  / #=^Exit
10870    :--- GET の場合 ---
10880    ^Get
10890    ;=Mode<>'Get' #=^Post
10900    B*="DispPage"      x=B !=^SearchPost ;=r Mode='Disp' #=^DoCommand
10910    B*="Static"        x=B !=^SearchPost ;=r Mode='Stat' #=^DoCommand
10920    B*="CreatePage"    x=B !=^SearchPost ;=r Mode='CrPg' #=^DoCommand
10930    B*="CreateGroup"   x=B !=^SearchPost ;=r Mode='CrGp' #=^DoCommand
10940    B*="ChangePage"    x=B !=^SearchPost ;=r Mode='ChPg' #=^DoCommand
10950    B*="ChangeGroup"   x=B !=^SearchPost ;=r Mode='ChGp' #=^DoCommand
10960    B*="IndexPage"     x=B !=^SearchPost ;=r Mode='Indx' #=^DoCommand
10970    B*="FrontPage"     x=B !=^SearchPost ;=r Mode='Frnt' #=^DoCommand
10980    B*="RecentChanges" x=B !=^SearchPost ;=r Mode='Rcnt' #=^DoCommand
10990    B*="Edit"          x=B !=^SearchPost ;=r Mode='Edit' #=^DoCommand
11000    B*="GroupList"     x=B !=^SearchPost ;=r Mode='List' #=^DoCommand
11010    B*="Append"        x=B !=^SearchPost ;=r Mode='Appd' #=^DoCommand
11020    B*="RSS"           x=B !=^SearchPost ;=r Mode='RSS ' #=^DoCommand
11030    Mode='Frnt' #=^DoCommand   : デフォルトは目次
11040    #=^Exit
11050    :--- POST の場合 ---
11060    ^Post
11070    y=Q
11080    B*="preview="      x=B !=^GetPost ;=r Mode='PrVw' #=^DoCommand
11090    B*="store="        x=B !=^GetPost ;=r Mode='Stor' #=^DoCommand
11100    B*="newpage="      x=B !=^GetPost ;=r Mode='NwPg' #=^DoCommand
11110    B*="newgroup="     x=B !=^GetPost ;=r Mode='NwGp' #=^DoCommand
11120    B*="pagerename="   x=B !=^GetPost ;=r Mode='PgNm' #=^DoCommand
11130    B*="NewGroupName=" x=B !=^GetPost ;=r Mode='GpNm' #=^DoCommand
11140    B*="message="      x=B !=^GetPost ;=r Mode='DoAp' #=^DoCommand
11150    B*="AddBottom="    x=B !=^GetPost ;=r Mode='DoAp' #=^DoCommand
11160    B*="AddTop="       x=B !=^GetPost ;=r Mode='DoAT' #=^DoCommand
11170    #=^Exit
11180 :
11190    :-------------------------
11200    : コマンドの実行
11210    :-------------------------
11220   ^DoCommand
11230 :  RSS は HTMLヘッダ不要
11240    ;=Mode='RSS ' !=^RSS            #=^Exit2
11250 :  HTML Header
11260    "Content-type: text/html; charset=UTF-8" / /
11270    "<!DOCTYPE html>" /
11280    "<html lang='ja'>"
11290    / "<head>" /
11300    "<meta charset='UTF-8' />" /
11310    ;=Mode<>'Frnt' #=^CheckCommand
11320 :  FrontPage
11330    "<link rel='alternate' type='application/rss+xml' title='RSS'"
11340    " href='" $*=Z "?RSS' />" /
11350    !=^FrontPage
11360    #=^Exit
11370 :
11380   ^CheckCommand
11390    ;=Mode='Disp' !=^DisplayPage    #=^Exit
11400    ;=Mode='Stat' !=^StaticPage     #=^Exit1
11410    ;=Mode='Indx' !=^IndexPage      #=^Exit
11420    ;=Mode='Rcnt' !=^RecentChanges  #=^Exit
11430    ;=Mode='Edit' !=^Edit           #=^Exit
11440    ;=Mode='PrVw' !=^Preview        #=^Exit
11450    ;=Mode='Stor' !=^StorePage      #=^Exit
11460    ;=Mode='CrPg' !=^CreatePage     #=^Exit
11470    ;=Mode='CrGp' !=^CreateGroup    #=^Exit
11480    ;=Mode='NwPg' !=^NewPage        #=^Exit
11490    ;=Mode='NwGp' !=^NewGroup       #=^Exit
11500    ;=Mode='ChPg' !=^ChangePage     #=^Exit
11510    ;=Mode='ChGp' !=^ChangeGroup    #=^Exit
11520    ;=Mode='PgNm' !=^DoPageRename   #=^Exit
11530    ;=Mode='GpNm' !=^DoGroupRename  #=^Exit
11540    ;=Mode='List' !=^GroupList      #=^Exit
11550    ;=Mode='DoAp' !=^DoAppend       #=^Exit
11560    ;=Mode='DoAT' !=^DoTopAppend    #=^Exit
11570    ;=Mode='Appd' !=^Append         #=^Exit
11580    "<p> Undefined Command </p>"
11590    #=^Exit
11600 :
11610    :-------------------------
11620    : 終了
11630    :-------------------------
11640 ^Exit
11650    a=I s=Q !=^SetADDR
11660    "<div id='footer'><hr />"
11670    "<p class='gototop'><a href='#main'>[TOP]</a></p>
11680    "<small><p class='wikitime'> " !=^TimerStop " from " $*=s
11690    "</p></small>" /
11700    "<p align='right'><em>"
11710    "<a href='http://www.mztn.org/'>" $*=J "</a></em><br />" /
11720    "<img src='"
11730    x=Q !=^PathLogo $*=Q
11740    "' alt='*' width='80' height='40' /></p></div>" /
11750 ^Exit1
11760    "<br />" / / "</body>" / "</html>" /
11770 ^Exit2
11780    "" /
11790    #=-1
11800 :
11810 :-------------------------------------------------
11820 : ページ管理ファイルのパス名を設定
11830 :  (in)  x : バッファアドレス
11840 :  (out) x : pages.txt のパス文字列を設定
11850 :-------------------------------------------------
11860 ^PathPages
11870    +pu
11880    p=x u=U+64
11890    p*=u p=p+%
11900    p*="pages.txt"
11910    -up
11920 ]
11930 :-------------------------------------------------
11940 : RSS Feed
11950 :-------------------------------------------------
11960 ^RSS
11970    "Content-type: text/xml; charset=UTF-8" / /
11980    "<?xml version='1.0' encoding='UTF-8' ?>" / /
11990    "<rdf:RDF" /
12000    " xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'" /
12010    " xmlns='http://purl.org/rss/1.0/'" /
12020    " xmlns:dc='http://purl.org/dc/elements/1.1/'" /
12030    ">" / /
12040    !=^PageDBRead
12050    !=^GroupDBRead
12060    ;=O=0 #=^rss02  : グループDB要素数のチェック
12070    "<channel rdf:about='"
12080    !=^RssURL "?RSS'>" /
12090    " <title>" u=U+512 $*=u "</title>" /
12100    " <link>" !=^RssURL "</link>" /
12110    " <description>" u=U+640 $*=u "</description>" /
12120    " <items>" /
12130    "  <rdf:Seq>" /
12140    i=0,O-1
12150      "  <rdf:li rdf:resource='"
12160      !=^RssURL2 ?=V[i*4+2]
12170      "' />" /
12180    @=i+1
12190    "  </rdf:Seq>" /
12200    " </items>" /
12210    "</channel>" /
12220 :
12230    i=0,O-1
12240      g=0 e=0
12250      ;=C=0 #=^rss01
12260      j=0,C-1
12270        ;=F[j*4+2]=V[i*4+2] g=g+1 ;=F[j*4+0]>e e=F[j*4+0]
12280      @=j+1
12290      ^rss01
12300      "  <item rdf:about='" !=^RssURL2 ?=V[i*4+2] "'>" /
12310      "   <title>" !=^PageTime " - " $*=V[i*4+3] "</title>" /
12320      "   <link>" !=^RssURL2 ?=V[i*4+2] "</link>" /
12330      "   <description>" $*=V[i*4+3] "</description>" /
12340      "   <dc:date>"
12350      !=^PageTime
12360      "   </dc:date>" /
12370      "  </item>" / /
12380    @=i+1
12390    ^rss02
12400    "</rdf:RDF>" /
12410 ]
12420 :
12430 :-------------------------------------------------
12440 : RSS item のURLを出力
12450 :  (in) U:設定領域先頭、Z:パス
12460 :-------------------------------------------------
12470 ^RssURL
12480    $*=U+128 $*=Z
12490 ]
12500 :
12510 :-------------------------------------------------
12520 : RSS item のURLを出力
12530 :  (in) U:設定領域先頭、Z:パス
12540 :-------------------------------------------------
12550 ^RssURL2
12560    !=^RssURL "?GroupList&amp;group="
12570 ]
12580 :
12590 :-------------------------------------------------
12600 : 日時を表示
12610 :  (in) e:UNIX時間 Q:バッファ
12620 :-------------------------------------------------
12630 ^PageTime
12640    +ts
12650    t=e s=Q !=^LocalTime
12660    ?=s{5} "/" ?[2]=s{4} "/" ?[2]=s{3} " "
12670    ?[2]=s{2} ":" ?[2]=s{1} ":" ?[2]=s{0}
12680    -st
12690 ]
12700 :
12710 :-------------------------------------------------
12720 : グループ管理ファイルのパス名を設定
12730 :  (in)  x : バッファアドレス
12740 :  (out) x : groups.txt のパス文字列を設定
12750 :-------------------------------------------------
12760 ^PathGroups
12770    +pu
12780    p=x u=U+64
12790    p*=u p=p+%
12800    p*="groups.txt"
12810    -up
12820 ]
12830 :
12840 :-------------------------------------------------
12850 : CSSファイルのパス名を設定
12860 :  (in)  x : バッファアドレス
12870 :  (out) x : rvtlwiki.css のパス文字列を設定
12880 :-------------------------------------------------
12890 ^PathCSS
12900    +p
12910    p=x
12920    p*=U p=p+%
12930    p*="rvtlwiki.css"
12940    -p
12950 ]
12960 :
12970 :-------------------------------------------------
12980 : ロゴファイルのパス名を設定
12990 :  (in)  x : バッファアドレス
13000 :  (out) x : rvtlwiki.png のパス文字列を設定
13010 :-------------------------------------------------
13020 ^PathLogo
13030    +p
13040    p=x
13050    p*=U p=p+%
13060    p*="rvtlwiki.png"
13070    -p
13080 ]
13090 :
13100 :-------------------------------------------------
13110 : 使用法ファイルのパス名を設定
13120 :  (in)  x : バッファアドレス
13130 :  (out) x : rvtlwiki.dat のパス文字列を設定
13140 :-------------------------------------------------
13150 ^PathHelp
13160    +p
13170    p=x
13180    p*=U p=p+%
13190    p*="rvtlwiki.dat"
13200    -p
13210 ]
13220 :
13230 :-------------------------------------------------
13240 : フロントページファイルのパス名を設定
13250 :  (in)  x : バッファアドレス
13260 :  (out) x : frontpage.dat のパス文字列を設定
13270 :-------------------------------------------------
13280 ^PathFront
13290    +p
13300    p=x
13310    p*=U p=p+%
13320    p*="frontpage.dat"
13330    -p
13340 ]
13350 :
13360 :-------------------------------------------------
13370 :  Readering Wiki File Wikiファイルの出力
13380 :  子プロセスを起動してhtml変換
13390 :     (in) x : ファイル名
13400 :    ^Preview
13410 :    ^StorePage
13420 :-------------------------------------------------
13430 ^RenderWikiText
13440    +xzbfgh
13450    b=z z=z+256
13460    f=z z=z+256
13470    g=z z=z+256
13480    h=z z=z+256
13490    b*="/usr/bin/rvtlw render.cgi - "
13500    |ve ;=%<0 b*="./render.elf.cgi "
13510    y=h h*=x                   : y="file.txt"
13520    f*=x                       : f="file.txt"
13530    x=b !=^MergeStr            :/usr/bin/rvtlw render.cgi - file.txt
13540    a=U['P'] s=g !=^ToStr      : page#
13550    y*=" " !=^MergeStr
13560    y=g    !=^MergeStr
13570    y*=" " !=^MergeStr
13580    y=g y*=" > " !=^MergeStr   : >
13590    y=f !=^MergeStr            : file.txt
13600    x(r-3)=0                   : 拡張子"txt"を除く
13610    y*="dat" !=^MergeStr       : file.dat
13620    ,*=b
13630    -hgfbzx
13640 ]
13650 :
13660 :-------------------------------------------------
13670 :  レンダリング済みhtmlファイルの出力
13680 :     (in) x : ファイル名
13690 :    ^DisplayPage
13700 :    ^FrontPage
13710 :    ^Preview
13720 :-------------------------------------------------
13730 ^DispWikiText
13740    |ca*=x
13750 ]
13760 :
13770 :-------------------------------------------------
13780 : ページの表示
13790 :-------------------------------------------------
13800 ^DisplayPage
13810    !=^PageDBRead
13820    B*="page=" x=B y=Q !=^GetPost
13830    x=Q !=^ToVal
13840    a=r !=^PageDBSearch a=r
13850    x=F[a*4+3]                         : title 指定
13860    !=^HTMLHeader
13870    x=Q                            : page 指定
13880    !=^HTMLTools
13890    "<h1>" $*=F[a*4+3] "</h1>"
13900    : 2023-10-22
13910    !=^GroupDBRead
13920    a=F[a*4+2] !=^GroupDBSearch
13930    / "<p style='text-align:right'>"
13940    "<a href='" $*=Z "?GroupList&group=" ?=V[r*4+2] "'>["
13950    $*=V[r*4+3] "]</a></p>" /
13960    x=Q !=^MakeDatName             : file名指定
13970    !=^DispWikiText
13980 ]
13990 :
14000 :-------------------------------------------------
14010 : 静的ページの表示
14020 :-------------------------------------------------
14030 ^StaticPage
14040    !=^PageDBRead
14050    B*="page=" x=B y=Q !=^GetPost
14060    x=Q !=^ToVal
14070    a=r !=^PageDBSearch a=r
14080    x=F[a*4+3]                         : title 指定
14090    !=^HTMLHeader
14100    "<h1>" $*=F[a*4+3] "</h1>"
14110    x=Q !=^MakeDatName             : file名指定
14120    !=^DispWikiText
14130 ]
14140 :
14150 :-------------------------------------------------
14160 : 追記用フォーム付のページ表示
14170 :-------------------------------------------------
14180 ^Append
14190    !=^PageDBRead
14200    B*="page=" x=B y=Q !=^GetPost
14210    x=Q !=^ToVal
14220    a=r b=r !=^PageDBSearch a=r
14230    x=F[a*4+3]                         : title 指定
14240    !=^HTMLHeader
14250    x=Q                            : page 指定
14260    !=^HTMLTools
14270    "<h1>" $*=F[a*4+3] " - 追記</h1>"
14280    "[<a href='#append'> 追記にジャンプ</a>]<br />"
14290    x=Q !=^MakeDatName             : file名指定
14300    !=^DispWikiText
14310    / "<a name='append'><a>" / "<div id='comment'>" /
14320    "<form action='" $*=Z "' method='post' >" / "<fieldset>"
14330    "<input type=hidden name=page value='" ?=b "'>" /
14340    "<strong>追記</strong><small>"
14350    " − ここに書いた文は、このページの最後に追加されます。"
14360    "</small>" /
14370    "<input type=submit name='message' value='書き込み' ><br />" /
14380    "<textarea cols='80' rows='8' name='msg' >" /
14390    "</textarea><br />" /
14400    "</fieldset>" / "</form>" / "</div>" /
14410    "<p>" "</p>" /
14420 ]
14430 :
14440 :-------------------------------------------------
14450 : 新規ページの作成
14460 :-------------------------------------------------
14470 ^CreatePage
14480    x=B
14490    x*="新規ページの作成"          : title 指定
14500    !=^HTMLHeader
14510    !=^HTMLTools
14520    "<h1>新規ページの作成</h1>"
14530    !=^GroupDBRead
14540    "<p>"
14550    " <form action='" $*=Z "' method='post'>" /
14560    " <strong>ページ分類を指定してください。</strong><br /> " /
14570    i=0,O-1
14580      "<input type=radio name=group id='group"
14590      ?=V[i*4+2] "' value='" ?=V[i*4+2]
14600      "<label for='group" ?=V[i*4+2] "'>" $*=V[i*4+3] "</label><br />" /
14610    @=i+1
14620    "  <br />" /
14630    " <strong>新しいページの名前を入力してください。</strong><br /> " /
14640    " <input type='text' name='newpage' value='' size='32'>" /
14650    " <input type='submit' value='新規作成'><br />" /
14660    "</form>" /
14670    "</p>" /
14680    !=^PageDBRead
14690    !=^GroupDBRead
14700    !=^GroupDBList
14710 ]
14720 :
14730 :-------------------------------------------------
14740 : 新規ページの作成後の表示
14750 :-------------------------------------------------
14760 ^NewPage
14770    +Sz
14780    S=z z=z+256
14790    x=B
14800    x*="新規ページ作成"            : title 指定
14810    !=^HTMLHeader
14820    !=^HTMLTools
14830    "<h1>新規ページ作成</h1>"
14840    B*="group=" x=B y=R !=^GetPost
14850    x=R !=^ToVal a=r
14860    x=B !=^PathPages S*=B !=^LockWait
14870    ;=r<0 "<p>ファイルがロックされています</p>" -zS ]
14880    !=^PageDBRead
14890    x=Q !=^RegistPage
14900    !=^GroupDBRead
14910    a=0 b=1 c=0                    : 更新日付降順
14920    !=^PageDBList
14930    !=^PageDBWrite
14940    x=S !=^Unlock
14950    -zS
14960 ]
14970 :
14980 :-------------------------------------------------
14990 : 新規グループの作成
15000 :-------------------------------------------------
15010 ^CreateGroup
15020    x=B
15030    x*="新規ページ分類の作成"          : title 指定
15040    !=^HTMLHeader
15050    !=^HTMLTools
15060    "<h1>新規ページ分類の作成</h1>"
15070    "<p>"
15080    "<form action='" $*=Z "' method='post'>" /
15090    "  <strong>新しいページ分類の名前を入力してください。
15100    "  </strong><br /> " /
15110    "  <input type='text' name='newgroup' value='' size='32'>" /
15120    "  <input type='submit' value='新規作成'><br />" /
15130    "</form>" /
15140    "</p>" /
15150    !=^PageDBRead
15160    !=^GroupDBRead
15170    !=^GroupDBList
15180 ]
15190 :
15200 :-------------------------------------------------
15210 : 新規グループの作成後の表示
15220 :-------------------------------------------------
15230 ^NewGroup
15240    x=B
15250    x*="新規ページ分類の作成"          : title 指定
15260    !=^HTMLHeader
15270    !=^HTMLTools
15280    "<h1>新規ページ分類の作成</h1>"
15290    x=B !=^PathGroups !=^LockWait
15300    ;=r<0 "<p>ファイルがロックされています</p>" ]
15310    !=^PageDBRead
15320    !=^GroupDBRead
15330    x=Q !=^RegistGroup
15340    !=^GroupDBList
15350    !=^GroupDBWrite
15360    x=B
15370    !=^Unlock
15380 ]
15390 :
15400 :-------------------------------------------------
15410 : 一覧の表示
15420 :-------------------------------------------------
15430 ^IndexPage
15440    x=B
15450    x*="ページ一覧"                : title 指定
15460    !=^HTMLHeader
15470    !=^HTMLTools
15480    "<h1>ページ一覧</h1>"
15490    !=^PageDBRead
15500    !=^GroupDBRead
15510    a=1 b=0 c=0                    : グループ昇順
15520    !=^PageDBList
15530 ]
15540 :
15550 :-------------------------------------------------
15560 : フロントページの表示
15570 :-------------------------------------------------
15580 ^FrontPage
15590    x=U+768                        : title 指定
15600    !=^HTMLHeader
15610    !=^HTMLTools
15620    "<h1>目次</h1>"
15630    x=B !=^PathFront !=^TextRead
15640    x=B
15650    !=^DispWikiText / "<hr />"
15660    !=^GroupDBRead
15670    !=^PageDBRead
15680    !=^GroupDBList
15690 ]
15700 :
15710 :-------------------------------------------------
15720 : 履歴ページの作成
15730 :-------------------------------------------------
15740 ^RecentChanges
15750    B*="count=" x=B y=Q !=^GetPost
15760    x=Q !=^ToVal
15770    c=r                            : 表示数
15780    x=B
15790    x*="更新履歴"                  : title 指定
15800    !=^HTMLHeader
15810    !=^HTMLTools
15820    !=^PageDBRead
15830    !=^GroupDBRead
15840    "<h1>更新履歴</h1>"
15850    "["
15860    ;=(c>0)&(C>c) ?=c "件 / "    : 表示件数
15870    ?=C "件] "               : すべての件数
15880    ;=(c>0)&(C>c) "<a href='" $*=Z "?RecentChanges&count=0'>すべて表示</a>"
15890    /
15900    a=0 b=1                        : 更新日付降順
15910    !=^PageDBList
15920 ]
15930 :
15940 :-------------------------------------------------
15950 : ページの編集
15960 :-------------------------------------------------
15970 ^Edit
15980    !=^PageDBRead
15990    B*="page=" x=B y=Q !=^GetPost
16000    x=Q !=^ToVal
16010    a=r !=^PageDBSearch a=r
16020    x=F[a*4+3]                         : title 指定
16030    !=^HTMLHeader
16040    x=Q                            : page 指定
16050    !=^HTMLTools
16060    "<h1>" $*=F[a*4+3] " - の編集</h1>"
16070    B*=Q                           : Page# をBにコピー
16080    x=Q !=^MakePathName
16090    "<form action='" $*=Z "' method='post' >" /
16100    "<input type=hidden name='time' value='" ?=F[a*4+0] "'>" /
16110    "<input type=hidden name='page' value='" $*=B "'>" /
16120    "<input type=submit name='preview' value='プレビュー' >" /
16130    "<input type=submit name='store' value='保存する' ><br />" /
16140    "<textarea cols='" ?=U['W'] "' rows='"
16150    ?=U['H'] "' name='msg' >" /
16160    |ca*=x                         : ファイルを cat
16170    "</textarea><br />" /
16180    "</form>" /
16190    "<p>" "</p>" /
16200    x=B !=^PathHelp
16210    |ca*=B
16220 ]
16230 :
16240 :-------------------------------------------------
16250 : プレビューの表示
16260 :-------------------------------------------------
16270 ^Preview
16280    +fz
16290    f=z z=z+256
16300    x*="Preview"                       : title 指定
16310    !=^HTMLHeader
16320    !=^HTMLTools
16330    "<h1>ページのプレビュー</h1>"
16340    !=^PageDBRead
16350    B*="page=" x=B y=Q !=^GetPost
16360    x=Q !=^ToVal  U['P']=r
16370    a=r !=^PageDBSearch n=r
16380    !=^GetMsg
16390    {=s }=s+r
16400    R*=Q x=Q B*="p" y=B !=^MergeStr
16410    f*=Q !=^MakePathName
16420    (*=x                               : テキスト書き込み
16430    !=^RenderWikiText
16440    x=f !=^MakeDatName                 : file名指定
16450    !=^DispWikiText
16460    :
16470    "<form action='" $*=Z "' method='post' >" /
16480    "<input type=hidden name=time value='" ?=F[n*4+0] "'>" /
16490    "<input type=hidden name=page value='" $*=R "'>" /
16500    "<input type=submit name='preview' value='プレビュー' >" /
16510    "<input type=submit name='store' value='保存する' ><br />" /
16520    "<textarea cols='" ?=U['W'] "' rows='"
16530    ?=U['H'] "' name='msg' >" /
16540    x=Q |ca*=x          : ファイルを cat
16550    "</textarea><br />" /
16560    "</form>" /
16570    -zf
16580 ]
16590 :
16600 :-------------------------------------------------
16610 : ページの保存結果の表示
16620 :-------------------------------------------------
16630 ^StorePage
16640    +qSz
16650    S=z z=z+256
16660    q=z z=z+256
16670    x=B !=^PathPages S*=B !=^LockWait
16680    ;=r<0 "<p>ファイルがロックされています</p>" -zSq ]
16690    !=^PageDBRead
16700    B*="page=" x=B y=Q !=^GetPost      : page #
16710    q*=Q
16720    x=Q !=^ToVal
16730    U['P']=r
16740    a=r !=^PageDBSearch n=r
16750    B*="time=" x=B y=R !=^GetPost      : タイムスタンプ
16760    x=R !=^ToVal t=r
16770    x=F[n*4+3]                         : title 指定
16780    !=^HTMLHeader
16790    x=Q                                : page 指定
16800    !=^HTMLTools
16810    "<h1>" $*=F[n*4+3] "</h1>"
16820 :
16830    ;=F[n*4+0]=t #=^sp00
16840       "<strong><p>ページが変更されています。保存されませんでした。<br />"
16850       "戻るボタンで戻って、編集内容をコピーして保存した後、"
16860       "変更履歴からもう一度ページを編集してください。</p></strong>"
16870       #=^sp01
16880 :
16890    ^sp00
16900    !=^GetMsg
16910    {=s }=s+r
16920    x=Q !=^MakePathName
16930    (*=x                               : テキスト書き込み
16940    !=^RenderWikiText
16950    a=n !=^UpdatePageTime
16960    !=^PageDBWrite                     : ページDB書き込み
16970 :
16980    ^sp01
16990    x=S
17000    !=^Unlock                          : アンロック
17010    x=q !=^MakeDatName                 : file名指定
17020    !=^DispWikiText
17030    -zSq
17040 ]
17050 :
17060 :-------------------------------------------------
17070 : コメントの最下部への追加
17080 :-------------------------------------------------
17090 ^DoAppend
17100    +qSz
17110    S=z z=z+256
17120    q=z z=z+256
17130    x=B !=^PathPages S*=B !=^LockWait
17140    ;=r<0 "<p>ファイルがロックされています</p>" -zSq ]
17150    !=^PageDBRead
17160    B*="page=" x=B y=Q !=^GetPost      : page #
17170    q*=Q
17180    x=Q !=^ToVal
17190    U['P']=r
17200    a=r !=^PageDBSearch n=r
17210    x=F[n*4+3]                         : title 指定
17220    !=^HTMLHeader
17230    x=Q                                : page 指定
17240    !=^HTMLTools
17250    "<h1>" $*=F[n*4+3] "</h1>"
17260    x=Q !=^MakePathName
17270    : 最下部に挿入
17280    !=^TextRead                        : 既存テキスト読み込み
17290    a=r
17300    w=T+r                              : テキスト最終
17310    w(0)=10 w(1)=0 w=w+1               : 改行挿入
17320    w*="----" w=w+%                    : <hr /> 文法に依存
17330    w(0)=10 w(1)=0 w=w+1               : 改行挿入
17340    t=_ s=R !=^TimeStr                 : 現在時刻の文字列
17350    w*="-" w=w+%                       : <ul> 文法に依存
17360    w*=s w=w+%                         : 時刻の挿入
17370    w(0)=10 w(1)=0 w=w+1               : 改行挿入
17380    !=^GetMsg                          : Pの領域
17390    w*=s w=w+%                         : テキストの追加
17400    a=w-T                              : テキストサイズ設定
17410 :
17420    !=^TextWrite                       : テキスト書き込み
17430    !=^RenderWikiText
17440    a=n !=^UpdatePageTime
17450    !=^PageDBWrite                     : ページDB書き込み
17460    x=S
17470    !=^Unlock                          : アンロック
17480 :
17490    x=q !=^MakeDatName                 : file名指定
17500    !=^DispWikiText                    : 表示
17510     -zSq
17520 ]
17530 :
17540 :-------------------------------------------------
17550 : コメントの最上部への追加
17560 :-------------------------------------------------
17570 ^DoTopAppend
17580    +qSz
17590    S=z z=z+256
17600    q=z z=z+256
17610    x=B !=^PathPages S*=B !=^LockWait
17620    ;=r<0 "<p>ファイルがロックされています</p>" -zSq ]
17630    !=^PageDBRead
17640    B*="page=" x=B y=Q !=^GetPost      : page #
17650    q*=Q
17660    x=Q !=^ToVal
17670    U['P']=r
17680    a=r !=^PageDBSearch n=r
17690    x=F[n*4+3]                             : title 指定
17700    !=^HTMLHeader
17710    x=Q                                : page 指定
17720    !=^HTMLTools
17730    "<h1>" $*=F[n*4+3] "</h1>"
17740    x=Q !=^MakePathName
17750    : 最上部に挿入
17760    +T
17770    t=_ s=R !=^TimeStr                 : 現在時刻の文字列
17780    T*="-" T=T+%                       : <ul> 文法に依存
17790    T*=s T=T+%                         : 時刻の挿入
17800    T(0)=10 T(1)=0 T=T+1               : 改行挿入
17810    !=^GetMsg                          : Pの領域
17820    T*=s T=T+%                         : コメントの挿入
17830    T(0)=10 T(1)=0 T=T+1               : 改行挿入
17840    T*="----" T=T+%                    : <hr /> 文法に依存
17850    T(0)=10 T(1)=0 T=T+1               : 改行挿入
17860    x=Q
17870    !=^TextRead                        : 既存テキスト読み込み
17880    t=T+r
17890    -T
17900    a=t-T                              : テキストサイズ設定
17910 :
17920    !=^TextWrite                       : テキスト書き込み
17930    !=^RenderWikiText
17940    a=n !=^UpdatePageTime
17950    !=^PageDBWrite                     : ページDB書き込み
17960    x=S
17970    !=^Unlock                          : アンロック
17980 :
17990    x=q !=^MakeDatName                 : file名指定
18000    !=^DispWikiText                    : 表示
18010     -zSq
18020 ]
18030 :
18040 :-------------------------------------------------
18050 : グループタイトルなどの変更
18060 :-------------------------------------------------
18070 ^ChangeGroup
18080    x*="ページ分類名の変更"              : title 指定
18090    !=^HTMLHeader
18100    !=^HTMLTools
18110    "<h1>ページ分類名の変更</h1>"
18120    !=^GroupDBRead
18130    "<p>"
18140    "<form action='" $*=Z "' method='post'>" /
18150    "  <strong>ページ分類を指定してください。</strong><br /> " /
18160    "  <select name='group'>" /
18170    i=0,O-1
18180      "    <option value='" ?=V[i*4+2] "'>" $*=V[i*4+3] "</option>" /
18190    @=i+1
18200    "  </select><br /><br />" /
18210    "  <strong>新しいページ分類の名前を入力してください。</strong><br />" /
18220    "  <input type='text' name='grouprename' value='' size='32'>" /
18230    "  <input type='submit' name='NewGroupName' value='変更'><br />" /
18240    "</form>" /
18250    "</p>" /
18260    !=^GroupDBRead
18270    !=^PageDBRead
18280    !=^GroupDBList
18290 ]
18300 :
18310 :-------------------------------------------------
18320 : ページタイトルなどの変更
18330 :-------------------------------------------------
18340 ^ChangePage
18350    x*="ページ情報の変更"                   : title 指定
18360    !=^HTMLHeader
18370    !=^HTMLTools
18380    !=^PageDBRead
18390    B*="page=" x=B y=Q !=^GetPost
18400    x=Q !=^ToVal
18410    a=r !=^PageDBSearch a=r
18420    "<h1>ページ情報の変更</h1>"
18430    !=^GroupDBRead
18440    "<p>"
18450    "<form action='" $*=Z "' method='post'>" /
18460    "  <input type='hidden' name='page' value='" $*=Q "'>" /
18470    "  <strong>ページ分類を指定してください。</strong><br /> " /
18480    "  <select name='group'>" /
18490    i=0,O-1
18500      "    <option value='"  ?=V[i*4+2]  "'"
18510      ;=(V[i*4+2]=F[a*4+2]) " selected"
18520      ">" $*=V[i*4+3] "</option>" /
18530    @=i+1
18540    "  </select><br /><br />" /
18550    "  <strong>変更するページの名前を入力してください。</strong><br /> " /
18560    "  <input type='text' name='newname' value='" $*=F[a*4+3] "' size='32'>"
18570    / "  <input type='submit' name='pagerename' value='変更'><br />" /
18580    "</form>" /
18590    "</p>" /
18600    !=^GroupDBList
18610 ]
18620 :
18630 :-------------------------------------------------
18640 : ページ名変更後の表示
18650 :-------------------------------------------------
18660 ^DoPageRename
18670    +Sz
18680    S=z z=z+256
18690    x*="ページ情報の変更"          : title 指定
18700    !=^HTMLHeader
18710    x=B !=^PathPages S*=B !=^LockWait
18720    ;=r<0 "<p>ファイルがロックされています</p>" -zS ]
18730    !=^PageDBRead
18740    B*="page=" x=B y=Q !=^GetPost
18750    x=Q !=^ToVal
18760    a=r !=^PageDBSearch a=r        : a = index
18770    !=^HTMLTools
18780    "<h1>ページ情報を変更しました</h1>"
18790    B*="newname=" x=B y=Q !=^GetPost
18800    B*="group=" x=B y=R !=^GetPost
18810    x=R !=^ToVal b=r               : b = group ID
18820    x=Q !=^UpdatePage
18830    !=^GroupDBRead
18840    a=0 b=1 c=0                    : 更新日付降順
18850    !=^PageDBList
18860    !=^PageDBWrite
18870    x=S
18880    !=^Unlock
18890    -zS
18900 ]
18910 :
18920 :-------------------------------------------------
18930 : グループ名変更後の表示
18940 :-------------------------------------------------
18950 ^DoGroupRename
18960    +Sz
18970    S=z z=z+256
18980    x*="ページ分類名の変更"        : title 指定
18990    !=^HTMLHeader
19000    !=^HTMLTools
19010    "<h1>ページ分類名を変更しました</h1>"
19020    x=B !=^PathGroups S*=B !=^LockWait
19030    ;=r<0 "<p>ファイルがロックされています</p>" -zS ]
19040    !=^GroupDBRead
19050    B*="group=" x=B y=R !=^GetPost
19060    x=R !=^ToVal a=r               : a = group ID
19070    B*="grouprename=" x=B y=R !=^GetPost x=R
19080    !=^UpdateGroup
19090    !=^PageDBRead
19100    !=^GroupDBList
19110    !=^GroupDBWrite
19120    x=S
19130    !=^Unlock
19140    -zS
19150 ]
19160 :
19170 :-------------------------------------------------
19180 : グループに属するページの一覧
19190 :-------------------------------------------------
19200 ^GroupList
19210    x*="ページ一覧"                : title 指定
19220    !=^HTMLHeader
19230    !=^HTMLTools
19240    "<h1>ページ一覧</h1>"
19250    B*="group=" x=B y=Q !=^GetPost
19260    x=Q !=^ToVal
19270    a=r
19280    !=^PageDBRead
19290    !=^GroupDBRead
19300    !=^GroupPageList
19310 ]
19320 :
19330 :-------------------------------------------------
19340 : パス名の生成
19350 : x : 1234567890 --> x: ./pages/1234567890.txt
19360 :-------------------------------------------------
19370 ^MakePathName
19380    +zwx
19390    w=z z=z+256
19400    w*=U+64
19410    y=x x=w       !=^MergeStr  : w=w+x
19420    x=w y*=".txt" !=^MergeStr  : w=w+".txt"
19430    -x
19440    x*=w
19450    -wz
19460 ]
19470 :
19480 :-------------------------------------------------
19490 : パス名の生成
19500 : x : 1234567890 --> x: ./pages/1234567890.dat
19510 :-------------------------------------------------
19520 ^MakeDatName
19530    +zwx
19540    w=z z=z+256
19550    w*=U+64
19560    y=x x=w       !=^MergeStr  : w=w+x
19570    x=w y*=".dat" !=^MergeStr  : w=w+".dat"
19580    -x
19590    x*=w
19600    -wz
19610 ]
19620 :
19630 :-------------------------------------------------
19640 : テキストリード x=FileName, T=BufferTop
19650 : r=bytes read
19660 :-------------------------------------------------
19670 ^TextRead
19680    {=T
19690    )*=x            : read file
19700    r=}-{
19710 ]
19720 :
19730 :-------------------------------------------------
19740 : テキストライト x=FileName, T=BufferTop a=size
19750 : r=bytes wrote
19760 :-------------------------------------------------
19770 ^TextWrite
19780    {=T }=T+a
19790    (*=x            : write file
19800    r=}-{
19810 ]
19820 :
19830 :-------------------------------------------------
19840 : ページ管理ファイルリード
19850 : ページ管理DB作成
19860 :-------------------------------------------------
19870 ^PageDBRead
19880    +zbxpqijZ
19890    b=z z=z+256
19900    {=A
19910    x=b !=^PathPages
19920    )*=b                           : read pages.txt
19930    Z=}-{
19940 :
19950    p=A
19960    q=D
19970    i=0
19980    ;=Z<20 #=^pdb00
19990    @
20000        x=p !=^ToVal F[i*4+1]=r
20010        @ p=p+1 @=(p(0)=9) p=p+1   : pをTABの次へ
20020        x=p !=^ToVal F[i*4+0]=r
20030        @ p=p+1 @=(p(0)=9) p=p+1   : pをTABの次へ
20040        x=p !=^ToVal F[i*4+2]=r
20050        @ p=p+1 @=(p(0)=9) p=p+1   : pをTABの次へ
20060        F[i*4+3]=q
20070        :
20080        : タイトルをD()にコピー
20090        j=0
20100        @
20110          q(j)=p(j)
20120          j=j+1
20130        @=(p(j-1)<' ')
20140        q(j-1)=0
20150        q=q+j
20160        p=p+j
20170        i=i+1
20180    @=(p>=(A+Z))
20190    ^pdb00
20200    C=i
20210    -Zjiqpxbz
20220 ]
20230 :
20240 :-------------------------------------------------
20250 : ページ管理DBに登録
20260 : a にグループNo
20270 : x にページタイトル
20280 :-------------------------------------------------
20290 ^RegistPage
20300    !=^CheckSpace ;=%=0 ]     : 名前長が０
20310    +tzywgx
20320    g=a
20330    w=z z=z+256
20340    y=z z=z+256
20350    F[C*4+1]=_
20360    a=F[C*4+1] s=B !=^ToStr w*=s
20370    x=B !=^MakePathName
20380    {=T
20390    }=T
20400    (*=x                     : xxx.txt
20410    x=w !=^MakeDatName
20420    (*=x                     : xxx.dat
20430    F[C*4+0]=F[C*4+1]
20440    F[C*4+2]=g
20450    ;=C>0 t=F[(C-1)*4+3]
20460    ;=C>0 @ t=t+1 @=(t(0)=0) t=t+1
20470    ;=C>0 F[C*4+3]=t
20480    ;=C=0 F[3]=D t=D
20490    -x
20500    t*=x
20510    C=C+1
20520    -gwyzt
20530 ]
20540 :
20550 :-------------------------------------------------
20560 : ページ管理DBを更新
20570 : a にインデックス、 b にグループNo
20580 : x にページタイトル
20590 :-------------------------------------------------
20600 ^UpdatePage
20610    !=^CheckSpace ;=%=0 ]     : 名前長が０
20620    +t
20630    F[a*4+2]=b
20640    ;=C>0 t=F[(C-1)*4+3]
20650    ;=C>0 @ t=t+1 @=(t(0)=0) t=t+1
20660    ;=C>0 F[a*4+3]=t : 最後部に新規割り当て
20670    ;=C=0 F[3]=D t=D
20680    t*=x
20690    -t
20700 ]
20710 :
20720 :-------------------------------------------------
20730 : ページ管理DBのタイムスタンプを更新
20740 : a にインデックス
20750 :-------------------------------------------------
20760 ^UpdatePageTime
20770    F[a*4+0]=_
20780 ]
20790 :
20800 :-------------------------------------------------
20810 : ページ管理DBリスト
20820 : ソート a=0:更新日付、1:グループ
20830 : 順序   b=0:昇順、    1:降順
20840 : 表示数 c=0:すべて    0以外:指定数
20850 :-------------------------------------------------
20860 ^PageDBList
20870    +ihn
20880    n=C            : ソート
20890    ;=n<2 #=^pdbl00
20900    ;=a=0 h=0
20910    ;=a=1 h=2
20920    ;=b=0 !=^HeapSort4
20930    ;=b=1 !=^HeapSort4d
20940    ^pdbl00
20950    "<table>" /
20960    "<tr><th>ページタイトル</th><th>最終更新日付</th>"
20970    "<th>ページ分類</th></tr>" /
20980    ;=C=0 #=^pdbl01
20990    ;=c=0 c=C
21000    i=0,c-1
21010      "<tr><td>"
21020      "<a href='" $*=Z "?DispPage&page=" ?=F[i*4+1]
21030      "&amp;UpdateTime=" ?=F[i*4+0] "'>"
21040      $*=F[i*4+3] "</a>"
21050      "</td><td>" /
21060      t=F[i*4+0] s=B !=^LocalTime
21070      ?=s{5} "/" ?[2]=s{4} "/" ?[2]=s{3} " "
21080      ?[2]=s{2} ":" ?[2]=s{1} ":" ?[2]=s{0}
21090      "</td><td>"
21100      a=F[i*4+2] !=^GroupDBSearch
21110      "<a href='" $*=Z "?GroupList&group=" ?=a "'>" $*=s "</a></td></tr>"
21120    @=i+1
21130    ^pdbl01
21140    "</table>" /
21150    -nhi
21160 ]
21170 :
21180 :-------------------------------------------------
21190 : ページ管理DB検索
21200 : a にファイル番号を渡す
21210 : r にインデックスを返す。r=-1 は未発見
21220 :-------------------------------------------------
21230 ^PageDBSearch
21240    +if
21250    f=0
21260    i=0
21270    @
21280      ;=F[i*4+1]=a f=1
21290      i=i+1
21300    @=((i>=C)|(f=1))
21310    ;=i<=C r=i-1 -fi ]         : found
21320    r=-1                       : not found
21330    -fi
21340 ]
21350 :
21360 :-------------------------------------------------
21370 : グループに属するページリスト
21380 : a にグループ番号
21390 :-------------------------------------------------
21400 ^GroupPageList
21410    +i
21420    !=^GroupDBSearch "<h2>" $*=s "</h2>" /
21430    "<table>" /
21440    "<tr><th>ページタイトル</th><th>最終更新日付</th>"
21450    "<th>ページ分類</th></tr>" /
21460    ;=C=0 #=^gpl01
21470    i=0,C-1
21480      ;=F[i*4+2]<>a  #=^gpl00
21490      "<tr><td>"
21500      "<a href='" $*=Z "?DispPage&page=" ?=F[i*4+1] "'>"
21510      $*=F[i*4+3] "</a>"
21520      "</td><td>" /
21530      t=F[i*4+0] s=B !=^LocalTime
21540      ?=s{5} "/" ?[2]=s{4} "/" ?[2]=s{3} " "
21550      ?[2]=s{2} ":" ?[2]=s{1} ":" ?[2]=s{0}
21560      "</td><td>"
21570      a=F[i*4+2] !=^GroupDBSearch
21580      $*=s  "</td></tr>"
21590      ^gpl00
21600    @=i+1
21610    ^gpl01
21620    "</table>" /
21630    -i
21640 :
21650 :-------------------------------------------------
21660 : ページ管理ファイル書き出し
21670 :-------------------------------------------------
21680 ^PageDBWrite
21690    +bpisz
21700    b=z z=z+256
21710    p=A
21720    ;=C=0 #=^pdbw01
21730    i=0,C-1
21740      a=F[i*4+1] s=p !=^ToStr p=p+r p(0)=9 p=p+1
21750      a=F[i*4+0] s=p !=^ToStr p=p+r p(0)=9 p=p+1
21760      a=F[i*4+2] s=p !=^ToStr p=p+r p(0)=9 p=p+1
21770      t=F[i*4+3]
21780      p*=t p=p+% p(0)=10 p=p+1
21790    @=i+1
21800    {=A }=p
21810    x=b !=^PathPages
21820    (*=b                           : write pages.txt
21830    ^pdbw01
21840    -zsipb
21850 ]
21860 :
21870 :-------------------------------------------------
21880 : グループ管理ファイルリード
21890 : グループ管理DB作成
21900 :-------------------------------------------------
21910 ^GroupDBRead
21920    +xZpqijbz
21930    b=z z=z+256
21940    {=X
21950    x=b !=^PathGroups
21960    )*=b                           : read groups.txt
21970    Z=}-{
21980    :
21990    p=X
22000    q=Y
22010    i=0
22020    ;=Z<20 #=^gdb00
22030    @
22040        x=p !=^ToVal V[i*4]=r      : 作成日付
22050        @ p=p+1 @=(p(0)=9) p=p+1   : pをTABの次へ
22060        x=p !=^ToVal V[i*4+1]=r    : 作成日付と同じ
22070        @ p=p+1 @=(p(0)=9) p=p+1   : pをTABの次へ
22080        x=p !=^ToVal V[i*4+2]=r    : ID
22090        @ p=p+1 @=(p(0)=9) p=p+1   : pをTABの次へ
22100        V[i*4+3]=q                 : 名前
22110        :
22120        : タイトルをY()にコピー
22130        j=0
22140        @
22150          q(j)=p(j)
22160          j=j+1
22170        @=(p(j-1)<' ')
22180        q(j-1)=0
22190        q=q+j
22200        p=p+j
22210        i=i+1
22220    @=(p>=(X+Z))
22230    ^gdb00
22240    O=i
22250    -zbjiqpZx
22260 ]
22270 :
22280 :-------------------------------------------------
22290 : グループ管理DBに登録
22300 : x にグループタイトル
22310 :-------------------------------------------------
22320 ^RegistGroup
22330    !=^CheckSpace ;=%=0 ]     : 名前長が０
22340    +t
22350    V[O*4]=_
22360    V[O*4+1]=V[O*4]
22370    V[O*4+2]=O
22380    ;=O>0 t=V[(O-1)*4+3]
22390    ;=O>0 @ t=t+1 @=(t(0)=0) t=t+1
22400    ;=O>0 V[O*4+3]=t
22410    ;=O=0 V[3]=D t=D
22420    t*=x
22430    O=O+1
22440    -t
22450 ]
22460 :
22470 :-------------------------------------------------
22480 : グループ管理ファイル書き出し
22490 :-------------------------------------------------
22500 ^GroupDBWrite
22510    +pibaz
22520    b=z z=z+256
22530    p=X
22540    i=0,O-1
22550      a=V[i*4]   s=p !=^ToStr p=p+r p(0)=9 p=p+1
22560      a=V[i*4+1] s=p !=^ToStr p=p+r p(0)=9 p=p+1
22570      a=V[i*4+2] s=p !=^ToStr p=p+r p(0)=9 p=p+1
22580      t=V[i*4+3]
22590      p*=t p=p+% p(0)=10 p=p+1
22600    @=i+1
22610    {=X }=p
22620    x=b !=^PathGroups
22630    (*=b                           : write groups.txt
22640    -zabip
22650 ]
22660 :
22670 :-------------------------------------------------
22680 : グループ管理ファイル検索
22690 : a にgroup ID
22700 : r にインデックス、s にグループ名アドレスを返す
22710 :-------------------------------------------------
22720 ^GroupDBSearch
22730    +if
22740    i=0 f=0
22750    @
22760      ;=a=V[i*4+2] s=V[i*4+3] f=1
22770      i=i+1
22780    @=((i>=O)|f=1)
22790    ;=f=0 r=-1 -fi ]
22800    r=i-1
22810    -fi
22820 ]
22830 :
22840 :-------------------------------------------------
22850 : グループ管理DBリスト
22860 :-------------------------------------------------
22870 ^GroupDBList
22880    +tgeji
22890    "<table>" /
22900    "<tr><th>ページ分類</th><th>ページ数</th><th>最新日付</th></tr>" /
22910    ;=O=0 #=^gdbl02
22920    i=0,O-1
22930      "<tr><td>"
22940      "<a href='" $*=Z "?GroupList&group=" ?=V[i*4+2] "'>"
22950      $*=V[i*4+3] "</a></td><td align='center'>"
22960      g=0 e=0
22970      ;=C=0 #=^gdbl01
22980      j=0,C-1
22990        ;=F[j*4+2]=V[i*4+2] g=g+1 ;=F[j*4+0]>e e=F[j*4+0]
23000      @=j+1
23010      ^gdbl01
23020      ?=g
23030      "</td><td>" /
23040      t=e s=Q !=^LocalTime
23050      ?=s{5} "/" ?[2]=s{4} "/" ?[2]=s{3} " "
23060      ?[2]=s{2} ":" ?[2]=s{1} ":" ?[2]=s{0}
23070      "</td></tr>"
23080    @=i+1
23090    ^gdbl02
23100    "</table>" /
23110    -ijegt
23120 ]
23130 :
23140 :-------------------------------------------------
23150 : 名称が空白のみなら長さ 0 を返す
23160 :-------------------------------------------------
23170 ^CheckSpace
23180    +fki
23190    x*=x k=%
23200    i=0 f=0
23210    @
23220      ;=x(i)<>' ' f=1
23230      i=i+1
23240    @=((f=1)|(i>=k))
23250    ;=f=0 %=0
23260    -ikf
23270 ]
23280 :
23290 :-------------------------------------------------
23300 : グループ管理ファイル検索
23310 : a にgroup ID
23320 : x に新グループ名
23330 :-------------------------------------------------
23340 ^UpdateGroup
23350    !=^CheckSpace ;=%=0 ]     : 名前長が０
23360    +rst
23370    t=V[(O-1)*4+3]
23380    @ t=t+1 @=(t(0)=0) t=t+1
23390    !=^GroupDBSearch
23400    V[r*4+3]=t t*=x  : 最後部に新規割り当て
23410    -tsr
23420 ]
23430 :
23440 :-------------------------------------------------
23450 : Get Post Data
23460 : POST文字列中の x で示された文字列に続くデータを
23470 : y の示す領域にコピー
23480 : r にデータの文字数を返す
23490 :-------------------------------------------------
23500 ^GetPost
23510     !=^SearchPost             : r に文字列アドレス
23520     ;=r=0 ]                   : 長さ0ならばreturn
23530     x=r
23540     y*=x r=%
23550 ]
23560 :
23570 :-------------------------------------------------
23580 : Get Post Msg
23590 : POST文字列中の msg= に続くデータのアドレスを取得
23600 : s にデータの文字列先頭アドレスを返す
23610 : r にデータの文字数を返す
23620 :-------------------------------------------------
23630 ^GetMsg
23640     +x
23650     B*="msg=" x=B
23660     !=^SearchPost             : r に文字列アドレス
23670     ;=r=0 -x ]                : 長さ0ならばreturn
23680     x=r s=r
23690     !=^StrLen
23700     -x
23710 ]
23720 :
23730 :-------------------------------------------------
23740 : HTML Header
23750 : x にタイトル
23760 :-------------------------------------------------
23770 ^HTMLHeader
23780   "<title>" $*=x "</title>" /
23790   "<link rel='stylesheet' type='text/css' href='"
23800   x=B !=^PathCSS $*=B
23810   "' />" /
23820   "</head>" / /
23830   "<body class='normal'>" / "<!--  -->" //
23840 ]
23850 :
23860 :-------------------------------------------------
23870 : Wiki Tools
23880 : x にページ
23890 :-------------------------------------------------
23900 ^HTMLTools
23910   / "<div id='menu'>" / "<ul>" /
23920   "<li class='top'><a href='" $*=Z "?FrontPage'>目次</a></li>" /
23930   ;=Mode='Disp' "<li><a href='" $*=Z "?Edit&page=" $*=x "'>編集</a></li>" /
23940   ;=Mode='Disp' "<li><a href='" $*=Z "?Append&page=" $*=x "'>追記</a></li>" /
23950   ;=Mode='Disp' "<li><a href='" $*=Z "?Static&page=" $*=x "'>静的</a></li>" /
23960   ;=Mode='DoAp' "<li><a href='" $*=Z "?Edit&page=" $*=x "'>編集</a></li>" /
23970   ;=Mode='DoAp' "<li><a href='" $*=Z "?Append&page=" $*=x "'>追記</a></li>" /
23980   ;=Mode='Stor' "<li><a href='" $*=Z "?Edit&page=" $*=x "'>編集</a></li>" /
23990   ;=Mode='Stor' "<li><a href='" $*=Z "?Append&page=" $*=x "'>追記</a></li>" /
24000   "<li><a href='" $*=Z "?RecentChanges&count=" ?=U['R']
24010     "'>更新履歴</a></li>" /
24020   "<li><a href='" $*=Z "?IndexPage'>一覧</a></li>" /
24030   "<li><a href='" $*=Z "?CreatePage'>新規ページ</a></li>" /
24040   "<li><a href='" $*=Z "?CreateGroup'>新規ページ分類</a></li>" /
24050   "<li><a href='" $*=Z "?ChangeGroup'>ページ分類変更</a></li>" /
24060   ;=Mode='Disp' "<li><a href='" $*=Z "?ChangePage&page="
24070   ;=Mode='Disp' $*=x "'>ページ変更</a>" /
24080   ;=Mode='DoAp' "<li><a href='" $*=Z "?ChangePage&page="
24090   ;=Mode='DoAp' $*=x "'>ページ変更</a>" /
24100   ;=Mode='Stor' "<li><a href='" $*=Z "?ChangePage&page="
24110   ;=Mode='Stor' $*=x "'>ページ変更</a>" /
24120   ;=Mode='Frnt' "<li><a href='" $*=Z "?RSS"
24130   ;=Mode='Frnt' "'>RSS</a>" /
24140   "</ul>" / "</div>" / /
24150 ]
24160 :
24170 :-------------------------------------------------
24180 : Read REMOTE_ADDR
24190 : r : IPアドレスを32ビット整数化
24200 :-------------------------------------------------
24210 ^REMOTE_ADDR
24220    +xszij
24230    x=z z=z+32
24240    s=z z=z+32
24250    x*="REMOTE_ADDR="
24260    !=^SearchEnv
24270    r=0
24280    i=0
24290    @
24300      j=0 r=r<<8
24310      @
24320        j=j*10+(s(i)-$30)
24330        i=i+1
24340      @=((s(i)='.')|(s(i)=0))
24350      r=r|j
24360      ;=(s(i)='.') i=i+1
24370    @=(s(i)=0)
24380    -jizxs
24390 ]
24400 :
24410 :-------------------------------------------------
24420 : Set REMOTE_ADDR
24430 : in  s : バッファ先頭アドレス
24440 : in  a : 32ビット整数のIPアドレス
24450 : out s : IPアドレス文字列
24460 :-------------------------------------------------
24470 ^SetADDR
24480    +sabcde
24490    b=a>>24
24500    c=(a>>16)&$FF
24510    d=(a>>8)&$FF
24520    e=a&$FF
24530    a=b !=^ToStr
24540    s(r)='.'
24550    a=c s=s+r+1 !=^ToStr
24560    s(r)='.'
24570    a=d s=s+r+1 !=^ToStr
24580    s(r)='.'
24590    a=e s=s+r+1 !=^ToStr
24600    s(r)=0
24610    -edcbas
24620 ]
24630 :
24640 :-------------------------------------------------
24650 : Read REQUEST_METHOD
24660 : r='GET' or r='POST'
24670 :-------------------------------------------------
24680 ^REQUEST
24690    x*="REQUEST_METHOD="
24700    !=^SearchEnv
24710    r=s(0)
24720 ]
24730 :
24740 :-------------------------------------------------
24750 : Get Query_String
24760 :
24770 : P() : QUERY_STRINGデータ
24780 : L[] : QUERYデータ文字列先頭配列
24790 : K   : QUERY_STRING文字列数
24800 :-------------------------------------------------
24810 ^RequestGet
24820     x*="QUERY_STRING=" s=W
24830     !=^SearchEnv
24840     x=W !=^StrLen
24850     a=r
24860     ;=r=0 #=^rg00
24870     i=0,r-1
24880       ;=W(i)='&' W(i)=0            : 文字列末
24890     @=i+1
24900     ^rg00
24910     x=W s=P !=^URLDEC2             : 一括変換
24920     L[0]=W                         : 先頭要素のアドレス
24930     w=W
24940     ;=r<=0 w(0)=0 K=j ]            : 20060516
24950     i=0,r-1
24960       c=P(i)
24970       ;=c=0 w(0)=0 w=w+1 j=j+1 L[j]=w #=^rg_next : 行先頭の登録
24980       ;=c>'>' w(0)=c w=w+1       #=^rg_next
24990       ;=c='"' w*="&quot;" w=w+%  #=^rg_next
25000       ;=c='<' w*="&lt;"   w=w+%  #=^rg_next
25010       ;=c='>' w*="&gt;"   w=w+%  #=^rg_next
25020       ;=c='&' w*="&amp;"  w=w+%  #=^rg_next
25030       w(0)=c w=w+1
25040       ^rg_next
25050     @=i+1
25060     w(0)=0 K=j                            : 要素の数
25070 ]
25080 :
25090 :-------------------------------------------------
25100 : 標準入力からPOSTされた文字列を取得
25110 :
25120 : W : ワーク領域、URLデコード+サニタイズ済みを返す
25130 : P : POST文字列(URLデコード済み)保存
25140 : L : POSTデータ文字列先頭配列
25150 : K : POST文字列数
25160 :-------------------------------------------------
25170 ^RequestPost
25180     +wacxijrs
25190     : CONTENT_LENGTH環境変数からデータ長を取得
25200     x*="CONTENT_LENGTH=" s=W
25210     !=^SearchEnv
25220     x=s
25230     !=^ToVal                       : データ長を数値化
25240     ;=((r<0)|(r>(N*3))) r=0 #=^rp00
25250     a=r x=W !=^SYSRead             : W にコピー
25260     i=0,a-1
25270       ;=W(i)='&' W(i)=0            : 文字列末
25280     @=i+1
25290    ^rp00
25300     W(i)=0                         :
25310     x=W s=P a=i !=^URLDEC2         : 一括変換
25320     L[0]=W  P(r)=0                 : 先頭要素のアドレス
25330     w=W j=0                        : W に戻す
25340     i=0,r-1
25350       c=P(i)
25360       ;=c=0 w(0)=0 w=w+1 j=j+1 L[j]=w #=^rp_next : 行先頭の登録
25370       ;=c>'>' w(0)=c w=w+1       #=^rp_next
25380       ;=c='"' w*="&quot;" w=w+%  #=^rp_next
25390       ;=c='<' w*="&lt;"   w=w+%  #=^rp_next
25400       ;=c='>' w*="&gt;"   w=w+%  #=^rp_next
25410       ;=c='&' w*="&amp;"  w=w+%  #=^rp_next
25420       w(0)=c w=w+1
25430       ^rp_next
25440     @=i+1
25450     w(0)=0
25460     K=j                            : 要素の数
25470     -srjixcaw
25480 ]
25490 :
25500 :-------------------------------------------------
25510 : x に検索文字列を設定
25520 : L[]にPOST文字列(URL decoded)の行頭アドレス
25530 : K にデータ要素数
25540 : r にデータ先頭アドレスを返す (0 なら無し)
25550 :-------------------------------------------------
25560 ^SearchPost
25570     +yi
25580     i=0
25590     @
25600       y=L[i]
25610       !=^CompareStr
25620       i=i+1
25630     @=((r>0)|(i>K))
25640     ;=r=0 -iy ]
25650     r=y+r
25660     -iy
25670 ]
25680 :
25690 :-------------------------------------------------
25700 : x に検索文字列を設定
25710 : L[]に行頭アドレス、PにPOST文字列(URL decoded)
25720 : a にデータ長
25730 : r にデータ先頭アドレスを返す (0 なら無し)
25740 :-------------------------------------------------
25750 ^SearchQuery
25760     +yi
25770     i=0
25780     @
25790       y=L[i]
25800       !=^CompareStr
25810       i=i+1
25820     @=((r>0)|(i>a))
25830     ;=r=0 -iy ]
25840     r=y+r
25850     -iy
25860 ]
25870 :
25880 :-----------------------------------------
25890 : 環境変数を検索
25900 :
25910 : x と s に 領域を確保
25920 :   x="検索文字列"
25930 :   s に値の文字列を格納
25940 :   未発見なら r=0 s(0)=0
25950 :-----------------------------------------
25960 ^SearchEnv
25970     +if                       : 変数退避
25980     [=0                       : 範囲チェックOnn
25990     i=0
26000     @
26010       y=\\i                   : 環境変数
26020       f=0
26030       ;=y=0 f=1
26040       ;=y<>0 ;=y(0)=0 f=1
26050       ;=f=0 !=^CompareStr
26060       i=i+1
26070     @=((f=1)|(r>0))
26080     ;=r=0 s(0)=0 -i ]
26090     y=y+r i=0
26100     +xy
26110     x=y y=s
26120     !=^CopyStr                : copy y to s
26130     -yx
26140     [=1                       : 範囲チェック ON
26150     -fi                       : 変数復帰
26160 ]
26170 :
26180 :-------------------------------------
26190 : 4バイト配列のヒープソート昇順
26200 : F[] のソート
26210 :  h=0:time, h=1:fname, h=2:GrNo, h=3:pointer
26220 : n に要素の個数
26230 :-------------------------------------
26240 ^HeapSort4
26250     +rkijf
26260     f=F-16                    : F[0]=f[1]
26270     k=n/2 r=n
26280     i=k
26290     @
26300       k=i
26310       !=^DownHeap4            : downheap(i,n)
26320       i=i-1
26330     @=(i<1)
26340     i=r
26350     @
26360       k=1 j=i !=^HeapSwap4    : swap(1,i)
26370       k=1 r=i-1 !=^DownHeap4  : downheap(1,i-1)
26380       i=i-1
26390     @=(i<2)
26400     -fjikr
26410 ]
26420 :
26430 :-------------------------------------
26440 : DownHeap (k, r) 昇順
26450 :-------------------------------------
26460 ^DownHeap4
26470     +krj
26480    ^h4shift01
26490     j=2*k
26500     ;=j>r #=^h4shift02
26510     ;=j<>r ;=f[(j+1)*4+h]>f[j*4+h] j=j+1
26520     ;=f[k*4+h]>=f[j*4+h] #=^h4shift02
26530     !=^HeapSwap4
26540     k=j
26550     #=^h4shift01
26560    ^h4shift02
26570     -jrk
26580 ]
26590 :
26600 :-------------------------------------
26610 : 4バイト配列のヒープソート降順
26620 : F[] のソート
26630 : h=0:time, h=1:fname, h=2:GrNo, h=3:pointer
26640 : n に要素の個数
26650 :-------------------------------------
26660 ^HeapSort4d
26670     +rkijf
26680     f=F-16
26690     k=n/2 r=n
26700     i=k
26710     @
26720       k=i
26730       !=^DownHeap4d            : downheap(i,n)
26740       i=i-1
26750     @=(i<1)
26760     i=r @
26770       k=1 j=i !=^HeapSwap4    : swap(1,i)
26780       k=1 r=i-1 !=^DownHeap4d  : downheap(1,i-1)
26790       i=i-1
26800     @=(i<2)
26810     -fjikr
26820 ]
26830 :
26840 :-------------------------------------
26850 : DownHeap (k, r) 降順
26860 :-------------------------------------
26870 ^DownHeap4d
26880     +krj
26890    ^h4shift03
26900     j=2*k
26910     ;=j>r #=^h4shift02
26920     ;=j<>r ;=f[(j+1)*4+h]<f[j*4+h] j=j+1
26930     ;=f[k*4+h]<=f[j*4+h] #=^h4shift04
26940     !=^HeapSwap4
26950     k=j
26960     #=^h4shift03
26970    ^h4shift04
26980     -jrk
26990 ]
27000 :
27010 :-------------------------------------
27020 : 4バイト配列データのSwap
27030 : Swap (k, j)
27040 :-------------------------------------
27050 ^HeapSwap4
27060     +wjk
27070     j=j-1 k=k-1     : F,E,G,Hの添え字は[0]から
27080     w=F[j*4+1] F[j*4+1]=F[k*4+1] F[k*4+1]=w
27090     w=F[j*4+0] F[j*4+0]=F[k*4+0] F[k*4+0]=w
27100     w=F[j*4+2] F[j*4+2]=F[k*4+2] F[k*4+2]=w
27110     w=F[j*4+3] F[j*4+3]=F[k*4+3] F[k*4+3]=w
27120     -kjw
27130 ]
27140 :
27150 :==========================================================================
27160 : 汎用ライブラリ
27170 :==========================================================================
27180 :-----------------------------------------
27190 : t に現在時刻 (UNIX時間1970/1/1 0:00:00
27200 : からの経過秒数)を渡す。t=_
27210 : 配列 s に時刻文字列を返す
27220 :-----------------------------------------
27230 ^TimeStr
27240     +zuvwx
27250     u=z z=z+256
27260     v=z z=z+256
27270     !=^LocalTime
27280     x=s s=v
27290     w=u                                    : 文字列先頭を保存
27300     a=x{5} !=^ToStr                        : year
27310     u*=v   u=u+%
27320     u*="/" u=u+%
27330     ;=x{4}<=9 u*="0" u=u+%
27340     a=x{4} !=^ToStr  u*=v u=u+%            : month
27350     u*="/" u=u+%
27360     ;=x{3}<=9 u*="0" u=u+%
27370     a=x{3} !=^ToStr  u*=v u=u+%            : day
27380     u*=" " u=u+%
27390     ;=x{2}<=9 u*="0" u=u+%
27400     a=x{2} !=^ToStr  u*=v u=u+%            : hour
27410     u*=":" u=u+%
27420     ;=x{1}<=9 u*="0" u=u+%
27430     a=x{1} !=^ToStr  u*=v u=u+%            : min
27440     u*=":" u=u+%
27450     ;=x{0}<=9 u*="0" u=u+%
27460     a=x{0} !=^ToStr  u*=v   u=u+%          : sec
27470     s*=w
27480     -xwvuz
27490 ]
27500 :-----------------------------------------
27510 : t に現在時刻 (UNIX時間1970/1/1 0:00:00
27520 : からの経過秒数)を渡す。t=_
27530 : 2バイト配列 s に以下の情報を返す
27540 : s{0} : sec   0..59
27550 : s{1} : min   0..59
27560 : s{2} : hour  0..23
27570 : s{3} : day   0..31
27580 : s{4} : month 1..12
27590 : s{5} : year  1980-
27600 : s{6} : week day 0-6
27610 :-----------------------------------------
27620 ^LocalTime
27630     +myTdwxiMVz
27640     m=z z=z+16
27650     m(1)=31 m(2)=28 m(3)=31 m(4)=30 m(5)=31 m(6)=30
27660     m(7)=31 m(8)=31 m(9)=30 m(10)=31 m(11)=30 m(12)=31
27670     : 2*(4*365+1)*24*60*60+(2*365*24*60*60)|-(9*3600)
27680     y=1980
27690     :T=315532800 : 1980/1/1 00:00:00 UTC
27700     T=315500400 : 1980/1/1 00:00:00 JST
27710     t=t-T ;=t<0 t=0
27720     t=t/60 s{0}=%                          : sec
27730     t=t/60 s{1}=%                          : min
27740     d=t/24 s{2}=%                          : hour
27750     w=366+365+365+365                      : w=1461days/4years
27760     x=d/w                                  : x=year*4
27770     y=y+(x*4)
27780     d=%                                    : days in 4years(0..1460)
27790     ;=d<=365 m(2)=29 x=0 d=d               : leap year
27800     ;=d>365 d=d-366 x=d/365 d=% x=x+1      : normal year
27810     y=y+x                                  : year
27820     i=1
27830     @
27840       ;=(d>=m(i)) d=d-m(i) i=i+1
27850     @=(d<m(i))
27860     M=i
27870     s{5}=y s{4}=M s{3}=d+1
27880     ;=(y<=2) y=y+12
27890     V=(y+(y/4)-(y/100)+(y/400)+((13*M+8)/5)+d)/7 s{6}=%
27900     -zVMixwdTym
27910 ]
27920 :
27930 :-------------------------------------------------
27940 : 10進数文字列 --> 数値変換
27950 :
27960 : x から始まる文字列を数値に変更して
27970 : r に値を返す。
27980 :-------------------------------------------------
27990 ^ToVal
28000     +i
28010     i=0
28020     r=0
28030     ;=(x(i)<'0')+(x(i)>'9') -i ]
28040     @
28050       r=r*10+(x(i)-$30)
28060       i=i+1
28070     @=((x(i)<'0')+(x(i)>'9'))
28080     -i
28090 ]
28100 :
28110 :-------------------------------------------------
28120 : 数値 --> 10進数文字列変換
28130 :
28140 : a の数値を文字列に変換して s からの領域に
28150 : 文字列として返す。
28160 : r に文字数を返す
28170 :-------------------------------------------------
28180 ^ToStr
28190     +aij
28200     i=0
28210     @
28220       a=a/10 +=%  : スタックにプッシュ
28230       i=i+1
28240     @=(a=0)
28250     j=0
28260     @
28270       i=i-1
28280       s(j)=;+$30  : スタックからポップ
28290       j=j+1
28300     @=(i=0)
28310     s(j)=0
28320     r=j
28330     -jia
28340 ]
28350 :
28360 :-------------------------------------------------
28370 : 文字列長の取得
28380 :
28390 : x に文字列を指定、ｒに文字数が返る
28400 :-------------------------------------------------
28410 ^StrLen
28420    x*=x
28430    r=%
28440 ]
28450 :
28460 :-------------------------------------------------
28470 : 部分文字列の比較   length(x) <= length(y)
28480 :
28490 : x の示す文字列が y の示す文字列と一致したら
28500 : r=文字列末または初めて異なる文字の位置
28510 : 一致していなければ r=0 を返す
28520 :-------------------------------------------------
28530 ^CompareStr
28540     +if
28550     i=-1
28560     f=0
28570     @
28580       i=i+1
28590       ;=(x(i)=y(i))&(x(i)=0) f=1  : 発見
28600       ;=x(i)<>y(i) f=2            : 違う
28610     @=((x(i)=0)|(f<>0))
28620     ;=i>0 ;=f=1 r=i
28630     ;=(x(i)=0)&(f=2)) r=i
28640     ;=(x(i)<>0) r=0
28650     -fi
28660 ]
28670 :
28680 :-------------------------------------------------
28690 : Copy String
28700 :
28710 :  x() : string1 (source)
28720 :  y() : string2 (destinnation)
28730 : return
28740 :  r   : length
28750 :-------------------------------------------------
28760 ^CopyStr
28770     y*=x
28780     r=%
28790 ]
28800 :
28810 :-------------------------------------------------
28820 : Concatinate string
28830 :
28840 :  x() : string1 (<255byte)
28850 :  y() : string2 (<255byte)
28860 : return
28870 :  s() : string1+string2
28880 :  r   : length
28890 :-------------------------------------------------
28900 ^ConcatStr
28910    s*=x r=%
28920    +s
28930    s=s+r s*=y
28940    -s
28950    r=r+%
28960 ]
28970 :
28980 :-------------------------------------------------
28990 : Merge string
29000 :
29010 :  x() : string1 (<255byte)
29020 :  y() : string2 (<255byte)
29030 : return
29040 :  x() : string1 + string2
29050 :  r   : length
29060 :-------------------------------------------------
29070 ^MergeStr
29080    !=^StrLen             : r = length(x)
29090    +x
29100    x=x+r
29110    x*=y
29120    r=r+%
29130    -x
29140 ]
29150 :
29160 :-------------------------------------
29170 : URLデコード
29180 :
29190 : x にURLエンコードした文字列を設定
29200 : s にデコード後の文字列を返す
29210 : r にデコード後の文字数を返す
29220 :-------------------------------------
29230 ^URLDEC
29240     +a
29250     !=^StrLen
29260     a=r
29270     !=^URLDEC2
29280     -a
29290 ]
29300 :
29310 :-------------------------------------
29320 : URLデコード2
29330 :
29340 : x にURLエンコード文字列の先頭設定
29350 : a に変更範囲の文字数を設定
29360 : s にデコード後の文字列を返す
29370 : r にデコード後の文字数を返す
29380 :-------------------------------------
29390 ^URLDEC2
29400    +uz
29410    u=z+16
29420    u[0]=x u[1]=a u[2]=s
29430    |ud
29440    r=u[3]
29450    -zu
29460 ]
29470 :
29480 :-------------------------------------------------
29490 : symlink
29500 : x() : oldname
29510 : y() : newname
29520 :-------------------------------------------------
29530 ^Symlink
29540   +abc
29550   a=83              : symlink
29560   b=x               : oldname
29570   c=y               : newname
29580   |zz
29590   r=|
29600   -cba
29610 ]
29620 :
29630 :-------------------------------------------------
29640 : unlink
29650 : x() : pathname
29660 :-------------------------------------------------
29670 ^Unlink
29680   +ab
29690   a=10              : unlink
29700   b=x               : name
29710   |zz
29720   r=|
29730   -ba
29740 ]
29750 :-------------------------------------------------
29760 : lock
29770 : x() : filename to be locked
29780 :-------------------------------------------------
29790 ^Lock
29800   +cyz
29810   c=z z=z+256
29820   y=z z=z+32
29830   y*=".lock"
29840   s=c               : to store x+y
29850   !=^ConcatStr
29860   y=s               : newname
29870   !=^Symlink
29880   -zyc
29890 ]
29900 :
29910 :-------------------------------------------------
29920 : lock & wait
29930 : x() : filename to be locked
29940 : r=0 : success, r=-1 : failure
29950 :-------------------------------------------------
29960 ^LockWait
29970   +ie
29980   i=0
29990   @
30000     "<!-- "
30010     !=^Lock
30020     " --->"
30030     e=|
30040     i=i+1
30050     _=1000000       : 1 sec
30060   @=((e>=0)|(i>2))
30070   ;=e<0 r=-1 -ei ]
30080   r=0
30090   -ei
30100 ]
30110 :
30120 :-------------------------------------------------
30130 : unlock
30140 : x() : filename to be unlocked
30150 :-------------------------------------------------
30160 ^Unlock
30170   +cyz
30180   c=z z=z+256
30190   y=z z=z+32
30200   y*=".lock"
30210   s=c               : to store x+y
30220   !=^ConcatStr
30230   x=s               : newname
30240   !=^Unlink
30250   r=|
30260   -zyc
30270 ]
30280 :
30290 :-------------------------------------------------
30300 : sys_read
30310 : x() : Buffer
30320 : a   : Size
30330 :-------------------------------------------------
30340 ^SYSRead
30350   +abcdi
30360   i=0
30370   d=a               : size
30380   a=3               : read
30390   b=0               : stdin
30400   @
30410     c=x             : buffer
30420     |zz
30430     r=|
30440     d=d-r
30450     x=x+r
30460   @=((r=0)|(r<0))
30470   -idcba
30480 ]
30490 :
30500 :-----------------------------------------
30510 : 時間を測定するプログラムにマージして実行
30520 :   !=^TimerStart から !=^TimerStop の時間
30530 :   #=-1 の前に !=^TimerStop を置く事
30540 :   変数スタックに値を積むためすべての変数
30550 :   は影響を受けない。
30560 :-----------------------------------------
30570 :----------------------------------
30580 : 時間計測開始
30590 :----------------------------------
30600 ^TimerStart
30610     +=_  +=%
30620 ]
30630 :
30640 :----------------------------------
30650 : 時間計測終了、経過時間表示
30660 :----------------------------------
30670 ^TimerStop
30680     -ut x=_ y=%
30690     d=x-t f=y-u
30700     ;=(f<0) d=d-1 f=f+1000000
30710     "  time:" ?=d "." ?[6]=f "sec" /
30720 ]
#=1
~
