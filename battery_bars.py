def battery_bars(percent):
    if percent >= 100:
        return "[#####]"
    elif percent >= 80:
        return "[####.]"
    elif percent >= 60:
        return "[###..]"
    elif percent >= 40:
        return "[##...]"
    elif percent >= 20:
        return "[#....]"
    else:
        return "[.....]"