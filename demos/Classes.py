import arcpy


class Search:
    """
    Searches for data and prints the results to the console
    """

    def __init__(self, input_feature_class, field_name, print_header=False):
        """
        :param input_feature_class: feature class used print fields
        :param field_name: the name of the field whose data will be printed
        """
        self.input_feature_class = input_feature_class
        self.field_name = field_name
        self.print_header = print_header

    def print_fields(self):
        """
        Prints the content of a field to the console
        """
        if self.print_header:
            print('\n' + self.field_name.upper())

        with arcpy.da.SearchCursor(self.input_feature_class, self.field_name) as search_cursor:
            for field_data in search_cursor:
                print(*field_data)  # unpack the tuple


# Print out the types of cats in our data
feature_cats = r'C:\AdvancedDemos.gdb\Advanced_Cats'
field_name = 'Type'

search_types = Search(feature_cats, field_name)
search_types.print_fields()

# # Print out the "Friendly" data
# search_friendly = Search(feature_cats, 'Friendly')
# search_friendly.print_fields()
#
# # Print out the "Size" data
# Search(feature_cats, 'Size', print_header=True).print_fields()
