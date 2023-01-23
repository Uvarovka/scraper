# scraper
Тут находится инструкция по установке нужного софта для работы парсеров и запуску самого парсера
## На вашей системе должен быть установлен python 3
# Установка модулей python
1) нажмите на клавиши» «Win» + «R». В окне «Выполнить» введите команду: ``` cmd ```

![image](https://user-images.githubusercontent.com/43270753/213953086-3c5a9301-370a-4863-b54c-fe13d18530a1.png)

2) в командной строке вводим ``` cd "путь распакованной папки" ```

![image](https://user-images.githubusercontent.com/43270753/213953198-4c1d0f33-9ed1-44bf-9427-fc9355adb513.png)

2) в командной строке вводим ``` pip install -r req.txt ```

![image](https://user-images.githubusercontent.com/43270753/213954236-96431a34-9c48-42ab-9928-798ce1b72cb9.png)

# Установка Webdriver
1) установить google chrome

2) написать в адресной строке google chrome chrome://version/

![image](https://user-images.githubusercontent.com/43270753/213951790-6238475e-6202-47ab-bb42-c8db9219703c.png)
 
5) перейти на [этот сайт](sites.google.com/chromium.org/driver/downloads) и скачать webdriver нужной версии для вашей ОС
 
![image](https://user-images.githubusercontent.com/43270753/213951854-26b85a0d-5864-40f4-aa05-d00bfb09c7e9.png)

6) нужно добавить webdriver в path для его работы, chromedriver.exe должен лежать в папке на диске c:/ в папке webdriver

![image](https://user-images.githubusercontent.com/43270753/213952427-b3518be0-630b-4cf5-bb0a-2b2fd1794f4c.png)

7) нажмите на клавиши» «Win» + «R». В окне «Выполнить» введите команду: ``` «systempropertiesadvanced» ``` (без кавычек), а затем нажмите на кнопку «ОК».

![image](https://user-images.githubusercontent.com/43270753/213952578-649920c8-bed9-440d-a9b2-a4c50d76539b.png)

8) В окне «Свойства системы», во вкладке «Дополнительно» нажмите на кнопку «Переменные среды…»

![image](https://user-images.githubusercontent.com/43270753/213952582-fceb3ff0-3410-42c2-baa1-a293cd8bba18.png)

9) в окне «Переменные среды» отображаются пользовательские переменные среды и системные переменные среды. Необходимо добавить путь к  C:\chromedriver\ в обе директории, чтобы всё работало наверняка.

![image](https://user-images.githubusercontent.com/43270753/213952609-795ed98e-7918-4f98-912e-c8d2d7591fb4.png)

10) вариант 1) добавить в конец списка после точки с запятой адрес к C:\chromedriver\  как показано на скриншоте ниже.

![image](https://user-images.githubusercontent.com/43270753/213952667-089fc38e-0152-4690-9b03-9d4b7297b033.png)

11) Вариант 2) нажмите кнопку Создать и укажите пусть к C:\chromedriver\ как показано на скриншоте ниже.

![image](https://user-images.githubusercontent.com/43270753/213952699-7517cccd-b16f-4b4e-b741-88b5557b692f.png)

12) чтобы проверить, добавленный путь, пропишите path в командной строке, затем проверьте наличие в конце списка адреса C:\chromedriver\ - путь к месту хранения chromedriver.exe

![image](https://user-images.githubusercontent.com/43270753/213952740-726e8ff0-020f-464b-9929-dce0d71b7181.png)

## 13)  !!!ПЕРЕЗАГРУЖАЕМ КОМПЬЮТЕР!!!

# Запуск парсера
1) нажмите на клавиши» «Win» + «R». В окне «Выполнить» введите команду: ``` cmd ```

![image](https://user-images.githubusercontent.com/43270753/213953086-3c5a9301-370a-4863-b54c-fe13d18530a1.png)

2) в командной строке вводим ``` cd "путь распакованной папки" ```

![image](https://user-images.githubusercontent.com/43270753/213953198-4c1d0f33-9ed1-44bf-9427-fc9355adb513.png)

3) в командной строке вводим ``` python main.py ```. Либо используем свой любимый вариант

![image](https://user-images.githubusercontent.com/43270753/213953932-a8b64bb6-82c5-4953-b166-a21197ddc0d1.png)

4) Вводим данные человека по которому проводим парсинг

![image](https://user-images.githubusercontent.com/43270753/213954812-eb3c6b79-ef40-417d-aebd-3c23585b400e.png)

5) наслаждаемся кривым принтом результатов парсинга

![image](https://user-images.githubusercontent.com/43270753/213954918-29373b02-5197-4ada-8e08-8e8608f5fbd0.png)

