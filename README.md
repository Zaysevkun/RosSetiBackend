<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
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
    <strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Zaysevkun/RosSetiBackend">View Demo</a>
    ·
    <a href="https://github.com/Zaysevkun/RosSetiBackend/issues">Report Bug</a>
    ·
    <a href="https://github.com/Zaysevkun/RosSetiBackend/issues">Request Feature</a>
  </p>
  



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

Наша команда представляет вам программное решение для кейса "Россети".
Это адаптивное приложение с формой для создания рационализаторских предложений, базой шаблонов, личным кабинетом, где можно отслеживать статус предложения и и обсуждать его с другими пользователями программы. Весь цикл рационализаторского предложения можно отследить в нашей программе, которая формирует актуальные реестры.
Наша система является уникальной, так как она удовлетворяет профильные потребности "ПАО Россети"



### Built With

* [Vuejs](https://vuejs.org/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/) [DRF](https://www.django-rest-framework.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites


* PostgreSQL
  ```sh
  createdb your_db_name
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Zaysevkun
   /RosSetiBackend
   .git
   ```
2. Create python virtual environment
   ```sh
   python -m venv myvenv
   source myvenv/bin/activate
   ```
3. Install Python requirements
   ```
   pip install -r requirements.txt
   ```
4. Create .env file in project root
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
5. Apply intial migrations 
   ```
   python manage.py migrate
   ```
6. Run project
   ```
   gunicorn config.wsgi
   ```




<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Zaysevkun/RosSetiBackend/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@rossetiofficial](https://twitter.com/rossetiofficial) - rossetiinfo@gmail.com

Project Link: [https://github.com/Zaysevkun/RosSetiBackend
](https://github.com/Zaysevkun/RosSetiBackend
)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()






[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/Zaysevkun/RosSetiBackend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/Zaysevkun/RosSetiBackend/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/Zaysevkun/RosSetiBackend/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/Zaysevkun/RosSetiBackend/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/Zaysevkun/RosSetiBackend/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/Zaysevkun
[product-screenshot]: https://github.com/Zaysevkun/RosSetiBackend/blob/master/project-screenshot.jpg?raw=true



