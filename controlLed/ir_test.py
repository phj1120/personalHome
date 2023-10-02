from time import sleep
import piir

remote = piir.Remote('light.json', 17)

while True:
    remote.send('turn')
    remote.send('add')
    remote.send('minus')
    remote.send('night')
    remote.send('10')
    remote.send('30')

    remote.send('turn')
    print('Done')
    sleep(1)