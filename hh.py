import json
import datetime

date = (datetime.datetime.date(datetime.datetime.now()))

with open(f"results/hackerRank_courses_at-{str(date.day)+"-"+str(date.month)+"-"+str(date.year)}.json", "r") as json_file:
    x = json.load(json_file)

all_badges_titles = set()
all_certificate_titles = set()
for dct in x:
    for badge in dct['badges']:
        all_badges_titles.add(badge)
    for certificate in dct['certificates']:
        all_certificate_titles.add(certificate)
    
print(all_badges_titles)
print(all_certificate_titles)

# import json
# import datetime
# import pandas as pd
# date = (datetime.datetime.date(datetime.datetime.now()))

# with open(f"results/hackerRank_courses_at-{str(date.day)+"-"+str(date.month)+"-"+str(date.year)}.json", "r") as json_file:
#     x = json.load(json_file)

# all_badges = {}
# all_certificate = {}
# for dct in x:
#     for badge in dct['badges']:
#         if badge in all_badges:
#             all_badges[badge] += 1
#         else:
#             all_badges[badge] = 1
#     for certificate in dct['certificates']:
#         if certificate in all_certificate:
#             all_certificate[certificate]+=1
#         else:
#             all_certificate[certificate]=1
    
# df = pd.DataFrame(all_certificate)
# print(df)