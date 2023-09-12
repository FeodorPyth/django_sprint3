# Blogicum

### Как запустить проект:

Создать пустую директорию или через командную строку перейти в папку, где будет храниться проект:

Для передвижения внутри файловой системы через командную строку используйте команду:
```
cd имя_папки
```

Для создания новой директории используйте команду:
```
mkdir имя_папки
```

Клонировать репозиторий и перейти в него в командной строке: 
```
git clone git@github.com:FeodorPyth/django_sprint3.git
```

```
cd django_spring3
```

Создать и активировать виртуальное окружение:

Windows
```python
python -m venv venv
source venv/Scripts/activate
```

Linux/macOS
```python
python3 -m venv venv
source venv/bin/activate
```

Обновить пакетный менеджер PIP:

Windows
```python
python -m pip install --upgrade pip
```

Linux/macOS
```python
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```python
pip install -r requirements.txt
```

Выполнить миграции:

Windows
```python
python manage.py makemigrations
python manage.py migrate
```

Linux/macOS
```python
python3 manage.py makemigrations
python3 manage.py migrate
```

Запустить проект:

Windows
```python
python manage.py runserver
```

Linux/macOS
```python
python3 manage.py runserver
```