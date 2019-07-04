#Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
a_scores = 0
list_scores = scores.split(" ")
int_list_scores = [int(i) for i in list_scores]
for score in int_list_scores:
    if score>=90:
        a_scores+=1

#Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
lst_org = org.split(" ")
lst_initial = []
for word in lst_org:
    if word not in stopwords:
        initial = word[0].upper()
        lst_initial.append(initial)
print(lst_initial)
acro = "".join(lst_initial)

#Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro_list=[]
list_sent=sent.split(" ")
for word in list_sent:
    if word not in stopwords:
        acro_element = word[:2].upper()
        acro_list.append(acro_element)
print(acro_list)
acro = ". ".join(acro_list)
print(acro)

