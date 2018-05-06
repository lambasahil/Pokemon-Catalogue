# FullStack-Project--5
You will see how to develop a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication.And also go through when to properly use the various HTTP methods available and how these methods relate to CRUD (create, read, update and delete) operations

## Pokemon Catalogue

## How to Run:

### Prerequisites

- [Python ](https://www.python.org/)  
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)

The project uses Python3 to run the server, so make sure it is installed.

Below are the modules needed to run the project:

* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Flask Framework](http://flask.pocoo.org/docs/0.12/)
* [OAuth2Client](https://github.com/google/oauth2client)
* [Requests](http://docs.python-requests.org/en/master/)
* [httplib2](https://github.com/httplib2/httplib2)

### Launch

Launch the Vagrant VM from inside the *vagrant* folder with:

`vagrant up`

`vagrant ssh`

Then move inside the Pokemon Catalogue folder:

`cd /vagrant/Pokemon\ Catalogue`

Then lift the application:

`python flask_project.py`

After the last command you are able to browse the application at this URL:

`http://localhost:5000/`

# Restful Api

Here `1` is the ID of the particular pokemon
`http://localhost:5000/1/JSON`
Returns the details of a given <id>
`
{
Pokemon: - [
- {
description: "Because of its resemblance to Poke Balls,it is thought that it was created when one was exposed toan energy pulse. It was first seen in the plant wheremodern Poke Balls were invented. Voltorb is generallyfound in powerplants and other areas with electric fields.",
id: 2,
img: "https://img00.deviantart.net/c453/i/2016/161/3/c/voltorb_png_by_unksoldier55-da5sg2c.png",
name: "Voltorb"
}
]
}
`
Returns all Pokemon from the database
`http://localhost:5000/pokemons_Catalogue/JSON`

`
{
Pokemon: - [
- {
description: "Pikachu, the Mouse Pokemon, and the evolvedform of Pichu. Pikachu's tail is sometimes struck bylightning as it raises it to check its surroundings",
id: 1,
img: "http://www.cartoonbucket.com/wp-content/uploads/2015/05/Laughing-Pikachu-Image.png",
name: "Pikachu"
},
- {
description: "Because of its resemblance to Poke Balls,it is thought that it was created when one was exposed toan energy pulse. It was first seen in the plant wheremodern Poke Balls were invented. Voltorb is generallyfound in powerplants and other areas with electric fields.",
id: 2,
img: "https://img00.deviantart.net/c453/i/2016/161/3/c/voltorb_png_by_unksoldier55-da5sg2c.png",
name: "Voltorb"
},
]`
