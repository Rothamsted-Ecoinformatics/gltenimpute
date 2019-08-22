import requests
import argparse
import json

parser = argparse.ArgumentParser(description='read a point')

parser.add_argument('lat',metavar='lat',type=float,help='enter the point latitude')
parser.add_argument('lon',metavar='lon',type=float,help='enter the point longitude')

args = parser.parse_args()
print(args.lat)

print("hello")

#resp = requests.get('https://landgisapi.opengeohub.org/query/point?lat='+str(args.lat)+'&lon='+str(args.lon)+'&coll=predicted250m&regex=sol_grtgroup_usda.soiltax_c_250m_b0..0cm_1950..2017_v0.1.tif')

#https://rest.soilgrids.org/query.html
resp = requests.get('https://rest.soilgrids.org/query?lat='+str(args.lat)+'&lon='+str(args.lon)+'&attributes=TAXNWRB') 
print(json.dumps(resp.json(), indent=4, sort_keys=True))