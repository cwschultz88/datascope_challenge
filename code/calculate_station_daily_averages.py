from data_retriever import get_cta_data
'''
calculates average daily turnstile fares collected per station

stores results in:
  data/average_daily_rides.csv
'''

def calculate_top_stations(cta_data, daytype_filter=None, save_filename=None):
    station_to_daily_rides = {}
    for datapoint in cta_data:
        if daytype_filter is not None and datapoint[3] != daytype_filter:
            continue

        # if not station entry, add it
        if datapoint[0] not in station_to_daily_rides:
            station_to_daily_rides[datapoint[0]] = [datapoint[1], []]

        # add daily ridership to storage
        station_to_daily_rides[datapoint[0]][1].append(int(datapoint[4]))

    stations_and_average_daily = []
    daily_ride_amounts = []
    for stationid in station_to_daily_rides:
        station_name, daily_rides = station_to_daily_rides[stationid]
        average_daily_rides = sum(daily_rides) / len(daily_rides)
        stations_and_average_daily.append((station_name, average_daily_rides))

    sorted_stations_and_average_daily = sorted(stations_and_average_daily, key=lambda x:-x[1])

    # print out top 5
    if daytype_filter is not None:
        print "*** Top 5 " + daytype_filter + " Stations ***"
    else:
        print "*** Top 5 Stations ***"
    for i in xrange(5):
        print str(i + 1) + ". " + sorted_stations_and_average_daily[i][0] + ' ' + str(sorted_stations_and_average_daily[i][1])

    # save results
    if save_filename is not None:
        save_file = open(save_filename, 'w')
        for station, average_rides in stations_and_average_daily:
            save_file.write(station + ',' + str(average_rides) + '\n')

    return sorted_stations_and_average_daily

def main():
    cta_data = get_cta_data()

    calculate_top_stations(cta_data,  None, 'data/average_daily_rides.csv')
    calculate_top_stations(cta_data, "W")
    calculate_top_stations(cta_data, "A")
    calculate_top_stations(cta_data, "U")
    '''
    station_to_daily_rides = {}
    for datapoint in cta_data:
        # if not station entry, add it
        if datapoint[0] not in station_to_daily_rides:
            station_to_daily_rides[datapoint[0]] = [datapoint[1], []]

        # add daily ridership to storage
        station_to_daily_rides[datapoint[0]][1].append(int(datapoint[4]))

    stations_and_average_daily = []
    daily_ride_amounts = []
    for stationid in station_to_daily_rides:
        station_name, daily_rides = station_to_daily_rides[stationid]
        average_daily_rides = sum(daily_rides) / len(daily_rides)
        stations_and_average_daily.append((station_name, average_daily_rides))

    sorted_stations_and_average_daily = sorted(stations_and_average_daily, key=lambda x:-x[1])

    print "*** General Stats ***"
    print "Mean Average Ridership of a CTA Station: "
    print "Std Deviation Ridership of a CTA Station: "
    print ""

    print "*** Top 10 Stations All Days*****"
    for i in xrange(10):
        print str(i + 1) + ". " + sorted_stations_and_average_daily[i][0] + ' ' + str(sorted_stations_and_average_daily[i][1])
    '''

if __name__ == '__main__':
    main()