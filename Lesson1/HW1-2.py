time = int(input('input time in seconds - '))
H = 3600
M = 60
hours = time // H
if hours < 10:
    hours = str("0" + str(hours))
else:
    str(hours)
minutes = (time - int(hours) * 3600) // M
if minutes < 10:
    minutes = str("0" + str(minutes))
else:
    str(minutes)
seconds = time - ((int(hours) * H) + (int(minutes) * M))
if seconds < 10:
    seconds = str("0" + str(seconds))
else:
    str(seconds)
print(str(hours) + ':' + str(minutes) + ':' + str(seconds))
