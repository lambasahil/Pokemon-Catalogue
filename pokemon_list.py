#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Pokemon_Category, Base, Pokemon

engine =  create_engine('postgresql://sahil:sahil@localhost/pokemon')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()

session = DBSession()

# Delete all the database

pokemon = session.query(Pokemon_Category).all()
items = session.query(Pokemon).all()

for i in pokemon:
    session.delete(i)

for i in items:
    session.delete(i)

session.commit()

print 'Previous database deleted'

# Menu for Electric pokemon

category1 = Pokemon_Category(category='Electric')

session.add(category1)

pokemon1 = Pokemon(name='Pikachu',
                   img="http://www.cartoonbucket.com/wp-content/uploads/"
                   "2015/05/Laughing-Pikachu-Image.png",
                   description="Pikachu, the Mouse Pokemon, and the evolved"
                   "form of Pichu. Pikachu's tail is sometimes struck by"
                   "lightning as it raises it to check its surroundings",
                   created_by='sahillamba61@gmail.com',
                   pokemon_category=category1)
session.add(pokemon1)

pokemon2 = Pokemon(name='Voltorb',
                   img="https://img00.deviantart.net/c453/i/2016/161/3/c/"
                   "voltorb_png_by_unksoldier55-da5sg2c.png",
                   description="Because of its resemblance to Poke Balls,"
                   "it is thought that it was created when one was exposed to"
                   "an energy pulse. It was first seen in the plant where"
                   "modern Poke Balls were invented. Voltorb is generally"
                   "found in power"
                   "plants and other areas with electric fields.",
                   created_by='sahillamba61@gmail.com',
                   pokemon_category=category1)
session.add(pokemon2)

# Menu for Water pokemon

category2 = Pokemon_Category(category='Water')

session.add(category2)

pokemon1 = Pokemon(name='Piplup',
                   img="https://cdn.bulbagarden.net/upload/thumb/b/b1/"
                   "393Piplup.png/250px-393Piplup.png",
                   description="It evolves into Prinplup starting at"
                   "level 16, which evolves into Empoleon starting at"
                   "level 36. Along with Turtwig and Chimchar, Piplup"
                   "is one of three starter Pokemon of Sinnoh available"
                   "at the beginning of Pokemon Diamond, Pearl, and Platinum.",
                   created_by='sahillamba61@gmail.com',
                   pokemon_category=category2)
session.add(pokemon1)

pokemon2 = Pokemon(name='Gyarados',
                   img="http://vignette2.wikia.nocookie.net/vsbattles/"
                   "images/b/b0/Gyarados_vector.png",
                   description="Huge and vicious, it is capable of destroying"
                   "entire cities in a rage. When Magikarp evolves"
                   "into Gyarados, its brain cells undergo a structural"
                   "transformation. It is said"
                   "that this transformation is to blame for this "
                   "Pokemon's wildly violent nature.",
                   created_by='sahillamba61@gmail.com',
                   pokemon_category=category2)
session.add(pokemon2)

# Menu for Fire pokemon

category3 = Pokemon_Category(category='Fire')

session.add(category3)

pokemon1 = Pokemon(name='Charmander',
                   img="https://vignette4.wikia.nocookie.net/pokemon/images/5/"
                   "55/004Charmander_OS_anime_3.png",
                   description="The flame wavers when Charmander is enjoying"
                   "itself. If the Pokemon becomes enraged, the flame burns"
                   "fiercely. The flame that burns at the tip of its tail is"
                   "an indication of its emotions. The flame wavers when"
                   "Charmander is happy, and blazes when it is enraged.",
                   created_by='sahillamba61@gmail.com',
                   pokemon_category=category3)
session.add(pokemon1)

pokemon2 = Pokemon(name='Arcanine',
                   img="http://4.bp.blogspot.com/-ywFznstsYjQ/UyCc8QnKoKI/"
                   "AAAAAAAAHWo/ZschryqJMuw/s1600/1rc8id67.wizardchan."
                   "Arcanine.png",
                   description="Arcanine, a Legendary Pokemon."
                   "The evolved form of Growlithe. Arcanine is "
                   "known for its bravery and fierce loyalty. "
                   "Growlithe evolves into Arcanine from its "
                   "use of a Fire Stone.",
                   created_by='sahillamba61@gmail.com',
                   pokemon_category=category3)
session.add(pokemon2)

# Menu for Fy pokemon

category4 = Pokemon_Category(category='Flying')

session.add(category4)

pokemon1 = Pokemon(name='Togekiss',
                   img="https://img00.deviantart.net/2812/i/2014/"
                   "249/f/7/__pokemon___togekiss_base__1__by_"
                   "loppiepiepie-d6pt9hn.png",
                   description="Togekiss is a white, avian Pokemon"
                   "with an ovoid body. While its feet are small "
                   "and situated closely together, its wings are "
                   "broad and triangular. Red and blue triangular "
                   "markings over its underside, and it has a short "
                   "tail consisting of three feathers.",
                   created_by='sahillamba61@gmail.com',
                   pokemon_category=category4)
session.add(pokemon1)

pokemon2 = Pokemon(name='Emolga',
                   img="https://vignette.wikia.nocookie.net/"
                   "pokemonfanon/images/9/90/Hannah_Emolga.png",
                   description="Emolga lives in treetops, "
                   "sometimes in holes gouged by Pikipek, "
                   "and uses its flaps to glide from tree to "
                   "tree. ... It does this in order to be able"
                   "to scare off bird Pokemon, giving Emolga "
                   "the capability to gather lots of food. It "
                   "then grills its food, being berries or bug "
                   "Pokemon, with electric shocks to eat.",
                   created_by='sahillamba61@gmail.com',
                   pokemon_category=category4)
session.add(pokemon2)

session.commit()

print 'Added All pokemons!'
