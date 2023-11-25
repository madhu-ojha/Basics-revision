s = "ababbb"
length = len(s)

left = 0
right = 0
max_count = 0
sett = set()

while right < length:
    if s[right] not in sett:
        sett.update(s[right])
        right += 1
        max_count = max(max_count, right-left)
    else:
        sett.remove(s[left])
        left += 1
print(max_count)
