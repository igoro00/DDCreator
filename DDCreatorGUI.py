import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from GUI.PictureGUI import PictureGUI


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)

        self.set_border_width(10)
        self.set_default_size(700, 400)
        self.pArray=[]

        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "DDCreator"
        self.set_titlebar(header_bar)

        #open button on the right
        openButton =Gtk.Button(label="Open File(s)")
        openButton.connect("clicked", self.onOpenFile)
        header_bar.pack_start(openButton)

        #main box
        mainBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        self.add(mainBox)
        self.addPhoto(mainBox)

        #properties
        propSW = Gtk.ScrolledWindow()
        propSW.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        propertiesBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        timeBox=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)

        label = Gtk.Label("heloo bihaz")
        timeInput = Gtk.Entry()
        timeBox.pack_start(label, False, False, 10)
        timeBox.pack_start(timeInput, True, True, 10)
        propertiesBox.pack_start(timeBox, False, False, 30)
        propSW.add(propertiesBox)
        mainBox.pack_end(propSW, True, True, 0)




    def addPhoto(self, mainBox):
        sw = Gtk.ScrolledWindow()
        sw.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        listboxPhotos = Gtk.ListBox()
        listboxPhotos.connect("row-selected", self.loadProperties)
        listboxPhotos.set_selection_mode(Gtk.SelectionMode.BROWSE)

        p = PictureGUI("/home/igor/Obrazy/wallpapers/Atacama/3:00.jpeg", "03:00")
        self.pArray.append(p)
        p = PictureGUI("/home/igor/Obrazy/wallpapers/Atacama/6:00.jpeg", "06:00")
        self.pArray.append(p)

        for i in self.pArray:
            listboxPhotos.add(i.addPic())
        sw.add(listboxPhotos)
        mainBox.pack_start(sw, True, True, 0)

    def onOpenFile(self, widget):
        dialog = Gtk.FileChooserDialog("Open file(s)", self, Gtk.FileChooserAction.OPEN,
                                       ("Cancel", Gtk.ResponseType.CANCEL,
                                       "Open", Gtk.ResponseType.OK))
        response =dialog.run()
        if(response == Gtk.ResponseType.OK):
            print("File selected: "+dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("rabini są niezdecydowani")
        dialog.destroy()

    def loadProperties(self, listbox, row):
        currentPic =self.pArray[row.get_index()]
        print(currentPic.picture.strTime)



window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()