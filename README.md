# HR Management 
## :information_source: Information 

The project was developed during the development course advancing enterprise applications with Django. In the project it has the departments, the companies, the employees and the documents that each employee produces. The use of Celery for sending e-mails was added to the project, and the use of several databases in the project such as: MYSQL and POSTGRES. For the user to access the system's functionalities, he must access the django administration panel and associate his user as an employee of a department and a company.


## ⚠️ Prerequisite

![](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

![](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)

![](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

![](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## Demo


![gestao_RH](https://user-images.githubusercontent.com/44611131/119913014-23cff280-bf33-11eb-8da0-27a681c2d2b2.png)




## ⚙️ Creating virtual machine

Create your virtual machine
```
python3 -m venv venv
```
Activate your virtual machine
```
source venv/bin/activate
```
After the virtual machine is activated, install the project dependencies
```
pip install -r requirements.txt```
```

## ⚙️ Installing MySQL

Enter the following commands in the terminal.

```
sudo apt update
sudo apt install mysql-server

```
### Configuring MySQL

For new installations, you will want to run the security script that is included. This changes some of the less secure default options for things like root logins and example users. Enter the command below.

```
sudo mysql_secure_installation
```
This will take you through a series of prompts where you can make some changes to the security options of your MySQL installation. The first prompt will ask you if you want to configure the Validate Password Plugin, which can be used to test the strength of your MySQL password. Regardless of your choice, the next prompt will be to set the password for the MySQL root user. Sign in and then confirm a secure password of your choice.

From there, you can press Y and then ENTER to accept the default answers for all subsequent questions. This will remove some anonymous users and the test database, disable remote login for root, and load all of these new rules so that MySQL immediately respects the changes you made.

### Testing MySQL

To see if MYSQL is running, type the following command.

```
systemctl status mysql.service
```

If MySQL is not running, you can start it with the following command.
```
sudo systemctl start mysql
```
Now try to connect your root user to MySQL.
```
mysql -u root -p
```
## ⚙️ Installing POSTGRESQL
To install POSTGRESQL, type the following commands in the terminal.

```
sudo apt update

sudo apt install postgresql postgresql-contrib

```

### Checking PostgreSQL
To log into PostgreeSQL as a postgre user, you can use psql
```
sudo su – postgres
```
To use PostgreSQL, type in the terminal.
```
Psql
```
If you want to leave the session, just use.
```
\q
```

### Creation of Roles and Users

To create a role, log in to the Postgres account, as you did before. Once you're in the Postgres console, you can create a new role (role) by typing.
```
createrole –interactive
```

The system will ask you to name the role and if it has a superuser permission. Similarly, you can also create a new user as the command.
createuser –interactive

Alternatively, from the normal command prompt, you can use the command as shown below.
```
sudo -u postgres createuser –interactive
```
Again, the system will ask for a username. The createuser command can be used with multiple options, which can be verified using createuse

## :rocket: Installation

![](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

```sh
git clone https://github.com/RamonBecker/AppHRManagement.git
```

![](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)


```sh
git clone https://github.com/RamonBecker/AppHRManagement.git
or install github https://desktop.github.com/ 

```

## :zap: Technologies	

- Python



## :memo: Developed features

- [x] CRUD Department
- [x] CRUD company
- [x] CRUD annual leave
- [x] CRUD  employee


## :technologist:	 Author

By Ramon Becker 👋🏽 Get in touch!



[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/RamonBecker)  [<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg' alt='linkedin' height='40'>](https://www.linkedin.com/in/https://www.linkedin.com/in/ramon-becker-da-silva-96b81b141//)
![Gmail Badge](https://img.shields.io/badge/-ramonbecker68@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:ramonbecker68@gmail.com)



