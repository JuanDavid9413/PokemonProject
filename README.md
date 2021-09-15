# PokemonProject

* The app is create in virtual enviroment.
* Teh app needs install pipenv. "pip3 install pipenv". 
* Next, you need to change routes in appconfig.json.
* the api has three endpoints.
    * http://localhost:4000/Pokemon (GetAll Pokemons) type GET
    * http://localhost:4000/createSchema (Create schemma to DB). type POST
    * http://localhost:4000/createInformation (Extract data to csv an add in bd) type POST

* you need to search info in DB
    * Execute http://localhost:4000/Pokemon with next parameters
        * field = Name field to DB. For example:
            * nombre
            * typeOne
            * typeTwo
            * total
            * hp
            * attack
            * defense
            * spAttack
            * spDefense
            * speed
            * generation
            * legendary 
        * And value what is it value search.
        
        * Example URL: 
            http://localhost:4000/Pokemon?field=nombre&value=Bulbasaur
            http://localhost:4000/Pokemon?field=typeOne&value=Grass
            http://localhost:4000/Pokemon?field=legendary&value=True

* the folder package admin all packages of project.
    * PackagePokemon extract all information to csv document.
    * PackegeDB admin all process the DB.
* The test folder has test unit. Only function one of three. The process return random info. 
* The DB created in SQLITE. It's name pokemonInfo.db
* Add swagger for see endpoints created 
    * http://localhost:4000/swagger/#/default