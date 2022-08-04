import pandas as pd
from modelloader import predictionreulst
# d = pd.read_excel("./confing/name.xlsx",index_col="label")
# dals=['87princess','Alan','Alisasa','Brian','Enoki mushroom','Fred','Hook','Huang Bro-Wei',
# 'Huang Bro-zhe','James','Joseph','Kart','Li Ke Tai Tai','Ma face lady','Mihara','Keigo','Pierre Liu',
# 'Tang Qiyang','yusheng','Zhong Mingxuan','aries','bacon','beef','coffee','cool','crown','ding','dinter',
# 'doctor','dontkjoanne','dried fish','e','egg','frog','gina','goldfish_brian','hajimesyacho','how how',
# 'imserious','jam','joeman','la','lawyer','lulu','mc jeng','ricky','soon','toyz','tsai','wawako','yuci']

# df = pd.DataFrame(dals)
# df.to_excel("./condata.xlsx")
# d = pd.read_excel("../confing/name.xlsx")
yber,df = predictionreulst("D:\work\GIT\detectionyoutubet\static\img\d6036476.jpg")
# print(d)
print(yber,df)
