import gi

gi.require_version("NM","1.0")
from gi.repository import GLib, NM
client = NM.Client.new(None)
print("version",client.get_version())
