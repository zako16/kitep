# Kitep


## Установка

1. Для запуска проекта нужен virtualenv созданный с помощью python3
2. Установите все по списку requirements.txt
3. В проекте : project=>settings.py загружен settings_local.py где мы сами прописываем нужный нам DB, по умолчанию в django стоит такая строчка:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
а также не забудьте добавить еще `DEBUG = True` и сгенерируйте secret key для проекта.

## Начало работы

Для администрации сайта:
1. Создайте superuser `python manage.py createsuperuser`
2. Супер-пользователь создает модератора сайта в админ-панеле, дает ему статус персонала сайта `is_staff`

Или же мной будут предоставлены логин и пароль модератора сайта

## URLs

Начальная ссылка на rest службу `[будет позже :)]`<br />
Ниже все ссылки для запросов, вконце каждой ссылки надо добавить `?format=json`, `Content-type = application/json`. Для загрузки данных с изображениями надо отправлять данные в форме `form-data`:<br />
* Слайды `GET`: `/slider/`
* Партнеры `GET`: `/partners/`<br />
  Один партнер `GET`: `/partners/[id_of_partner]/`<br />
* Книги:<br />
  Список всех книг `GET`: `/books/`<br />
  Список всех категорий `GET`: `/books/categories/`<br />
  Список книг по одной категории `GET`: `/books/categories/[category_id]/`<br />
  Список годов выпуска `GET`: `/books/years/`<br />
  Список книг по году выпуска `GET`: `/books/years/[year]/`<br />
  Список статусов книг `GET`: `/books/statuses/`<br />
  Список типов обложек книг `GET`: `/books/covertypes/`<br />
  Список книг по пользователю `GET`: `/books/users/[username]/`<br />

  Создание книги `POST`: `/books/`<br />
  Редактирование книги `PUT`: `/books/[book_id]/`<br />
  Закрытие предложения `PUT`: `/books/[book_id]/` где надо указать `is_issue:false`<br />
  Удаление книги `DELETE`: `/books/[book_id]/`<br />
* Аккаунты, пользователи:<br />

## Модели для запросов

1. Слайдер:
```
id : int
slide : text
title : text
```
2. Партнеры:
```
id : int
title : text
slug : text
description : text
image : text
created_at : text
updated_at : text
```
3. Новости:
```
id : int
title : text
description : text
image : text
created_at : text
updated_at : text
```
4. Категории книг:
```
id : int
title : text
slug : text
```
5. Статусы книг (состояние книги):
```
id : int
status : text
```
6. Годы издания книг (примерно от 1990-2017):
```
id : int
year : int
```
7. Типы обложек (по умолчанию их пока два вообще: твердая и мягкая. Но бывают и кожанные и тряпичные):
```
id : int
type : text
```
8. Издатель книги:
```
id : int
title : text
```
9. Книга:
```
title : text
author : text
cover : int (id)
category : int (id)
description : text
user : int (id)
year : int (id)
coverType : int (id)
publisher : int (id)
status : int (id)
exchange : boolean
sale : boolean
price : int
created_at : text
updated_at : text
is_issue : boolean
```
9.1. Книга для POST и PUT методов:
```
title : text
author : text
cover : int (id)
category : int (id)
description : text
user : int (id)
year : int (id)
coverType : int (id)
publisher : int (id)
status : int (id)
exchange : boolean
sale : boolean
price : int
is_issue : boolean
```


###### Примечания:
 * редактировать и удалять книги через службу могут только те пользователи которые создали их
 * частичное редактирование предложений доступно
 * если предложение закрыли, то закрытые предложения доступны для просмотра тем кто создавал и штабу сайта
 * удаление и редактирование через службу открытых и закрытых предложений доступно лишь пользователям которые создавали их