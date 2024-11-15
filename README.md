# Cheque Generator V3


Этот проект представляет собой генератор чеков и баркодов на Python. Он создает случайные баркоды и формирует XML-файлы для чеков, которые могут быть использованы в различных приложениях, связанных с торговлей и учетом.


## Описание


Проект включает в себя следующие функции:


- Генерация случайных баркодов.

- Создание XML-структуры для чеков, включая заголовок и содержимое.

- Генерация случайных дат для чеков.

- Сохранение сгенерированного XML в файл.


## Установка


Для работы с проектом не требуется установка дополнительных библиотек, так как используются только стандартные модули Python.


## Использование


1. Склонируйте репозиторий:


   ```bash

   git clone https://github.com/AlexCompDev/cheque_generator_v3.git

   cd cheque_generator_v3

  Запустите скрипт:
  
    python cheque_generator_v3.py

 После выполнения скрипта будет создан файл cheque.xml с сгенерированным чеком.

Пример выходных данных

Сгенерированный XML-файл будет выглядеть примерно так:

xml

<Cheque>

    <Header>

        <Date>01-12-2022T14:30:00</Date>

        <Kassa>5</Kassa>

        <Shift>2</Shift>

        <Number>3</Number>

        <Type>Продажа</Type>

    </Header>

    <Content>

        <Bottle>

            <Barcode>1234567890123</Barcode>

            <EAN>9876543210123</EAN>

            <Price>49.99</Price>

        </Bottle>

        <!-- Другие бутылки и позиции Nomark -->

    </Content>

</Cheque>

Вклад

Если вы хотите внести свой вклад в проект, пожалуйста, создайте форк репозитория, внесите изменения и создайте pull request.
