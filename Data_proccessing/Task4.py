"""
Распакуйте данный список так чтобы вывести на экран осмысленную надпись используя форматирование строк.
Менять порядок элементов в списке нельзя,необходимо использовать распаковку списка.
"""
name = input("введите свое имя")
example = ["я","зовут","слон","Меня","журавль","и",name,"гений"]
print('{3} {1} {6} {5} {0} {7}'.format(*example))
