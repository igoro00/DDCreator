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

        mainBox.pack_end(propSW, True, True, 0)

        propertiesBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        propSW.add(propertiesBox)

        propertiesLabel = Gtk.Label()
        propertiesLabel.set_markup("<big><big><big><b>Properties</b></big></big></big>")
        propertiesBox.pack_start(propertiesLabel, False, False, 0)

        propertiesBox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        propertiesBox.pack_start(propertiesBox2, False, False, 0)

        #time
        timeBox=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        timeLabel = Gtk.Label("Time:")
        self.timeInput = Gtk.Entry()
        self.timeInput.set_max_length(5)
        self.timeInput.set_alignment(0.5) #its ratio from 0 to 1 how to right its aligned. 0,5 is center
        timeBox.pack_start(timeLabel, False, False, 10)
        timeBox.pack_start(self.timeInput, True, True, 10)
        propertiesBox2.pack_start(timeBox, False, False, 5)


        #transition
        transitionBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        transitionLabel = Gtk.Label("Transition:")
        self.transitionInput = Gtk.Entry()
        self.transitionInput.set_max_length(5)
        self.transitionInput.set_alignment(0.5)  # its ratio from 0 to 1 how to right its aligned. 0,5 is center
        self.transitionInput.connect("changed", self.changedProp)
        transitionBox.pack_start(transitionLabel, False, False, 10)
        transitionBox.pack_start(self.transitionInput, True, True, 10)
        propertiesBox2.pack_start(transitionBox, False, False, 5)

        #Apply and reset buttons
        applyBox = Gtk.Box(spacing= 20)
        propertiesBox.pack_end(applyBox, False, False, 0)

        self.applyButton = Gtk.Button("Apply")
        self.applyButton.connect("clicked", self.apply)
        self.applyButton.set_sensitive(False)
        applyBox.pack_start(self.applyButton, False, False, 0)



    def addPhoto(self, mainBox):
        sw = Gtk.ScrolledWindow()
        sw.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        listboxPhotos = Gtk.ListBox()
        listboxPhotos.connect("row-selected", self.loadProperties)
        listboxPhotos.set_selection_mode(Gtk.SelectionMode.BROWSE)

        p = PictureGUI("/home/igor/Obrazy/wallpapers/Atacama/3:00.jpeg", "03:00", 5)
        self.pArray.append(p)
        p = PictureGUI("/home/igor/Obrazy/wallpapers/Atacama/6:00.jpeg", "06:00", 5)
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
        self.currentIndex = row.get_index()
        print(currentPic.picture.strTime)
        self.timeInput.set_text(currentPic.picture.strTime)
        self.transitionInput.set_text(str(currentPic.picture.transition))

    def changedProp(self, widget):
        #if its something to apply, make Apply clickable, otherwise make it not clickable
        if (self.pArray[self.currentIndex].picture.strTime != self.timeInput.get_text()) or (
            str(self.pArray[self.currentIndex].picture.transition) != self.transitionInput.get_text()
        ):
            self.applyButton.set_sensitive(True)
        else:
            self.applyButton.set_sensitive(False)

    def apply(self, widget):
        self.pArray[self.currentIndex].picture.strTime=self.timeInput.get_text()
        self.pArray[self.currentIndex].picture.transition = self.transitionInput.get_text()
        self.applyButton.set_sensitive(False)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()