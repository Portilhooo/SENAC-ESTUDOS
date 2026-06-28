mb= float(input("Digite o tamanho do arquivo em MB"))
vel= float(input("Digite a sua velocidade da sua internet em Mbps"))
tempo_segundos = (mb*8) / vel
tempo_min = tempo_segundos/60

print("O tempo aproximado de download é de:",tempo_min, "m")
