import csv
import os
import django
import sys
import pandas as pd

os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "edaproj.settings")  # 1. 여기서 프로젝트명.settings입력
django.setup()

from homepage.models import Born

CSV_PATH = './homepage/static/csv/bird.csv'  # 3. csv 파일 경로

born_df = pd.read_csv(CSV_PATH)
print(born_df)

# bulk_list = []
# with open(CSV_PATH, newline='') as csvfile:  # 4. newline =''
#     data_reader = csv.reader(csvfile)
#     next(csvfile) # 첫 행 제거
#     for i, row in enumerate(data_reader):
#         try:
#             bulk_list.append(Born(
#                 id=row[0],
#                 huml = row[1],
#                 humw = row[2],
#                 ulnal = row[3],
#                 ulnaw = row[4],
#                 feml = row[5],
#                 femw = row[6],
#                 tibl = row[7],
#                 tibw = row[8],
#                 tarl = row[9],
#                 tarw = row[10],
#                 type = row[11]
#             ))
#         except:
#             print(row[0])
# Born.objects.bulk_create(bulk_list)
# print(Born.objects.values())