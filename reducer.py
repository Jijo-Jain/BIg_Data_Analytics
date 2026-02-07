import sys

current = None
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    key, value = line.split("\t", 1)
    value = int(value)

    if current == key:
        count += value
    else:
        if current is not None:
            print(f"{current}\t{count}")
        current = key
        count = value

if current is not None:
    print(f"{current}\t{count}")
