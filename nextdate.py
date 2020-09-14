import datetime

date = input().split('-')

month = {
    'JAN': '1',
    'FEB': '2',
    'MAR': '3',
    'APR': '4'
}

revmonth = dict(map(reversed,month.items()))

date1 = datetime.date(int(date[2]),int(month[date[1]]),int(date[0]))

nextdate = str(date1 + datetime.timedelta(days=1))

nextdate = nextdate.split('-')

print(nextdate)

nextdate[1] = revmonth[nextdate[1].strip('0')]


print(nextdate[2]+'-'+nextdate[1]+'-'+nextdate[0])