"""
Using Python and NetworkManager on GTK
to control network
"""
import gi

gi.require_version("NM","1.0")
from gi.repository import GLib, NM
client = NM.Client.new(None)
# print("version",client.get_version())

devices = client.get_devices()
print("devices")
for dev in devices:
    print(" -name:",dev.get_iface())
    print("  type:",dev.get_type_description())
    print("  state:",dev.get_state().value_nick)
