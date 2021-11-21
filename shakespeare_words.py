from urllib import request
import re
import enchant
import os

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd",
              'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers',
              'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what',
              'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were',
              'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the',
              'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
              'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from',
              'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
              'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
              'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can',
              'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain',
              'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn',
              "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn',
              "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't",
              'wouldn', "wouldn't", "thou", "thy", "shall", "thee", "would", "let"]

d = enchant.Dict("en_US")

url = "https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt"
file = request.urlopen(url)
text = ""
with open('raw_data.txt', 'w') as raw_file:
    for line in file:
        decoded_line = line.decode("utf-8")
        raw_file.write(decoded_line)

text_to_remove_1 = "<<THIS ELECTRONIC VERSION OF THE COMPLETE WORKS OF WILLIAM" \
                   "SHAKESPEARE IS COPYRIGHT 1990-1993 BY WORLD LIBRARY, INC., AND IS" \
                   "PROVIDED BY PROJECT GUTENBERG ETEXT OF ILLINOIS BENEDICTINE COLLEGE" \
                   "WITH PERMISSION.  ELECTRONIC AND MACHINE READABLE COPIES MAY BE" \
                   "DISTRIBUTED SO LONG AS SUCH COPIES (1) ARE FOR YOUR OR OTHERS" \
                   "PERSONAL USE ONLY, AND (2) ARE NOT DISTRIBUTED OR USED" \
                   "COMMERCIALLY.  PROHIBITED COMMERCIAL DISTRIBUTION INCLUDES BY ANY" \
                   "SERVICE THAT CHARGES FOR DOWNLOAD TIME OR FOR MEMBERSHIP.>>"

with open('raw_data.txt', 'r') as file:
    raw_data = file.read() \
        .replace('\n', '') \
        .replace(text_to_remove_1, '') \
        .replace('THE ENDEnd of this Etext of The Complete Works of William Shakespeare', '') \
        .replace('*This Etext has certain copyright implications you should read!*', '') \
        .replace('ACT', '').replace('SCENE', '')

processed_data = re.sub('[^\w]', ' ', raw_data)

with open('temp_data.txt', 'w') as file:
    file.write(processed_data[9700:].lower())

with open('temp_data.txt', 'r') as file:
    data = file.read()

temp_list = data.split()

#word_list = list(set(stop_words).symmetric_difference(set(temp_list)))

with open("shakespeare_data.txt", "w") as output_file:
    for word in temp_list:
        if word not in stop_words and d.check(word):
            output_file.write(word + '\n')

os.remove("raw_data.txt")
os.remove("temp_data.txt")
© 2021 GitHub, Inc.
