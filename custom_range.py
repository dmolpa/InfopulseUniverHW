def custom_range(stop=0,start=0):
    yield start
    if start+1 < stop:
        yield from custom_range(stop,start+1)

for i in custom_range(14):
    print(i)