from gi.repository import GTK

window = GTK.Window()
window.connect("delete-event", GTK.main_quit)
window.show_all()
GTK.main()
