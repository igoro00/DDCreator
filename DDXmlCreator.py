import require_python_3
import loop
import utils

print("Enter name of the file you want create?")
name = input()
name = name + ".xml"
f = open(name, "w+")

#beginning(open of <backgroud> and whole <starttime>)
f.write("<backgroud>\n   <starttime>\n       <year>2014</year>\n       <month>01</month>\n       <day>11</day>\n        <minute>00</minute>\n       <second>00</second>\n   </starttime>")

while(1):
    print("How many pictures do you have?")
    count = input()
    if(count.isdigit()):
        count = int(count)
        break
    else:
        print("This value is not valid!")

for i in range(count):
    loop.ask(f, i, count)


f.close()