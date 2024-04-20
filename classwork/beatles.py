
beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

band_members_to_add = ["Stu Sutcliffe", "Pete Best"]
for member in band_members_to_add:
    beatles.append(member)
del beatles[-2:]
beatles.insert(0, "Ringo Starr")
print("Updated Beatles lineup:", beatles)
