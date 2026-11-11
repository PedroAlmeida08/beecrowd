dia_inicio = int(input().split()[1])
h_inicio, m_inicio, s_inicio = map(int, input().split(" : "))

dia_final = int(input().split()[1])
h_fim, m_fim, s_fim = map(int, input().split(" : "))

inicio_em_seg = (dia_inicio * 86400) + (h_inicio * 3600) + \
    (m_inicio * 60) + s_inicio
fim_em_seg = (dia_final * 86400) + (h_fim * 3600) + (m_fim * 60) + s_fim

duracao_total = fim_em_seg - inicio_em_seg

dias = duracao_total // 86400
resto = duracao_total % 86400

horas = resto // 3600
resto = resto % 3600

minutos = resto // 60
segundos = resto % 60

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
