import geopandas
import matplotlib.pyplot as plt
import pandas as pd
import shapely
from shapely.geometry import Point, Polygon
import seaborn as sns
from geopandas.tools import sjoin
import numpy as np

geo_md = geopandas.read_file('lithogeomd_polygon.shp')  # geolitholohies in MD
geo_va = geopandas.read_file('lithogeova_polygon.shp')  # geolithologies in VA
meta = pd.read_csv('lithtbl.txt')  # lithological characteristics

geo_md = geo_md.drop(geo_md[geo_md.LITH_CODE=='water'].index)
geo_md = geo_md.drop(geo_md[geo_md.LITH_CODE=='no_geol'].index)
geo_va = geo_va.drop(geo_va[geo_va.LITH_CODE=='water'].index)
geo_va = geo_va.drop(geo_va[geo_va.LITH_CODE=='no_geol'].index)

geo_md = geo_md.merge(meta,how='left',on='LITH_CODE')
geo_va = geo_va.merge(meta,how='left',on='LITH_CODE')
geology = df = pd.concat([geo_md,geo_va],axis=0)

nitrate1 = pd.read_csv('total_nitrogen.csv')
nitrate1['Point'] = nitrate1['Point'].apply(shapely.wkt.loads)
nitrate = geopandas.GeoDataFrame(nitrate1,crs='EPSG:4269',geometry='Point')
joined = sjoin(geology,nitrate,how='inner',op='contains')

joined.info()

print(len(joined['MINERALOGY'].unique()))

ax=joined.boxplot(by='MINERALOGY', column=['MeasureValue'], grid=False,rot=5)
ax.set_ylabel('Total nitrogen concentration')
#sns.swarmplot(x='ROCK_TYPE_CLASS',y='MeasureValue', data=joined)
plt.show()

sns.countplot()