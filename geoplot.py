
import json # reading geojson files

import warnings
warnings.filterwarnings("ignore")

# Brussels
# Chicago
# DC
# Detroit
# Lisbon
# Madrid
# MexicoCity
# Paris
# SanFrancisco
# TelAviv
# Zurich

city = 'TelAviv'
data = json.load(open("/home/hakhan/Google Drive/Scooter_Sheets/Dictionaries/Scripts/Neighborhood polygons/US_Cities_Zip_Codes_Data/"+city+".geojson"))
import matplotlib.pyplot as plt # plotting data
fig = plt.figure() # create a figure to contain the plot elements
ax = fig.gca(xlabel="Longitude", ylabel="Latitude")


from shapely.geometry import asShape # manipulating geometry
from descartes import PolygonPatch
count = 0



for feat in data["features"]:
# convert the geometry to shapely
    # if count < 1or  count > 30 :
    
    geom = asShape(feat["geometry"])
    x, y = geom.centroid.x, geom.centroid.y
    # plot the centroids
    if 1:
    # # if count > 30 :
        ax.plot(x, y)
        # ax.text(x,y,str(count))
    count+=1
    # ax.text(x, y, feat["properties"]["ward"], fontsize=6, bbox = dict(fc='w', alpha=0.3))
    # plot the polygon features: type help(PolygonPatch) for more args
    # if count > 30 :
    if 1:
        ax.add_patch(PolygonPatch(feat["geometry"], fc='grey', ec='blue',
                alpha=0.6, lw=0.1, ls='-', zorder=2))

ax.clear # clear the axes memory
plt.savefig('NHImages/'+city+'.png')
# plt.show()

print(count)