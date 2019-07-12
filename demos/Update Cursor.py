import arcpy

in_table = r'C:\AdvancedDemos.gdb\Advanced_Cats'
fields = ['Type', 'Size', 'Friendly']

output = '\nFriendly Cats:\n'

with arcpy.da.UpdateCursor(in_table, fields) as uc:
    for row in uc:
        if row[0].lower() == 'raccoon':
            row[1] = 10
            row[2] = 1
            # row[1] = 3
            # row[2] = 0
            uc.updateRow(row)

print('fin.')
