What is the Stream Bank Locator and how does it work?
	SBLocate is a python script that runs within an ArcPro toolbox. For this application it is aimed at delineating the edges of a stream, but what it really is doing is turning areas that have similar slope values into one continuous polygon. It could be applied to similar applications such as finding the edges or roadways, or with a bit of work inverted to locate areas with high slope values like cliff faces. 
Regardless, the output from this script is not the desired line feature class but is a polygon that in theory has a perimeter that is equal to the stream's bank. With that in mind this is a semi automated process. SBLocate should do most of the heavy lifting but some thoughtful inputs and (hopefully) brief work on the output is required to get the desired line feature class of the stream bank. 
	This document is a comprehensive step by step guide on how to set up, run and produce a finished product, with some notes on things to avoid.  

Needed Files
Slope raster 
Any slope raster will do as long as it's a file saved somewhere on your computer, what we used for our project can be downloaded as follows 
Oregon DOGAMI lidar viewer >  Bare earth slope (degrees) > … > description > ArcGIS Online Map Viewer > Save to portal  > Open Arc Pro > Catalog > Portal > Add and open slope map > Right clip on slope layer in contents > Sharing > Save as layer file 
This will be your slope raster input
The tool only accepts layer files, not rasters opened in ArcPro. Some of the functions will not run if the raster image open in pro is too large, but will have no problem running on the saved raster image. If you wish to run this on a different raster, simply Right clip on slope layer in contents > Sharing > Save as layer file 
Stream centerline data
Any line is a valid input for the stream centerline, for this project we used the ODFW Centerline data 
Download this, add the database to ArcPro and add the WRS_Gen9 to your map
Tool Setup
Download both SBLocate.py and Steam Bank Locator.atbx
In ArcPro, got to catalog > Toolboxes > add toolbox and choose Stream Bank Locator.atbx
Expand the new Stream Bank toolbox, right click Stream Bank Locator >choose properties > Execution. Click the folder icon in the top right, then select the SBLocate.py file

Arcpro Set up
Make sure your environment is set to the current workplace
Analysis toolbar > Environments > Current Workplace
Make sure you are allowing geoprocessing tools to overwrite existing data
Project > Options > Geoprocessing > Allow geoprocessing tools to overwrite existing data
Create the line feature layer for the desired stream
Select the desired stream centerline from WRS > Selection > New layer from selection features. This will be your input for the Stream centerline.
NOTE the longer your stream centerline, the longer the tool will have to run. Some stream centerlines will be too long for the tool, and it will fail after running for quite some time. It's recommended to trim your centerline to a reasonable size.
 If you need a shorter Line segment, use the split tool to segment the WSR layer BEFORE making a new layer. Make a new layer from the segment using the above process
If the tool runs and fails, make sure to delete Delete BufferOut, ClippedRaster, and ReclassedRaster from, your geodatabase
Running the Tool
To run the tool, double click the Stream Bank Locator script in the toolbox or right click > open

Tool Inputs
Stream Center Line
The stream centerline you created earlier
Buffer Distance (ft)
The distance the tool will clip the raster from your stream centerline. Make sure it is big enough to capture the full extent of the stream, but be careful to not make it too big or it will greatly increase the run time of the tool. 
Slope Raster
The slope raster file you saved earlier 
Slope value
This value will determine what is included in the final polygon and what is not. Whatever slope value is chosen, all slope values above that value will be removed from the slope raster. You want to choose a slope value greater than the slope of your stream, but less than the slope of the stream bank. This may take some trial and error, and some values will work better in some areas than in others. I often find a slope value between 6-8 is a good starting place.
Steam Polygon
This is what your output polygon will be named. Since this will be an input to python code, make sure the name has no spaces or special characters. If you run the tool multiple times, make sure to give it a different name. 
SUGGESTION: including the slope value used in the name of your polygon can be very useful if you have many polygon layers
Final Steps
After the tool has run, the stream polygon can be found in your geodatabase. 
Add the polygon to your map
Select the stream polygon, make a new layer from your selection, run the polygon to line tool on the new polygon layer
Often your stream will be connected to areas that are not part of your stream. Use modify tools to disconnect the stream polygon from the rest of the undesired polygon before you make your stream polygon a new layer.
To reach the modify tools, select the Edit Ribbon > Modify 
Split will help disconnect your stream from undesired areas, 
Once you have your line feature class, you may still need to clean up your data
Again using the split tool will help remove unwanted lines. Once your line is split, select the unwanted areas and then delete them.
The split tool can also be used at the start and end of the stream to make distinct left and right sides of your stream 
Continue Feature can help extend a line over a desired area, like between to disconnected areas
Finally, if desired, you can use the merge tool to turn all of the segmented lines into one continuous feature. Make sure all the individual segments are selected, and then run the tool

Warnings
If the tool fails, 
Delete BufferOut, ClippedRaster, ReclassedRaster
