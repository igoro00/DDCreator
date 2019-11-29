import utils
from xml.etree.ElementTree import ElementTree, Element, SubElement, Comment

def write(picArray, name):

    totalSecondsSoFarOhGoshIWantToKillMyself =0
    
    background = Element('background')
    starttime = SubElement(background, 'starttime')

    year = SubElement(starttime, 'year')
    year.text = '2019'

    month = SubElement(starttime, 'month')
    month.text = '1'

    day = SubElement(starttime, 'day')
    day.text = '1'

    hour = SubElement(starttime, 'hour')
    hour.text = '0'

    minute = SubElement(starttime, 'minute')
    minute.text = '0'

    second = SubElement(starttime, 'second')
    second.text = '0'

    for i in range(len(picArray)):
        comment = Comment(picArray[i].picture.strTime)
        background.append(comment)

        static = SubElement(background, 'static')

        duration = SubElement(static, 'duration')
        dur = utils.strToSec(picArray[i].picture.strTime)
        dur -= totalSecondsSoFarOhGoshIWantToKillMyself
        duration.text = str(float(dur))
        totalSecondsSoFarOhGoshIWantToKillMyself += dur

        path = SubElement(static, 'file')
        path.text = picArray[i].picture.path

        transition = SubElement(background, 'transition', {'type':'overlay'})
        duration = SubElement(transition, 'duration')
        duration.text = '5.0'
        fromPath = SubElement(transition, 'from')
        fromPath.text = picArray[i].picture.path
        toPath = SubElement(transition, 'to')
        if (i < (len(picArray)-1)):
            #if its not last then do it normally
            toPath.text = picArray[i+1].path
        else:
            #but if its the last one, end it with the first pic
            toPath.text = picArray[0].path


    print(utils.prettify(background))
    tree = ElementTree(background)
    f = open(name, 'w+')
    f.write(utils.prettify(background))