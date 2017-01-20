"""
In this comprehensive exercise, we have to bring together the information of two files. In the first file, we have a list of nearly 15000 lines of post codes with the corresponding city names plus additional information. Here are some arbitrary lines of this file:

68309,"Mannheim",8222,"Mannheim",8,"Baden-Wrttemberg"
68519,"Viernheim",6431,"Bergstraße",6,"Hessen"
68526,"Ladenburg",8226,"Rhein-Neckar-Kreis",8,"Baden-Württemberg"
68535,"Edingen-Neckarhausen",8226,"Rhein-Neckar-Kreis",8,"Baden-Württemberg"

The other file contains a list of the 19 largest German cities. Each line consists of the rank, the name of the city, the population, and the state (Bundesland):

1.  Berlin          3.382.169 Berlin
2.  Hamburg         1.715.392 Hamburg
3.  München         1.210.223 Bayern
4.  Köln              962.884 Nordrhein-Westfalen
5.  Frankfurt am Main 646.550 Hessen
6.  Essen             595.243 Nordrhein-Westfalen
7.  Dortmund          588.994 Nordrhein-Westfalen
8.  Stuttgart         583.874 Baden-Württemberg
9.  Düsseldorf        569.364 Nordrhein-Westfalen
10. Bremen            539.403 Bremen
11. Hannover          515.001 Niedersachsen
12. Duisburg          514.915 Nordrhein-Westfalen
13. Leipzig           493.208 Sachsen
14. Nürnberg          488.400 Bayern
15. Dresden           477.807 Sachsen
16. Bochum            391.147 Nordrhein-Westfalen
17. Wuppertal         366.434 Nordrhein-Westfalen
18. Bielefeld         321.758 Nordrhein-Westfalen
19. Mannheim          306.729 Baden-Württemberg

Our task is to create a list with the top 19 cities, with the city names accompanied by the postal code. If you want to test the following program, you have to save the list above in a file called largest_cities_germany.txt and you have to download and save the list of German post codes 

city name + postal code
"""

import re
import codecs

# exp1 = r"^([\d]+\.)\s{1,2}([\w\s]+)\s\d"
# cities = []
# with open("largest_cities_germany.txt","r") as f_obj:
# 	for line in f_obj:
# 		m_obj = re.search(exp1, line)
# 		cities.append([m_obj.group(1), m_obj.group(2).strip()])
# 		# print(type(m_obj.group(1)))	type: string
# 		# print(m_obj.group(1)+" "+m_obj.group(2))

# # print(cities)

# exp2 = r""
# with open("post_codes_germany.txt", "r") as file:
# 	for line in file:
# 		mtch = re.search(exp2, line)
# 		for city in cities:
# 			if mtch.group(2) == city[1]:
# 				city.append(mtch.group(1))


# fh_post_codes = codecs.open("post_codes_germany.txt","r","utf-8")
PLZ = {}
with codecs.open("post_codes_germany.txt","r","utf-8") as fh_post_codes:
	for line in fh_post_codes:
	    (post_code, city, rest) = line.split(",",2)
	    PLZ[city.strip("\"")] = post_code
	    
#print(PLZ.get('München'))

# fh_largest_cities = open("largest_cities_germany.txt")
with codecs.open("largest_cities_germany.txt","r","utf-8") as cities:
	for line in cities:
		print(line)
	    # re_obj = re.search(r"^[0-9]{1,2}\.\s+([\wÄÖÜäöüß\s]+\w)\s+[0-9]",line)
	    # city = re_obj.group(1)
	    # print(city, PLZ.get(city))
