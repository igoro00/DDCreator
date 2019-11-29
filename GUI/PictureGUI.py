import gi
import sys
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
sys.path.append('..')
from CMD.picture import pic


class PictureGUI():
    def __init__(self, path, strTime, transition):
        self.picture = pic(path, strTime, transition)

    def addPic(self):
        row = Gtk.ListBoxRow()
        marginBox = Gtk.Box(spacing=10)
        marginBox.set_margin_top(10)
        marginBox.set_margin_bottom(10)
        marginBox.set_margin_start(10)
        marginBox.set_margin_end(20)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        marginBox.add(box)
        row.add(marginBox)

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.picture.path, height=250, width=140, preserve_aspect_ratio=True)
        image = Gtk.Image()
        image.set_from_pixbuf(pixbuf)
        box.pack_start(image, True, True, 0)

        dataBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        box.pack_start(dataBox, fill=False, expand=False, padding=0)

        moreDataBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        dataBox.pack_end(moreDataBox, fill=False, expand=False, padding=0)

        pathLabel = Gtk.Label(self.picture.path)
        dataBox.pack_end(pathLabel, fill=False, expand=False, padding=0)

        strTimeLabel = Gtk.Label("Time: %s" % self.picture.strTime)
        moreDataBox.pack_start(strTimeLabel, fill=True, expand=True, padding=0)

        transitionLabel = Gtk.Label("Transition: %s" % self.picture.transition)
        moreDataBox.pack_start(transitionLabel, fill=True, expand=True, padding=0)

        return row
