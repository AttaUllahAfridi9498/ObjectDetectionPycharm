

counter=0
total=100

for x in range(total):
    if(counter==0 or counter== total):
        print("Counter matches the total value")
    counter += 1
    print(counter, ",")
    break
