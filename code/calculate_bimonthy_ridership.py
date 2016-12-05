from data_retriever import get_cta_data
from time import strptime

'''
 Calculates the average turnstile fares collected per station in bimothly periods

 Only considers stations in filter_station_list

 Saves results in:
   data/bimonthly_average_daily_rides_per_station.csv

'''

filter_station_list = set(['Lake/State',
                           'Clark/Lake',
                           'Chicago/State',
                           'Belmont-North Main',
                           'Fullerton',
                           'Grand/State',
                           'Roosevelt',
                           "O'Hare Airport",
                           'Washington/Dearborn',
                           'Jackson/State',
                           'Monroe/State',
                           '95th/Dan Ryan'])


def main():
    cta_data = get_cta_data()
    bimonthly_month_daily_rides = {i: [] for i in xrange(6)}
    for data in cta_data:
        if data[1] in filter_station_list:
            date = strptime(data[2], "%m/%d/%y")
            month = date.tm_mon
            if month == 1 or month == 2:
                bimonthly_month_daily_rides[0].append(int(data[4]))
            elif month == 3 or month == 4:
                bimonthly_month_daily_rides[1].append(int(data[4]))
            elif month == 5 or month == 6:
                bimonthly_month_daily_rides[2].append(int(data[4]))
            elif month == 7 or month == 8:
                bimonthly_month_daily_rides[3].append(int(data[4]))
            elif month == 9 or month == 10:
                bimonthly_month_daily_rides[4].append(int(data[4]))
            else:
                bimonthly_month_daily_rides[5].append(int(data[4]))

    bimonthly_average_daily_rides_per_station = {bimonthly_period_index: sum(bimonthly_month_daily_rides[bimonthly_period_index]) / len(bimonthly_month_daily_rides[bimonthly_period_index]) for bimonthly_period_index in bimonthly_month_daily_rides}
    bimonthly_average_daily_rides_per_station_savefile = open('data/bimonthly_average_daily_rides_per_station.csv', 'w')
    for bimonthly_period_index in bimonthly_average_daily_rides_per_station:
        bimonthly_average_daily_rides_per_station_savefile.write(str(bimonthly_period_index + 1) + ',' + str(bimonthly_average_daily_rides_per_station[bimonthly_period_index]) + '\n')
if __name__ == '__main__':
    main()