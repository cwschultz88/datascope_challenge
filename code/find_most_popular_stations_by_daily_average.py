from data_retriever import get_cta_data

def calculate_top_stations(cta_data, number_of_stations_to_display, print_title, daytype_filter=None):
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

    print print_title
    for i in xrange(number_of_stations_to_display):
        print str(i + 1) + ". " + sorted_stations_and_average_daily[i][0] + ' ' + str(sorted_stations_and_average_daily[i][1])

    return sorted_stations_and_average_daily

def main():
    cta_data = get_cta_data()

    calculate_top_stations(cta_data, 5, "*** Top 5 Stations All Days *****")
    calculate_top_stations(cta_data, 5, "*** Top 5 Stations Weekdays *****", "W")
    calculate_top_stations(cta_data, 5, "*** Top 5 Stations Saturdays *****", "A")
    calculate_top_stations(cta_data, 5, "*** Top 5 Stations Sunday/Holiday *****", "U")
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