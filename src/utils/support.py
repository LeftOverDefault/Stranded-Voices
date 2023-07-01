def ConvertDashUnderscore(string):
    underscore_string = ""
    string_list = string.split("-")
    for i in string_list:
        underscore_string += i + "_"
    return underscore_string[:-1]


def ConvertUnderscoreDash(string):
    dash_string = ""
    string_list = string.split("_")
    for i in string_list:
        dash_string += i + "-"
    return dash_string[:-1]