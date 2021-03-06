[![Python application](https://github.com/ds-vasilev/python-final-attestation/actions/workflows/python-app-refactoring.yml/badge.svg)](https://github.com/ds-vasilev/python-final-attestation/actions/workflows/python-app-refactoring.yml)

This is Python QA Engineer courses attestations work.
The project used Python + Pytest autotests. 
The goal of the project is to test registration, logging and booking of https://cypress-tourism-app.herokuapp.com
In the project was used Page object pattern. 


Test app: 
```
https://cypress-tourism-app.herokuapp.com
```

How to start:
```python3 -m venv env
source env/bin/activate
```

Requirements in:
```
pip install -r requirements.txt
```

Tests start:
```
Pytest
```

Code-check implemented through:
```
https://pre-commit.com/
```

Test cases in:
```
./Test-cases.xlsx
```


Logging implemented through:
```
Logging
```

Repports in:
```
Allure
$ allure serve ./python-final-attestation/report
```


План работы:
```
 • Необходимо написать ui тесты на https://cypress-tourism-app.herokuapp.com 

 • Необходимо написать тесты на  3 раздела (авторизация, регистрация и бронирование отеля). Для каждого раздела необходимо добавить позитивные и негативные тесты (количество на выбор студента). Для раздела бронирования достаточно позитивного теста. 

 • Необходимо составить к тестам тестовую документацию. В тест кейсах должны быть предварительные шаги (если это необходимо), шаги, ожидаемый результат. Как и где ее хранить остается на выбор студента.
```

Проект должен быть выложен на github и удовлетворять следующим критериям:
``` 
 ✓  Необходимо настроить CI (GitHub Actions). В проекте должен присутствовать файл настроек, который описывают логику взаимодействия с CI.

 ✓ Необходимо настроить линтер (программа, которая проверяет код на соответствие стандартам в соответствии с определенным набором правил), который должен запускаться локально/на стороне travis-ci. 

 ✓  К каждому тесту должны присутствовать тест кейсы 
            
 ✓ README.md заполнен и содержит актуальную информацию

 ✓ В файле README.md стоят бейджики GitHub Actions

 ✓ Доступна инструкция по установке зависимостей

 ✓ Описано как запустить тесты

 ✓ Есть информация о цели тестирования и краткое описание проекта

 ✓ Для тестирования используется фреймворк pytest 

 ✓ Результатом тестирования является сгенерированный отчет (например, Allure)
```
