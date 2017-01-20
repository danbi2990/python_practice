import re
import codecs

# f = codecs.open('C:\sample2.txt', "r", "utf-8")

f = codecs.open('C:\sample.txt', "r", encoding='utf-16', errors='ignore')
f2 = codecs.open('C:\sample3.txt', "r", encoding='utf-16', errors='ignore')
data = f.read()

exp = r"[\d]{1,2}\.\s"
exp_title = r"[\d]{1,2}\.\s..*\n"

correctSequence = f2.read()
correctTitleSequence = re.compile(exp).split(correctSequence)
content = re.compile(exp).split(data)
number = re.findall(exp, data)

# print(correctTitleSequence[1])
# print(content)

result = [None] * 85
for i in range(1, len(correctTitleSequence)):
    for j in range(0, len(content)):
        if correctTitleSequence[i] in content[j]:
            result[i] = content[j]
            # print(i, j)

print(result)

for i in range(1, len(result)):
    if result[i] is not None:
        text_file = open("Output.txt", "a")
        text_file.write(result[i])

text_file.close()

# print(result)

# result2 = " ".join(result)

# print(result2)

# print(content[1])
# print(number[0])

# titles = re.findall(exp_title, data)
# for i in range(len(titles)):
#     print(titles[i])

# print(re.findall(r"[\d]{2}\.\s.", data))

# codecs.open('C:\sample2.txt', "r",encoding='utf-8', errors='ignore')

# print(re.findall(r"[\d]{2}\.\s", data))

# l = re.split(r'[\d\d\.]', data)
"""
with codecs.open('C:\sample2.txt', "r", encoding='utf-16', errors='ignore') as input_data:
    for i in range(len(a)):
        s = ""
        for line in input_data:
            # print(line)
            s += line
            print(line[0:3])
            if re.match(r'^\d\d\.', line[0:3]):
                print(True)
                a[i] = s
                i += i + 1
"""