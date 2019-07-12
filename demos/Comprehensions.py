from pprint import pprint
import arcpy

feature_cats = r'C:\AdvancedDemos.gdb\Advanced_Cats'

fields = [(field.name, field.type) for field in arcpy.ListFields(feature_cats)]

pprint(fields)
