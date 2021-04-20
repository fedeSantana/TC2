from scipy import signal
import matplotlib.pyplot as plt
from splane import bodePlot, pzmap

R = 1000 # 1KOhm
C = 0.000001 # 1uF

# Esta normalizado
# Docs https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.TransferFunction.html
num = [1, -1]
dem = [1, 1]

sys = signal.TransferFunction(num, dem)

# Docs https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.bode.html
w, mag, phase = signal.bode(sys)

plt.figure()
plt.semilogx(w, mag) # Bode magnitude plot
plt.ylim([-1,1])

plt.figure()
plt.semilogx(w, phase) # Bode phase plot

pzmap(sys) # Diagrama de polos y ceros. Función con efectos colaterales. 

plt.show()