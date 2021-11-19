# PuCharmWork
 
Время выполнения нового filter.py:
![](Skrins/scren1.jpg)
Время выполнения старого old_filter.py:
![](Skrins/scren2.jpg)

Разница во времени вызвана тем, что в новом варианте большая часть времени затричивается
на передачу данных пользователем.

Время выполения filter_with_filename.py:
![](Skrins/scren3.JPG)

Уменьшение времени работы файла вызвана тем, что пользователь не вводит данные.Также увеличению 
скорости работы способствует использование библиотеки numpy вместо циклов.

Изображение до преобразования:
![](img3.jpg)
Результат преобразования filter_with_filename.py:
![](res_firstnew.jpg)
Результат преобразования old_filter.py:
![](res_secondold.jpg)

Doc tests:

get_img:

![](Skrins/scren4.jpg)

get_pixel_art:

![](Skrins/scren5.jpg)