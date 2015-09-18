#!/usr/bin/rvtlw

10020 :-------------------------------------------------------------
10030 : RvtlWiki (rvtlwiki.cgi)
10040 : version : 2.00 (32bit EUC) 2015/09/19
10050 : Copyright (C) 2005-2015
10060 :   Jun Mizutani <mizutani.jun@nifty.ne.jp> http://www.mztn.org/
10070 : & Toshio Moritake <odinsroom@gmail.com> http://www.odin.hyork.net/
10080 :     RvtlWiki may be copied under the terms of the
10090 :     GNU General Public License.
10100 :------------------------------------------------------------
10110    |ve
10120    ;=(%>>32)=0 #=^START
10130      "rvtl64 �Ǥ�ư��ޤ���rvtl �ǵ�ư���Ƥ���������"
10140      #=-1
10150   ^START
10160    z=&                : heap top
10170    U=z z=z+1024       : �桼�������ΰ�
10180 :-------------------------------------------------------------
10190 : �桼������
10200 :-------------------------------------------------------------
10210    u=U                : �ѹ��Բ�
10220    u*="./data/"       : data�ǥ��쥯�ȥ�Υѥ�̾ U[0]
10230    u=U+64             : �ѹ��Բ�
10240    u*="./pages/"      : pages�ǥ��쥯�ȥ�Υѥ�̾ U[16]
10250    u=U+128            : �ѹ��Բ�
10260    u*="http://www.example.com/rvtlwiki/" : URL U[32]
10270    u=U+768            : �ѹ��Բ�
10280    u*="RvtlWiki"      : �ե��ȥڡ����Υ����ȥ�
10290    u=U+512            : �ѹ��Բ�
10300    u*="RvtlWiki New"  : RSS�����ȥ�
10310    u=U+640            : �ѹ��Բ�
10320    u*="RvtlWiki RSS"  : RSS description
10330    U['N']=256*1024    : ����ڡ���������
10340    U['W']=80          : �Խ��ΰ�η��
10350    U['H']=30          : �Խ��ΰ�ιԿ�
10360    U['R']=40          : ��������ɽ�����
10370 :-------------------------------------------------------------
10380 : �����Х��ѿ�(��������)
10390 :-------------------------
10400 : C          : �ڡ���DB���ǿ�
10410 : I          : ��⡼��IP���ɥ쥹���ݻ�
10420 : M          : CGI�⡼��
10430 : N          : buffer size ñ��
10440 : O          : ���롼��DB���ǿ�
10450 : S          : �������ѿ��Ȥ��� Lockfile̾
10460 : z=&        : heap top
10470 :-------------------------
10480 : ���꡼����
10490 :-------------------------
10500    N=U['N']
10510    *=*+(7*N)          : �����ĥ
10520    B=z z=z+256        : Buffer
10530    Q=z z=z+256        : Post Data Buffer
10540    R=z z=z+256        : Data Buffer
10550    Z=z z=z+256        : rvtlwiki.cgi
10560    J=z z=z+256        : version
10570    :E
10580    F=z z=z+24576      : FileName      (num <1535)
10590    :G
10600    :H
10610    L=z z=z+256        : POST�ǡ���ʸ������Ƭ����
10620    X=z z=z+8192       : Group�����ǡ������
10630    Y=z z=z+8192       : Group�����ȥ��Ǽ
10640    V=z z=z+4096       : Group�����ǡ���
10650    A=z z=z+N          : �ڡ��������ե�����
10660    D=z z=z+N          : �ڡ������������ȥ�Buffer
10670    T=z z=z+N          : text
10680    P=z z=z+N          : POSTʸ����(URL�ǥ����ɺѤ�)��¸
10690    W=z z=z+(N*3)      : work
10700 :
10710    Z*="rvtlwiki.cgi"
10720    |ve ;=%<0 Z*="rvtlwiki.elf.cgi"
10730    J*="Powered by RvtlWiki 2.00(32bit)"
10740    [=0                : �ϰϥ����å�OFF
10750    C=0                : �ڡ���DB���ǿ�
10760    O=0                : ���롼��DB���ǿ�
10770    !=^TimerStart
10780 :
10790    :-------------------------
10800    : ư��⡼�ɤη���
10810    :-------------------------
10820    !=^REMOTE_ADDR I=r
10830    x=B s=W !=^REQUEST
10840    ;=r='P' x=B !=^RequestPost Mode='Post' #=^Get
10850    ;=r='G' x=B !=^RequestGet  Mode='Get'  #=^Get
10860    "No REQUEST_METHOD"  / #=^Exit
10870    :--- GET �ξ�� ---
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
11030    Mode='Frnt' #=^DoCommand   : �ǥե���Ȥ��ܼ�
11040    #=^Exit
11050    :--- POST �ξ�� ---
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
11200    : ���ޥ�ɤμ¹�
11210    :-------------------------
11220   ^DoCommand
11230 :  RSS �� HTML�إå�����
11240    ;=Mode='RSS ' !=^RSS            #=^Exit2
11250 :  HTML Header
11260    "Content-type: text/html; charset=EUC-JP" / /
11270    "<!DOCTYPE html>" /
11280    "<html lang='ja'>"
11290    / "<head>" /
11300    "<meta charset='EUC-JP' />" /
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
11620    : ��λ
11630    :-------------------------
11640 ^Exit
11650    a=I s=Q !=^SetADDR
11660    "<div id='footer'><hr /><small><p align='right'> "
11670    !=^TimerStop " from " $*=s
11680    "</p></small><hr />" /
11690    "<p align='right'><em>"
11700    "<a href='http://www.mztn.org/'>" $*=J "</a></em><br />" /
11710    "<img src='"
11720    x=Q !=^PathLogo $*=Q
11730    "' alt='*' width='80' height='40' /></p></div>" /
11740 ^Exit1
11750    "<br />" / / "</body>" / "</html>" /
11760 ^Exit2
11770    "" /
11780    #=-1
11790 :
11800 :-------------------------------------------------
11810 : �ڡ��������ե�����Υѥ�̾������
11820 :  (in)  x : �Хåե����ɥ쥹
11830 :  (out) x : pages.txt �Υѥ�ʸ���������
11840 :-------------------------------------------------
11850 ^PathPages
11860    +pu
11870    p=x u=U+64
11880    p*=u p=p+%
11890    p*="pages.txt"
11900    -up
11910 ]
11920 :-------------------------------------------------
11930 : RSS Feed
11940 :-------------------------------------------------
11950 ^RSS
11960    "Content-type: text/xml; charset=EUC-JP" / /
11970    "<?xml version='1.0' encoding='EUC-JP' ?>" / /
11980    "<rdf:RDF" /
11990    " xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'" /
12000    " xmlns='http://purl.org/rss/1.0/'" /
12010    " xmlns:dc='http://purl.org/dc/elements/1.1/'" /
12020    ">" / /
12030    !=^PageDBRead
12040    !=^GroupDBRead
12050    ;=O=0 #=^rss02  : ���롼��DB���ǿ��Υ����å�
12060    "<channel rdf:about='"
12070    !=^RssURL "?RSS'>" /
12080    " <title>" u=U+512 $*=u "</title>" /
12090    " <link>" !=^RssURL "</link>" /
12100    " <description>" u=U+640 $*=u "</description>" /
12110    " <items>" /
12120    "  <rdf:Seq>" /
12130    i=0,O-1
12140      "  <rdf:li rdf:resource='"
12150      !=^RssURL2 ?=V[i*4+2]
12160      "' />" /
12170    @=i+1
12180    "  </rdf:Seq>" /
12190    " </items>" /
12200    "</channel>" /
12210 :
12220    i=0,O-1
12230      g=0 e=0
12240      ;=C=0 #=^rss01
12250      j=0,C-1
12260        ;=F[j*4+2]=V[i*4+2] g=g+1 ;=F[j*4+0]>e e=F[j*4+0]
12270      @=j+1
12280      ^rss01
12290      "  <item rdf:about='" !=^RssURL2 ?=V[i*4+2] "'>" /
12300      "   <title>" !=^PageTime " - " $*=V[i*4+3] "</title>" /
12310      "   <link>" !=^RssURL2 ?=V[i*4+2] "</link>" /
12320      "   <description>" $*=V[i*4+3] "</description>" /
12330      "   <dc:date>"
12340      !=^PageTime
12350      "   </dc:date>" /
12360      "  </item>" / /
12370    @=i+1
12380    ^rss02
12390    "</rdf:RDF>" /
12400 ]
12410 :
12420 :-------------------------------------------------
12430 : RSS item ��URL�����
12440 :  (in) U:�����ΰ���Ƭ��Z:�ѥ�
12450 :-------------------------------------------------
12460 ^RssURL
12470    $*=U+128 $*=Z
12480 ]
12490 :
12500 :-------------------------------------------------
12510 : RSS item ��URL�����
12520 :  (in) U:�����ΰ���Ƭ��Z:�ѥ�
12530 :-------------------------------------------------
12540 ^RssURL2
12550    !=^RssURL "?GroupList&amp;group="
12560 ]
12570 :
12580 :-------------------------------------------------
12590 : ������ɽ��
12600 :  (in) e:UNIX���� Q:�Хåե�
12610 :-------------------------------------------------
12620 ^PageTime
12630    +ts
12640    t=e s=Q !=^LocalTime
12650    ?=s{5} "/" ?[2]=s{4} "/" ?[2]=s{3} " "
12660    ?[2]=s{2} ":" ?[2]=s{1} ":" ?[2]=s{0}
12670    -st
12680 ]
12690 :
12700 :-------------------------------------------------
12710 : ���롼�״����ե�����Υѥ�̾������
12720 :  (in)  x : �Хåե����ɥ쥹
12730 :  (out) x : groups.txt �Υѥ�ʸ���������
12740 :-------------------------------------------------
12750 ^PathGroups
12760    +pu
12770    p=x u=U+64
12780    p*=u p=p+%
12790    p*="groups.txt"
12800    -up
12810 ]
12820 :
12830 :-------------------------------------------------
12840 : CSS�ե�����Υѥ�̾������
12850 :  (in)  x : �Хåե����ɥ쥹
12860 :  (out) x : rvtlwiki.css �Υѥ�ʸ���������
12870 :-------------------------------------------------
12880 ^PathCSS
12890    +p
12900    p=x
12910    p*=U p=p+%
12920    p*="rvtlwiki.css"
12930    -p
12940 ]
12950 :
12960 :-------------------------------------------------
12970 : ���ե�����Υѥ�̾������
12980 :  (in)  x : �Хåե����ɥ쥹
12990 :  (out) x : rvtlwiki.png �Υѥ�ʸ���������
13000 :-------------------------------------------------
13010 ^PathLogo
13020    +p
13030    p=x
13040    p*=U p=p+%
13050    p*="rvtlwiki.png"
13060    -p
13070 ]
13080 :
13090 :-------------------------------------------------
13100 : ����ˡ�ե�����Υѥ�̾������
13110 :  (in)  x : �Хåե����ɥ쥹
13120 :  (out) x : rvtlwiki.dat �Υѥ�ʸ���������
13130 :-------------------------------------------------
13140 ^PathHelp
13150    +p
13160    p=x
13170    p*=U p=p+%
13180    p*="rvtlwiki.dat"
13190    -p
13200 ]
13210 :
13220 :-------------------------------------------------
13230 : �ե��ȥڡ����ե�����Υѥ�̾������
13240 :  (in)  x : �Хåե����ɥ쥹
13250 :  (out) x : frontpage.dat �Υѥ�ʸ���������
13260 :-------------------------------------------------
13270 ^PathFront
13280    +p
13290    p=x
13300    p*=U p=p+%
13310    p*="frontpage.dat"
13320    -p
13330 ]
13340 :
13350 :-------------------------------------------------
13360 :  Readering Wiki File Wiki�ե�����ν���
13370 :  �ҥץ�����ư����html�Ѵ�
13380 :     (in) x : �ե�����̾
13390 :    ^Preview
13400 :    ^StorePage
13410 :-------------------------------------------------
13420 ^RenderWikiText
13430    +xzbfgh
13440    b=z z=z+256
13450    f=z z=z+256
13460    g=z z=z+256
13470    h=z z=z+256
13480    b*="/usr/bin/rvtlw render.cgi - "
13490    |ve ;=%<0 b*="./render.elf.cgi "
13500    y=h h*=x                   : y="file.txt"
13510    f*=x                       : f="file.txt"
13520    x=b !=^MergeStr            :/usr/bin/rvtlw render.cgi - file.txt
13530    a=U['P'] s=g !=^ToStr      : page#
13540    y*=" " !=^MergeStr
13550    y=g    !=^MergeStr
13560    y*=" " !=^MergeStr
13570    y=g y*=" > " !=^MergeStr   : >
13580    y=f !=^MergeStr            : file.txt
13590    x(r-3)=0                   : ��ĥ��"txt"�����
13600    y*="dat" !=^MergeStr       : file.dat
13610    ,*=b
13620    -hgfbzx
13630 ]
13640 :
13650 :-------------------------------------------------
13660 :  ������󥰺Ѥ�html�ե�����ν���
13670 :     (in) x : �ե�����̾
13680 :    ^DisplayPage
13690 :    ^FrontPage
13700 :    ^Preview
13710 :-------------------------------------------------
13720 ^DispWikiText
13730    |ca*=x
13740 ]
13750 :
13760 :-------------------------------------------------
13770 : �ڡ�����ɽ��
13780 :-------------------------------------------------
13790 ^DisplayPage
13800    !=^PageDBRead
13810    B*="page=" x=B y=Q !=^GetPost
13820    x=Q !=^ToVal
13830    a=r !=^PageDBSearch a=r
13840    x=F[a*4+3]                         : title ����
13850    !=^HTMLHeader
13860    x=Q                            : page ����
13870    !=^HTMLTools
13880    "<h1>" $*=F[a*4+3] "</h1>"
13890    x=Q !=^MakeDatName             : file̾����
13900    !=^DispWikiText
13910 ]
13920 :
13930 :-------------------------------------------------
13940 : ��Ū�ڡ�����ɽ��
13950 :-------------------------------------------------
13960 ^StaticPage
13970    !=^PageDBRead
13980    B*="page=" x=B y=Q !=^GetPost
13990    x=Q !=^ToVal
14000    a=r !=^PageDBSearch a=r
14010    x=F[a*4+3]                         : title ����
14020    !=^HTMLHeader
14030    "<h1>" $*=F[a*4+3] "</h1>"
14040    x=Q !=^MakeDatName             : file̾����
14050    !=^DispWikiText
14060 ]
14070 :
14080 :-------------------------------------------------
14090 : �ɵ��ѥե������դΥڡ���ɽ��
14100 :-------------------------------------------------
14110 ^Append
14120    !=^PageDBRead
14130    B*="page=" x=B y=Q !=^GetPost
14140    x=Q !=^ToVal
14150    a=r b=r !=^PageDBSearch a=r
14160    x=F[a*4+3]                         : title ����
14170    !=^HTMLHeader
14180    x=Q                            : page ����
14190    !=^HTMLTools
14200    "<h1>" $*=F[a*4+3] " - �ɵ�</h1>"
14210    "[<a href='#append'> �ɵ��˥�����</a>]<br />"
14220    x=Q !=^MakeDatName             : file̾����
14230    !=^DispWikiText
14240    / "<a name='append'><a>" / "<div id='comment'>" /
14250    "<form action='" $*=Z " method='post' >" / "<fieldset>"
14260    "<input type=hidden name=page value='" ?=b "'>" /
14270    "<strong>�ɵ�</strong><small>"
14280    " - �����˽񤤤�ʸ�ϡ����Υڡ����κǸ���ɲä���ޤ���"
14290    "</small>" /
14300    "<input type=submit name='message' value='�񤭹���' ><br />" /
14310    "<textarea cols='80' rows='8' name='msg' >" /
14320    "</textarea><br />" /
14330    "</fieldset>" / "</form>" / "</div>" /
14340    "<p>" "</p>" /
14350 ]
14360 :
14370 :-------------------------------------------------
14380 : �����ڡ����κ���
14390 :-------------------------------------------------
14400 ^CreatePage
14410    x=B
14420    x*="�����ڡ����κ���"          : title ����
14430    !=^HTMLHeader
14440    !=^HTMLTools
14450    "<h1>�����ڡ����κ���</h1>"
14460    !=^GroupDBRead
14470    "<p>"
14480    " <form action='" $*=Z "' method='post'>" /
14490    " <strong>�ڡ���ʬ�����ꤷ�Ƥ���������</strong><br /> " /
14500    i=0,O-1
14510      "<input type=radio name=group id='group"
14520      ?=V[i*4+2] "' value='" ?=V[i*4+2]
14530      "<label for='group" ?=V[i*4+2] "'>" $*=V[i*4+3] "</label><br />" /
14540    @=i+1
14550    "  <br />" /
14560    " <strong>�������ڡ�����̾�������Ϥ��Ƥ���������</strong><br /> " /
14570    " <input type='text' name='newpage' value='' size='32'>" /
14580    " <input type='submit' value='��������'><br />" /
14590    "</form>" /
14600    "</p>" /
14610    !=^PageDBRead
14620    !=^GroupDBRead
14630    !=^GroupDBList
14640 ]
14650 :
14660 :-------------------------------------------------
14670 : �����ڡ����κ������ɽ��
14680 :-------------------------------------------------
14690 ^NewPage
14700    +Sz
14710    S=z z=z+256
14720    x=B
14730    x*="�����ڡ�������"            : title ����
14740    !=^HTMLHeader
14750    !=^HTMLTools
14760    "<h1>�����ڡ�������</h1>"
14770    B*="group=" x=B y=R !=^GetPost
14780    x=R !=^ToVal a=r
14790    x=B !=^PathPages S*=B !=^LockWait
14800    ;=r<0 "<p>�ե����뤬��å�����Ƥ��ޤ�</p>" -zS ]
14810    !=^PageDBRead
14820    x=Q !=^RegistPage
14830    !=^GroupDBRead
14840    a=0 b=1 c=0                    : �������չ߽�
14850    !=^PageDBList
14860    !=^PageDBWrite
14870    x=S !=^Unlock
14880    -zS
14890 ]
14900 :
14910 :-------------------------------------------------
14920 : �������롼�פκ���
14930 :-------------------------------------------------
14940 ^CreateGroup
14950    x=B
14960    x*="�����ڡ���ʬ��κ���"          : title ����
14970    !=^HTMLHeader
14980    !=^HTMLTools
14990    "<h1>�����ڡ���ʬ��κ���</h1>"
15000    "<p>"
15010    "<form action='" $*=Z "' method='post'>" /
15020    "  <strong>�������ڡ���ʬ���̾�������Ϥ��Ƥ���������
15030    "  </strong><br /> " /
15040    "  <input type='text' name='newgroup' value='' size='32'>" /
15050    "  <input type='submit' value='��������'><br />" /
15060    "</form>" /
15070    "</p>" /
15080    !=^PageDBRead
15090    !=^GroupDBRead
15100    !=^GroupDBList
15110 ]
15120 :
15130 :-------------------------------------------------
15140 : �������롼�פκ������ɽ��
15150 :-------------------------------------------------
15160 ^NewGroup
15170    x=B
15180    x*="�����ڡ���ʬ��κ���"          : title ����
15190    !=^HTMLHeader
15200    !=^HTMLTools
15210    "<h1>�����ڡ���ʬ��κ���</h1>"
15220    x=B !=^PathGroups !=^LockWait
15230    ;=r<0 "<p>�ե����뤬��å�����Ƥ��ޤ�</p>" ]
15240    !=^PageDBRead
15250    !=^GroupDBRead
15260    x=Q !=^RegistGroup
15270    !=^GroupDBList
15280    !=^GroupDBWrite
15290    x=B
15300    !=^Unlock
15310 ]
15320 :
15330 :-------------------------------------------------
15340 : ������ɽ��
15350 :-------------------------------------------------
15360 ^IndexPage
15370    x=B
15380    x*="�ڡ�������"                : title ����
15390    !=^HTMLHeader
15400    !=^HTMLTools
15410    "<h1>�ڡ�������</h1>"
15420    !=^PageDBRead
15430    !=^GroupDBRead
15440    a=1 b=0 c=0                    : ���롼�׾���
15450    !=^PageDBList
15460 ]
15470 :
15480 :-------------------------------------------------
15490 : �ե��ȥڡ�����ɽ��
15500 :-------------------------------------------------
15510 ^FrontPage
15520    x=U+768                        : title ����
15530    !=^HTMLHeader
15540    !=^HTMLTools
15550    "<h1>�ܼ�</h1>"
15560    x=B !=^PathFront !=^TextRead
15570    x=B
15580    !=^DispWikiText / "<hr />"
15590    !=^GroupDBRead
15600    !=^PageDBRead
15610    !=^GroupDBList
15620 ]
15630 :
15640 :-------------------------------------------------
15650 : ����ڡ����κ���
15660 :-------------------------------------------------
15670 ^RecentChanges
15680    B*="count=" x=B y=Q !=^GetPost
15690    x=Q !=^ToVal
15700    c=r                            : ɽ����
15710    x=B
15720    x*="��������"                  : title ����
15730    !=^HTMLHeader
15740    !=^HTMLTools
15750    !=^PageDBRead
15760    !=^GroupDBRead
15770    "<h1>��������</h1>"
15780    "["
15790    ;=(c>0)&(C>c) ?=c "�� / "    : ɽ�����
15800    ?=C "��] "               : ���٤Ƥη��
15810    ;=(c>0)&(C>c) "<a href='" $*=Z "?RecentChanges&count=0'>���٤�ɽ��</a>"
15820    /
15830    a=0 b=1                        : �������չ߽�
15840    !=^PageDBList
15850 ]
15860 :
15870 :-------------------------------------------------
15880 : �ڡ������Խ�
15890 :-------------------------------------------------
15900 ^Edit
15910    !=^PageDBRead
15920    B*="page=" x=B y=Q !=^GetPost
15930    x=Q !=^ToVal
15940    a=r !=^PageDBSearch a=r
15950    x=F[a*4+3]                         : title ����
15960    !=^HTMLHeader
15970    x=Q                            : page ����
15980    !=^HTMLTools
15990    "<h1>" $*=F[a*4+3] " - ���Խ�</h1>"
16000    B*=Q                           : Page# ��B�˥��ԡ�
16010    x=Q !=^MakePathName
16020    "<form action='" $*=Z "' method='post' >" /
16030    "<input type=hidden name='time' value='" ?=F[a*4+0] "'>" /
16040    "<input type=hidden name='page' value='" $*=B "'>" /
16050    "<input type=submit name='preview' value='�ץ�ӥ塼' >" /
16060    "<input type=submit name='store' value='��¸����' ><br />" /
16070    "<textarea cols='" ?=U['W'] "' rows='"
16080    ?=U['H'] "' name='msg' >" /
16090    |ca*=x                         : �ե������ cat
16100    "</textarea><br />" /
16110    "</form>" /
16120    "<p>" "</p>" /
16130    x=B !=^PathHelp
16140    |ca*=B
16150 ]
16160 :
16170 :-------------------------------------------------
16180 : �ץ�ӥ塼��ɽ��
16190 :-------------------------------------------------
16200 ^Preview
16210    +fz
16220    f=z z=z+256
16230    x*="Preview"                       : title ����
16240    !=^HTMLHeader
16250    !=^HTMLTools
16260    "<h1>�ڡ����Υץ�ӥ塼</h1>"
16270    !=^PageDBRead
16280    B*="page=" x=B y=Q !=^GetPost
16290    x=Q !=^ToVal  U['P']=r
16300    a=r !=^PageDBSearch n=r
16310    !=^GetMsg
16320    {=s }=s+r
16330    R*=Q x=Q B*="p" y=B !=^MergeStr
16340    f*=Q !=^MakePathName
16350    (*=x                               : �ƥ����Ƚ񤭹���
16360    !=^RenderWikiText
16370    x=f !=^MakeDatName                 : file̾����
16380    !=^DispWikiText
16390    :
16400    "<form action='" $*=Z "' method='post' >" /
16410    "<input type=hidden name=time value='" ?=F[n*4+0] "'>" /
16420    "<input type=hidden name=page value='" $*=R "'>" /
16430    "<input type=submit name='preview' value='�ץ�ӥ塼' >" /
16440    "<input type=submit name='store' value='��¸����' ><br />" /
16450    "<textarea cols='" ?=U['W'] "' rows='"
16460    ?=U['H'] "' name='msg' >" /
16470    x=Q |ca*=x          : �ե������ cat
16480    "</textarea><br />" /
16490    "</form>" /
16500    -zf
16510 ]
16520 :
16530 :-------------------------------------------------
16540 : �ڡ�������¸��̤�ɽ��
16550 :-------------------------------------------------
16560 ^StorePage
16570    +qSz
16580    S=z z=z+256
16590    q=z z=z+256
16600    x=B !=^PathPages S*=B !=^LockWait
16610    ;=r<0 "<p>�ե����뤬��å�����Ƥ��ޤ�</p>" -zSq ]
16620    !=^PageDBRead
16630    B*="page=" x=B y=Q !=^GetPost      : page #
16640    q*=Q
16650    x=Q !=^ToVal
16660    U['P']=r
16670    a=r !=^PageDBSearch n=r
16680    B*="time=" x=B y=R !=^GetPost      : �����ॹ�����
16690    x=R !=^ToVal t=r
16700    x=F[n*4+3]                         : title ����
16710    !=^HTMLHeader
16720    x=Q                                : page ����
16730    !=^HTMLTools
16740    "<h1>" $*=F[n*4+3] "</h1>"
16750 :
16760    ;=F[n*4+0]=t #=^sp00
16770       "<strong><p>�ڡ������ѹ�����Ƥ��ޤ�����¸����ޤ���Ǥ�����<br />"
16780       "���ܥ������äơ��Խ����Ƥ򥳥ԡ�������¸�����塢"
16790       "�ѹ����򤫤�⤦���٥ڡ������Խ����Ƥ���������</p></strong>"
16800       #=^sp01
16810 :
16820    ^sp00
16830    !=^GetMsg
16840    {=s }=s+r
16850    x=Q !=^MakePathName
16860    (*=x                               : �ƥ����Ƚ񤭹���
16870    !=^RenderWikiText
16880    a=n !=^UpdatePageTime
16890    !=^PageDBWrite                     : �ڡ���DB�񤭹���
16900 :
16910    ^sp01
16920    x=S
16930    !=^Unlock                          : �����å�
16940    x=q !=^MakeDatName                 : file̾����
16950    !=^DispWikiText
16960    -zSq
16970 ]
16980 :
16990 :-------------------------------------------------
17000 : �����Ȥκǲ����ؤ��ɲ�
17010 :-------------------------------------------------
17020 ^DoAppend
17030    +qSz
17040    S=z z=z+256
17050    q=z z=z+256
17060    x=B !=^PathPages S*=B !=^LockWait
17070    ;=r<0 "<p>�ե����뤬��å�����Ƥ��ޤ�</p>" -zSq ]
17080    !=^PageDBRead
17090    B*="page=" x=B y=Q !=^GetPost      : page #
17100    q*=Q
17110    x=Q !=^ToVal
17120    U['P']=r
17130    a=r !=^PageDBSearch n=r
17140    x=F[n*4+3]                         : title ����
17150    !=^HTMLHeader
17160    x=Q                                : page ����
17170    !=^HTMLTools
17180    "<h1>" $*=F[n*4+3] "</h1>"
17190    x=Q !=^MakePathName
17200    : �ǲ���������
17210    !=^TextRead                        : ��¸�ƥ������ɤ߹���
17220    a=r
17230    w=T+r                              : �ƥ����Ⱥǽ�
17240    w(0)=10 w(1)=0 w=w+1               : ��������
17250    w*="----" w=w+%                    : <hr /> ʸˡ�˰�¸
17260    w(0)=10 w(1)=0 w=w+1               : ��������
17270    t=_ s=R !=^TimeStr                 : ���߻����ʸ����
17280    w*="-" w=w+%                       : <ul> ʸˡ�˰�¸
17290    w*=s w=w+%                         : ���������
17300    w(0)=10 w(1)=0 w=w+1               : ��������
17310    !=^GetMsg                          : P���ΰ�
17320    w*=s w=w+%                         : �ƥ����Ȥ��ɲ�
17330    a=w-T                              : �ƥ����ȥ���������
17340 :
17350    !=^TextWrite                       : �ƥ����Ƚ񤭹���
17360    !=^RenderWikiText
17370    a=n !=^UpdatePageTime
17380    !=^PageDBWrite                     : �ڡ���DB�񤭹���
17390    x=S
17400    !=^Unlock                          : �����å�
17410 :
17420    x=q !=^MakeDatName                 : file̾����
17430    !=^DispWikiText                    : ɽ��
17440     -zSq
17450 ]
17460 :
17470 :-------------------------------------------------
17480 : �����ȤκǾ����ؤ��ɲ�
17490 :-------------------------------------------------
17500 ^DoTopAppend
17510    +qSz
17520    S=z z=z+256
17530    q=z z=z+256
17540    x=B !=^PathPages S*=B !=^LockWait
17550    ;=r<0 "<p>�ե����뤬��å�����Ƥ��ޤ�</p>" -zSq ]
17560    !=^PageDBRead
17570    B*="page=" x=B y=Q !=^GetPost      : page #
17580    q*=Q
17590    x=Q !=^ToVal
17600    U['P']=r
17610    a=r !=^PageDBSearch n=r
17620    x=F[n*4+3]                             : title ����
17630    !=^HTMLHeader
17640    x=Q                                : page ����
17650    !=^HTMLTools
17660    "<h1>" $*=F[n*4+3] "</h1>"
17670    x=Q !=^MakePathName
17680    : �Ǿ���������
17690    +T
17700    t=_ s=R !=^TimeStr                 : ���߻����ʸ����
17710    T*="-" T=T+%                       : <ul> ʸˡ�˰�¸
17720    T*=s T=T+%                         : ���������
17730    T(0)=10 T(1)=0 T=T+1               : ��������
17740    !=^GetMsg                          : P���ΰ�
17750    T*=s T=T+%                         : �����Ȥ�����
17760    T(0)=10 T(1)=0 T=T+1               : ��������
17770    T*="----" T=T+%                    : <hr /> ʸˡ�˰�¸
17780    T(0)=10 T(1)=0 T=T+1               : ��������
17790    x=Q
17800    !=^TextRead                        : ��¸�ƥ������ɤ߹���
17810    t=T+r
17820    -T
17830    a=t-T                              : �ƥ����ȥ���������
17840 :
17850    !=^TextWrite                       : �ƥ����Ƚ񤭹���
17860    !=^RenderWikiText
17870    a=n !=^UpdatePageTime
17880    !=^PageDBWrite                     : �ڡ���DB�񤭹���
17890    x=S
17900    !=^Unlock                          : �����å�
17910 :
17920    x=q !=^MakeDatName                 : file̾����
17930    !=^DispWikiText                    : ɽ��
17940     -zSq
17950 ]
17960 :
17970 :-------------------------------------------------
17980 : ���롼�ץ����ȥ�ʤɤ��ѹ�
17990 :-------------------------------------------------
18000 ^ChangeGroup
18010    x*="�ڡ���ʬ��̾���ѹ�"              : title ����
18020    !=^HTMLHeader
18030    !=^HTMLTools
18040    "<h1>�ڡ���ʬ��̾���ѹ�</h1>"
18050    !=^GroupDBRead
18060    "<p>"
18070    "<form action='" $*=Z "' method='post'>" /
18080    "  <strong>�ڡ���ʬ�����ꤷ�Ƥ���������</strong><br /> " /
18090    "  <select name='group'>" /
18100    i=0,O-1
18110      "    <option value='" ?=V[i*4+2] "'>" $*=V[i*4+3] "</option>" /
18120    @=i+1
18130    "  </select><br /><br />" /
18140    "  <strong>�������ڡ���ʬ���̾�������Ϥ��Ƥ���������</strong><br />" /
18150    "  <input type='text' name='grouprename' value='' size='32'>" /
18160    "  <input type='submit' name='NewGroupName' value='�ѹ�'><br />" /
18170    "</form>" /
18180    "</p>" /
18190    !=^GroupDBRead
18200    !=^PageDBRead
18210    !=^GroupDBList
18220 ]
18230 :
18240 :-------------------------------------------------
18250 : �ڡ��������ȥ�ʤɤ��ѹ�
18260 :-------------------------------------------------
18270 ^ChangePage
18280    x*="�ڡ���������ѹ�"                   : title ����
18290    !=^HTMLHeader
18300    !=^HTMLTools
18310    !=^PageDBRead
18320    B*="page=" x=B y=Q !=^GetPost
18330    x=Q !=^ToVal
18340    a=r !=^PageDBSearch a=r
18350    "<h1>�ڡ���������ѹ�</h1>"
18360    !=^GroupDBRead
18370    "<p>"
18380    "<form action='" $*=Z "' method='post'>" /
18390    "  <input type='hidden' name='page' value='" $*=Q "'>" /
18400    "  <strong>�ڡ���ʬ�����ꤷ�Ƥ���������</strong><br /> " /
18410    "  <select name='group'>" /
18420    i=0,O-1
18430      "    <option value='"  ?=V[i*4+2]  "'"
18440      ;=(V[i*4+2]=F[a*4+2]) " selected"
18450      ">" $*=V[i*4+3] "</option>" /
18460    @=i+1
18470    "  </select><br /><br />" /
18480    "  <strong>�ѹ�����ڡ�����̾�������Ϥ��Ƥ���������</strong><br /> " /
18490    "  <input type='text' name='newname' value='" $*=F[a*4+3] "' size='32'>"
18500    / "  <input type='submit' name='pagerename' value='�ѹ�'><br />" /
18510    "</form>" /
18520    "</p>" /
18530    !=^GroupDBList
18540 ]
18550 :
18560 :-------------------------------------------------
18570 : �ڡ���̾�ѹ����ɽ��
18580 :-------------------------------------------------
18590 ^DoPageRename
18600    +Sz
18610    S=z z=z+256
18620    x*="�ڡ���������ѹ�"          : title ����
18630    !=^HTMLHeader
18640    x=B !=^PathPages S*=B !=^LockWait
18650    ;=r<0 "<p>�ե����뤬��å�����Ƥ��ޤ�</p>" -zS ]
18660    !=^PageDBRead
18670    B*="page=" x=B y=Q !=^GetPost
18680    x=Q !=^ToVal
18690    a=r !=^PageDBSearch a=r        : a = index
18700    !=^HTMLTools
18710    "<h1>�ڡ���������ѹ����ޤ���</h1>"
18720    B*="newname=" x=B y=Q !=^GetPost
18730    B*="group=" x=B y=R !=^GetPost
18740    x=R !=^ToVal b=r               : b = group ID
18750    x=Q !=^UpdatePage
18760    !=^GroupDBRead
18770    a=0 b=1 c=0                    : �������չ߽�
18780    !=^PageDBList
18790    !=^PageDBWrite
18800    x=S
18810    !=^Unlock
18820    -zS
18830 ]
18840 :
18850 :-------------------------------------------------
18860 : ���롼��̾�ѹ����ɽ��
18870 :-------------------------------------------------
18880 ^DoGroupRename
18890    +Sz
18900    S=z z=z+256
18910    x*="�ڡ���ʬ��̾���ѹ�"        : title ����
18920    !=^HTMLHeader
18930    !=^HTMLTools
18940    "<h1>�ڡ���ʬ��̾���ѹ����ޤ���</h1>"
18950    x=B !=^PathGroups S*=B !=^LockWait
18960    ;=r<0 "<p>�ե����뤬��å�����Ƥ��ޤ�</p>" -zS ]
18970    !=^GroupDBRead
18980    B*="group=" x=B y=R !=^GetPost
18990    x=R !=^ToVal a=r               : a = group ID
19000    B*="grouprename=" x=B y=R !=^GetPost x=R
19010    !=^UpdateGroup
19020    !=^PageDBRead
19030    !=^GroupDBList
19040    !=^GroupDBWrite
19050    x=S
19060    !=^Unlock
19070    -zS
19080 ]
19090 :
19100 :-------------------------------------------------
19110 : ���롼�פ�°����ڡ����ΰ���
19120 :-------------------------------------------------
19130 ^GroupList
19140    x*="�ڡ�������"                : title ����
19150    !=^HTMLHeader
19160    !=^HTMLTools
19170    "<h1>�ڡ�������</h1>"
19180    B*="group=" x=B y=Q !=^GetPost
19190    x=Q !=^ToVal
19200    a=r
19210    !=^PageDBRead
19220    !=^GroupDBRead
19230    !=^GroupPageList
19240 ]
19250 :
19260 :-------------------------------------------------
19270 : �ѥ�̾������
19280 : x : 1234567890 --> x: ./pages/1234567890.txt
19290 :-------------------------------------------------
19300 ^MakePathName
19310    +zwx
19320    w=z z=z+256
19330    w*=U+64
19340    y=x x=w       !=^MergeStr  : w=w+x
19350    x=w y*=".txt" !=^MergeStr  : w=w+".txt"
19360    -x
19370    x*=w
19380    -wz
19390 ]
19400 :
19410 :-------------------------------------------------
19420 : �ѥ�̾������
19430 : x : 1234567890 --> x: ./pages/1234567890.dat
19440 :-------------------------------------------------
19450 ^MakeDatName
19460    +zwx
19470    w=z z=z+256
19480    w*=U+64
19490    y=x x=w       !=^MergeStr  : w=w+x
19500    x=w y*=".dat" !=^MergeStr  : w=w+".dat"
19510    -x
19520    x*=w
19530    -wz
19540 ]
19550 :
19560 :-------------------------------------------------
19570 : �ƥ����ȥ꡼�� x=FileName, T=BufferTop
19580 : r=bytes read
19590 :-------------------------------------------------
19600 ^TextRead
19610    {=T
19620    )*=x            : read file
19630    r=}-{
19640 ]
19650 :
19660 :-------------------------------------------------
19670 : �ƥ����ȥ饤�� x=FileName, T=BufferTop a=size
19680 : r=bytes wrote
19690 :-------------------------------------------------
19700 ^TextWrite
19710    {=T }=T+a
19720    (*=x            : write file
19730    r=}-{
19740 ]
19750 :
19760 :-------------------------------------------------
19770 : �ڡ��������ե�����꡼��
19780 : �ڡ�������DB����
19790 :-------------------------------------------------
19800 ^PageDBRead
19810    +zbxpqijZ
19820    b=z z=z+256
19830    {=A
19840    x=b !=^PathPages
19850    )*=b                           : read pages.txt
19860    Z=}-{
19870 :
19880    p=A
19890    q=D
19900    i=0
19910    ;=Z<20 #=^pdb00
19920    @
19930        x=p !=^ToVal F[i*4+1]=r
19940        @ p=p+1 @=(p(0)=9) p=p+1   : p��TAB�μ���
19950        x=p !=^ToVal F[i*4+0]=r
19960        @ p=p+1 @=(p(0)=9) p=p+1   : p��TAB�μ���
19970        x=p !=^ToVal F[i*4+2]=r
19980        @ p=p+1 @=(p(0)=9) p=p+1   : p��TAB�μ���
19990        F[i*4+3]=q
20000        :
20010        : �����ȥ��D()�˥��ԡ�
20020        j=0
20030        @
20040          q(j)=p(j)
20050          j=j+1
20060        @=(p(j-1)<' ')
20070        q(j-1)=0
20080        q=q+j
20090        p=p+j
20100        i=i+1
20110    @=(p>=(A+Z))
20120    ^pdb00
20130    C=i
20140    -Zjiqpxbz
20150 ]
20160 :
20170 :-------------------------------------------------
20180 : �ڡ�������DB����Ͽ
20190 : a �˥��롼��No
20200 : x �˥ڡ��������ȥ�
20210 :-------------------------------------------------
20220 ^RegistPage
20230    !=^CheckSpace ;=%=0 ]     : ̾��Ĺ����
20240    +tzywgx
20250    g=a
20260    w=z z=z+256
20270    y=z z=z+256
20280    F[C*4+1]=_
20290    a=F[C*4+1] s=B !=^ToStr w*=s
20300    x=B !=^MakePathName
20310    {=T
20320    }=T
20330    (*=x                     : xxx.txt
20340    x=w !=^MakeDatName
20350    (*=x                     : xxx.dat
20360    F[C*4+0]=F[C*4+1]
20370    F[C*4+2]=g
20380    ;=C>0 t=F[(C-1)*4+3]
20390    ;=C>0 @ t=t+1 @=(t(0)=0) t=t+1
20400    ;=C>0 F[C*4+3]=t
20410    ;=C=0 F[3]=D t=D
20420    -x
20430    t*=x
20440    C=C+1
20450    -gwyzt
20460 ]
20470 :
20480 :-------------------------------------------------
20490 : �ڡ�������DB�򹹿�
20500 : a �˥���ǥå����� b �˥��롼��No
20510 : x �˥ڡ��������ȥ�
20520 :-------------------------------------------------
20530 ^UpdatePage
20540    !=^CheckSpace ;=%=0 ]     : ̾��Ĺ����
20550    +t
20560    F[a*4+2]=b
20570    ;=C>0 t=F[(C-1)*4+3]
20580    ;=C>0 @ t=t+1 @=(t(0)=0) t=t+1
20590    ;=C>0 F[a*4+3]=t : �Ǹ����˿����������
20600    ;=C=0 F[3]=D t=D
20610    t*=x
20620    -t
20630 ]
20640 :
20650 :-------------------------------------------------
20660 : �ڡ�������DB�Υ����ॹ����פ򹹿�
20670 : a �˥���ǥå���
20680 :-------------------------------------------------
20690 ^UpdatePageTime
20700    F[a*4+0]=_
20710 ]
20720 :
20730 :-------------------------------------------------
20740 : �ڡ�������DB�ꥹ��
20750 : ������ a=0:�������ա�1:���롼��
20760 : ���   b=0:���硢    1:�߽�
20770 : ɽ���� c=0:���٤�    0�ʳ�:�����
20780 :-------------------------------------------------
20790 ^PageDBList
20800    +ihn
20810    n=C            : ������
20820    ;=n<2 #=^pdbl00
20830    ;=a=0 h=0
20840    ;=a=1 h=2
20850    ;=b=0 !=^HeapSort4
20860    ;=b=1 !=^HeapSort4d
20870    ^pdbl00
20880    "<table>" /
20890    "<tr><th>�ڡ��������ȥ�</th><th>�ǽ���������</th>"
20900    "<th>�ڡ���ʬ��</th></tr>" /
20910    ;=C=0 #=^pdbl01
20920    ;=c=0 c=C
20930    i=0,c-1
20940      "<tr><td>"
20950      "<a href='" $*=Z "?DispPage&page=" ?=F[i*4+1] "'>"
20960      $*=F[i*4+3] "</a>"
20970      "</td><td>" /
20980      t=F[i*4+0] s=B !=^LocalTime
20990      ?=s{5} "/" ?[2]=s{4} "/" ?[2]=s{3} " "
21000      ?[2]=s{2} ":" ?[2]=s{1} ":" ?[2]=s{0}
21010      "</td><td>"
21020      a=F[i*4+2] !=^GroupDBSearch
21030      $*=s  "</td></tr>"
21040    @=i+1
21050    ^pdbl01
21060    "</table>" /
21070    -nhi
21080 ]
21090 :
21100 :-------------------------------------------------
21110 : �ڡ�������DB����
21120 : a �˥ե������ֹ���Ϥ�
21130 : r �˥���ǥå������֤���r=-1 ��̤ȯ��
21140 :-------------------------------------------------
21150 ^PageDBSearch
21160    +if
21170    f=0
21180    i=0
21190    @
21200      ;=F[i*4+1]=a f=1
21210      i=i+1
21220    @=((i>=C)|(f=1))
21230    ;=i<=C r=i-1 -fi ]         : found
21240    r=-1                       : not found
21250    -fi
21260 ]
21270 :
21280 :-------------------------------------------------
21290 : ���롼�פ�°����ڡ����ꥹ��
21300 : a �˥��롼���ֹ�
21310 :-------------------------------------------------
21320 ^GroupPageList
21330    +i
21340    !=^GroupDBSearch "<h2>" $*=s "</h2>" /
21350    "<table>" /
21360    "<tr><th>�ڡ��������ȥ�</th><th>�ǽ���������</th>"
21370    "<th>�ڡ���ʬ��</th></tr>" /
21380    ;=C=0 #=^gpl01
21390    i=0,C-1
21400      ;=F[i*4+2]<>a  #=^gpl00
21410      "<tr><td>"
21420      "<a href='" $*=Z "?DispPage&page=" ?=F[i*4+1] "'>"
21430      $*=F[i*4+3] "</a>"
21440      "</td><td>" /
21450      t=F[i*4+0] s=B !=^LocalTime
21460      ?=s{5} "/" ?[2]=s{4} "/" ?[2]=s{3} " "
21470      ?[2]=s{2} ":" ?[2]=s{1} ":" ?[2]=s{0}
21480      "</td><td>"
21490      a=F[i*4+2] !=^GroupDBSearch
21500      $*=s  "</td></tr>"
21510      ^gpl00
21520    @=i+1
21530    ^gpl01
21540    "</table>" /
21550    -i
21560 :
21570 :-------------------------------------------------
21580 : �ڡ��������ե�����񤭽Ф�
21590 :-------------------------------------------------
21600 ^PageDBWrite
21610    +bpisz
21620    b=z z=z+256
21630    p=A
21640    ;=C=0 #=^pdbw01
21650    i=0,C-1
21660      a=F[i*4+1] s=p !=^ToStr p=p+r p(0)=9 p=p+1
21670      a=F[i*4+0] s=p !=^ToStr p=p+r p(0)=9 p=p+1
21680      a=F[i*4+2] s=p !=^ToStr p=p+r p(0)=9 p=p+1
21690      t=F[i*4+3]
21700      p*=t p=p+% p(0)=10 p=p+1
21710    @=i+1
21720    {=A }=p
21730    x=b !=^PathPages
21740    (*=b                           : write pages.txt
21750    ^pdbw01
21760    -zsipb
21770 ]
21780 :
21790 :-------------------------------------------------
21800 : ���롼�״����ե�����꡼��
21810 : ���롼�״���DB����
21820 :-------------------------------------------------
21830 ^GroupDBRead
21840    +xZpqijbz
21850    b=z z=z+256
21860    {=X
21870    x=b !=^PathGroups
21880    )*=b                           : read groups.txt
21890    Z=}-{
21900    :
21910    p=X
21920    q=Y
21930    i=0
21940    ;=Z<20 #=^gdb00
21950    @
21960        x=p !=^ToVal V[i*4]=r      : ��������
21970        @ p=p+1 @=(p(0)=9) p=p+1   : p��TAB�μ���
21980        x=p !=^ToVal V[i*4+1]=r    : �������դ�Ʊ��
21990        @ p=p+1 @=(p(0)=9) p=p+1   : p��TAB�μ���
22000        x=p !=^ToVal V[i*4+2]=r    : ID
22010        @ p=p+1 @=(p(0)=9) p=p+1   : p��TAB�μ���
22020        V[i*4+3]=q                 : ̾��
22030        :
22040        : �����ȥ��Y()�˥��ԡ�
22050        j=0
22060        @
22070          q(j)=p(j)
22080          j=j+1
22090        @=(p(j-1)<' ')
22100        q(j-1)=0
22110        q=q+j
22120        p=p+j
22130        i=i+1
22140    @=(p>=(X+Z))
22150    ^gdb00
22160    O=i
22170    -zbjiqpZx
22180 ]
22190 :
22200 :-------------------------------------------------
22210 : ���롼�״���DB����Ͽ
22220 : x �˥��롼�ץ����ȥ�
22230 :-------------------------------------------------
22240 ^RegistGroup
22250    !=^CheckSpace ;=%=0 ]     : ̾��Ĺ����
22260    +t
22270    V[O*4]=_
22280    V[O*4+1]=V[O*4]
22290    V[O*4+2]=O
22300    ;=O>0 t=V[(O-1)*4+3]
22310    ;=O>0 @ t=t+1 @=(t(0)=0) t=t+1
22320    ;=O>0 V[O*4+3]=t
22330    ;=O=0 V[3]=D t=D
22340    t*=x
22350    O=O+1
22360    -t
22370 ]
22380 :
22390 :-------------------------------------------------
22400 : ���롼�״����ե�����񤭽Ф�
22410 :-------------------------------------------------
22420 ^GroupDBWrite
22430    +pibaz
22440    b=z z=z+256
22450    p=X
22460    i=0,O-1
22470      a=V[i*4]   s=p !=^ToStr p=p+r p(0)=9 p=p+1
22480      a=V[i*4+1] s=p !=^ToStr p=p+r p(0)=9 p=p+1
22490      a=V[i*4+2] s=p !=^ToStr p=p+r p(0)=9 p=p+1
22500      t=V[i*4+3]
22510      p*=t p=p+% p(0)=10 p=p+1
22520    @=i+1
22530    {=X }=p
22540    x=b !=^PathGroups
22550    (*=b                           : write groups.txt
22560    -zabip
22570 ]
22580 :
22590 :-------------------------------------------------
22600 : ���롼�״����ե����븡��
22610 : a ��group ID
22620 : r �˥���ǥå�����s �˥��롼��̾���ɥ쥹���֤�
22630 :-------------------------------------------------
22640 ^GroupDBSearch
22650    +if
22660    i=0 f=0
22670    @
22680      ;=a=V[i*4+2] s=V[i*4+3] f=1
22690      i=i+1
22700    @=((i>=O)|f=1)
22710    ;=f=0 r=-1 -fi ]
22720    r=i-1
22730    -fi
22740 ]
22750 :
22760 :-------------------------------------------------
22770 : ���롼�״���DB�ꥹ��
22780 :-------------------------------------------------
22790 ^GroupDBList
22800    +tgeji
22810    "<table>" /
22820    "<tr><th>�ڡ���ʬ��</th><th>�ڡ�����</th><th>�ǿ�����</th></tr>" /
22830    ;=O=0 #=^gdbl02
22840    i=0,O-1
22850      "<tr><td>"
22860      "<a href='" $*=Z "?GroupList&group=" ?=V[i*4+2] "'>"
22870      $*=V[i*4+3] "</a></td><td align='center'>"
22880      g=0 e=0
22890      ;=C=0 #=^gdbl01
22900      j=0,C-1
22910        ;=F[j*4+2]=V[i*4+2] g=g+1 ;=F[j*4+0]>e e=F[j*4+0]
22920      @=j+1
22930      ^gdbl01
22940      ?=g
22950      "</td><td>" /
22960      t=e s=Q !=^LocalTime
22970      ?=s{5} "/" ?[2]=s{4} "/" ?[2]=s{3} " "
22980      ?[2]=s{2} ":" ?[2]=s{1} ":" ?[2]=s{0}
22990      "</td></tr>"
23000    @=i+1
23010    ^gdbl02
23020    "</table>" /
23030    -ijegt
23040 ]
23050 :
23060 :-------------------------------------------------
23070 : ̾�Τ�����Τߤʤ�Ĺ�� 0 ���֤�
23080 :-------------------------------------------------
23090 ^CheckSpace
23100    +fki
23110    x*=x k=%
23120    i=0 f=0
23130    @
23140      ;=x(i)<>' ' f=1
23150      i=i+1
23160    @=((f=1)|(i>=k))
23170    ;=f=0 %=0
23180    -ikf
23190 ]
23200 :
23210 :-------------------------------------------------
23220 : ���롼�״����ե����븡��
23230 : a ��group ID
23240 : x �˿����롼��̾
23250 :-------------------------------------------------
23260 ^UpdateGroup
23270    !=^CheckSpace ;=%=0 ]     : ̾��Ĺ����
23280    +rst
23290    t=V[(O-1)*4+3]
23300    @ t=t+1 @=(t(0)=0) t=t+1
23310    !=^GroupDBSearch
23320    V[r*4+3]=t t*=x  : �Ǹ����˿����������
23330    -tsr
23340 ]
23350 :
23360 :-------------------------------------------------
23370 : Get Post Data
23380 : POSTʸ������� x �Ǽ����줿ʸ�����³���ǡ�����
23390 : y �μ����ΰ�˥��ԡ�
23400 : r �˥ǡ�����ʸ�������֤�
23410 :-------------------------------------------------
23420 ^GetPost
23430     !=^SearchPost             : r ��ʸ���󥢥ɥ쥹
23440     ;=r=0 ]                   : Ĺ��0�ʤ��return
23450     x=r
23460     y*=x r=%
23470 ]
23480 :
23490 :-------------------------------------------------
23500 : Get Post Msg
23510 : POSTʸ������� msg= ��³���ǡ����Υ��ɥ쥹�����
23520 : s �˥ǡ�����ʸ������Ƭ���ɥ쥹���֤�
23530 : r �˥ǡ�����ʸ�������֤�
23540 :-------------------------------------------------
23550 ^GetMsg
23560     +x
23570     B*="msg=" x=B
23580     !=^SearchPost             : r ��ʸ���󥢥ɥ쥹
23590     ;=r=0 -x ]                : Ĺ��0�ʤ��return
23600     x=r s=r
23610     !=^StrLen
23620     -x
23630 ]
23640 :
23650 :-------------------------------------------------
23660 : HTML Header
23670 : x �˥����ȥ�
23680 :-------------------------------------------------
23690 ^HTMLHeader
23700   "<title>" $*=x "</title>" /
23710   "<link rel='stylesheet' type='text/css' href='"
23720   x=B !=^PathCSS $*=B
23730   "' />" /
23740   "</head>" / /
23750   "<body class='normal'>" / "<!--  -->" //
23760 ]
23770 :
23780 :-------------------------------------------------
23790 : Wiki Tools
23800 : x �˥ڡ���
23810 :-------------------------------------------------
23820 ^HTMLTools
23830   / "<div id='menu'>" / "<ul>" /
23840   "<li class='top'><a href='" $*=Z "?FrontPage'>�ܼ�</a></li>" /
23850   ;=Mode='Disp' "<li><a href='" $*=Z "?Edit&page=" $*=x "'>�Խ�</a></li>" /
23860   ;=Mode='Disp' "<li><a href='" $*=Z "?Append&page=" $*=x "'>�ɵ�</a></li>" /
23870   ;=Mode='Disp' "<li><a href='" $*=Z "?Static&page=" $*=x "'>��Ū</a></li>" /
23880   ;=Mode='DoAp' "<li><a href='" $*=Z "?Edit&page=" $*=x "'>�Խ�</a></li>" /
23890   ;=Mode='DoAp' "<li><a href='" $*=Z "?Append&page=" $*=x "'>�ɵ�</a></li>" /
23900   ;=Mode='Stor' "<li><a href='" $*=Z "?Edit&page=" $*=x "'>�Խ�</a></li>" /
23910   ;=Mode='Stor' "<li><a href='" $*=Z "?Append&page=" $*=x "'>�ɵ�</a></li>" /
23920   "<li><a href='" $*=Z "?RecentChanges&count=" ?=U['R']
23930     "'>��������</a></li>" /
23940   "<li><a href='" $*=Z "?IndexPage'>����</a></li>" /
23950   "<li><a href='" $*=Z "?CreatePage'>�����ڡ���</a></li>" /
23960   "<li><a href='" $*=Z "?CreateGroup'>�����ڡ���ʬ��</a></li>" /
23970   "<li><a href='" $*=Z "?ChangeGroup'>�ڡ���ʬ���ѹ�</a></li>" /
23980   ;=Mode='Disp' "<li><a href='" $*=Z "?ChangePage&page="
23990   ;=Mode='Disp' $*=x "'>�ڡ����ѹ�</a>" /
24000   ;=Mode='DoAp' "<li><a href='" $*=Z "?ChangePage&page="
24010   ;=Mode='DoAp' $*=x "'>�ڡ����ѹ�</a>" /
24020   ;=Mode='Stor' "<li><a href='" $*=Z "?ChangePage&page="
24030   ;=Mode='Stor' $*=x "'>�ڡ����ѹ�</a>" /
24040   ;=Mode='Frnt' "<li><a href='" $*=Z "?RSS"
24050   ;=Mode='Frnt' "'>RSS</a>" /
24060   "</ul>" / "</div>" / /
24070 ]
24080 :
24090 :-------------------------------------------------
24100 : Read REMOTE_ADDR
24110 : r : IP���ɥ쥹��32�ӥå�������
24120 :-------------------------------------------------
24130 ^REMOTE_ADDR
24140    +xszij
24150    x=z z=z+32
24160    s=z z=z+32
24170    x*="REMOTE_ADDR="
24180    !=^SearchEnv
24190    r=0
24200    i=0
24210    @
24220      j=0 r=r<<8
24230      @
24240        j=j*10+(s(i)-$30)
24250        i=i+1
24260      @=((s(i)='.')|(s(i)=0))
24270      r=r|j
24280      ;=(s(i)='.') i=i+1
24290    @=(s(i)=0)
24300    -jizxs
24310 ]
24320 :
24330 :-------------------------------------------------
24340 : Set REMOTE_ADDR
24350 : in  s : �Хåե���Ƭ���ɥ쥹
24360 : in  a : 32�ӥå�������IP���ɥ쥹
24370 : out s : IP���ɥ쥹ʸ����
24380 :-------------------------------------------------
24390 ^SetADDR
24400    +sabcde
24410    b=a>>24
24420    c=(a>>16)&$FF
24430    d=(a>>8)&$FF
24440    e=a&$FF
24450    a=b !=^ToStr
24460    s(r)='.'
24470    a=c s=s+r+1 !=^ToStr
24480    s(r)='.'
24490    a=d s=s+r+1 !=^ToStr
24500    s(r)='.'
24510    a=e s=s+r+1 !=^ToStr
24520    s(r)=0
24530    -edcbas
24540 ]
24550 :
24560 :-------------------------------------------------
24570 : Read REQUEST_METHOD
24580 : r='GET' or r='POST'
24590 :-------------------------------------------------
24600 ^REQUEST
24610    x*="REQUEST_METHOD="
24620    !=^SearchEnv
24630    r=s(0)
24640 ]
24650 :
24660 :-------------------------------------------------
24670 : Get Query_String
24680 :
24690 : P() : QUERY_STRING�ǡ���
24700 : L[] : QUERY�ǡ���ʸ������Ƭ����
24710 : K   : QUERY_STRINGʸ�����
24720 :-------------------------------------------------
24730 ^RequestGet
24740     x*="QUERY_STRING=" s=W
24750     !=^SearchEnv
24760     x=W !=^StrLen
24770     a=r
24780     ;=r=0 #=^rg00
24790     i=0,r-1
24800       ;=W(i)='&' W(i)=0            : ʸ������
24810     @=i+1
24820     ^rg00
24830     x=W s=P !=^URLDEC2             : ����Ѵ�
24840     L[0]=W                         : ��Ƭ���ǤΥ��ɥ쥹
24850     w=W
24860     ;=r<=0 w(0)=0 K=j ]            : 20060516
24870     i=0,r-1
24880       c=P(i)
24890       ;=c=0 w(0)=0 w=w+1 j=j+1 L[j]=w #=^rg_next : ����Ƭ����Ͽ
24900       ;=c>'>' w(0)=c w=w+1       #=^rg_next
24910       ;=c='"' w*="&quot;" w=w+%  #=^rg_next
24920       ;=c='<' w*="&lt;"   w=w+%  #=^rg_next
24930       ;=c='>' w*="&gt;"   w=w+%  #=^rg_next
24940       ;=c='&' w*="&amp;"  w=w+%  #=^rg_next
24950       w(0)=c w=w+1
24960       ^rg_next
24970     @=i+1
24980     w(0)=0 K=j                            : ���Ǥο�
24990 ]
25000 :
25010 :-------------------------------------------------
25020 : ɸ�����Ϥ���POST���줿ʸ��������
25030 :
25040 : W : ����ΰ衢URL�ǥ�����+���˥������Ѥߤ��֤�
25050 : P : POSTʸ����(URL�ǥ����ɺѤ�)��¸
25060 : L : POST�ǡ���ʸ������Ƭ����
25070 : K : POSTʸ�����
25080 :-------------------------------------------------
25090 ^RequestPost
25100     +wacxijrs
25110     : CONTENT_LENGTH�Ķ��ѿ�����ǡ���Ĺ�����
25120     x*="CONTENT_LENGTH=" s=W
25130     !=^SearchEnv
25140     x=s
25150     !=^ToVal                       : �ǡ���Ĺ����Ͳ�
25160     ;=((r<0)|(r>(N*3))) r=0 #=^rp00
25170     a=r x=W !=^SYSRead             : W �˥��ԡ�
25180     i=0,a-1
25190       ;=W(i)='&' W(i)=0            : ʸ������
25200     @=i+1
25210    ^rp00
25220     W(i)=0                         :
25230     x=W s=P a=i !=^URLDEC2         : ����Ѵ�
25240     L[0]=W  P(r)=0                 : ��Ƭ���ǤΥ��ɥ쥹
25250     w=W j=0                        : W ���᤹
25260     i=0,r-1
25270       c=P(i)
25280       ;=c=0 w(0)=0 w=w+1 j=j+1 L[j]=w #=^rp_next : ����Ƭ����Ͽ
25290       ;=c>'>' w(0)=c w=w+1       #=^rp_next
25300       ;=c='"' w*="&quot;" w=w+%  #=^rp_next
25310       ;=c='<' w*="&lt;"   w=w+%  #=^rp_next
25320       ;=c='>' w*="&gt;"   w=w+%  #=^rp_next
25330       ;=c='&' w*="&amp;"  w=w+%  #=^rp_next
25340       w(0)=c w=w+1
25350       ^rp_next
25360     @=i+1
25370     w(0)=0
25380     K=j                            : ���Ǥο�
25390     -srjixcaw
25400 ]
25410 :
25420 :-------------------------------------------------
25430 : x �˸���ʸ���������
25440 : L[]��POSTʸ����(URL decoded)�ι�Ƭ���ɥ쥹
25450 : K �˥ǡ������ǿ�
25460 : r �˥ǡ�����Ƭ���ɥ쥹���֤� (0 �ʤ�̵��)
25470 :-------------------------------------------------
25480 ^SearchPost
25490     +yi
25500     i=0
25510     @
25520       y=L[i]
25530       !=^CompareStr
25540       i=i+1
25550     @=((r>0)|(i>K))
25560     ;=r=0 -iy ]
25570     r=y+r
25580     -iy
25590 ]
25600 :
25610 :-------------------------------------------------
25620 : x �˸���ʸ���������
25630 : L[]�˹�Ƭ���ɥ쥹��P��POSTʸ����(URL decoded)
25640 : a �˥ǡ���Ĺ
25650 : r �˥ǡ�����Ƭ���ɥ쥹���֤� (0 �ʤ�̵��)
25660 :-------------------------------------------------
25670 ^SearchQuery
25680     +yi
25690     i=0
25700     @
25710       y=L[i]
25720       !=^CompareStr
25730       i=i+1
25740     @=((r>0)|(i>a))
25750     ;=r=0 -iy ]
25760     r=y+r
25770     -iy
25780 ]
25790 :
25800 :-----------------------------------------
25810 : �Ķ��ѿ��򸡺�
25820 :
25830 : x �� s �� �ΰ�����
25840 :   x="����ʸ����"
25850 :   s ���ͤ�ʸ������Ǽ
25860 :   ̤ȯ���ʤ� r=0 s(0)=0
25870 :-----------------------------------------
25880 ^SearchEnv
25890     +if                       : �ѿ�����
25900     [=0                       : �ϰϥ����å�Onn
25910     i=0
25920     @
25930       y=\\i                   : �Ķ��ѿ�
25940       f=0
25950       ;=y=0 f=1
25960       ;=y<>0 ;=y(0)=0 f=1
25970       ;=f=0 !=^CompareStr
25980       i=i+1
25990     @=((f=1)|(r>0))
26000     ;=r=0 s(0)=0 -i ]
26010     y=y+r i=0
26020     +xy
26030     x=y y=s
26040     !=^CopyStr                : copy y to s
26050     -yx
26060     [=1                       : �ϰϥ����å� ON
26070     -fi                       : �ѿ�����
26080 ]
26090 :
26100 :-------------------------------------
26110 : 4�Х�������Υҡ��ץ����Ⱦ���
26120 : F[] �Υ�����
26130 :  h=0:time, h=1:fname, h=2:GrNo, h=3:pointer
26140 : n �����ǤθĿ�
26150 :-------------------------------------
26160 ^HeapSort4
26170     +rkijf
26180     f=F-16                    : F[0]=f[1]
26190     k=n/2 r=n
26200     i=k
26210     @
26220       k=i
26230       !=^DownHeap4            : downheap(i,n)
26240       i=i-1
26250     @=(i<1)
26260     i=r
26270     @
26280       k=1 j=i !=^HeapSwap4    : swap(1,i)
26290       k=1 r=i-1 !=^DownHeap4  : downheap(1,i-1)
26300       i=i-1
26310     @=(i<2)
26320     -fjikr
26330 ]
26340 :
26350 :-------------------------------------
26360 : DownHeap (k, r) ����
26370 :-------------------------------------
26380 ^DownHeap4
26390     +krj
26400    ^h4shift01
26410     j=2*k
26420     ;=j>r #=^h4shift02
26430     ;=j<>r ;=f[(j+1)*4+h]>f[j*4+h] j=j+1
26440     ;=f[k*4+h]>=f[j*4+h] #=^h4shift02
26450     !=^HeapSwap4
26460     k=j
26470     #=^h4shift01
26480    ^h4shift02
26490     -jrk
26500 ]
26510 :
26520 :-------------------------------------
26530 : 4�Х�������Υҡ��ץ����ȹ߽�
26540 : F[] �Υ�����
26550 : h=0:time, h=1:fname, h=2:GrNo, h=3:pointer
26560 : n �����ǤθĿ�
26570 :-------------------------------------
26580 ^HeapSort4d
26590     +rkijf
26600     f=F-16
26610     k=n/2 r=n
26620     i=k
26630     @
26640       k=i
26650       !=^DownHeap4d            : downheap(i,n)
26660       i=i-1
26670     @=(i<1)
26680     i=r @
26690       k=1 j=i !=^HeapSwap4    : swap(1,i)
26700       k=1 r=i-1 !=^DownHeap4d  : downheap(1,i-1)
26710       i=i-1
26720     @=(i<2)
26730     -fjikr
26740 ]
26750 :
26760 :-------------------------------------
26770 : DownHeap (k, r) �߽�
26780 :-------------------------------------
26790 ^DownHeap4d
26800     +krj
26810    ^h4shift03
26820     j=2*k
26830     ;=j>r #=^h4shift02
26840     ;=j<>r ;=f[(j+1)*4+h]<f[j*4+h] j=j+1
26850     ;=f[k*4+h]<=f[j*4+h] #=^h4shift04
26860     !=^HeapSwap4
26870     k=j
26880     #=^h4shift03
26890    ^h4shift04
26900     -jrk
26910 ]
26920 :
26930 :-------------------------------------
26940 : 4�Х�������ǡ�����Swap
26950 : Swap (k, j)
26960 :-------------------------------------
26970 ^HeapSwap4
26980     +wjk
26990     j=j-1 k=k-1     : F,E,G,H��ź������[0]����
27000     w=F[j*4+1] F[j*4+1]=F[k*4+1] F[k*4+1]=w
27010     w=F[j*4+0] F[j*4+0]=F[k*4+0] F[k*4+0]=w
27020     w=F[j*4+2] F[j*4+2]=F[k*4+2] F[k*4+2]=w
27030     w=F[j*4+3] F[j*4+3]=F[k*4+3] F[k*4+3]=w
27040     -kjw
27050 ]
27060 :
27070 :==========================================================================
27080 : ���ѥ饤�֥��
27090 :==========================================================================
27100 :-----------------------------------------
27110 : t �˸��߻��� (UNIX����1970/1/1 0:00:00
27120 : ����ηв��ÿ�)���Ϥ���t=_
27130 : ���� s �˻���ʸ������֤�
27140 :-----------------------------------------
27150 ^TimeStr
27160     +zuvwx
27170     u=z z=z+256
27180     v=z z=z+256
27190     !=^LocalTime
27200     x=s s=v
27210     w=u                                    : ʸ������Ƭ����¸
27220     a=x{5} !=^ToStr                        : year
27230     u*=v   u=u+%
27240     u*="/" u=u+%
27250     ;=x{4}<=9 u*="0" u=u+%
27260     a=x{4} !=^ToStr  u*=v u=u+%            : month
27270     u*="/" u=u+%
27280     ;=x{3}<=9 u*="0" u=u+%
27290     a=x{3} !=^ToStr  u*=v u=u+%            : day
27300     u*=" " u=u+%
27310     ;=x{2}<=9 u*="0" u=u+%
27320     a=x{2} !=^ToStr  u*=v u=u+%            : hour
27330     u*=":" u=u+%
27340     ;=x{1}<=9 u*="0" u=u+%
27350     a=x{1} !=^ToStr  u*=v u=u+%            : min
27360     u*=":" u=u+%
27370     ;=x{0}<=9 u*="0" u=u+%
27380     a=x{0} !=^ToStr  u*=v   u=u+%          : sec
27390     s*=w
27400     -xwvuz
27410 ]
27420 :-----------------------------------------
27430 : t �˸��߻��� (UNIX����1970/1/1 0:00:00
27440 : ����ηв��ÿ�)���Ϥ���t=_
27450 : 2�Х������� s �˰ʲ��ξ�����֤�
27460 : s{0} : sec   0..59
27470 : s{1} : min   0..59
27480 : s{2} : hour  0..23
27490 : s{3} : day   0..31
27500 : s{4} : month 1..12
27510 : s{5} : year  1980-
27520 : s{6} : week day 0-6
27530 :-----------------------------------------
27540 ^LocalTime
27550     +myTdwxiMVz
27560     m=z z=z+16
27570     m(1)=31 m(2)=28 m(3)=31 m(4)=30 m(5)=31 m(6)=30
27580     m(7)=31 m(8)=31 m(9)=30 m(10)=31 m(11)=30 m(12)=31
27590     : 2*(4*365+1)*24*60*60+(2*365*24*60*60)|-(9*3600)
27600     y=1980
27610     :T=315532800 : 1980/1/1 00:00:00 UTC
27620     T=315500400 : 1980/1/1 00:00:00 JST
27630     t=t-T ;=t<0 t=0
27640     t=t/60 s{0}=%                          : sec
27650     t=t/60 s{1}=%                          : min
27660     d=t/24 s{2}=%                          : hour
27670     w=366+365+365+365                      : w=1461days/4years
27680     x=d/w                                  : x=year*4
27690     y=y+(x*4)
27700     d=%                                    : days in 4years(0..1460)
27710     ;=d<=365 m(2)=29 x=0 d=d               : leap year
27720     ;=d>365 d=d-366 x=d/365 d=% x=x+1      : normal year
27730     y=y+x                                  : year
27740     i=1
27750     @
27760       ;=(d>=m(i)) d=d-m(i) i=i+1
27770     @=(d<m(i))
27780     M=i
27790     s{5}=y s{4}=M s{3}=d+1
27800     ;=(y<=2) y=y+12
27810     V=(y+(y/4)-(y/100)+(y/400)+((13*M+8)/5)+d)/7 s{6}=%
27820     -zVMixwdTym
27830 ]
27840 :
27850 :-------------------------------------------------
27860 : 10�ʿ�ʸ���� --> �����Ѵ�
27870 :
27880 : x ����Ϥޤ�ʸ�������ͤ��ѹ�����
27890 : r ���ͤ��֤���
27900 :-------------------------------------------------
27910 ^ToVal
27920     +i
27930     i=0
27940     r=0
27950     ;=(x(i)<'0')+(x(i)>'9') -i ]
27960     @
27970       r=r*10+(x(i)-$30)
27980       i=i+1
27990     @=((x(i)<'0')+(x(i)>'9'))
28000     -i
28010 ]
28020 :
28030 :-------------------------------------------------
28040 : ���� --> 10�ʿ�ʸ�����Ѵ�
28050 :
28060 : a �ο��ͤ�ʸ������Ѵ����� s ������ΰ��
28070 : ʸ����Ȥ����֤���
28080 : r ��ʸ�������֤�
28090 :-------------------------------------------------
28100 ^ToStr
28110     +aij
28120     i=0
28130     @
28140       a=a/10 +=%  : �����å��˥ץå���
28150       i=i+1
28160     @=(a=0)
28170     j=0
28180     @
28190       i=i-1
28200       s(j)=;+$30  : �����å�����ݥå�
28210       j=j+1
28220     @=(i=0)
28230     s(j)=0
28240     r=j
28250     -jia
28260 ]
28270 :
28280 :-------------------------------------------------
28290 : ʸ����Ĺ�μ���
28300 :
28310 : x ��ʸ�������ꡢ���ʸ�������֤�
28320 :-------------------------------------------------
28330 ^StrLen
28340    x*=x
28350    r=%
28360 ]
28370 :
28380 :-------------------------------------------------
28390 : ��ʬʸ��������   length(x) <= length(y)
28400 :
28410 : x �μ���ʸ���� y �μ���ʸ����Ȱ��פ�����
28420 : r=ʸ�������ޤ��Ͻ��ưۤʤ�ʸ���ΰ���
28430 : ���פ��Ƥ��ʤ���� r=0 ���֤�
28440 :-------------------------------------------------
28450 ^CompareStr
28460     +if
28470     i=-1
28480     f=0
28490     @
28500       i=i+1
28510       ;=(x(i)=y(i))&(x(i)=0) f=1  : ȯ��
28520       ;=x(i)<>y(i) f=2            : �㤦
28530     @=((x(i)=0)|(f<>0))
28540     ;=i>0 ;=f=1 r=i
28550     ;=(x(i)=0)&(f=2)) r=i
28560     ;=(x(i)<>0) r=0
28570     -fi
28580 ]
28590 :
28600 :-------------------------------------------------
28610 : Copy String
28620 :
28630 :  x() : string1 (source)
28640 :  y() : string2 (destinnation)
28650 : return
28660 :  r   : length
28670 :-------------------------------------------------
28680 ^CopyStr
28690     y*=x
28700     r=%
28710 ]
28720 :
28730 :-------------------------------------------------
28740 : Concatinate string
28750 :
28760 :  x() : string1 (<255byte)
28770 :  y() : string2 (<255byte)
28780 : return
28790 :  s() : string1+string2
28800 :  r   : length
28810 :-------------------------------------------------
28820 ^ConcatStr
28830    s*=x r=%
28840    +s
28850    s=s+r s*=y
28860    -s
28870    r=r+%
28880 ]
28890 :
28900 :-------------------------------------------------
28910 : Merge string
28920 :
28930 :  x() : string1 (<255byte)
28940 :  y() : string2 (<255byte)
28950 : return
28960 :  x() : string1 + string2
28970 :  r   : length
28980 :-------------------------------------------------
28990 ^MergeStr
29000    !=^StrLen             : r = length(x)
29010    +x
29020    x=x+r
29030    x*=y
29040    r=r+%
29050    -x
29060 ]
29070 :
29080 :-------------------------------------
29090 : URL�ǥ�����
29100 :
29110 : x ��URL���󥳡��ɤ���ʸ���������
29120 : s �˥ǥ����ɸ��ʸ������֤�
29130 : r �˥ǥ����ɸ��ʸ�������֤�
29140 :-------------------------------------
29150 ^URLDEC
29160     +a
29170     !=^StrLen
29180     a=r
29190     !=^URLDEC2
29200     -a
29210 ]
29220 :
29230 :-------------------------------------
29240 : URL�ǥ�����2
29250 :
29260 : x ��URL���󥳡���ʸ�������Ƭ����
29270 : a ���ѹ��ϰϤ�ʸ����������
29280 : s �˥ǥ����ɸ��ʸ������֤�
29290 : r �˥ǥ����ɸ��ʸ�������֤�
29300 :-------------------------------------
29310 ^URLDEC2
29320    +uz
29330    u=z+16
29340    u[0]=x u[1]=a u[2]=s
29350    |ud
29360    r=u[3]
29370    -zu
29380 ]
29390 :
29400 :-------------------------------------------------
29410 : symlink
29420 : x() : oldname
29430 : y() : newname
29440 :-------------------------------------------------
29450 ^Symlink
29460   +abc
29470   a=83              : symlink
29480   b=x               : oldname
29490   c=y               : newname
29500   |zz
29510   r=|
29520   -cba
29530 ]
29540 :
29550 :-------------------------------------------------
29560 : unlink
29570 : x() : pathname
29580 :-------------------------------------------------
29590 ^Unlink
29600   +ab
29610   a=10              : unlink
29620   b=x               : name
29630   |zz
29640   r=|
29650   -ba
29660 ]
29670 :-------------------------------------------------
29680 : lock
29690 : x() : filename to be locked
29700 :-------------------------------------------------
29710 ^Lock
29720   +cyz
29730   c=z z=z+256
29740   y=z z=z+32
29750   y*=".lock"
29760   s=c               : to store x+y
29770   !=^ConcatStr
29780   y=s               : newname
29790   !=^Symlink
29800   -zyc
29810 ]
29820 :
29830 :-------------------------------------------------
29840 : lock & wait
29850 : x() : filename to be locked
29860 : r=0 : success, r=-1 : failure
29870 :-------------------------------------------------
29880 ^LockWait
29890   +ie
29900   i=0
29910   @
29920     "<!-- "
29930     !=^Lock
29940     " --->"
29950     e=|
29960     i=i+1
29970     _=1000000       : 1 sec
29980   @=((e>=0)|(i>2))
29990   ;=e<0 r=-1 -ei ]
30000   r=0
30010   -ei
30020 ]
30030 :
30040 :-------------------------------------------------
30050 : unlock
30060 : x() : filename to be unlocked
30070 :-------------------------------------------------
30080 ^Unlock
30090   +cyz
30100   c=z z=z+256
30110   y=z z=z+32
30120   y*=".lock"
30130   s=c               : to store x+y
30140   !=^ConcatStr
30150   x=s               : newname
30160   !=^Unlink
30170   r=|
30180   -zyc
30190 ]
30200 :
30210 :-------------------------------------------------
30220 : sys_read
30230 : x() : Buffer
30240 : a   : Size
30250 :-------------------------------------------------
30260 ^SYSRead
30270   +abcdi
30280   i=0
30290   d=a               : size
30300   a=3               : read
30310   b=0               : stdin
30320   @
30330     c=x             : buffer
30340     |zz
30350     r=|
30360     d=d-r
30370     x=x+r
30380   @=((r=0)|(r<0))
30390   -idcba
30400 ]
30410 :
30420 :-----------------------------------------
30430 : ���֤�¬�ꤹ��ץ����˥ޡ������Ƽ¹�
30440 :   !=^TimerStart ���� !=^TimerStop �λ���
30450 :   #=-1 ������ !=^TimerStop ���֤���
30460 :   �ѿ������å����ͤ��Ѥि�᤹�٤Ƥ��ѿ�
30470 :   �ϱƶ�������ʤ���
30480 :-----------------------------------------
30490 :----------------------------------
30500 : ���ַ�¬����
30510 :----------------------------------
30520 ^TimerStart
30530     +=_  +=%
30540 ]
30550 :
30560 :----------------------------------
30570 : ���ַ�¬��λ���в����ɽ��
30580 :----------------------------------
30590 ^TimerStop
30600     -ut x=_ y=%
30610     d=x-t f=y-u
30620     ;=(f<0) d=d-1 f=f+1000000
30630     "  time:" ?=d "." ?[6]=f "sec" /
30640 ]

#=1
~

