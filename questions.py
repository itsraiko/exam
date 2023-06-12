##first question graphic:
##
import matplotlib.pyplot as plt

kayma_hizi = [0.0, 12, 24, 36, 48]
kayma_gerilmesi = [0.0, 1.0, 1.9, 3.1, 4.0]

plt.plot(kayma_hizi, kayma_gerilmesi, marker='o')
plt.xlabel('Kayma Hızı (RPS)')
plt.ylabel('Kayma Gerilmesi (Pa)')
plt.title('Kayma Gerilmesi - Kayma Hızı Grafiği')
plt.grid(True)
plt.show()
##
##first question math problem:
##
import math

kayma_hizi = [0.0, 12, 24, 36, 48]
kayma_gerilmesi = [0.0, 1.0, 1.9, 3.1, 4.0]
yoğunluk = 1200  # kg/m^3
g = 9.81  # m/s^2

kayma_orani = [kh * 2 * math.pi for kh in kayma_hizi]  # R/s to rad/s

kalınlık = [kg / (yoğunluk * g) for kg in kayma_gerilmesi]

ortalama_dinamik_visko = sum(kayma_orani) / len(kayma_orani)
ortalama_kinematik_visko = sum(kayma_orani) / sum(kalınlık)

print("Ortalama Dinamik Viskozite:", ortalama_dinamik_visko, "Pa.s")
print("Ortalama Kinematik Viskozite:", ortalama_kinematik_visko, "m^2/s")
##
