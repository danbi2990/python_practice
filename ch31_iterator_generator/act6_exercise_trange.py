

# Q1.
# calculate first and evaluate condition
# def trange(start, end, step):
# 	shour, smin, ssec = start[0], start[1], start[2]
# 	while True:
# 		yield (shour, smin, ssec)
# 		shour += step[0] + (smin+step[1])//60
# 		smin = (smin + step[1] + (ssec+step[2])//60) % 60
# 		ssec = (ssec + step[2]) % 60

# 		if shour > end[0]:
# 			return
# 		if shour == end[0] and smin > end[1]:
# 			return
# 		if shour == end[0] and smin == end[1] and ssec > end[2]:
# 			return

# for time in trange((10, 10, 10), (13, 50, 15), (0, 15, 12)):
#     print(time)


# Q2.
# def rtrange(start, end, step):
# 	shour, smin, ssec = start[0], start[1], start[2]
# 	while True:
# 		new_start = yield (shour, smin, ssec)
# 		if new_start is not None:
# 			shour, smin, ssec = new_start[0], new_start[1], new_start[2]
# 			continue

# 		shour += step[0] + (smin+step[1])//60
# 		smin = (smin + step[1] + (ssec+step[2])//60) % 60
# 		ssec = (ssec + step[2]) % 60

# 		if shour > end[0]:
# 			return
# 		if shour == end[0] and smin > end[1]:
# 			return
# 		if shour == end[0] and smin == end[1] and ssec > end[2]:
# 			return

# ts = rtrange((10, 10, 10), (13, 50, 15), (0, 15, 12))  
# for _ in range(3):
#     print(next(ts))

# print(ts.send((8, 5, 50)))
# for _ in range(3):
#     print(next(ts))


# Q3.
# import random

# def trange(start, end, step):
# 	shour, smin, ssec = start[0], start[1], start[2]
# 	while True:
# 		temp = random.uniform(10.0, 25.0)
# 		yield "%02d:%02d:%02d %3.1f" % (shour, smin, ssec, temp)
# 		shour += step[0] + (smin+step[1])//60
# 		smin = (smin + step[1] + (ssec+step[2])//60) % 60
# 		ssec = (ssec + step[2]) % 60

# 		if shour > end[0]:
# 			return
# 		if shour == end[0] and smin > end[1]:
# 			return
# 		if shour == end[0] and smin == end[1] and ssec > end[2]:
# 			return

# ts = trange((6,0,0),(23,0,0),(0,0,90))
# for i in range(10):
# 	print(str(i) +": "+next(ts))


# Q4.
import random

def random_ones_and_zeros():
    p = 0.5
    while True:
        x = random.random()
        message = yield 1 if x < p else 0
        if message != None:
            p = message
        
x = random_ones_and_zeros()
next(x)  # we are not interested in the return value
for p in [0.2, 0.8]:
    x.send(p)
    print("\nprobabiliy: " + str(p))    
    for i in range(15):
        print(next(x), end=" ")
