# Дипломная работа на тему разработка интернет магазина на Django

## Содержание

[Содержание](#содержание)

[Введение](#введение)

[1 Цель разработки интернет магазина](#1-цель-разработки-интернет-магазина)

[2 Технический раздел](#2-технический-раздел)
> [2.1 Обзор используемых инструментов](#21-обзор-используемых-инструментов)
>> [2.1.1 Pycharm](#211-pycharm)
>>
>> [2.1.2 Фреймворк Django](#212-фреймворк-django)
>>
>> [2.1.3 База данных PostgreSQL](#213-база-данных-postgresql)
>>
>> [2.1.4 JavaScript для AJAX](#214-javascript-для-ajax)
>>
>> [2.1.5 Django debug toolbar](#215-django-debug-toolbar)

[3 Проектный раздел](#3-проектный-раздел)

> [3.1 Архитектура системы](#31-архитектура-системы)
>
> [3.2 Проектирование с помощью диаграммы вариантов](#32-проектирование-с-помощью-диаграммы-вариантов)
>
> [3.3 Проектирование с помощью диаграммы вариантов](#33-проектирование-с-помощью-диаграммы-отношений)
>
> [3.4 Интерфейс](#34-интерфейс)

[4 Экспериментальный раздел](#4-экспериментальный-раздел)

> [4.1 Функции интернет магазина](#41-функции-интернет-магазина)
>
> [4.2 Создание интернет магазина](#42-создание-интернет-магазина)
>
>> [4.2.1 Страницы регистрации и авторизации](#421-страницы-регистрации-и-авторизации)
>>
>> [4.2.2 Поиск и фильтрация](#422-поиск-и-фильтрация)
>>
>> [4.2.3 Добавление в корзину и просмотр корзины](#423-добавление-в-корзину-и-просмотр-корзины)
>>
>> [4.2.4 Страница оформления заказа](#424-страница-оформления-заказа)
>
> [4.3 Настройка админ панели](#43-настройка-админ-панели)
>
>> [4.3.1 Страница заказов](#431-страница-заказов)
>>
>> [4.3.2 Страница товаров](#432-страница-товаров)
>>
>> [4.3.3 Страница списка пользователей](#433-страница-списка-пользователей)

[Заключение](#заключение)

[Список используемых материалов](#список-используемых-материалов)

## Введение

С увеличением распространения интернета все больше компаний переходят к онлайн-торговле. Этот тренд открывает предпринимателям новые возможности, позволяя им расширить географию своей деятельности и увеличить доходы за счет сокращения операционных расходов. Именно в этом контексте становится актуальной тема создания интернет-магазина для продажи мебели.

Цель данной дипломной работы заключается в разработке и реализации интернет-магазина для продажи мебели. Для достижения этой цели были сформулированы следующие задачи:

- Провести анализ предметной области, связанной с продажей мебели онлайн.
- Разработать концепцию интернет-магазина, учитывая особенности мебельной индустрии и потребности потенциальных клиентов.
- Реализовать созданную концепцию в виде функционального интернет-магазина с удобным пользовательским интерфейсом и надежной системой обработки заказов.

## 1 Цель разработки интернет магазина

Цель данного дипломного проекта заключается в создании интернет-магазина, который учитывает современный ритм жизни и потребности пользователей в экономии времени. Интернет-магазин позволит клиентам совершать покупки онлайн, не выходя из дома, что является более удобным и эффективным способом для многих людей.

Основные преимущества интернет-магазина включают:

- Отсутствие необходимости в физическом магазине, что экономит затраты на аренду или строительство помещения.
- Отсутствие необходимости в продавцах, что уменьшает операционные расходы на заработную плату.
- Непрерывная доступность магазина, что способствует увеличению прибыли за счет возможности продажи в любое время суток.
- В рамках создаваемого интернет-магазина пользователи смогут регистрироваться, осуществлять поиск и использовать фильтры для удобства выбора товаров, а также оформлять покупки. Администратор же получит доступ к управлению списком товаров с возможностью добавления, редактирования и удаления, а также к управлению списком пользователей и просмотру заказов пользователей.

## 2 Технический раздел

### 2.1 Обзор используемых инструментов

#### 2.1.1 Pycharm

PyCharm, разработанный компанией JetBrains, является мощной интегрированной средой разработки (IDE), предназначенной для увеличения производительности и комфорта программистов, работающих с Python. Имея широкий набор функций и инструментов, PyCharm стал предпочтительным выбором для разработчиков Python по всему миру.

Основные особенности данной IDE включают в себя:

Поддержка различных версий Python: обеспечивает поддержку широкого спектра версий Python, что позволяет разработчикам выбирать наиболее подходящую версию для своих проектов.

Автозаполнение кода: предлагает автозаполнение кода на основе контекста, что значительно ускоряет процесс написания кода и уменьшает вероятность ошибок.

Отладка: обеспечивает полноценную поддержку отладки Python-приложений, позволяя устанавливать точки останова, отслеживать значения переменных и анализировать выполнение кода.

Рефакторинг: инструменты рефакторинга помогают улучшить структуру и качество кода, автоматически переименовывая переменные и функции, извлекая методы, оптимизируя импорты и многое другое.

Интеграция с системами управления версиями: удобная интеграция с Git, SVN, Mercurial и другими системами управления версиями обеспечивает эффективное управление версиями кода.

Поддержка виртуальных сред: позволяет создавать и управлять виртуальными средами Python, обеспечивая изоляцию зависимостей и упрощая управление зависимостями проекта.

Интегрированный терминал: включает в себя встроенный терминал командной строки, что позволяет выполнять различные команды и скрипты прямо из среды разработки.

Поддержка плагинов: расширение функциональности с помощью различных плагинов, что позволяет настраивать среду разработки под конкретные потребности пользователя.

Удобная навигация по проекту: легкость ориентации в больших проектах и быстрый доступ к определениям классов, функций и переменных с помощью инструментов навигации.

PyCharm обеспечивает эффективный и комфортный процесс разработки Python-проектов, позволяя разработчикам сосредоточиться на решении задач, в то время как IDE заботится о рутинных операциях и обеспечивает удобство работы.

![окно создания проекта в Pycharm](/images/pycharm.png)

#### 2.1.2 Фреймворк Django

Django - это веб-фреймворк на языке программирования Python, который предоставляет разработчикам инструменты и шаблоны для создания мощных веб-приложений. Разработанный с учетом принципа "Don't repeat yourself" (DRY), этот фреймворк позволяет программистам писать меньше кода, что способствует увеличению производительности и уменьшению количества ошибок.

Основные преимущества Django:

Быстрая разработка: предоставляет готовые инструменты и функциональность, что позволяет создавать веб-приложения быстро и эффективно. За счет использования множества встроенных модулей, разработка приложений на Django занимает меньше времени, чем при использовании других фреймворков.

Мощная административная панель: поставляется с встроенной административной панелью, которая позволяет администраторам управлять данными и настройками приложений без необходимости написания дополнительного кода. Административная панель предоставляет доступ к базе данных, позволяет создавать, редактировать и удалять записи, а также управлять пользователями и группами.

Масштабируемость: разработан с учетом возможности масштабирования, что позволяет создавать веб-приложения, способные обрабатывать большие объемы данных и высокие нагрузки. Благодаря своей модульной структуре и гибкости, Django позволяет разрабатывать приложения любой сложности, от простых блогов до сложных корпоративных систем.

Безопасность: включает множество встроенных механизмов безопасности, которые защищают приложения от распространенных атак, таких как инъекции SQL, межсайтовый скриптинг (XSS) и межсайтовый запрос подделки (CSRF). Django также предоставляет средства для аутентификации, авторизации и защиты конфиденциальных данных, что делает его одним из самых безопасных фреймворков для разработки веб-приложений.

Активное сообщество: имеет огромное и активное сообщество разработчиков, которые постоянно работают над улучшением фреймворка и созданием новых расширений и плагинов. Благодаря этому, разработчики могут быстро найти решение для своих задач, получить помощь и поддержку от опытных коллег, а также делиться своим опытом и знаниями.

Гибкость и расширяемость: предоставляет разработчикам гибкие инструменты для создания разнообразных приложений, включая веб-сайты, веб-сервисы, API и многое другое. Благодаря модульной структуре и возможности интеграции с другими технологиями и фреймворками, Django позволяет создавать приложения, которые отвечают всем требованиям бизнеса и пользователей.

Поддержка многоязычности и мультиплатформенности: поддерживает создание многоязычных и мультиплатформенных приложений, что делает его идеальным выбором для разработки международных проектов и приложений, работающих на различных устройствах и платформах.

#### 2.1.3 База данных PostgreSQL

PostgreSQL - это мощная система управления базами данных (СУБД) с открытым исходным кодом, которая предоставляет разработчикам надежное и эффективное хранилище данных для их приложений. Её отличительной особенностью является объектно-реляционная архитектура, которая позволяет хранить данные в виде объектов и связей между ними, что обеспечивает более гибкую и интуитивно понятную модель данных.

Преимущества PostgreSQL:

Открытый исходный код: PostgreSQL распространяется под лицензией PostgreSQL, которая позволяет свободно использовать, модифицировать и распространять код, что делает его идеальным выбором для коммерческих и некоммерческих проектов.

Мощные функциональные возможности предоставляют широкий набор функций, включая поддержку транзакций, многопоточности, репликации данных, триггеров, хранимых процедур и многое другое.

Поддержка различных типов данных, включая числа, строки, даты, времена, массивы, JSON, XML, геометрические данные и многое другое.

Производительность и масштабируемость обеспечена благодаря использованию оптимизированных алгоритмов и структур данных, а также поддержке параллельной обработки запросов и распределенных транзакций.

Высокий уровень безопасности и надежности достигается благодаря использованию различных механизмов защиты данных, включая аутентификацию, авторизацию, шифрование и аудит доступа.

Активное сообщество и поддержка: огромное и активное сообщество разработчиков и пользователей, которые постоянно работают над улучшением и развитием системы, созданием новых расширений и модулей, а также предоставлением помощи и поддержки другим участникам сообщества.

Расширяемость и гибкость: гибкие инструменты и API для создания собственных расширений и модулей, что позволяет адаптировать систему под свои уникальные потребности и требования. Благодаря этой расширяемости появляется возможность использования для решения широкого круга задач и проблем.

![Логотип PostgreSQL](/images/logo-postgreSQL.jpg)

#### 2.1.4 JavaScript для AJAX

JavaScript используется для реализации асинхронных запросов на сервер с использованием технологии AJAX (Asynchronous JavaScript and XML). AJAX позволяет обновлять части веб-страницы без полной её перезагрузки, что повышает интерактивность и отзывчивость веб-приложения. JavaScript также может использоваться для создания дополнительных интерактивных элементов интерфейса веб-приложения.

![AJAX-запрос с использованием JavaScript](/images/ajax-cart.png)

#### 2.1.5 Django Debug Toolbar

Django Debug Toolbar - это инструмент отладки для веб-приложений на основе Django, который обеспечивает удобный интерфейс для мониторинга производительности и анализа запросов к базе данных. Этот инструмент помогает разработчикам легко отслеживать и оптимизировать производительность своего приложения.

Преимущества Django Debug Toolbar включают:

Подробную информацию о времени выполнения запросов к базе данных, включая количество запросов, время выполнения каждого запроса и список вызванных SQL-запросов.
Анализ запросов к базе данных, позволяющий выявить возможные проблемы производительности и оптимизировать работу с базой данных.
Интеграцию с панелью управления Django, что обеспечивает удобный доступ к инструментам отладки прямо из административной части приложения.
Поддержку различных расширений и настроек для настройки поведения и внешнего вида инструмента в соответствии с потребностями разработчика.
Использование Django Debug Toolbar позволяет значительно ускорить процесс отладки и оптимизации веб-приложений на основе Django, что делает его незаменимым инструментом для разработчиков.
![Отображение панели django debug toolbar](/images/django-debug-toolbar.png)

### Подведение итогов

Проект, разработанный с использованием передовых технологий в области веб-разработки, представляет собой высокофункциональное веб-приложение, способное эффективно удовлетворять потребности пользователей. Выбран интегрированную среду разработки PyCharm для создания приложения, воспользовавшись её множеством функций для увеличения производительности разработчика.

В основе веб-приложения лежит фреймворк Django, который обеспечивает мощный инструментарий для быстрой и эффективной разработки веб-приложений. Был использован функционал Django для работы с базами данных, управления URL, аутентификации пользователей и многого другого, создавая веб-приложение с высоким уровнем функциональности и безопасности.

В качестве базы данных выбрана PostgreSQL, надежная и мощная система управления базами данных, обеспечивающая высокую производительность и надежность. PostgreSQL обеспечивает безопасность и целостность данных приложений.

JavaScript играет немаловажную роль в нашем проекте, с помощью обработки javascript производились ajax запросы на сервер. Это позволяет нам обновлять содержимое страницы без перезагрузки и создавать динамичный пользовательский интерфейс, повышая удобство использования приложения.

Django Debug Toolbar очень удобный инструмент для отладки во время разработки приложений с использованием фреймворка Django. Этот инструмент предоставляет подробную информацию о запросах к базе данных и другие полезные данные, помогая эффективно оптимизировать производительность приложения.

Все эти технологии и инструменты работают совместно, обеспечивая высокий уровень функциональности и производительности веб-приложения. Было создано мощное и современное приложение, готовое к использованию и масштабированию, демонстрируя преимущества использования передовых технологий в веб-разработке.

## 3 Проектный раздел

### 3.1 Архитектура системы

Архитектура данной системы построена с учетом принципов модульности, масштабируемости и безопасности. Применена трехзвенная архитектура, включающая клиентский, серверный и уровень данных.

![Архитектура интернет магазина 1](/images/architecture-market.png)

Клиентский уровень:

- На данном уровне осуществляется взаимодействие пользователей с системой через веб-браузер. Для создания динамичного и удобного пользовательского интерфейса используются HTML, CSS и JavaScript. JavaScript применяется для обработки событий и отправки асинхронных запросов на сервер с использованием технологии AJAX.

Серверный уровень:

- На серверном уровне используется фреймворк Django, написанный на языке Python. Django обеспечивает удобные средства для разработки веб-приложений, включая маршрутизацию URL, обработку запросов, аутентификацию пользователей, работу с базой данных и другие функциональности. Также применяется Django Debug Toolbar для удобной отладки и анализа производительности приложения.

Уровень данных:

- В качестве базы данных выбран PostgreSQL, обеспечивающий высокую производительность, надежность и безопасность хранения данных. Модели данных в Django ORM отображаются на таблицы PostgreSQL, обеспечивая согласованность и целостность данных.
Вся система построена с использованием современных технологий и лучших практик веб-разработки, что обеспечивает высокую производительность, надежность и безопасность нашего веб-приложения.

![Архитектура интернет магазина 2](/images/architecture-market2.png)

### 3.2 Проектирование с помощью диаграммы вариантов

Диаграмма вариантов использования является важным инструментом для моделирования функциональности системы, позволяя описать основные действия, которые могут выполняться в системе. В контексте интернет-магазина, такие диаграммы помогают понять, как пользователи будут взаимодействовать с системой и какие функции им будут доступны.

Варианты использования для зарегистрированного пользователя:

![Use-case диаграмма пользователь](/images/usecase_user1.png)

- Просмотр каталога товаров:
Пользователь может просматривать доступный ассортимент товаров в магазине.
- Поиск товаров:
Пользователь может осуществлять поиск товаров по различным критериям для быстрого нахождения нужного продукта.
- Использование фильтрации:
Пользователь может применять фильтры для уточнения результатов поиска в соответствии с его предпочтениями.
- Добавление товаров в корзину:
После выбора нужных товаров, пользователь может добавить их в корзину для последующего оформления покупки.
- Оформление покупки:
Пользователь имеет возможность оформить покупку, указав необходимую информацию для доставки и оплаты товаров.

Варианты использования для администратора:

![Use-case диаграмма администратор](/images/usecase_admin1.png)

- Просмотр списка товаров:
Администратор может просматривать полный список товаров в магазине для управления ассортиментом.
- Удаление товара:
Администратор может удалять товары из каталога в случае необходимости.
- Добавление товара:
Администратор имеет возможность добавлять новые товары в магазин для расширения ассортимента.
- Просмотр списка покупок:
Администратор может просматривать список совершенных покупок для отслеживания активности покупателей.
- Просмотр списка пользователей:
Администратор может просматривать список зарегистрированных пользователей для управления учетными записями.
- Редактирование пользователей:
Администратор имеет возможность редактировать данные пользователей, например, изменять их контактные данные или пароли.
- Удаление пользователей:
В случае необходимости, администратор может удалять учетные записи пользователей из системы.

Эти варианты использования помогают описать основные функциональные возможности интернет-магазина и понять, как различные типы пользователей будут взаимодействовать с системой. Данная диаграмма является основой для дальнейшего проектирования и разработки функциональности магазина.

### 3.3 Проектирование с помощью диаграммы отношений

Для создания диаграммы отношений объектов (ERD) для нашего интернет-магазина необходимо определить основные сущности и их атрибуты, а также связи между этими сущностями. В контексте интернет-магазина мы можем выделить следующие основные сущности:

Пользователь:

    ID пользователя
    Имя
    Фамилия
    Адрес электронной почты
    Пароль
    Роль (например, обычный пользователь или администратор)
    Номер телефона
    Аватар

Категория:

    ID категории
    Название категории
    URL категории

Товар:

    ID товара
    Наименование
    Описание
    Цена
    Скидка в %
    Количество
    Изображение
    Категория (ссылка на категорию товара)

Корзина:

    ID корзины
    ID пользователя (ссылка на пользователя)
    Список товаров (ссылка на товар)
    Количество каждого товара

Заказ:

    ID заказа
    ID пользователя (ссылка на пользователя)
    Дата и время заказа
    Список товаров (ссылка на товар)
    Общая сумма заказа
    Требуется доставка
    Адрес доставки
    Оплата при получении
    Оплачено
    Статус заказа

Теперь, когда мы определили основные сущности и их атрибуты, мы можем определить связи между ними:

Сущность Пользователь может иметь одну или несколько Корзин (один ко многим).
Сущность Пользователь может иметь один или несколько Заказов (один ко многим).
Сущность Корзина связана с сущностью Товар по отношению многие ко многим (так как в корзине может быть несколько товаров, и каждый товар может быть в нескольких корзинах).
Сущность Заказ также связана с сущностью Товар по отношению многие ко многим (один товар может быть в нескольких заказах, и каждый заказ может содержать несколько товаров).
Сущность Товар связана с сущностью Категория по отношению один ко многим (одна категория может содержать много товаров, но каждый товар принадлежит только одной категории).
С использованием этой информации мы можем создать ERD, иллюстрирующую структуру базы данных для нашего интернет-магазина.

![Диаграмма отношений](/images/design_db1.png)

### 3.4 Интерфейс

При проектировании интерфейса интернет-магазина важно создать простой, интуитивно понятный и приятный глазу дизайн. Интерфейс должен быть минималистичным, без лишних элементов, чтобы пользователи могли быстро находить нужную информацию. Важно также разделить контент на логические блоки и обеспечить хорошую организацию информации. Дизайн должен быть адаптивным, чтобы хорошо отображаться на разных устройствах. Необходимо также уделить внимание эстетике и брендированию, чтобы создать цельный облик магазина. Наконец, тестирование среди реальных пользователей и оптимизация интерфейса помогут обеспечить его удобство и эффективность.
![Интерфейс](/images/interface_market_example.png)

## 4 Экспериментальный раздел

### 4.1 Функции интернет магазина

В начале работы над дипломным проектом были определены основные функции, которыми должен обладать интернет-магазин. Для пользователей были установлены следующие функциональности:

Регистрация и авторизация, чтобы пользователи могли создавать учетные записи и входить в систему для совершения покупок.
Возможность поиска и фильтрации товаров, чтобы пользователи могли быстро находить интересующие их товары с помощью поиска и применения фильтров.
Добавление товаров в корзину, чтобы пользователи могли собирать необходимые товары перед оформлением покупки.
Оформление покупки, чтобы пользователи могли завершить процесс покупки и указать необходимую информацию для доставки.

Для работы администратора были определены следующие функциональности:

Добавление товаров в магазин, чтобы администратор мог обновлять ассортимент магазина и добавлять новые товары.
Удаление товаров из магазина, чтобы администратор мог управлять ассортиментом и удалять товары по необходимости.
Просмотр списка пользователей, чтобы администратор мог контролировать активность пользователей и управлять учетными записями.
Редактирование пользователей, чтобы администратор мог изменять данные учетных записей пользователей при необходимости.
Просмотр списка покупок, чтобы администратор мог отслеживать заказы и управлять процессом доставки.

### 4.2 Создание интернет магазина

#### 4.2.1 Страницы регистрации и авторизации

Страница регистрации очень важна, так как для совершения покупок пользователь должен быть зарегистрирован. Регистрация подразумевает прохождение валидации, где каждое поле должно быть заполнено и соответствовать определенным стандартам. В случае ошибки валидации появляется сообщение об ошибке, и пользователю необходимо исправить данные для успешной регистрации. После заполнения всех полей и нажатия кнопки «Зарегистрироваться», данные отправляются на сервер с помощью POST запроса и сохраняются в базе данных пользователя.

![Регистрация](/images/registration.png)

Для авторизации пользователю требуется ввести только логин и пароль. В случае совпадения введенных данных с данными в базе данных, пользователь получает сообщение об успешном входе и переходит на главную страницу.

![Авторизация](/images/authorization.png)

#### 4.2.2 Поиск и фильтрация

Поиск и фильтрация предоставляет пользователю удобный способ найти нужные товары в интернет-магазине. Пользователь может ввести ключевые слова для поиска и использовать фильтры для уточнения результатов.

Функционал поиска и фильтрации включает:

Поле для ввода ключевых слов поиска.
Фильтры по различным критериям, таким как категория товара, цена, и т. д.
Кнопка для запуска поиска.
Отображение результатов поиска с учетом введенных ключевых слов и выбранных фильтров.
![Использование фильтров](/images/filters.png)
Возможность сортировки результатов по различным параметрам, таким как цена или популярность.
Страница поиска и фильтрации позволяет пользователям эффективно находить нужные товары среди широкого ассортимента, представленного в интернет-магазине.
Для того, чтобы произвести
фильтрацию пользователю необходимо только кликнуть на необходимую
ему категорию (рисунок 4.3).
В поле поиска, пользователь может найти товар по ключевым словам и
не обязательно писать все слово целиком, поиск работает по совпадению
нескольких символов.
![Использование поиска](/images/search.png)

#### 4.2.3 добавление в корзину и просмотр корзины

После выбора необходимого товара пользователем и нажатия на кнопку "Добавить в корзину", товар добавляется в корзину.

После успешного добавления товара в корзину, пользователь может просмотреть содержимое корзины. На странице корзины отображается список выбранных товаров, их количество, цена за единицу товара, общая стоимость товара и возможность изменения количества товара или удаления товара из корзины.

Таким образом, функционал корзины позволяет пользователям легко добавлять и управлять товарами, которые они хотят приобрести в интернет-магазине.

![Корзина](/images/cart.png)

#### 4.2.4 Страница оформления заказа

После добавления товаров в корзину пользователь переходит к оформлению заказа, нажав на кнопку "Оформить заказ". На странице оформления заказа пользователю предоставляется форма для заполнения адреса доставки и данных карты.

На форме оформления заказа пользователь должен ввести следующие данные:

Имя, фамилия, адрес доставки, номер телефона, способ доставки, адрес доставки, способ оплаты.
После заполнения всех необходимых полей пользователь может нажать на кнопку "Оформить заказ" для завершения процесса оформления заказа.

![Оформление заказа](/images/order.png)

## 4.3 Настройка админ панели

Для управления интернет-магазином администратору предоставлены следующие страницы в административной панели Django:

### 4.3.1 Страница заказов

На этой странице администратор может просматривать список заказов, просматривать подробную информацию о каждом заказе и управлять статусом заказа, например, помечать заказы как выполненные или отмененные

![Админ панель заказы](/images/orders_admin.png)

### 4.3.2 Страница товаров

Здесь администратор может добавлять новые товары в магазин, вводя информацию о названии товара, его описании, цене, наличии и других характеристиках, а также просматривать список всех товаров в магазине и управлять ими, включая удаление товаров, которые больше не продаются

![Админ панель товары](/images/products.png)

### 4.3.3 Страница списка пользователей
Здесь администратор может просматривать список зарегистрированных пользователей магазина, просматривать информацию о каждом пользователе и выполнять действия, такие как редактирование данных пользователя или удаление его аккаунта

![Админ панель пользователи](/images/users.png)

Через административную панель Django администратор может эффективно управлять всеми аспектами функционирования интернет-магазина, обеспечивая плавную работу и удобство для пользователей.

## Заключение

В ходе выполнения данной дипломной работы было установлено, что разработка интернет-магазина включает две основные части: административную панель и публичную часть. Для реализации проекта использовались база данных PostgreSQL, фреймворк Django на языке Python для бэкэнда, а также JavaScript, HTML5 и CSS для фронтенда

Основные функциональные возможности, воплощенные в интернет-магазине, включают:

Регистрацию и аутентификацию пользователей.
Поиск и фильтрацию товаров для удобства навигации.
Добавление товаров в корзину для последующего оформления заказа.

Администратору интернет-магазина доступны следующие функции:

Просмотр списка товаров, их добавление и удаление.
Просмотр списка покупок для контроля и анализа.
Управление пользователями, включая просмотр, редактирование и удаление профилей.
В целом, созданный интернет-магазин представляет собой полноценное веб-приложение, готовое к использованию.

## Список используемых материалов

Django Documentation: Официальная документация Django, предоставляющая подробное описание функций, API и примеров использования.

Python.org Documentation: Документация по Python на официальном сайте Python.org, включающая руководства, стандартную библиотеку и примеры кода.

"Django 4 в примерах" Антонио Меле : Книга, рассматривающая основы разработки веб-приложений с использованием Django, с подробными объяснениями и практическими примерами.

"PostgreSQL Documentation": Документация PostgreSQL, содержащая описание функций, SQL-команд и советы по оптимизации запросов.

Stack Overflow и другие онлайн-ресурсы: Поиск решений и советов на популярных веб-ресурсах для программистов, таких как Stack Overflow, для решения конкретных задач и проблем в процессе разработки.
