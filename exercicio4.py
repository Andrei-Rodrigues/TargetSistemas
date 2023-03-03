sp = float(67836.43)
rj = float(36678.66)
mg = float(29229.88)
es = float(27165.48)
outros = float(19849.53)

print('Estados - SP, RJ, MG, ES, Outros')
estado = str(input('Digite algum estado da lista para verificar o seu percentual de faturamento (Outros para verificar outros estados): ')).lower()

if estado == 'sp':
    perc = sp / 100
    print('O percetual de faturamento de São Paulo é {:.2f}%'.format(perc))
if estado == 'rj':
    perc = rj / 100
    print('O percetual de faturamento do Rio de Janeiro é {:.2f}%'.format(perc))
elif estado == 'mg':
        perc = mg / 100
        print('O percetual de faturamento de Minas Gerais é {:.2f}%'.format(perc))
elif estado == 'es':
    perc = es / 100
    print('O percetual de faturamento do Espirito Santo é {:.2f}%'.format(perc))

elif estado == 'outros':
    perc = outros / 100
    print('O percetual de faturamento de outros estados é {:.2f}%'.format(perc))
