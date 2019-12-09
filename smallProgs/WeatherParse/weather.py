import csv

line_count = 0
temp_total = 0
rainy_days = 0
timelist = []
templist = []
unformatted_fieldnames = '"Местное время в Огурцово";"T";"Po";"P";"Pa";"U";"DD";"Ff";"ff10";"ff3";"N";"WW";"W1";"W2' \
                         '";"Tn";"Tx";"Cl";"Nh";"H";"Cm";"Ch";"VV";"Td";"RRR";"tR";"E";"Tg";"E\'";"sss"'.split(';')
fieldnames = [element.strip('"') for element in unformatted_fieldnames]

with open('weather_2019.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', fieldnames=fieldnames)
    for row in reader:

        if row['Местное время в Огурцово'].startswith('#'):
            del row['Местное время в Огурцово']
        else:

            timelist.append(row['Местное время в Огурцово'][0:10])
            templist.append(float(row['T']))
            line_count += 1
            temp_total += float(row['T'])
            if row['RRR'] == '' or row['RRR'] == 'Осадков нет':
                pass
            else:
                rainy_days += 1

avarage_temp_total = temp_total / line_count
result = {i: timelist.count(i) for i in timelist}
count_per_day = list(result.values())

temp_sum_daily = []
for number in count_per_day:
    temp_sum_daily.append(sum(templist[0:number]))
    del templist[0:number]

daily_temp = {list(result.keys())[i]: round(temp_sum_daily[i], 2) for i in range(len(list(result.keys())))}

max_temp, max_date = max(zip(daily_temp.values(), daily_temp.keys()))
min_temp, min_date = min(zip(daily_temp.values(), daily_temp.keys()))

print(f'Средняя температура - {round(avarage_temp_total, 2)} градусов, дождливых дней было {rainy_days}. Самый теплый '
      f'день был - {max_date}, самый холодный день - {min_date}')
