medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}km, {}hm, {}dam, {}dm, {}cm, {}mm'.format(medida, km, hm, dam, dm, cm, mm))
