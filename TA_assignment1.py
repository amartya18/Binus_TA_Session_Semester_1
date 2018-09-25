totaltime = int(input("Input time spent on the road: "))
acc = int(input("Input the acceleration: "))
dist = int(input("Input the distance: "))

for i in range (0, totaltime + 1):
    print("Duration:",i,"Distance","*" * int((0.5 * acc * i * i) / 10))
    veloc = acc * i
if veloc > 60:
    print("The person went over the speed limit.(Max speed was",veloc,"m/s)")
else:
    print("The person did not go over the speed limit.(Max speed was", veloc, "m/s)")
s = int(0.5 * acc * totaltime * totaltime)
if s >= dist:
    print("The person reached the destination.(Reached",s,"m)")
else:
    print("The person did not reached the destination.(Reached",s,"m)")
