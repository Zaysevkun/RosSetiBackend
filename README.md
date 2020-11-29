[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Zaysevkun/RosSetiBackend">
    <img src="https://github.com/Zaysevkun/RosSetiBackend/blob/master/rossetilogo.jpg?raw=true" alt="Logo" width="400" height="120">
  </a>

  <h3 align="center">Росcети сервис рационализационной деятельности</h3>
</p>
  <p>
    Это глобальный веб сервис по акселерации рационализационной деятельности в ПАО Россети
    <br />
    <a href="https://github.com/Zaysevkun/RosSetiBackend">
    <strong>Документация »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Zaysevkun/RosSetiBackend">Демо</a>
    ·
    <a href="https://github.com/Zaysevkun/RosSetiBackend/issues">Сообщить о баге</a>
    ·
    <a href="https://github.com/Zaysevkun/RosSetiBackend/issues">Предложить фичу</a>
  </p>
  



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Содержание</h2></summary>
  <ol>
    <li>
      <a href="#О-проекте">О проекте</a>
      <ul>
        <li><a href="#Стек-технологий">Стек технологий</a></li>
      </ul>
    </li>
    <li>
      <a href="#">Первый запуск проекта</a>
      <ul>
        <li><a href="#Требования">Требования</a></li>
        <li><a href="#Установка">Установка</a></li>
      </ul>
    </li>
    <li><a href="#Роадмап">Роадмап</a></li>
    <li><a href="#contributing">Контрибьютинг в проект</a></li>
    <li><a href="#Лицензия">Лицензиия</a></li>
    <li><a href="#Контакты">Контакты</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## О проекте

![Product Name Screen Shot][product-screenshot]

Наша команда представляет вам программное решение для кейса "Россети".
Это адаптивное приложение с формой для создания рационализаторских предложений, базой шаблонов, личным кабинетом, где можно отслеживать статус предложения и и обсуждать его с другими пользователями программы. Весь цикл рационализаторского предложения можно отследить в нашей программе, которая формирует актуальные реестры.
Наша система является уникальной, так как она удовлетворяет профильные потребности "ПАО Россети"



### Стек технологий

* [Vuejs](https://vuejs.org/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/) [DRF](https://www.django-rest-framework.org/)



<!-- GETTING STARTED -->
## Первый запуск проекта

Руководство по запуску проекта локально.

### Требования


* PostgreSQL
  ```sh
  createdb your_db_name
  ```

### Установка

1. Склонировать репозиторий
   ```sh
   git clone https://github.com/Zaysevkun
   /RosSetiBackend
   .git
   ```
2. Создать venv
   ```sh
   python -m venv myvenv
   source myvenv/bin/activate
   ```
3. Установить зависимости
   ```
   pip install -r requirements.txt
   ```
4. Создать .env файл в корне проекта
   ```
   SECRET_KEY=qwerty123
   DATABASE_URL=postgres://your_db_user_name:user_password@127.0.0.1:5432/your_db_name
   ALLOWED_HOSTS=*
   DEBUG=0
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=user@example.com
   EMAIL_HOST_PASSWORD=your_password
   DEFAULT_FROM_EMAIL=user@wxample.com
   ```   
5. Применить миграции
   ```
   python manage.py migrate
   ```
6. Запустить проект
   ```
   gunicorn config.wsgi
   ```




<!-- ROADMAP -->
## Роадмап

Смотрите [open issues](https://github.com/Zaysevkun/RosSetiBackend/issues) для списка заявленного функционала (и замеченных багов).



<!-- CONTRIBUTING -->
## Контрибьютинг

1. Форкните проект
2. Создайте ветку feature (`git checkout -b feature/AmazingFeature`)
3. Закоммитьте изменения (`git commit -m 'Add some AmazingFeature'`)
4. Запуште ветку (`git push origin feature/AmazingFeature`)
5. Откройте пул реквест



<!-- LICENSE -->
## Лицензия

Распостраняется по лицензии MIT. Смотри `LICENSE` для дополнительной информации.



<!-- CONTACT -->
## Контакты

Россети - [@rossetiofficial](https://twitter.com/rossetiofficial) - rossetiinfo@gmail.com

Проект: [https://github.com/Zaysevkun/RosSetiBackend
](https://github.com/Zaysevkun/RosSetiBackend
)

Проект на Heroku(Backend API):[https://rosseti.herokuapp.com/](https://rosseti.herokuapp.com/)










[contributors-shield]: https://img.shields.io/github/contributors/Zaysevkun/RosSetiBackend.svg?style=for-the-badge
[contributors-url]: https://github.com/Zaysevkun/RosSetiBackend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Zaysevkun/RosSetiBackend.svg?style=for-the-badge
[forks-url]: https://github.com/Zaysevkun/RosSetiBackend/network/members
[stars-shield]: https://img.shields.io/github/stars/Zaysevkun/RosSetiBackend.svg?style=for-the-badge
[stars-url]: https://github.com/Zaysevkun/RosSetiBackend/stargazers
[issues-shield]: https://img.shields.io/github/issues/Zaysevkun/RosSetiBackend.svg?style=for-the-badge
[issues-url]: https://github.com/Zaysevkun/RosSetiBackend/issues
[license-shield]: https://img.shields.io/github/license/Zaysevkun/RosSetiBackend.svg?style=for-the-badge
[license-url]: https://github.com/Zaysevkun/RosSetiBackend/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/Zaysevkun
[product-screenshot]: https://github.com/Zaysevkun/RosSetiBackend/blob/master/project-screenshot.jpg?raw=true



