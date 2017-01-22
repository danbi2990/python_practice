import pickle

# cities = ["Paris", "Dijon", "Lyon", "Strasbourg"]
# fh = open("data.pkl", "bw")
# pickle.dump(cities, fh)
# fh.close()

# f = open("data.pkl", "rb")
# villes = pickle.load(f)
# print(villes)

fh = open("data.pkl", "wb")
programming_languages = ["Python", "Perl", "C++", "Java", "Lisp"]
python_dialects = ["Jython", "IronPython", "CPython"]
pickle_object = (programming_languages, python_dialects)
pickle.dump(pickle_object, fh)
fh.close()

f = open("data.pkl", "rb")
(languages, dialects) = pickle.load(f)
print(languages, dialects)
