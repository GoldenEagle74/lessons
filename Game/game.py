
import game_map
import titles
import text


inventory = []
def inventory():
    return inventory

titles.bloody_valley()

text.database('start')

game_map.char(1)
for i in range(2): game_map.char(2)

while True:
    location = input('[1]\n[2]\n[3]\n[4]\n[5]\n[6]\n[0] - выход\nВведите локацию: ')
    if location == '0': break
    for i in range(2):
        try: game_map.char(int(location))
        except: pass
