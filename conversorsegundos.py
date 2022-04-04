segundos = float(input('Digite o valor em segundos que deseja converter para dias e horas:'))

dias = segundos // 86400
segundosrestantes = segundos % 86400
                 
horas = segundosrestantes // 3600
segundosresthoras = segundosrestantes % 3600
                 
minutos = segundosresthoras // 60
segundosrestantesfinal = segundosrestantes % 60


print('o valor', segundos,'equivale a', dias,'dias', horas, 'horas', minutos, 'minutos e', segundosrestantesfinal,
'segundos.')
       
