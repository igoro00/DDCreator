import utils

def write(timeArray, timeSecArray, photosArray, count):
    name = input("Enter name of the file you want create?(without '.xml')\n")  + ".xml"
    if(utils.askYN("Do you want to save your config to %s?(y/n) "%(name))):
        return
    f = open(name, "w+")

    f.write("<backgroud>\n")
    f.write("   <starttime>\n")
    f.write("       <year>2019</year>\n")
    f.write("       <month>01</month>\n")
    f.write("       <day>01</day>\n")
    f.write("       <hour>00</hour>\n")
    f.write("       <minute>00</minute>\n")
    f.write("       <second>00</second>\n")
    f.write("   </starttime>\n")
    
    for i in range(count):
        f.write("   <!-- %s -->\n"%(timeArray[i]))
        f.write("   <static>\n")
        f.write("       <duration>%d.0</duration>\n"%(timeSecArray[i]))
        f.write("       <file>%s</file>\n"%(photosArray[i]))
        f.write("   </static>\n")
        f.write('   <transition type="overlay">\n')
        f.write("       <duration>5.0</duration>\n")
        f.write("       <from>%s</from>\n"%(photosArray[i]))
        if i < (count -1):
            #if not last
            f.write("       <to>%s</to>\n"%(photosArray[i+1]))
            f.write("   </transition>\n")

    f.write("       <to>%s</to>\n"%(photosArray[0]))
    f.write("   </transition>\n")
    f.write("</backgroud>")
    f.close()
    