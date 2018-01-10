import arcpy

chr_map_doc_base = r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Upper_Yaquina_TMDL_BC_Automated_Outline.mxd'
chr_png_map_new = r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Up_Yaq_Outline.png'
mapdoc = arcpy.mapping.MapDocument(chr_map_doc_base)
arcpy.mapping.ExportToPNG (mapdoc, chr_png_map_new, resolution=300)
