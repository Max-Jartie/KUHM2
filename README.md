# Конфигурационное управление  

# Домашнее задание №2  

Вариант №19  

Разработать инструмент командной строки для визуализации графа зависимостей, включая транзитивные зависимости. Зависимости определяются по имени Python-пакета (анализируемого через pip). Для представления графа используется формат Mermaid.  

Конфигурационный файл имеет формат CSV и содержит:  
- Путь к программе для визуализации графов.  
- Имя анализируемого пакета.  
- Путь к файлу-результату (код Mermaid-графа).  
- URL-адрес репозитория.  

Все функции визуализатора должны быть покрыты тестами.  

---

## Описание всех функций и настроек  

1. Анализ зависимостей  
   - Рекурсивное построение графа зависимостей Python-пакета.  
   - Включает как прямые, так и транзитивные зависимости.  

2. Генерация графа Mermaid  
   - Формирование графа зависимостей в формате Mermaid.  
   - Связи между пакетами отображаются в виде узлов и стрелок.  

3. Конфигурация из CSV-файла  
   - Имя пакета для анализа.  
   - Путь для сохранения результата.  

4. Вывод на экран и сохранение  
   - Mermaid-код выводится в консоль и сохраняется в файл.  

---

## Описание поддерживаемых команд  

* Запуск программы:  
   Анализирует зависимости указанного пакета и сохраняет Mermaid-граф.  

* Запуск юнит-тестов:  
   Проверяет функции по анализу зависимостей и генерации Mermaid-графа.  

---

## Команда для запуска проекта  

Запускаем программу с конфигурационным файлом:  

python visualizer.py config.csv


---

## Команда для запуска юнит-тестов  

Для запуска тестов используйте команду:  

python -m unittest discover tests


---

## Описание работы программы  

1. Считывание конфигурации из файла config.csv.  
2. Анализ зависимостей для указанного Python-пакета с использованием встроенного модуля importlib.metadata.  
3. Генерация графа зависимостей в формате Mermaid.  
4. Сохранение результата в указанный файл, например output/requests_graph.mmd.  

---

## Пример Mermaid-графа  

Выполнение программы для пакета requests создаст следующий Mermaid-граф:  

graph TD
    "requests" --> "urllib3"
    "requests" --> "certifi"
    "requests" --> "chardet"
    "requests" --> "idna"


---

## Пример конфигурационного файла  

Файл config.csv содержит настройки программы:  

/path/to/visualizer,requests,output/requests_graph.mmd,https://github.com/username/repository


---

## Результат работы юнит-тестов  

![tests](https://github.com/username/repository/blob/main/screenshots/tests_result.png)  

---

## Результат работы программы  

### Граф зависимостей в формате Mermaid  
![mermaid](https://github.com/username/repository/blob/main/screenshots/graph_result.png)  

### Вывод содержимого файла  
graph TD
    "requests" --> "urllib3"
    "requests" --> "certifi"
    "requests" --> "chardet"
    "requests" --> "idna"


---

## Вывод в консоль  

После запуска программы выводится сообщение:  
Анализируем зависимости для пакета 'requests'...
Граф зависимостей сохранен в 'output/requests_graph.mmd' в формате Mermaid.


--- 

## Примечания  
- Для визуализации Mermaid-кода используйте [Mermaid Live Editor](https://mermaid.live).  
- Программа работает с пакетами, установленными в текущей среде Python.  

---

Теперь проект полностью готов к запуску и тестированию! 🚀
