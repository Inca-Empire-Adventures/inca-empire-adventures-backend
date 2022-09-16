* Notar que se requieren dependenciales adicionales requeridas 
```
python -m pip install Django
pip install --upgrade pip
pip install -r requerimientos.txt
```

#### Comando para iniciar una imagen de postgres en docker
```
docker run -it -p 3306:3306 -e TZ=America/Lima -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=inca-db --name inca-docker mysql:latest --character-set-server=latin1 --collation-server=latin1_general_ci 

--- Creacion de la base de datos
DROP SCHEMA IF EXISTS `inca-db`;

CREATE SCHEMA IF NOT EXISTS `inca-db` DEFAULT CHARACTER SET latin1 COLLATE latin1_general_ci;

USE `inca-db`;
CREATE USER IF NOT EXISTS 'inca-db' identified by 'secreto';
GRANT ALL PRIVILEGES ON `inca-db`.* TO 'inca-db'@'%';
FLUSH PRIVILEGES;
```

```
# Coneccion pg admin
    # user: root
    # password: password
    # puerto base de datos: 3306
    # puerto docker: 3306
```