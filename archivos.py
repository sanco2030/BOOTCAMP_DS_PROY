f = open('empresas.txt','w')
f.write('empresa 1,empresa1.com,2020202021')
f.close()

fa = open('empresas.txt','a')
fa.write('\n')
fa.write('empresa 2,empresa2.com,2020202022')
fa.close()

fr = open('empresas.txt','r')
data_empresas = fr.read()
print(data_empresas)
print(type(data_empresas))
fr.close()