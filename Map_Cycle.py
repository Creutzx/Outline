import arcpy
import os

#Specify output path and final output PDF
outPath = r'\\DEQHQ1\TMDL_WR\MidCoast\GIS\Figures\python\makelocinstate'

#Specify the map document and the data frame
mxd = arcpy.mapping.MapDocument(r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Upper_Yaquina_TMDL_BC_Automated_V2.mxd')
df = arcpy.mapping.ListDataFrames(mxd)[0]

#zoom to upper Yaquina watershed
watershedLayer = arcpy.mapping.ListLayers(mxd, 'HUC 10', df)[0]
arcpy.SelectLayerByAttribute_management(watershedLayer)
df.zoomToSelectedFeatures()

#Turn on visibility for each of the watershed properties and export the page
lyrList = ["Elevation Range", "Precipitation Range", "Upper_Yaquina_Soils"]
for lyrName in lyrList:
    lyr = arcpy.mapping.ListLayers(mxd, lyrName, df)[0]
    lyr.visible = True

#Export each map image
    tmpPNG = outPath + lyrName + '_.png'
    if os.path.exists(tmpPNG):
        os.remove(tmpPNG)
    arcpy.mapping.ExportToPNG(mxd, tmpPNG)

#Turn off layer visibility and clean up for next pass through the loop
    lyr.visible = False
    del lyr, tmpPNG
del mxd, df
