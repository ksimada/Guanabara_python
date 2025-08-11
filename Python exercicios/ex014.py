#Escreva um programa que converta uma temperatura digitada em °C e converta para °F
temp_c = float(input('Informa a temperatura em °C:'))
temp_f = ((temp_c*9)/5)+32
print("A temperatura de {}°C corresponde a {}°F".format(temp_c, temp_f))