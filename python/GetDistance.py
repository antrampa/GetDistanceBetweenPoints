import simplejson, urllib
orig_lat = 41.43206
orig_lng = -81.38992
dest_lat = -33.86748
dest_lng = 151.20699
orig_coord = orig_lat, orig_lng
dest_coord = dest_lat, dest_lng
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key=AIzaSyCc4jrUVb9Ky0b7eef5Bo2ValXnXFq8N4o"
result= simplejson.load(urllib.urlopen(url))
print(result)
# driving_time = result['rows'][0]['elements'][0]['duration']['value']