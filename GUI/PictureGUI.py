import gi
import sys
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
sys.path.append('..')
from CMD.picture import pic


class PictureGUI():
    def __init__(self, path, strTime, transition):
        self.path = path
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

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.path, height=250, width=140, preserve_aspect_ratio=True)
        image = Gtk.Image()
        image.set_from_pixbuf(pixbuf)
        pathLabel = Gtk.Label(self.path)

        box.pack_start(image, True, True, 0)
        box.pack_start(pathLabel, True, True, 0)
        return row
