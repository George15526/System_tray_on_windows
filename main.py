import pystray
from PIL import Image
import webbrowser

def click_to_schoolweb(icon, item):
    print('click: ', item)
    webbrowser.open('https://w3.nknu.edu.tw/zh/')

def on_quit(icon, item):
    print('Quitting...')
    icon.stop()
    

menu = (
    pystray.MenuItem('Quit', on_quit),
    pystray.MenuItem('NKNU Website', click_to_schoolweb),
)

image = Image.open('static/g.png')
icon = pystray.Icon('name', image, '411031111軟體三林鈺祐', menu)
icon.run()