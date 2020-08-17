import geopandas
import matplotlib.pyplot as plt
import pandas as pd
import shapely
from shapely.geometry import Point, Polygon

geo_md = geopandas.read_file('lithogeomd_polygon.shp')  # geolitholohies in MD
geo_va = geopandas.read_file('lithogeova_polygon.shp')  # geolithologies in VA
meta = pd.read_csv('lithtbl.txt')  # lithological characteristics

geo_md = geo_md.drop(geo_md[geo_md.LITH_CODE=='water'].index)
geo_md = geo_md.drop(geo_md[geo_md.LITH_CODE=='no_geol'].index)
geo_va = geo_va.drop(geo_va[geo_va.LITH_CODE=='water'].index)
geo_va = geo_va.drop(geo_va[geo_va.LITH_CODE=='no_geol'].index)

geo_md = geo_md.merge(meta,how='left',on='LITH_CODE')
geo_va = geo_va.merge(meta,how='left',on='LITH_CODE')

'''
water_md = pd.read_csv('md_water_short.csv')
water_md['Point'] = water_md['Point'].apply(shapely.wkt.loads)
md_gdf = geopandas.GeoDataFrame(water_md,crs='EPSG:4269', geometry='Point')
water_va = pd.read_csv('va_water_short.csv')
water_va['Point'] = water_va['Point'].apply(shapely.wkt.loads)
va_gdf = geopandas.GeoDataFrame(water_va,crs='EPSG:4269', geometry='Point')

HUC12_MD=pd.read_csv('HUC12_MD.csv')
HUC12_MD['geometry'] = HUC12_MD['geometry'].apply(shapely.wkt.loads)
huc12_md = geopandas.GeoDataFrame(HUC12_MD, crs='epsg:4269')
HUC12_VA=pd.read_csv('HUC12_VA.csv')
HUC12_VA['geometry'] = HUC12_VA['geometry'].apply(shapely.wkt.loads)
huc12_va = geopandas.GeoDataFrame(HUC12_VA, crs='epsg:4269')
print(geo_va.index)
print('---------')
huc12_va.index = list(huc12_va.index)
print(huc12_va.index)
intersect_mask = geo_va.geometry.intersects(huc12_va)
huc12_va1 = huc12_va[intersect_mask]
'''

ax = geo_md.plot(geo_md['LITH_CODE'])
geo_va.plot(geo_va['LITH_CODE'],ax=ax)
#md_gdf.plot(ax=ax,markersize=5,color='blue')
#va_gdf.plot(ax=ax,markersize=5,color='blue')
#huc12_md.boundary.plot(ax=ax,edgecolor='black',linewidth=0.3)
#huc12_va.boundary.plot(ax=ax,edgecolor='black',linewidth=0.3)
plt.show()

