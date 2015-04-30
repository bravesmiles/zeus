from zeus import ZeusClient
import os
import json
import random
import csv
import time

BATCH_AMOUNT = 5000
ZEUS_API = "http://api.ciscozeus.io"
token = "68c5e168"
z = ZeusClient(token, ZEUS_API)

# log_name = raw_input("please input the log_name:")
log_name = "stackoverflow"
sample_file = "StackOverflow/StackOverflow_20140116-20140122.csv"

csvfile = open("data/"+sample_file)
reader = csv.reader(csvfile)

header = reader.next()

logs = []
for row in reader:
    try:
        timestamp = int(time.mktime(time.strptime(row[0], "%Y-%m-%d %H:%M:%S")))
        message = row[1]
        logs.append({"message": message, "timestamp": timestamp})
    except:
        print "invalid"

total = len(logs)
num_package = total/BATCH_AMOUNT
for i in range(num_package):
    print 'Sending %d~%d'%(i*BATCH_AMOUNT, (i+1)*BATCH_AMOUNT)
    print z.sendLog(log_name, logs[i*BATCH_AMOUNT:(i+1)*BATCH_AMOUNT])

print 'Sending %d~%d'%((i+1)*BATCH_AMOUNT, total)
print z.sendLog(log_name, logs[(i+1)*BATCH_AMOUNT: total])
