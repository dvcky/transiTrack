# PREREQUISITES: requests, protobuf, gtfs-realtime-bindings, pyqt5, qt-material

# google_transit downloaded at http://web.mta.info/developers/developer-data-terms.html

from google.transit import gtfs_realtime_pb2
import os
import requests

r = requests.get("https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace", headers={"x-api-key":"API KEY HERE"})

feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(r.content)
file = open('data', 'w')
file.write(str(feed))
#for entity in feed.entity:
#  if entity.HasField('trip_update'):
#    file.write(str(entity))
