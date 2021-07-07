import json
import requests
class five_sim:
    def __init__(self, api_key):
        self.api_key = api_key
    def get_country_list(self):
        temp = json.loads(
            requests.get('https://5sim.net/v1/guest/countries',
                         headers={
                             'Authorization': 'Bearer ' + self.token,
                             'Content-Type': 'application/json',
                         }).text)
        lista = []
        for country in temp:
            lista.append(str(country))
        return lista
    def get_product_list_activation(self):
        #this is updated to 07/07/2021
        return """airtel
akelni
alibaba
aliexpress
amazon
aol
avito
azino
bittube
blablacar
blizzard
blockchain
burgerking
careem
cekkazan
citymobil
delivery
discord
dixy
dodopizza
domdara
dostavista
drugvokrug
dukascopy
ebay
edgeless
electroneum
facebook
fiverr
foodpanda
forwarding
gameflip
gcash
get
globus
glovo
google
grabtaxi
green
hqtrivia
icard
icq
imo
iost
jd
kakaotalk
keybase
komandacard
lazada
lbry
lenta
lianxin
line
livescore
magnit
magnolia
mailru
mamba
mega
michat
microsoft
miratorg
mtscashback
naver
netflix
nimses
nttgame
odnoklassniki
okey
openpoint
oraclecloud
other
ozon
papara
paymaya
paypal
perekrestok
pof
pokermaster
proton
pubg
qiwiwallet
quipp
reuse
ripkord
seosprint
shopee
skout
snapchat
steam
tango
tantan
telegram
tencentqq
tiktok
tinder
truecaller
uber
uploaded
vernyi
viber
vkontakte
wechat
weibo
weku
whatsapp
yahoo
yandex
youdo
youla
""".split("\n")
    def get_number(self, country, product, operator = "any"):
        temp = json.loads(requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product,
                     headers={
                         'Authorization': 'Bearer ' + self.token,
                         'Content-Type': 'application/json',
                     }).text)
        try:
            return {"phone":temp["phone"], "id": temp["id"]}
        except KeyError:
            return None
    def get_code(self, id):
        temp =json.loads(requests.get('https://5sim.net/v1/user/check/' + str(id), headers={
    'Authorization': 'Bearer ' + self.token,
    'Content-Type': 'application/json',
        }).text)
        if len(temp["sms"])==0:
            return None
        else:
            try:
                lista = []
                for message in temp:
                    lista.append({"code": message["code"], "sender": message["sender"]})
                return lista
            except KeyError:
                return None
class onlinesim:
    def __init__(self, api_key):
        self.api_key = api_key
    def get_balance(self):
        return json.loads(requests.get("http://onlinesim.ru/api/getBalance.php?apikey="+self.api_key).text)["balance"]
    def get_frozen_balance(self):
        return json.loads(requests.get("http://onlinesim.ru/api/getBalance.php?apikey=" + self.api_key).text)["zbalance"]
    def Get_number(self,country_id,service):
        try:
            return json.loads(requests.post("http://onlinesim.ru/api/getNum.php",data={"apikey":self.api_key, "country":country_id,"service":service}).text)["tzid"]
        except KeyError:
            return None
    def get_country_ids(self):
        temp =json.loads(requests.get(
            "http://onlinesim.ru/api/getNumberStats.php?apikey=" + self.api_key).text)
        lista = []
        for country in temp:
            lista.append({"id":str(country), "name": country["name"]})
        return lista
    def get_code(self,tzid):
        try:
            return json.loads(requests.get(
                "http://onlinesim.ru/api/getState.php?apikey=" + self.api_key).text)["msg"]
        except KeyError:
            return None
    def get_total_numbers_for_country(self, country_id):
        return json.loads(requests.get("http://onlinesim.ru/api/getNumberStats.php?apikey=" + self.api_key+"&country="+ str(country_id)).text)
class smspva:
    def __init__(self, api_key):
        self.api_key = api_key
    def get_balance(self):
        return json.loads(requests.get(
            "http://smspva.com/priemnik.php?metod=get_balance&apikey=" + self.api_key).text)["balance"]
    def get_service_price(self,country,  service):
        return json.loads(requests.get(
            "http://smspva.com/priemnik.php?metod=get_service_price&country="+ country+ "&service="+service+ "&apikey=" + self.api_key).text)["price"]
    def get_country_list(self):#updated at 07/07/2021
        return """RU
UA
DE
KZ
HT
RO
AR
AR
BA
KH
CM
CA_V
CL
CY
DO
EG
EE
FI
FR
GH
IN
ID
IQ
IE
KE
KG
LA
LV
LT
MY
MX
MD
MA
NL
NZ
NG
PK
PH
PL
PT
ZA
ES
SE
UK
US
VN
VN""".split("\n")
    def get_service_list(self):
        return """opt28
opt97
opt97
opt22
opt22
opt86
opt86
opt46
opt46
opt61
opt61
opt44
opt44
opt10
opt10
opt59
opt59
opt56
opt56
opt25
opt25
opt78
opt78
opt81
opt81
opt89
opt89
opt122
opt122
opt76
opt76
opt98
opt98
opt112
opt112
opt51
opt51
opt26
opt26
opt124
opt124
opt123
opt123
opt53
opt53
opt92
opt92
opt45
opt45
opt27
opt27
opt40
opt40
opt32
opt32
opt31
opt31
opt21
opt21
opt2
opt2
opt43
opt43
opt6
opt6
opt13
opt13
opt68
opt68
opt77
opt77
opt35
opt35
opt108
opt108
opt1
opt1
opt30
opt30
opt420
opt420
opt110
opt110
opt120
opt120
opt103
opt103
opt111
opt111
opt118
opt118
opt16
opt16
opt94
opt94
opt71
opt71
opt60
opt60
opt37
opt37
opt8
opt8
opt42
opt42
opt105
opt105
opt114
opt114
opt75
opt75
opt38
opt38
opt126
opt126
opt33
opt33
opt4
opt4
opt100
opt100
opt17
opt17
opt96
opt96
opt99
opt99
opt121
opt121
opt47
opt47
opt7
opt7
opt15
opt15
opt0
opt0
opt73
opt73
opt95
opt95
opt116
opt116
opt101
opt101
opt5
opt5
opt113
opt113
opt70
opt70
opt115
opt115
opt19
opt19
opt109
opt109
opt129
opt129
opt83
opt83
opt84
opt84
opt91
opt91
opt107
opt107
opt57
opt57
opt128
opt128
opt48
opt48
opt127
opt127
opt49
opt49
opt117
opt117
opt90
opt90
opt119
opt119
opt58
opt58
opt125
opt125
opt55
opt55
opt82
opt82
opt74
opt74
opt29
opt29
opt34
opt34
opt14
opt14
opt52
opt52
opt104
opt104
opt9
opt9
opt66
opt66
opt41
opt41
opt72
opt72
opt85
opt85
opt39
opt39
opt11
opt11
opt69
opt69
opt24
opt24
opt67
opt67
opt54
opt54
opt80
opt80
opt20
opt20
opt106
opt106
opt65
opt65
opt3
opt3
opt88
opt88
opt23
opt23
opt93
opt93""".split("\n")
    def get_service_descriptions(self):
        return """1
	
opt28
	  1688.com	
opt28
2
	
opt97
	  32red.com	
opt97
3
	
opt22
	  888casino	
opt22
4
	
opt86
	  Adidas & Nike	
opt86
5
	
opt46
	  Airbnb	
opt46
6
	
opt61
	  Alibaba | Taobao	
opt61
7
	
opt44
	  Amazon	
opt44
8
	
opt10
	  AOL	
opt10
9
	
opt59
	  Avito	
opt59
10
	
opt56
	  Badoo	
opt56
11
	
opt25
	  BetFair	
opt25
12
	
opt78
	  Blizzard	
opt78
13
	
opt81
	  Bolt	
opt81
14
	
opt89
	  Careem	
opt89
15
	
opt122
	  CashWalk	
opt122
16
	
opt76
	  CityMobil	
opt76
17
	
opt98
	  Clubhouse	
opt98
18
	
opt112
	  CoinBase	
opt112
19
	
opt51
	  CONTACT	
opt51
20
	
opt26
	  Craigslist	
opt26
21
	
opt124
	  Credit Karma	
opt124
22
	
opt123
	  Dabbl	
opt123
23
	
opt53
	  Deliveroo	
opt53
24
	
opt92
	  DiDi	
opt92
25
	
opt45
	  Discord	
opt45
26
	
opt27
	  Dodopizza + PapaJohns	
opt27
27
	
opt40
	  DoorDash	
opt40
28
	
opt32
	  Drom.RU	
opt32
29
	
opt31
	  Drug Vokrug	
opt31
30
	
opt21
	  EasyPay	
opt21
31
	
opt2
	  Facebook	
opt2
32
	
opt43
	  FastMail	
opt43
33
	
opt6
	  Fiverr	
opt6
34
	
opt13
	  Fotostrana	
opt13
35
	
opt68
	  G2A.COM	
opt68
36
	
opt77
	  Gameflip	
opt77
37
	
opt35
	  GetTaxi	
opt35
38
	
opt108
	  Glovo | Raketa	
opt108
39
	
opt1
	  GMail, YTube	
opt1
40
	
opt30
	  GrabTaxi	
opt30
41
	
opt420
	  Grailed	
opt420
42
	
opt110
	  Grindr	
opt110
43
	
opt120
	  Hinge	
opt120
44
	
opt103
	  ICard	
opt103
45
	
opt111
	  IMO	
opt111
46
	
opt118
	  Inboxdollars	
opt118
47
	
opt16
	  Instagram	
opt16
48
	
opt94
	  JD.com	
opt94
49
	
opt71
	  KakaoTalk	
opt71
50
	
opt60
	  Lazada	
opt60
51
	
opt37
	  Line Messenger	
opt37
52
	
opt8
	  LinkedIn	
opt8
53
	
opt42
	  LiveScore	
opt42
54
	
opt105
	  LocalBitcoins	
opt105
55
	
opt114
	  Locanto.com	
opt114
56
	
opt75
	  Lyft	
opt75
57
	
opt38
	  LYKA	
opt38
58
	
opt126
	  Magnit	
opt126
59
	
opt33
	  Mail.RU	
opt33
60
	
opt4
	  Mail.ru Group	
opt4
61
	
opt100
	  Mamba	
opt100
62
	
opt17
	  MeetMe	
opt17
63
	
opt96
	  MiChat	
opt96
64
	
opt99
	  Momo	
opt99
65
	
opt121
	  Monese	
opt121
66
	
opt47
	  MoneyLion 	
opt47
67
	
opt7
	  MS Office 365	
opt7
68
	
opt15
	  MS, Bing, HotMail, Azure	
opt15
69
	
opt0
	  myopinions & erewards	
opt0
70
	
opt73
	  Naver	
opt73
71
	
opt95
	  NetBet	
opt95
72
	
opt116
	  Neteller	
opt116
73
	
opt101
	  Netflix	
opt101
74
	
opt5
	  OD	
opt5
75
	
opt113
	  OfferUp	
opt113
76
	
opt70
	  OLX + goods.ru	
opt70
77
	
opt115
	  Oracle Cloud	
opt115
78
	
opt19
	  OTHER	
opt19
79
	
opt109
	  Paddy Power	
opt109
80
	
opt129
	  Payactiv	
opt129
81
	
opt83
	  PayPal + Ebay	
opt83
82
	
opt84
	  POF.com	
opt84
83
	
opt91
	  Postmates	
opt91
84
	
opt107
	  Prom.UA	
opt107
85
	
opt57
	  Proton Mail	
opt57
86
	
opt128
	  Root	
opt128
87
	
opt48
	  Shopee	
opt48
88
	
opt127
	  Signal	
opt127
89
	
opt49
	  Skout	
opt49
90
	
opt117
	  Skrill	
opt117
91
	
opt90
	  Snapchat	
opt90
92
	
opt119
	  Sneakersnstuff	
opt119
93
	
opt58
	  Steam	
opt58
94
	
opt125
	  Swagbucks	
opt125
95
	
opt55
	  TAN (micropayment)	
opt55
96
	
opt82
	  Tango	
opt82
97
	
opt74
	  Taxi Maksim	
opt74
98
	
opt29
	  Telegram	
opt29
99
	
opt34
	  Tencent QQ	
opt34
100
	
opt14
	  The Insiders	
opt14
101
	
opt52
	  Ticketmaster	
opt52
102
	
opt104
	  TikTok	
opt104
103
	
opt9
	  Tinder	
opt9
104
	
opt66
	  Twilio	
opt66
105
	
opt41
	  Twitter	
opt41
106
	
opt72
	  Uber	
opt72
107
	
opt85
	  Venmo	
opt85
108
	
opt39
	  Verse	
opt39
109
	
opt11
	  Viber	
opt11
110
	
opt69
	  VK	
opt69
111
	
opt24
	  WebMoney&ENUM	
opt24
112
	
opt67
	  WeChat	
opt67
113
	
opt54
	  Weebly	
opt54
114
	
opt80
	  WESTSTEIN	
opt80
115
	
opt20
	  WhatsAPP	
opt20
116
	
opt106
	  Wing Money	
opt106
117
	
opt65
	  Yahoo	
opt65
118
	
opt3
Yahoo Small Business	
opt3
119
	
opt88
	  Yalla.live	
opt88
120
	
opt23
	  Yandex	
opt23
121
	
opt93
	  Zoho	
opt93"""
    def get_number(self, country, service):
        temp = json.loads(requests.get(
            "http://smspva.com/priemnik.php?metod=get_number&country=" + country + "&service=" + service + "&apikey=" + self.api_key).text)
        try:
            return {"number":temp["number"], "id":temp["id"]}
        except KeyError:
            return None
    def Get_Code(self,id, country, service):
        try:
            return json.loads(requests.get(
            "http://smspva.com/priemnik.php?metod=get_sms&country=" + country + "&service=" + service + "&id="+ id+"&apikey=" + self.api_key).text)["sms"]
        except KeyError:
            return None