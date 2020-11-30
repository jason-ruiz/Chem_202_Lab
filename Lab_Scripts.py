import gspread
import statistics
from oauth2client.service_account import ServiceAccountCredentials

# assigning credentials
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets' ,"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("scratch.json", scope)
client = gspread.authorize(creds)

# specific google sheet to open
sheet = client.open("Copy of Post-Lab 7: Calorimetry Part 2: Enthalpy of Reaction - Line chart 1").sheet1

# getting all values
all = sheet.get_all_values()

print("Choose a column number in google sheets")

# iterating through the names
for i in all[0]:
    print(i)

# digging through column number in sheets
data = sheet.col_values(raw_input('Column Number: '))
print("Name: " + data[0])

# gathering values
x = [item for item in data if item]
g = raw_input('Column Name: ')
x.remove(g)

# finding the total sum
sum = 0
tuple = []
for ele in x:
    tuple.append(ele)
    sum += float(ele)
    std = float(ele)
# finding average
res = sum
ave = sum / len(x)
print("The addition of float list elements is : " + str(res))
print("The average of float list elements is : " + str(ave))
