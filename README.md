[![Contributors][contributors-shield]][contributors-url]


<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="assets/logo.png" alt="Logo" width="80" height="90">
  </a>

  <h3 align="center">(2000-2020) Grammys DB</h3>

  <p align="center">
    Base de Datos no relacional de los premios Grammys (2000-2020)
    <br />
    <a href="https://github.com/Isiguenza/GrammysDB"><strong>Proyecto</strong></a>
    <br />
    <br />
    <a href="#">Azure DB</a>
  </p>
</p>

## Sobre el Proyecto

![Diagrama ER](https://github.com/Isiguenza/GrammysDB/blob/main/assets/screenshot.png)

En este proyecto se abordará la creación y uso de bases de datos con lenguaje de python para poder administrar la manera en que una variedad de canciones se relacionan con sus autores, intérpretes, álbumes, género disquera y posibles premios Grammys (2000-2020).

Porque sobre los premios Grammy:
* Nos inspiramos por los recientes premiso Grammy.
* No existe alguna base de datos que relaciona los datos de Spotify con los Premios Grammy
* Creimos que era la base de datos más completa :smile:

### Desarrollo

Estos fueron los las librerias, lenguajes y base de datos que utilizamos.
* [Python](https://www.python.org/)
* [Spotipy](https://spotipy.readthedocs.io/en/2.16.1/)
* [Azure](https://azure.microsoft.com/)

### Origen de los datos

Para poder obtener los datos que conforman nuestra base de datos creamos un [código en python](https://github.com/Isiguenza/GrammysDB/blob/main/spotify_data.py) que recopila los datos de una playlist de spotify (título, artista, álbum, año del lanzamiento del álbum, autor y disquera)  esto con el fin de  poder crear una base de datos limpia y sin datos  innecesarios.

### Historia de los datos

Los premios Grammy (originalmente, Gramophone Award) son una distinción otorgada por la Academia Nacional de Artes y Ciencias de la Grabación de Estados Unidos para dar reconocimiento a un logro especialmente destacado en la industria musical. La ceremonia de entrega anual cuenta con las actuaciones de artistas y con la presentación de aquellos premios que despiertan un mayor interés popular. 

La primera ceremonia de los premios Grammy se celebró el 4 de mayo de 1959, para honrar y respetar los logros musicales de los artistas intérpretes o ejecutantes del año 1958. Actualmente los premios Grammy se celebran cada año  y se premian alrededor de 87 categorías. 

Dentro de nuestra playlist contamos con 65 álbumes de 54 artistas diferentes que fueron ganadores o nominados a algún premio Grammy entre el año 2000 y 2019. Los géneros que abarcamos son: alternativo, country, dance, pop, rock, electrónica, hip-hop/rap, rap, R&B, hip house, indie pop, neo soul y pop latino. 

Se tiene también el listado de 29 disqueras involucradas por cada álbum y para los casos especiales en el que hubiera un álbum producido por dos o más disqueras se consideró solo una; lo mismo aplica para más de un artista o autor de las canciones.

### Prerequisitos

Antes de poder correr nuestro codigo es necesario instalar las siguientes dependencias.
* Spotipy | Pyodbc | Pandas | Sqlalchemy
 ```py
 pip install spotipy
 pip install pyodbc
 pip install pandas
 pip install sqlalchemy
 ```


## Contributors y Contacto

* Iñaki Sigüenza - [@inakisiguenza](https://github.com/Isiguenza)
* Mariana Navarrete - [@hotelshrimpdraw]()
* Alia González - [@aliag]()

* Link del Proyecto: [https://github.com/Isiguenza/GrammysDB](https://github.com/Isiguenza/GrammysDB)


<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/Isiguenza/GrammysDB/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew

