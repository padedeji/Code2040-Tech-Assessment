import datetime, iso8601

#This function adds seconds to an iso8601 datestamp and returns the new datestamp

def dating_game(datestamp, interval):
    new_date = iso8601.parse_date(datestamp) + datetime.timedelta(seconds=int(interval))
    new_date = new_date.isoformat()[:-6] + 'Z' #removes +00:00 from the new datestamp
    return new_date

print(dating_game("2016-08-31T06:41:50Z", "236872"))
