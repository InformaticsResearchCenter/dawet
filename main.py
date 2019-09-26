import dawet

ws = dawet.Dawet()

# vr = ws.getData("1184047", "pertemuan1", 0)

vr = ws.setData("1184047", "pertemuan1", 0, 10)

print(vr)