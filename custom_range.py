def custom_range(start,stop):
    yield start
    if start+1 < stop:
        yield from custom_range(start+1,stop)

for i in custom_range(0,14):
    print(i)