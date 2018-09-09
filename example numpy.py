import matplotlib.pyplot as plt
X =[[2104],[1416],[1539],[852],[1940]]
Y =[[400],[232],[315],[178],[240]]

plt.title('prediksi harga rumah')
plt.xlabel('Luas')
plt.ylabel('Harga ($)')
plt.plot(X, Y, 'k.')
plt.grid(True)
plt.show()

