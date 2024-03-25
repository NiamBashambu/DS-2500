import geopandas as gpd
from shapely.geometry import Point



park_data= gpd.read_file("/Users/niambashambu/Desktop/DS 2500/Labs/Open_Space.geojson")
park_data.plot()

park_data = park_data.to_crs(epsg=3347)

wvh_lat, wvh_lon = 42.3398, -71.0892
wvh_point = Point(wvh_lon, wvh_lat)
wvh_point_transformed = gpd.GeoSeries([wvh_point], crs="EPSG:4326").to_crs(epsg=3347)

park_data['distance_to_wvh'] = park_data.geometry.distance(wvh_point_transformed)
closest_park = park_data.loc[park_data['distance_to_wvh'].idxmin()]
#park_type = closest_park["TYPE"] == 1
total_acres = park_data['ACRES'].sum()

#closest_large_park = park_data[park_data['ACRES'] >= 150].loc[park_data['distance_to_wvh'].idxmin()]
#name_park = closest_large_park["NAME"]

dorchester_parks_count = park_data[park_data['DISTRICT'] == 'Dorchester'].shape[0]


print(dorchester_parks_count,total_acres)