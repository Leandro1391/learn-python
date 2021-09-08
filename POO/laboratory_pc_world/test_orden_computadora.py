from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado
from Computadora import Computadora
from Orden import Orden

unRaton = Raton('Lenovo', 'usb')
unMonitor = Monitor('Lenovo', '21')
unTeclado = Teclado('Lenovo', 'usb' )

dueRaton = Raton('Pirulin', 'SCASI')
dueMonitor = Monitor('HP', '21')
dueTeclado = Teclado('HP', 'COM')

ratonTres = Raton('Exo', 'SCASI')
monitorTres = Monitor('Exo', '18')
tecladoTres = Teclado('Genius', 'COM')


unaComputadora = Computadora('Enigma', unMonitor, unTeclado, unRaton)
segundaComputadora = Computadora('Pentium', dueMonitor, dueTeclado, dueRaton)
terceraComputadora = Computadora('Pentium', monitorTres, tecladoTres, ratonTres)

computadorasUno = [unaComputadora, segundaComputadora]

unaOrden = Orden(computadorasUno)

unaOrden.agregarComputadora(terceraComputadora)

print(f'{unaOrden}')
