import arcpy

mxd = r'\\Deqhq1\tmdl\TMDL_WR\MidCoast\GIS\BacteriaTMDL\UpperYaquinaRiver\MapDocs\templates\Watershed_location_in_OR_TMDL_Ver00.mxd'
chr_png_map_new = r'\\Deqhq1\tmdl\TMDL_WR\MidCoast\Documents\Bacteria\TMDLReports\upper-yaquina-river\figures\Up_Yaq_Outline_kmb.png'
chr_png_map_soils = r'\\Deqhq1\tmdl\TMDL_WR\MidCoast\Documents\Bacteria\TMDLReports\upper-yaquina-river\figures\Up_Yaq_Soils_kmb.png'
mapdoc = arcpy.mapping.MapDocument(mxd)
# make sure the page layout is current view to get map with multiple data frames
mapdoc.activeView = 'PAGE_LAYOUT'
# have to save and then reload mxd for the change in active view to take effect
mapdoc.save()

del mapdoc
mapdoc = arcpy.mapping.MapDocument(mxd)
arcpy.mapping.ExportToPNG (mapdoc, chr_png_map_new)

mxd = r'\\Deqhq1\tmdl\TMDL_WR\MidCoast\GIS\BacteriaTMDL\UpperYaquinaRiver\MapDocs\templates\Watershed_location_in_OR_TMDL_Ver00.mxd'
chr_png_map_new = r'\\Deqhq1\tmdl\TMDL_WR\MidCoast\Documents\Bacteria\TMDLReports\upper-yaquina-river\figures\Up_Yaq_Outline_With_Soils_kmb.png'
mxd_new = arcpy.mapping.MapDocument(mxd)
layers = arcpy.mapping.ListLayers(mxd_new)

df = arcpy.mapping.ListDataFrames(mxd_new)[0]
addLayer = arcpy.mapping.Layer(r"\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Upper_Yaquina_Soils.lyr")
arcpy.mapping.AddLayer(df, addLayer)

mxd.saveACopy(mxd_new)
del mxd_new, addLayer

# make sure the page layout is current view to get map with multiple data frames
mapdoc.activeView = 'PAGE_LAYOUT'
# have to save and then reload mxd for the change in active view to take effect
mapdoc.save()

del mapdoc
mapdoc = arcpy.mapping.MapDocument(mxd)
arcpy.mapping.ExportToPNG (mapdoc, chr_png_map_new)
