#
text1 ="Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language. It was created by Guido van Rossum during 1985- 1990. Like Perl, Python source code is also available under the GNU General Public License (GPL). This tutorial gives enough understanding on Python programming language."
text2 ="Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."

#tokenization
text1 = text1.split()
text2 = text2.split()

#Remove StopWords - article-the,a,an , helping verb-is,am ,are was ,were..........
from nltk.corpus import stopwords
x = stopwords.words("english")

for stopword in x:
    if stopword in text1:
        text1.remove(stopword)

    if stopword in text2:
        text2.remove(stopword)

set1 = set(text1)
set2 = set(text2)
#similarity
#Jaccards Index: len(intersection)/len(union)
JI = len(set1.intersection(set2))/len(set1.union(set2))
print(JI*100,"%")
