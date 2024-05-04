#Import needed libraries
import arcpy
from arcpy.sa import *

#Set inputs
Streamline = arcpy.GetParameterAsText(0)
BufferDistance = arcpy.GetParameterAsText(1)
SlopeRaster = arcpy.GetParameterAsText(2)
SlopeValue = arcpy.GetParameterAsText(3)

#Set outputs
StreamPolygon = arcpy.GetParameterAsText(4)

#Creates buffer from stream centerline
arcpy.Buffer_analysis(Streamline, "BufferOut", BufferDistance, "Full", "FLAT")

#Clips slope raster based off buffer extent
arcpy.Clip_management(SlopeRaster, "#", "ClippedRaster", "BufferOut", "#", "ClippingGeometry")

#Reclassifys clipped slope raster based on SlopeValue imput
outReclass1 = Reclassify("ClippedRaster", "Value",
                         RemapRange([[0, SlopeValue, 1], [SlopeValue, 100, "NODATA"]]))
outReclass1.save ("ReclassedRaster")

#Converts reclassified raster to a polygon
arcpy.RasterToPolygon_conversion("ReclassedRaster", StreamPolygon, "SIMPLIFY")

#Deletes uneeded files that are used in the script
arcpy.management.Delete("BufferOut")
arcpy.management.Delete("ClippedRaster")
arcpy.management.Delete("ReclassedRaster")
