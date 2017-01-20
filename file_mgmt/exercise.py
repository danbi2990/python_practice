# The file cities_and_times.txt contains city names and times. Each line
# contains the name of the city, followed by the name of the day ("Sun")
# and the time in the form hh:mm. Read in the file and create an
# alphabetically ordered list of the form

# Finally, the list should be dumped for later usage with the pickle
# module. We will use this list in our chapter on Numpy dtype.

import pickle

# lst = open("cities_and_times.txt", "r").readlines()
# sorted_lst = sorted(lst)


# pkl_file = open("cities_and_times.pkl", "wb")
# # pickle_object = [item for item in sorted_lst]
# tuples = tuple(item for item in sorted_lst)
# # print(sorted_lst)
# pickle.dump(sorted_lst, pkl_file)

# pkl_file.close()

# f = open("cities_and_times.pkl", "rb")
# loaded_list = pickle.load(f)
# print(loaded_list)


lines = open("cities_and_times.txt").readlines()
lines.sort()


cities = []
for line in lines:
	*city, day, time = line.split()
	hours, minutes = time.split(":")
	cities.append((" ".join(city), day, (int(hours), int(minutes))))

fh = open("cities_and_times.pkl", "wb")
pickle.dump(cities, fh)
fh.close()
