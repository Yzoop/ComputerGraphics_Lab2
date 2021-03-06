# Чтение информации из графических файлов
Решение лабораторной работы №2 по компьютерной графике.
__________________
## Инструкция к приложению
### Установка
Скачать можно по следующей ссылке: [ColorInformer версии 1.0.0](https://github.com/Yzoop/ComputerGraphics_Lab2/releases/download/1.0.0/ColorInformer.zip).
В скачанном архиве находится нужное Вам приложение с именем *ColorInformer.exe*. Разорхивируйте этот исполняемый файл в любое удобное для Вас место.
### Запуск
Кликните 2 раза на файл *ColorInformer.exe* для запуска.
### Использование
После успешного запуска приложения, откроется окно ![app](https://i.ibb.co/6N0NZ2x/app1.png)<br>
Для выбора нужной папки, нажмите на кнопку **Выбрать папку**.
![choose a folder](https://i.ibb.co/5sH6BjW/app2.png) <br>
После выбора папки требуется подождать некоторое время в зависимости от количества изображений в папке.
В результате работы приложения выведется таблица с информацией:
![asd](https://i.ibb.co/1Xdp0z2/app3.png)
__________________
## Описание решения
Для обработки изображений был использован язык программирования `Python`, фреймворк `PyQt5` для оконного приложения, библиотеки `Pillow` и `os` для обработки изображений и работы с файлами соответственно.
[`Pillow`](https://pillow.readthedocs.io/en/stable/) документация описывает, как загружать изображение/я во временную память и получать информацию.
