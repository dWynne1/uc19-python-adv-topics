import arcpy

in_table = r'C:\AdvancedDemos.gdb\Advanced_Cats'
field_names = ['OID@', 'Type']
sql = "friendly = 1"

output = '\nFriendly Cats:\n'

with arcpy.da.SearchCursor(in_table, field_names, sql) as sc:
    for row in sc:
        output += 'OID: {0} -- {1} cat\n'.format(*row)
        
print(output)
