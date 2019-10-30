import os
diretorio = 'C:/Users/ecaet/Pictures/wallpapper 2/1/'
arquivos = os.listdir(diretorio)        
for x in range(len(arquivos)):
        print('Arquivo ',arquivos[x],' \nAlterado para: ','imagem-'+str(x)+'.png \n')
        os.rename(diretorio+arquivos[x], diretorio+('imagem-'+str(x)+'.png'))
print('\n--------------------- Arquivos Renomeados ---------------------')
print(exit())

