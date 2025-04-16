import pygame
import sys
import random
import math
import os
from pathlib import Path
import time

# Initialize Pygame and mixer for sounds
pygame.init()
pygame.mixer.init()

# Constants
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
BLUE = (70, 130, 180)
GREEN = (34, 139, 34)
RED = (220, 20, 60)
GRAY = (200, 200, 200)
BUTTON_COLOR = (100, 149, 237)
HOVER_COLOR = (65, 105, 225)

# Game data with 100 animal questions
GAME_DATA = {
    "animals": {
        "name": "ANIMAL ZONE",
        "questions": [
            {
                "question": "Which animal is known as the king of the jungle?",
                "options": ["Lion", "Tiger", "Elephant", "Giraffe"],
                "correct": "Lion",
                "fact": "Male lions have magnificent manes!",
                "image": "lion.png"
            },
            {
                "question": "Which animal have the black tear marks on its face?",
                "options": ["Cheetah", "Pronghorn Antelope", "Springbok", "Greyhound"],
                "correct": "Cheetah",
                "fact": "Cheetahs can reach speeds up to 70 mph!",
                "image": "cheetah.png"
            },
            
                 
            {
                "question": "find the animal which is the native to Africa?",
                "options": ["Lion", "Tiger", "Elephant", "Giraffe"],
                "correct": "Lion",
                "fact": "Male lions have magnificent manes that can indicate their age and health.",
                "image": "lion.png"
            },
            {
                "question": "What is the largest animal on Earth?",
                "options": ["African Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "correct": "Blue Whale",
                "fact": "The heart of a blue whale can weigh as much as a small car.",
                "image": "bluewhale.png"
            },
            {
                "question": "Which of these animals is a marsupial?",
                "options": ["Fox", "Wolf", "Kangaroo", "Zebra"],
                "correct": "Kangaroo",
                "fact": "Female kangaroos have a pouch called a marsupium where their young develop.",
                "image": "kangaroo.png"
            },
            {
                "question": "What is a group of lions called?",
                "options": ["Herd", "Pack", "Pride", "Swarm"],
                "correct": "Pride",
                "fact": "Lion prides are typically made up of related females, their cubs, and a few adult males.",
                "image": "lion.png"
            },
            {
                "question": "Which bird is known for its ability to mimic sounds?",
                "options": ["Eagle", "Owl", "Parrot", "Sparrow"],
                "correct": "Parrot",
                "fact": "Parrots can mimic human speech and other sounds due to their specialized vocal organs and learning abilities.",
                "image": "parrot.png"
            },
            {
                "question": "What is the fastest land animal?",
                "options": ["Lion", "Cheetah", "Leopard", "Hyena"],
                "correct": "Cheetah",
                "fact": "Cheetahs can reach speeds of up to 75 mph (120 km/h) in short bursts.",
                "image": "cheetah.png"
            },
            {
                "question": "Which animal has black and white stripes?",
                "options": ["Leopard", "Jaguar", "Zebra", "Tiger"],
                "correct": "Zebra",
                "fact": "Each zebra has a unique stripe pattern, just like human fingerprints.",
                "image": "zebra.png"
            },
            {
                "question": "What is a baby frog called?",
                "options": ["Calf", "Cub", "Tadpole", "Kitten"],
                "correct": "Tadpole",
                "fact": "Tadpoles are aquatic larvae with gills and tails, undergoing metamorphosis to become adult frogs.",
                "image": "tadpole.png"
            },
            {
                "question": "Which of these animals is a reptile?",
                "options": ["Salamander", "Frog", "Snake", "Newt"],
                "correct": "Snake",
                "fact": "Snakes are cold-blooded vertebrates that belong to the order Squamata and lack limbs.",
                "image": "snake.png"
            },
            {
                "question": "What do bees produce?",
                "options": ["Silk", "Wool", "Honey", "Venom"],
                "correct": "Honey",
                "fact": "Bees produce honey from nectar collected from flowers, using it as a food source for the colony.",
                "image": "honeybee.png"
            },
            {
                "question": "Which animal has a very long neck?",
                "options": ["Elephant", "Camel", "Giraffe", "Horse"],
                "correct": "Giraffe",
                "fact": "A giraffe's neck can be up to 6 feet (1.8 meters) long and contains only seven vertebrae, the same as humans.",
                "image": "giraffe.png"
            },
            {
                "question": "What is a group of wolves called?",
                "options": ["Flock", "Herd", "Pack", "Colony"],
                "correct": "Pack",
                "fact": "Wolf packs are social structures with a clear hierarchy, typically led by an alpha male and female.",
                "image": "wolf.png"
            },
            {
                "question": "Which of these is a nocturnal animal?",
                "options": ["Squirrel", "Rabbit", "Owl", "Sparrow"],
                "correct": "Owl",
                "fact": "Owls have excellent night vision due to their large eyes and specialized retinal cells.",
                "image": "owl.png"
            },
            {
                "question": "What is the largest cat species?",
                "options": ["Lion", "Tiger", "Leopard", "Jaguar"],
                "correct": "Tiger",
                "fact": "Tigers are solitary animals known for their orange fur with black stripes, and they are powerful predators.",
                "image": "tiger.png"
            },
            {
                "question": "Which animal is known for its trunk?",
                "options": ["Rhinoceros", "Hippopotamus", "Elephant", "Giraffe"],
                "correct": "Elephant",
                "fact": "An elephant's trunk is a versatile appendage used for breathing, smelling, touching, grasping, and producing sounds.",
                "image": "elephanT.png"
            },
            {
                "question": "What is a baby deer called?",
                "options": ["Foal", "Lamb", "Fawn", "Kid"],
                "correct": "Fawn",
                "fact": "Fawns are born with spots that help them camouflage in their woodland environment.",
                "image": "fawn.png"
            },
            {
                "question": "Which of these animals lives in the ocean?",
                "options": ["Gorilla", "Chimpanzee", "Dolphin", "Zebra"],
                "correct": "Dolphin",
                "fact": "Dolphins are highly intelligent marine mammals that communicate using a complex system of clicks and whistles.",
                "image": "dolphin.png"
            },
            {
                "question": "What do silkworms produce?",
                "options": ["Honey", "Wax", "Silk", "Wool"],
                "correct": "Silk",
                "fact": "Silkworms spin cocoons made of silk fibers, which are then harvested to produce silk fabric.",
                "image": "silkworm.png"
            },
            {
                "question": "Which bird is a symbol of peace?",
                "options": ["Eagle", "Hawk", "Dove", "Crow"],
                "correct": "Dove",
                "fact": "The white dove has long been a symbol of peace in various cultures.",
                "image": "dove.png"
            },
            {
                "question": "What is the largest bird in the world?",
                "options": ["Eagle", "Ostrich", "Albatross", "Penguin"],
                "correct": "Ostrich",
                "fact": "Ostriches are flightless birds native to Africa and can run at speeds of up to 45 mph (72 km/h).",
                "image": "ostrich.png"
            },
            {
                "question": "Which animal carries its young in a pouch?",
                "options": ["Fox", "Rabbit", "Kangaroo", "Wolf"],
                "correct": "Kangaroo",
                "fact": "The kangaroo's pouch provides a safe and nourishing environment for its joey to grow.",
                "image": "kangaroo.png"
            },
            {
                "question": "What is a group of fish called?",
                "options": ["Herd", "Flock", "School", "Pride"],
                "correct": "School",
                "fact": "Fish form schools for protection against predators and to improve their foraging efficiency.",
                "image": "fish.png"
            },
            {
                "question": "Which of these animals is an amphibian?",
                "options": ["Lizard", "Turtle", "Frog", "Snake"],
                "correct": "Frog",
                "fact": "Amphibians like frogs have smooth, moist skin and typically spend part of their life in water and part on land.",
                "image": "frog.png"
            },
            {
                "question": "What do cows produce?",
                "options": ["Wool", "Eggs", "Milk", "Honey"],
                "correct": "Milk",
                "fact": "Female cows produce milk to feed their calves, and this milk is also a primary source of dairy for humans.",
                "image": "cow.png"
            },
            {
                "question": "Which animal is known for its humps?",
                "options": ["Horse", "Donkey", "Camel", "Zebra"],
                "correct": "Camel",
                "fact": "Camel humps store fat, which can be converted into energy and water when needed.",
                "image": "camel.png"
            },
            {
                "question": "What is a baby sheep called?",
                "options": ["Calf", "Cub", "Lamb", "Fawn"],
                "correct": "Lamb",
                "fact": "Lambs are known for their soft wool and gentle nature.",
                "image": "lamb.png"
            },
            {
                "question": "Which of these animals can fly?",
                "options": ["Tiger", "Elephant", "Bat", "Cheetah"],
                "correct": "Bat",
                "fact": "Bats are the only mammals capable of true flight.",
                "image": "bat.ng"
            },
            {
                "question": "What is a group of geese called?",
                "options": ["Gaggle", "Herd", "Flock", "Swarm"],
                "correct": "Gaggle",
                "fact": "A group of geese on the ground is called a gaggle, while a group in flight is often called a skein or wedge.",
                "image": "geese.png"
            },
            {
                "question": "Which animal is known for its spots?",
                "options": ["Zebra", "Tiger", "Leopard", "Lion"],
                "correct": "Leopard",
                "fact": "Leopards have distinctive rosette-shaped spots that help them camouflage in their diverse habitats.",
                "image": "leopard.png"
            },
            {
                "question": "What is a baby goat called?",
                "options": ["Kid", "Foal", "Puppy", "Kitten"],
                "correct": "Kid",
                "fact": "Goats are known for their agility and playful nature, especially the young kids.",
                "image": "goat.png"
            },
            {
                "question": "Which of these is a primate?",
                "options": ["Fox", "Wolf", "Monkey", "Zebra"],
                "correct": "Monkey",
                "fact": "Monkeys are intelligent primates with grasping hands and feet, found in various parts of the world.",
                "image": "monkey.png"
            },
            {
                "question": "What do hens lay?",
                "options": ["Milk", "Wool", "Eggs", "Honey"],
                "correct": "Eggs",
                "fact": "Hens are female chickens that lay eggs, a common source of food worldwide.",
                "image": "hen.png"
            },
            {
                "question": "Which animal is known for its long snout?",
                "options": ["Hippopotamus", "Rhinoceros", "Elephant", "Giraffe"],
                "correct": "Elephant",
                "fact": "An elephant's snout, or trunk, is a highly sensitive and muscular organ.",
                "image": "elephant.png"
            },
            {
                "question": "What is a baby horse called?",
                "options": ["Calf", "Cub", "Foal", "Kitten"],
                "correct": "Foal",
                "fact": "Foals are young horses that typically stand and nurse shortly after birth.",
                "image": "foal.png"
            },
            {
                "question": "Which of these animals lives in the desert?",
                "options": ["Penguin", "Polar Bear", "Camel", "Dolphin"],
                "correct": "Camel",
                "fact": "Camels are well-adapted to survive in harsh desert environments with their ability to conserve water.",
                "image": "camel.png"
            },
            {
                "question": "What is a group of owls called?",
                "options": ["Parliament", "Herd", "Flock", "Pride"],
                "correct": "Parliament",
                "fact": "A group of owls is called a parliament, possibly due to their perceived wisdom.",
                "image": "owl.png"
            },
            {
                "question": "Which animal is known for its stripes?",
                "options": ["Leopard", "Jaguar", "Zebra", "Lion"],
                "correct": "Zebra",
                "fact": "The stripes of a zebra may help to confuse predators when they are in a group.",
                "image": "zebra.png"
            },
            {
                "question": "What is a baby pig called?",
                "options": ["Lamb", "Fawn", "Piglet", "Kid"],
                "correct": "Piglet",
                "fact": "Piglets are young pigs, often born in large litters.",
                "image": "piglet.png"
            },
            {
                "question": "Which of these is a rodent?",
                "options": ["Rabbit", "Squirrel", "Fox", "Wolf"],
                "correct": "Squirrel",
                "fact": "Rodents are mammals characterized by their continuously growing incisors.",
                "image": "squirrel.png"
            },
            {
                "question": "What do sheep produce?",
                "options": ["Milk", "Eggs", "Wool", "Honey"],
                "correct": "Wool",
                "fact": "Sheep are domesticated ruminant mammals primarily raised for their woolly fleece.",
                "image": "sheep.png"
            },
            {
                "question": "Which animal is known for its tusks?",
                "options": ["Hippopotamus", "Giraffe", "Elephant", "Zebra"],
                "correct": "Elephant",
                "fact": "Elephant tusks are elongated, continuously growing front teeth.",
                "image": "elephant.png"
            },
            {
                "question": "What is a baby rabbit called?",
                "options": ["Kitten", "Pup", "Bunny", "Chick"],
                "correct": "Bunny",
                "fact": "Baby rabbits are often called bunnies or kits.",
                "image": "rabbit.png"
            },
            {
                "question": "Which of these animals lives in the Arctic?",
                "options": ["Lion", "Tiger", "Polar Bear", "Cheetah"],
                "correct": "Polar Bear",
                "fact": "Polar bears are adapted to survive in the cold Arctic regions with thick fur and a layer of blubber.",
                "image": "polarbear.png"
            },
            {
                "question": "What is a group of crows called?",
                "options": ["Murder", "Pack", "Flock", "Swarm"],
                "correct": "Murder",
                "fact": "A group of crows is called a murder, a rather ominous-sounding collective noun.",
                "image": "crow.png"
            },
            {
                "question": "Which animal is known for its shell?",
                "options": ["Snake", "Lizard", "Turtle", "Frog"],
                "correct": "Turtle",
                "fact": "A turtle's shell is a bony structure that protects its body from predators and environmental hazards.",
                "image": "turtle.png"
            },
            {
                "question": "What is a baby chicken called?",
                "options": ["Duckling", "Gosling", "Chick", "Fawn"],
                "correct": "Chick",
                "fact": "Chicks are young domestic fowl, typically hatched from eggs.",
                "image": "babychicken.png"
            },
            {
                "question": "Which of these is a carnivore?",
                "options": ["Cow", "Horse", "Lion", "Elephant"],
                "correct": "Lion",
                "fact": "Carnivores are animals that primarily feed on meat.",
                "image": "lion.png"
            },
            {
                "question": "What do ducks produce?",
                "options": ["Milk", "Wool", "Eggs", "Honey"],
                "correct": "Eggs",
                "fact": "Female ducks lay eggs, which are often larger and richer than chicken eggs.",
                "image": "duck.png"
            },
            {
                "question": "Which animal is known for its camouflage?",
                "options": ["Lion", "Zebra", "Chameleon", "Giraffe"],
                "correct": "Chameleon",
                "fact": "Chameleons can change their skin color to blend in with their surroundings or to communicate.",
                "image" : "chameleon.png"
            },
            {
                "question": "Which animal has the longest lifespan?",
                "options": ["Galapagos Tortoise", "Bowhead Whale", "Greenland Shark", "African Elephant"],
                "correct": "Greenland Shark",
                "fact": "Greenland sharks can live over 400 years!",
                "image": "shark.png"
            }
        ]
    },
    "fruits": 
    {
        "name": "FRUITS WORLD",
        "questions": 
        [
            {
                "question": "Which fruit is known as the 'king of fruits'?",
                "options": ["Apple", "Banana", "Mango", "Grapes"],
                "correct": "Mango",
                "fact": "Mango is considered the national fruit of India and is loved worldwide!",
                "image": "mango.png"
            },
            {
                "question": "Which fruit has seeds on the outside?",
                "options": ["Strawberry", "Blueberry", "Raspberry", "Blackberry"],
                "correct": "Strawberry",
                "fact": "Strawberries are the only fruits with seeds on the outside!",
                "image": "strawberry.png"
            },
            {
                "question": "Which fruit is the largest tree-borne fruit?",
                "options": ["Durian", "Jackfruit", "Mango", "Papaya"],
                "correct": "Jackfruit",
                "fact": "Jackfruits can weigh up to 80 pounds (36 kg)!",
                "image": "jackfruit.png"
            },
            {
                "question": "Which fruit is high in potassium?",
                "options": ["Apple", "Banana", "Cherry", "Pineapple"],
                "correct": "Banana",
                "fact": "Bananas are a great source of potassium, vital for muscles and heart health!",
                "image": "banana.png"
            },
            {
                "question": "Which fruit is green on the outside and sour?",
                "options": ["Lemon", "Lime", "Orange", "Grapefruit"],
                "correct": "Lime",
                "fact": "Limes are rich in vitamin C and antioxidants!",
                "image": "lime.png"
            },
            {
                "question": "Which fruit symbolizes hospitality?",
                "options": ["Apple", "Pineapple", "Banana", "Pear"],
                "correct": "Pineapple",
                "fact": "In the 18th century, pineapples symbolized wealth and hospitality!",
                "image": "pineapple.png"
            },
            {
                "question": "Which fruit turns into raisins when dried?",
                "options": ["Grape", "Plum", "Cherry", "Blueberry"],
                "correct": "Grape",
                "fact": "Raisins are dried grapes packed with energy!",
                "image": "grape.png"
            },
            {
                "question": "Which fruit was originally called 'Chinese gooseberry'?",
                "options": ["Mango", "Kiwi", "Lychee", "Rambutan"],
                "correct": "Kiwi",
                "fact": "Kiwi fruits were once known as Chinese gooseberries!",
                "image": "kiwi.png"
            },
            {
                "question": "Which fruit contains papain enzyme to tenderize meat?",
                "options": ["Pineapple", "Papaya", "Mango", "Banana"],
                "correct": "Papaya",
                "fact": "Papayas have papain, an enzyme used in meat tenderizers!",
                "image": "papaya.png"
            },
            {
                "question": "Which fruit is famous for its strong smell but sweet taste?",
                "options": ["Durian", "Jackfruit", "Mangosteen", "Lychee"],
                "correct": "Durian",
                "fact": "Durian is called the 'King of Fruits' in Southeast Asia!",
                "image": "durian.png"
            },
            {
                "question": "Which fruit is often used to make wine?",
                "options": ["Apple", "Grape", "Cherry", "Plum"],
                "correct": "Grape",
                "fact": "Grapes are the primary fruit used for making wine!",
                "image": "winegrape.png"
            },
            {
                "question": "Which fruit is known as the 'forbidden fruit' in the Bible?",
                "options": ["Fig", "Apple", "Pomegranate", "Grape"],
                "correct": "Apple",
                "fact": "The apple is often depicted as the forbidden fruit in art and literature!",
                "image": "apple.png"
            },
            {
                "question": "Which fruit has varieties named 'Cavendish' and 'Plantain'?",
                "options": ["Banana", "Apple", "Mango", "Pineapple"],
                "correct": "Banana",
                "fact": "Cavendish bananas are the most commonly eaten type today!",
                "image": "banana.png"
            },
            {
                "question": "Which fruit has a spiky outer skin and juicy yellow flesh inside?",
                "options": ["Durian", "Pineapple", "Jackfruit", "Mangosteen"],
                "correct": "Pineapple",
                "fact": "Pineapples are loaded with vitamin C and bromelain!",
                "image": "pineapple.png"
            },
            {
                "question": "Which fruit is small, red, and often used in jams and desserts?",
                "options": ["Blueberry", "Strawberry", "Raspberry", "Blackberry"],
                "correct": "Strawberry",
                "fact": "Strawberries are packed with antioxidants and vitamin C!",
                "image": "strawberry.png"
            },
            { 
                "question": "Which fruit is native to the Mediterranean region and has many seeds inside?",
                "options": ["Orange", "Pomegranate", "Fig", "Grape"],
                "correct": "Pomegranate",
                "fact": "Pomegranates symbolize fertility and abundance!",
                "image": "pomegranate.png"
            },
            {
                "question": "Which tropical fruit is known for its dragon-like skin?",
                "options": ["Rambutan", "Durian", "Dragon Fruit", "Lychee"],
                "correct": "Dragon Fruit",
                "fact": "Dragon fruit is rich in antioxidants and fiber!",
                "image": "dragonfruit.png"
            },
            {
                "question": "Which fruit is small, blue, and known for its high antioxidant levels?",
                "options": ["Blueberry", "Blackberry", "Grape", "Currant"],
                "correct": "Blueberry",
                "fact": "Blueberries are among the most antioxidant-rich fruits!",
                "image": "blueberry.png"
            },
            {
                "question": "Which fruit has a creamy texture and is rich in healthy fats?",
                "options": ["Banana", "Avocado", "Mango", "Papaya"],
                "correct": "Avocado",
                "fact": "Avocados are loaded with heart-healthy monounsaturated fats!",
                "image": "avocado.png"
            },
            {       
                "question": "Which fruit is dried to make prunes?",
                "options": ["Plum", "Grape", "Cherry", "Fig"],
                "correct": "Plum",
                "fact": "Prunes are dried plums that aid digestion!",
                "image": "plum.png"
            },
            {
                "question": "Which fruit is shaped like a star when cut crosswise?",
                "options": ["Starfruit", "Pineapple", "Kiwi", "Mango"],
                "correct": "Starfruit",
                "fact": "Starfruit, also called carambola, has a unique star shape!",
                "image": "starfruit.png"
            },
            {
                "question": "Which fruit is the primary ingredient in guacamole?",
                "options": ["Avocado", "Mango", "Tomato", "Banana"],
                "correct": "Avocado",
                "fact": "Avocados are essential for making creamy guacamole!",
                "image": "avocado.png"
            },
            {
                "question": "Which fruit is known for its fuzzy skin and sweet orange flesh?",
                "options": ["Nectarine", "Peach", "Plum", "Apricot"],
                "correct": "Peach",
                "fact": "Peaches are a summer favorite packed with vitamins A and C!",
                "image": "peach.png"
            },
            {
                "question": "Which small fruit is often dried to make currants?",
                "options": ["Blackcurrant", "Gooseberry", "Grape", "Blueberry"],
                "correct": "Blackcurrant",
                "fact": "Blackcurrants are rich in vitamin C and antioxidants!",
                "image": "blackcurrant.png"
            },
            {
                "question": "Which fruit is a hybrid between a pomelo and an orange?",
                "options": ["Lime", "Lemon", "Grapefruit", "Tangerine"],
                "correct": "Grapefruit",
                "fact": "Grapefruits were discovered in Barbados!",
                "image": "grapefruit.png"
            },
            {
                "question": "Which citrus fruit is often paired with tequila shots?",
                "options": ["Orange", "Lime", "Lemon", "Grapefruit"],
                "correct": "Lime",
                "fact": "Limes add a refreshing tangy flavor to drinks and food!",
                "image": "lime.png"
            },
            {
                "question": "Which tiny fruit grows on vines and is often made into jelly?",
                "options": ["Currant", "Grape", "Berry", "Fig"],
                "correct": "Grape",
                "fact": "Grapes are also used to make jellies and jams!",
                "image": "grape.png"
            },
            {
                "question": "Which fruit is known for its ability to float in water?",
                "options": ["Apple", "Watermelon", "Orange", "Cranberry"],
                "correct": "Cranberry",
                "fact": "Cranberries float because of tiny air pockets inside!",
                "image": "cranberry.png"
            },
            {
                "question": "Which fruit is commonly used in Thanksgiving sauces?",
                "options": ["Blueberry", "Cranberry", "Cherry", "Plum"],
                "correct": "Cranberry",
                "fact": "Cranberry sauce is a traditional Thanksgiving dish!",
                "image": "cranberry.png"
            },
            {
                "question": "Which fruit has a leathery red skin and juicy white flesh?",
                "options": ["Lychee", "Rambutan", "Durian", "Mangosteen"],
                "correct": "Lychee",
                "fact": "Lychees are sweet, fragrant fruits from Asia!",
                "image": "lychee.png"
            },
            {
                "question": "Which fruit is known for having a pit and is called a 'stone fruit'?",
                "options": ["Apple", "Pear", "Peach", "Grape"],
                "correct": "Peach",
                "fact": "Stone fruits have a large seed inside, called a pit!",
                "image": "peach.png"
            },
            {
                "question": "Which fruit's name comes from the Latin word for 'seeded apple'?",
                "options": ["Pomegranate", "Apple", "Pear", "Orange"],
                "correct": "Pomegranate",
                "fact": "Pomegranate means 'seeded apple' in Latin!",
                "image": "pomegranate.png"
            },
            {
                "question": "Which fruit is known as the 'Queen of Fruits'?",
                "options": ["Durian", "Mangosteen", "Lychee", "Rambutan"],
                "correct": "Mangosteen",
                "fact": "Mangosteens are prized for their sweet and tangy flavor!",
                "image": "mangosteen.png"
            },
            {
                "question": "Which fruit has varieties called 'Blood' and 'Valencia'?",
                "options": ["Apple", "Orange", "Grape", "Mango"],
                "correct": "Orange",
                "fact": "Blood oranges have a beautiful red flesh!",
                "image": "orange.png"
            },
            {
                "question": "Which fruit is known to have the highest oil content?",
                "options": ["Olive", "Avocado", "Coconut", "Almond"],
                "correct": "Olive",
                "fact": "Olives are rich in healthy oils and used for making olive oil!",
                "image": "olive.png"
            },
            {
                "question": "Which tropical fruit has hairy red skin and juicy white flesh?",
                "options": ["Lychee", "Dragon Fruit", "Rambutan", "Mangosteen"],
                "correct": "Rambutan",
                "fact": "Rambutans are related to lychees and taste sweet!",
                "image": "rambutan.png"
            },
            {
                "question": "Which fruit is often associated with teachers?",
                "options": ["Apple", "Orange", "Banana", "Peach"],
                "correct": "Apple",
                "fact": "Apples are traditionally given to teachers as gifts!",
                "image": "apple.png"
            },
            {
                "question": "Which fruit has a nickname 'alligator pear'?",
                "options": ["Kiwi", "Mango", "Avocado", "Guava"],
                "correct": "Avocado",
                "fact": "Avocados are called alligator pears due to their bumpy skin!",
                "image": "avocado.png"
            },
            {
                "question": "Which fruit is dried to make dates?",
                "options": ["Palm Fruit", "Banana", "Grape", "Fig"],
                "correct": "Palm Fruit",
                "fact": "Dates come from date palm trees and are packed with energy!",
                "image": "palm fruit.png"
            },
            {
                "question": "Which small, round, green fruit is often sour?",
                "options": ["Kiwi", "Gooseberry", "Lime", "Grape"],
                "correct": "Gooseberry",
                "fact": "Gooseberries are tart and rich in vitamin C!",
                "image": "gooseberry.png"
            },
            {
                "question": "Which fruit has a strong smell and is banned in some hotels?",
                "options": ["Durian", "Jackfruit", "Mango", "Papaya"],
                "correct": "Durian",
                "fact": "Durian is famous for its powerful smell and unique taste!",
                "image": "durian.png"
            },
            {
                "question": "Which fruit is often mistaken for a vegetable and is used in salads?",
                "options": ["Tomato", "Cucumber", "Bell Pepper", "Carrot"],
                "correct": "Tomato",
                "fact": "Tomatoes are botanically fruits even though used like veggies!",
                "image": "tomato.png"
            },
            {
                "question": "Which fruit has seeds called 'pips'?",
                "options": ["Apple", "Banana", "Pear", "Grape"],
                "correct": "Apple",
                "fact": "Apple seeds are often referred to as pips!",
                "image": "apple.png"
            },
            {
                "question": "Which fruit is traditionally eaten on New Year’s Eve in Spain?",
                "options": ["Grape", "Fig", "Pomegranate", "Pear"],
                "correct": "Grape",
                "fact": "Spaniards eat 12 grapes at midnight for good luck!",
                "image": "grape.png"
            },
            {
                "question": "Which fruit’s juice is commonly used to make cider?",
                "options": ["Apple", "Pear", "Cherry", "Plum"],
                "correct": "Apple",
                "fact": "Apple cider is a popular drink, especially in autumn!",
                "image": "apple.png"
            },
            {
                "question": "Which tropical fruit has pink skin and sweet black seeds inside?",
                "options": ["Dragon Fruit", "Papaya", "Rambutan", "Lychee"],
                "correct": "Dragon Fruit",
                "fact": "Dragon fruits are rich in antioxidants and look amazing!",
                "image": "dragonfruit.png"
            },
            {
                "question": "Which fruit is the primary ingredient in a traditional Indian 'lassi' drink?",
                "options": ["Mango", "Banana", "Coconut", "Pineapple"],
                "correct": "Mango",
                "fact": "Mango lassi is a creamy, refreshing Indian beverage!",
                "image": "mango.png"
            },
            {
                "question": "Which fruit is made into wine in regions like Bordeaux and Napa Valley?",
                "options": ["Grape", "Cherry", "Pear", "Apple"],
                "correct": "Grape",
                "fact": "Grapes are crushed and fermented to create delicious wines!",
                "image": "grape.png"
            },
            {
                "question": "Which green fruit is known for its sour taste and vitamin C content?",
                "options": ["Lime", "Grapefruit", "Green Apple", "Lemon"],
                "correct": "Lime",
                "fact": "Limes are packed with vitamin C and are very sour!",
                "image": "lime.png"
            },
            {
                "question": "Which fruit looks like a giant spiky ball on the outside but is sweet inside?",
                "options": ["Durian", "Jackfruit", "Mangosteen", "Rambutan"],
                "correct": "Jackfruit",
                "fact": "Jackfruits can grow over 30kg and are super versatile!",
                "image": "jackfruit.png"
            },
            {
                "question": "Which fruit is the symbol of hospitality and welcome?",
                "options": ["Banana", "Pineapple", "Apple", "Orange"],
                "correct": "Pineapple",
                "fact": "Pineapples represent warmth, welcome, and friendship!",
                "image": "pineapple.png"
            },
            {
                "question": "Which fruit can be red, green, or black and is dried into raisins?",
                "options": ["Blueberry", "Blackberry", "Grape", "Cranberry"],
                "correct": "Grape",
                "fact": "Raisins are just dried grapes!",
                "image": "raisin.png"
            },
            {
                "question": "Which fruit contains enzymes that break down proteins, making it a great meat tenderizer?",
                "options": ["Papaya", "Banana", "Pineapple", "Apple"],
                "correct": "Papaya",
                "fact": "Papayas contain papain, a natural meat tenderizer!",
                "image": "papaya.png"
            },
            {
                "question": "Which fruit’s seeds are called 'stones' because of their hard shells?",
                "options": ["Peach", "Plum", "Cherry", "All of these"],
                "correct": "All of these",
                "fact": "Peaches, plums, and cherries are all stone fruits!",
                "image": "peach.png, plum.png, cherry.png"
            },
            {
                "question": "Which fruit is traditionally given as a gift during Chinese New Year?",
                "options": ["Apple", "Orange", "Banana", "Grape"],
                "correct": "Orange",
                "fact": "Oranges symbolize wealth and good fortune!",
                "image": "orange.png"
            },
            {
                "question": "Which fruit's juice was once used as invisible ink?",
                "options": ["Lemon", "Orange", "Pineapple", "Banana"],
                "correct": "Lemon",
                "fact": "Lemon juice can be used to make secret invisible messages!",
                "image": "lemon.png"
            },
            {
                "question": "Which fruit has a crown of leaves on top and is grown in Hawaii?",
                "options": ["Banana", "Pineapple", "Coconut", "Papaya"],
                "correct": "Pineapple",
                "fact": "Hawaii is famous for its sweet pineapples!",
                "image": "pineapple.png"
            },
            {
                "question": "Which fruit is rich in potassium and has a yellow peel?",
                "options": ["Apple", "Banana", "Peach", "Pear"],
                "correct": "Banana",
                "fact": "Bananas are great for heart health because of their potassium!",
                "image": "banana.png"
            },
            {
                "question": "Which fruit has varieties named 'Hass' and 'Fuerte'?",
                "options": ["Banana", "Avocado", "Mango", "Peach"],
                "correct": "Avocado",
                "fact": "Hass avocados are the most popular type worldwide!",
                "image": "avocado.png"
            },
            {
                "question": "Which red fruit is closely associated with love and Valentine’s Day?",
                "options": ["Cherry", "Strawberry", "Apple", "Raspberry"],
                "correct": "Strawberry",
                "fact": "Strawberries symbolize love and romance!",
                "image": "strawberry.png"
            },      
            {
                "question": "Which fruit has tiny edible seeds and is often green or yellow inside?",
                "options": ["Kiwi", "Mango", "Papaya", "Peach"],
                "correct": "Kiwi",
                "fact": "Kiwis are packed with vitamin C and tiny edible seeds!",
                "image": "kiwi.png"
            },
            {
                "question": "Which fruit is often eaten with whipped cream during summer festivals in Europe?",
                "options": ["Strawberry", "Blueberry", "Raspberry", "Peach"],
                "correct": "Strawberry",
                "fact": "Strawberries and cream are a classic treat!",
                "image": "strawberry.png"
            },
            {
                "question": "Which fruit has a skin that changes from green to yellow to red when ripe?",
                "options": ["Mango", "Banana", "Papaya", "Peach"],
                "correct": "Mango",
                "fact": "Mangoes change color as they ripen!",
                "image": "mango.png"
            },
            {
                "question": "Which fruit has a pit and is fuzzy on the outside?",
                "options": ["Peach", "Plum", "Cherry", "Grape"],
                "correct": "Peach",
                "fact": "Peaches are soft and fuzzy outside with a pit inside!",
                "image": "peach.png"
            },
            {
                "question": "Which fruit is commonly associated with ancient Greek mythology and Persephone?",
                "options": ["Pomegranate", "Apple", "Grape", "Pear"],
                "correct": "Pomegranate",
                "fact": "Pomegranates symbolize life and fertility!",
                "image": "pomegranate.png"
            },
            {
                "question": "Which yellow fruit is the largest herbaceous plant fruit?",
                "options": ["Banana", "Pineapple", "Papaya", "Mango"],
                "correct": "Banana",
                "fact": "Banana plants are giant herbs, not trees!",
                "image": "banana.png"
            },
            {
                "question": "Which fruit is used to make guacamole?",
                "options": ["Avocado", "Tomato", "Lemon", "Mango"],
                "correct": "Avocado",
                "fact": "Guacamole’s main ingredient is avocado!",
                "image": "avocado.png"
            },
            {
                "question": "Which citrus fruit has a sweeter variety called 'mandarin'?",
                "options": ["Orange", "Lime", "Lemon", "Grapefruit"],
                "correct": "Orange",
                "fact": "Mandarins are a type of small, sweet orange!",
                "image": "orange.png"
            },
            {
                "question": "Which fruit is famous for being part of a Thanksgiving cranberry sauce?",
                "options": ["Cranberry", "Blueberry", "Raspberry", "Blackberry"],
                "correct": "Cranberry",
                "fact": "Cranberries are a holiday classic in sauces!",
                "image": "cranberry.png"
            },
            {
                "question": "Which fruit is shaped like a star when cut crosswise?",
                "options": ["Starfruit", "Kiwi", "Pineapple", "Banana"],
                "correct": "Starfruit",
                "fact": "Starfruit gets its name from its star-like slices!",
                "image": "starfruit.png"
            },
            {
                "question": "Which fruit can float because 25% of its volume is air?",
                "options": ["Apple", "Orange", "Grape", "Banana"],
                "correct": "Apple",
                "fact": "Apples float on water because of the air inside!",
                "image": "apple.png"
            },
            {
                "question": "Which fruit is known for having a strong tart taste and comes in varieties like Bing and Rainier?",
                "options": ["Cherry", "Plum", "Peach", "Grape"],
                "correct": "Cherry",
                "fact": "Bing cherries are sweet, Rainier cherries are golden!",
                "image": "cherry.png"
            },
            {
                "question": "Which fruit is shaped like a bell and used in Caribbean cooking?",
                "options": ["Bell Apple", "Ackee", "Guava", "Coconut"],
                "correct": "Ackee",
                "fact": "Ackee is Jamaica’s national fruit!",
                "image": "ackee.png"
            },
            {
                "question": "Which fruit's oil is extracted and used in beauty products?",
                "options": ["Avocado", "Coconut", "Grape", "Peach"],
                "correct": "Coconut",
                "fact": "Coconut oil is popular for hair and skin care!",
                "image": "coconut.png"
            },
            {
                "question": "Which fruit is a key ingredient in Mojito cocktails?",
                "options": ["Lime", "Lemon", "Orange", "Grapefruit"],
                "correct": "Lime",
                "fact": "Limes give mojitos their fresh zesty flavor!",
                "image": "lime.png"
            },
            {
                "question": "Which fruit is known as 'Indian Gooseberry'?",
                "options": ["Amla", "Guava", "Tamarind", "Lychee"],
                "correct": "Amla",
                "fact": "Amla is rich in vitamin C and used in Ayurveda!",
                "image": "amla.png"
            },
            {
                "question": "Which fruit is often dried and turned into prunes?",
                "options": ["Plum", "Grape", "Fig", "Date"],
                "correct": "Plum",
                "fact": "Prunes are dried plums!",
                "image": "plum.png"
            },
            {
                "question": "Which fruit is the main ingredient in the dessert 'banana split'?",
                "options": ["Banana", "Mango", "Pineapple", "Peach"],
                "correct": "Banana",
                "fact": "Bananas are the star of a banana split!",
                "image": "banana.png"
            },
            {
                "question": "Which fruit's name comes from the Latin word for 'seeded apple'?",
                "options": ["Pomegranate", "Peach", "Plum", "Grape"],
                "correct": "Pomegranate",
                "fact": "Pomegranate means 'apple with many seeds'!",
                "image": "pomegranate.png"
            },
            {
                "question": "Which fruit has varieties called 'Bartlett' and 'Anjou'?",
                "options": ["Apple", "Pear", "Peach", "Plum"],
                "correct": "Pear",
                "fact": "Bartlett pears are juicy and sweet!",
                "image": "pear.png"
            },
            {
                "question": "Which fruit is called 'the king of fruits'?",
                "options": ["Mango", "Durian", "Pineapple", "Banana"],
                "correct": "Mango",
                "fact": "Mangoes are celebrated as the king of fruits!",
                "image": "mango.png"
            },
            {
                "question": "Which fruit is traditionally thrown at a festival in Spain?",
                "options": ["Tomato", "Apple", "Orange", "Grape"],
                "correct": "Tomato",
                "fact": "La Tomatina festival in Spain is all about tomato fights!",
                "image": "tomato.png"
            },
            {
                "question": "Which small blue fruit grows on bushes and is rich in antioxidants?",
                "options": ["Blueberry", "Blackberry", "Raspberry", "Cranberry"],
                "correct": "Blueberry",
                "fact": "Blueberries are superfoods packed with antioxidants!",
                "image": "blueberry.png"
            },
            {
                "question": "Which fruit is shaped like a tear and has a creamy interior?",
                "options": ["Pear", "Fig", "Date", "Lychee"],
                "correct": "Fig",
                "fact": "Figs are naturally sweet and tear-shaped!",
                "image": "fig.png"
            },
            {
                "question": "Which fruit has varieties like 'Kent' and 'Tommy Atkins'?",
                "options": ["Mango", "Banana", "Papaya", "Peach"],
                "correct": "Mango",
                "fact": "Kent mangoes are juicy and sweet!",
                "image": "mango.png"
            },
            {
                "question": "Which fruit is sometimes called a 'Chinese date'?",
                "options": ["Jujube", "Lychee", "Dragonfruit", "Guava"],
                "correct": "Jujube",
                "fact": "Jujubes are small sweet fruits like dates!",
                "image": "jujube.png"
            },
            {
                "question": "Which fruit is shaped like a large seed pod and has a sour pulp used in chutneys?",
                "options": ["Tamarind", "Guava", "Papaya", "Coconut"],
                "correct": "Tamarind",
                "fact": "Tamarind pulp adds a tangy flavor to dishes!",
                "image": "tamarind.png"
            },
            {
                "question": "Which fruit's seeds were found preserved in King Tutankhamun's tomb?",
                "options": ["Pomegranate", "Date", "Grape", "Fig"],
                "correct": "Date",
                "fact": "Dates were highly valued in ancient Egypt!",
                "image": "date.png"
            },
            {
                "question": "Which tropical fruit has a hairy skin but a sweet and juicy interior?",
                "options": ["Rambutan", "Lychee", "Mangosteen", "Durian"],
                "correct": "Rambutan",
                "fact": "Rambutan looks wild but tastes amazing!",
                "image": "rambutan.png"
            },
            {
                "question": "Which fruit has a very thick skin and is used to make lemonade?",
                "options": ["Lemon", "Orange", "Lime", "Grapefruit"],
                "correct": "Lemon",
                "fact": "Lemonade is made from fresh lemons!",
                "image": "lemon.png"
            },
            {
                "question": "Which fruit can survive freezing temperatures and still taste sweet after thawing?",
                "options": ["Persimmon", "Apple", "Pear", "Plum"],
                "correct": "Persimmon",
                "fact": "Frozen persimmons become extra sweet!",
                "image": "persimmon.png"
            }
        ]                 
    },
    "flowers": 
    {
        "name": "FLOWER GARDEN",
        "questions": 
        [
            {
                "question": "Which flower is known as the 'king of flowers'?",
                "options": ["Rose", "Lotus", "Sunflower", "Tulip"],
                "correct": "Rose",
                "fact": "The rose has long been a symbol of love and beauty!",
                "image": "rose.png"
            },
            {
                "question": "Which flower is the national flower of India?",
                "options": ["Rose", "Marigold", "Lotus", "Jasmine"],
                "correct": "Lotus",
                "fact": "The lotus represents purity and divinity in India!",
                "image": "lotus.png"
            },
            {
                "question": "Which flower is associated with Holland and famous for its colorful fields?",
                "options": ["Tulip", "Daffodil", "Rose", "Sunflower"],
                "correct": "Tulip",
                "fact": "The Netherlands is world-famous for its tulip gardens!",
                "image": "tulip.png"
            },
            {
                "question": "Which flower always faces the sun as it moves across the sky?",
                "options": ["Sunflower", "Daisy", "Marigold", "Poppy"],
                "correct": "Sunflower",
                "fact": "Sunflowers exhibit heliotropism, turning toward the sun!",
                "image": "sunflower.png"
            },
            {
                "question": "Which flower is traditionally given on Valentine’s Day?",
                "options": ["Rose", "Lily", "Tulip", "Orchid"],
                "correct": "Rose",
                "fact": "Roses, especially red ones, symbolize romantic love!",
                "image": "rose.png"
            },
            {
                "question": "Which flower blooms only at night and is known as the 'Queen of the Night'?",
                "options": ["Night-blooming Cereus", "Moonflower", "Jasmine", "Orchid"],
                "correct": "Night-blooming Cereus",
                "fact": "The night-blooming cereus opens its flowers after dark!",
                "image": "nightbloomingcereus.png"
            },
            {
                "question": "Which flower is a symbol of remembrance for soldiers?",
                "options": ["Poppy", "Rose", "Daisy", "Violet"],
                "correct": "Poppy",
                "fact": "Red poppies are worn in honor of fallen soldiers!",
                "image": "poppy.png"
            },
            {
                "question": "Which flower is known for its strong sweet scent and is used in perfumes?",
                "options": ["Jasmine", "Rose", "Lavender", "Violet"],
                "correct": "Jasmine",
                "fact": "Jasmine flowers are tiny but highly fragrant!",
                "image": "jasmine.png"
            },
            {
                "question": "Which flower is often associated with death and used in Day of the Dead celebrations?",
                "options": ["Marigold", "Rose", "Sunflower", "Daisy"],
                "correct": "Marigold",
                "fact": "Marigolds are believed to guide spirits back to the living world!",
                "image": "marigold.png"
            },
            {
                "question": "Which small, blue flower's name means 'forget me not'?",
                "options": ["Forget-Me-Not", "Bluebell", "Lavender", "Cornflower"],
                "correct": "Forget-Me-Not",
                "fact": "Forget-me-nots symbolize true love and remembrance!",
                "image": "forgetmenot.png"
            },
            {
                "question": "Which flower symbolizes new beginnings and is often used at weddings?",
                "options": ["Lily", "Orchid", "Rose", "Daisy"],
                "correct": "Lily",
                "fact": "Lilies, especially white ones, represent purity and fresh starts!",
                "image": "lily.png"
            },
            {
                "question": "Which flower is famously large and smells like rotting flesh?",
                "options": ["Rafflesia", "Corpse Flower", "Titan Arum", "Sunflower"],
                "correct": "Corpse Flower",
                "fact": "The corpse flower can grow over 10 feet tall and smells terrible!",
                "image": "corpseflower.png"
            },
            {
                "question": "Which flower’s seeds are used to produce oil and snacks?",
                "options": ["Sunflower", "Poppy", "Daisy", "Lavender"],
                "correct": "Sunflower",
                "fact": "Sunflower seeds are nutritious and widely used in cooking!",
                "image": "sunflower.png"
            },
            {
                "question": "Which flower is often linked with royalty and wealth?",
                "options": ["Orchid", "Rose", "Lotus", "Tulip"],
                "correct": "Orchid",
                "fact": "Orchids were once so rare they symbolized luxury!",
                "image": "orchid.png"
            },
            {
                "question": "Which flower has varieties named 'Peace' and 'Mr. Lincoln'?",
                "options": ["Rose", "Tulip", "Carnation", "Daffodil"],
                "correct": "Rose",
                "fact": "There are over 300 species of roses worldwide!",
                "image": "rose.png"
            },
            {
                "question": "Which flower has trumpet-shaped blooms and is often yellow or white?",
                "options": ["Daffodil", "Tulip", "Lily", "Daisy"],
                "correct": "Daffodil",
                "fact": "Daffodils are often seen as a sign of spring’s arrival!",
                "image": "daffodil.png"
            },
            {
                "question": "Which flower has been cultivated in Japan for centuries and is celebrated in 'Hanami' festivals?",
                "options": ["Cherry Blossom", "Rose", "Magnolia", "Daisy"],
                "correct": "Cherry Blossom",
                "fact": "Cherry blossoms are a symbol of fleeting beauty in Japanese culture!",
                "image": "cherryblossom.png"
            },
            {
                "question": "Which flower is called the 'flower of the dead' in Mexican culture?",
                "options": ["Marigold", "Rose", "Orchid", "Sunflower"],
                "correct": "Marigold",
                "fact": "Marigolds are believed to attract the souls of the dead during Día de los Muertos!",
                "image": "marigold.png"
            },
            {
                "question": "Which purple flower is commonly used to make soothing essential oils?",
                "options": ["Lavender", "Violet", "Bluebell", "Lilac"],
                "correct": "Lavender",
                "fact": "Lavender is famous for its calming fragrance and therapeutic uses!",
                "image": "lavender.png"
            },
            {
                "question": "Which small flower has a name that sounds like a command to 'speed well'?",
                "options": ["Veronica", "Violet", "Daisy", "Iris"],
                "correct": "Veronica",
                "fact": "Veronicas are hardy flowers that thrive in many climates!",
                "image": "veronica.png"
            }, 
            {
                "question": "Which flower is known for growing in muddy waters and symbolizes purity?",
                "options": ["Lotus", "Water Lily", "Rose", "Iris"],
                "correct": "Lotus",
                "fact": "Despite growing in mud, the lotus blooms beautifully clean!",
                "image": "lotus.png"
            },
            {
                "question": "Which bright flower is named after a tool used for sewing?",
                "options": ["Snapdragon", "Needle Flower", "Buttonbush", "Thimbleweed"],
                "correct": "Snapdragon",
                "fact": "Snapdragon flowers resemble a dragon's face that opens and closes!",
                "image": "snapdragon.png"
            },
            {
                "question": "Which flower's name means 'rainbow' in Greek mythology?",
                "options": ["Iris", "Rose", "Tulip", "Lily"],
                "correct": "Iris",
                "fact": "Iris flowers are named after the Greek goddess of the rainbow!",
                "image": "iris.png"
            },
            {
                "question": "Which flower is considered the fastest growing plant?",
                "options": ["Bamboo Flower", "Sunflower", "Lotus", "Dandelion"],
                "correct": "Bamboo Flower",
                "fact": "Bamboo flowers very rarely but grows incredibly fast when it does!",
                "image": "bambooflower.png"
            },
            {
                "question": "Which flower is often given to celebrate Mother's Day?",
                "options": ["Carnation", "Rose", "Daisy", "Lily"],
                "correct": "Carnation",
                "fact": "Carnations represent a mother's eternal love!",
                "image": "carnation.png"
            },
            {
                "question": "Which flower’s seeds can sleep for hundreds of years before growing?",
                "options": ["Lotus", "Sunflower", "Tulip", "Daisy"],
                "correct": "Lotus",
                "fact": "Ancient lotus seeds over 1,000 years old have been germinated!",
                "image": "lotus.png"
            },
            {
                "question": "Which flower produces saffron, the most expensive spice?",
                "options": ["Crocus", "Lavender", "Daffodil", "Orchid"],
                "correct": "Crocus",
                "fact": "Saffron comes from the stigma of the crocus flower!",
                "image": "crocus.png"
            },
            {
                "question": "Which flower is famously associated with Scotland?",
                "options": ["Thistle", "Rose", "Heather", "Daffodil"],
                "correct": "Thistle",
                "fact": "The thistle is Scotland’s national flower and symbol!",
                "image": "thistle.png"
            },
            {
                "question": "Which flower is known as the 'flower of the gods'?",
                "options": ["Carnation", "Rose", "Iris", "Daisy"],
                "correct": "Carnation",
                "fact": "In Greek, 'carnation' means 'divine flower'!",
                "image": "carnation.png"
            },
            {
                "question": "Which flower was sacred to ancient Egyptians?",
                "options": ["Blue Lotus", "Rose", "Sunflower", "Orchid"],
                "correct": "Blue Lotus",
                "fact": "Blue lotuses symbolized rebirth and the sun in ancient Egypt!",
                "image": "bluelotus.png"
            },
            {
                "question": "Which flower shares its name with a precious stone?",
                "options": ["Amaryllis", "Jasmine", "Carnelian", "Rose"],
                "correct": "Carnelian",
                "fact": "Carnelian flowers and stones were prized by ancient civilizations!",
                "image": "carnelian.png"
            },
            {
                "question": "Which flower symbolizes modesty and youth?",
                "options": ["Daisy", "Rose", "Lily", "Tulip"],
                "correct": "Daisy",
                "fact": "Daisies are simple yet charming, symbolizing innocence!",
                "image": "daisy.png"
            },
            {
                "question": "Which flower is traditionally associated with 25th wedding anniversaries?",
                "options": ["Iris", "Rose", "Tulip", "Sunflower"],
                "correct": "Iris",
                "fact": "Irises symbolize faith, hope, and wisdom!",
                "image": "iris.png"
            },
            {
                "question": "Which flower has a variety called 'Black Beauty'?",
                "options": ["Tulip", "Rose", "Lily", "Poppy"],
                "correct": "Tulip",
                "fact": "Black Beauty tulips are deep purple, almost black!",
                "image": "tulip.png"
            },
            {
                "question": "Which tiny flower carpets the forest floors in spring?",
                "options": ["Bluebell", "Violet", "Daisy", "Lavender"],
                "correct": "Bluebell",
                "fact": "Bluebells create stunning blue carpets in woodlands!",
                "image": "bluebell.png"
            },
            {
                "question": "Which flower's name comes from the French word for 'lion’s tooth'?",
                "options": ["Dandelion", "Sunflower", "Rose", "Tulip"],
                "correct": "Dandelion",
                "fact": "Dandelion leaves are jagged, resembling lion teeth!",
                "image": "dandelion.png"
            },
            {
                "question": "Which tropical flower is often worn behind the ear in Hawaii?",
                "options": ["Plumeria", "Hibiscus", "Orchid", "Lotus"],
                "correct": "Plumeria",
                "fact": "Plumeria flowers symbolize positivity and aloha spirit!",
                "image": "plumeria.png"
            },
            {
                "question": "Which flower is linked to apologies and forgiveness?",
                "options": ["Hyacinth", "Daisy", "Rose", "Tulip"],
                "correct": "Hyacinth",
                "fact": "Purple hyacinths symbolize sorrow and asking for forgiveness!",
                "image": "hyacinth.png"
            },
            {
                "question": "Which flower is the largest unbranched inflorescence in the world?",
                "options": ["Titan Arum", "Rafflesia", "Sunflower", "Rose"],
                "correct": "Titan Arum",
                "fact": "The Titan Arum’s huge bloom can reach over 10 feet!",
                "image": "titanarum.png"
            },
            {
                "question": "Which flower is considered sacred in Buddhism?",
                "options": ["Lotus", "Sunflower", "Rose", "Lavender"],
                "correct": "Lotus",
                "fact": "The lotus represents spiritual enlightenment and rebirth!",
                "image": "lotus.png"
            },
            {
                "question": "Which flower is commonly associated with remembrance?",
                "options": ["Poppy", "Rose", "Daisy", "Sunflower"],
                "correct": "Poppy",
                "fact": "Red poppies are worn to honor soldiers who died in wars!",
                "image": "poppy.png"
            },
            {
                "question": "Which flower is the national flower of Japan?",
                "options": ["Cherry Blossom", "Lotus", "Rose", "Orchid"],
                "correct": "Cherry Blossom",
                "fact": "Cherry blossoms (Sakura) symbolize the beauty of life!",
                "image": "cherryblossom.png"
            },
            {
                "question": "Which flower blooms at night and wilts by morning?",
                "options": ["Moonflower", "Sunflower", "Tulip", "Lily"],
                "correct": "Moonflower",
                "fact": "Moonflowers open in the evening and glow under moonlight!",
                "image": "moonflower.png"
            },
            {
                "question": "Which fragrant flower is used extensively in perfumes?",
                "options": ["Jasmine", "Rose", "Lavender", "Orchid"],
                "correct": "Jasmine",
                "fact": "Jasmine oil is one of the most precious perfume ingredients!",
                "image": "jasmine.png"
            },
            {
                "question": "Which yellow flower turns towards the sun?",
                "options": ["Sunflower", "Dandelion", "Marigold", "Tulip"],
                "correct": "Sunflower",
                "fact": "Sunflowers track the sun’s movement across the sky!",
                "image": "sunflower.png"
            },
            {
                "question": "Which flower is associated with resurrection in Christianity?",
                "options": ["Lily", "Rose", "Daisy", "Tulip"],
                "correct": "Lily",
                "fact": "White lilies symbolize purity and the resurrection of Jesus!",
                "image": "lily.png"
            },
            {
                "question": "Which flower is considered a symbol of luxury and beauty?",
                "options": ["Orchid", "Rose", "Tulip", "Sunflower"],
                "correct": "Orchid",
                "fact": "Orchids are exotic and have been prized for centuries!",
                "image": "orchid.png"
            },
            {
                "question": "Which flower gets its name from the Greek word for 'star'?",
                "options": ["Aster", "Daisy", "Sunflower", "Rose"],
                "correct": "Aster",
                "fact": "Aster flowers have a star-like shape!",
                "image": "aster.png"
            },
            {
                "question": "Which flower’s oil is known for calming effects?",
                "options": ["Lavender", "Rose", "Jasmine", "Lily"],
                "correct": "Lavender",
                "fact": "Lavender oil is used for relaxation and stress relief!",
                "image": "lavender.png"
            },
            {
                "question": "Which flower has varieties like 'Queen of Night'?",
                "options": ["Tulip", "Rose", "Lily", "Daffodil"],
                "correct": "Tulip",
                "fact": "The 'Queen of Night' tulip is a deep, almost black color!",
                "image": "tulip.png"
            },
            {
                "question": "Which flower is known as 'the harbinger of spring'?",
                "options": ["Crocus", "Snowdrop", "Daffodil", "Tulip"],
                "correct": "Snowdrop",
                "fact": "Snowdrops often bloom while snow is still on the ground!",
                "image": "snowdrop.png"
            },
            {
                "question": "Which flower is famous for its trumpet-like shape?",
                "options": ["Daffodil", "Tulip", "Rose", "Lily"],
                "correct": "Daffodil",
                "fact": "Daffodils are bright symbols of new beginnings!",
                "image": "daffodil.png"
            },
            {
                "question": "Which flower is traditionally used in Hawaiian leis?",
                "options": ["Plumeria", "Orchid", "Hibiscus", "Sunflower"],
                "correct": "Plumeria",
                "fact": "Plumerias are fragrant and colorful, perfect for leis!",
                "image": "plumeria.png"
            },
            {
                "question": "Which flower was once used to treat wounds during wars?",
                "options": ["Yarrow", "Lavender", "Rose", "Tulip"],
                "correct": "Yarrow",
                "fact": "Yarrow was nicknamed 'soldier's woundwort'!",
                "image": "yarrow.png"
            },
            {
                "question": "Which flower represents peace and sympathy?",
                "options": ["White Lily", "Red Rose", "Sunflower", "Tulip"],
                "correct": "White Lily",
                "fact": "White lilies are often used in funerals to symbolize peace!",
                "image": "lily.png"
            },
            {
                "question": "Which flower’s petals are edible and often used in salads?",
                "options": ["Nasturtium", "Rose", "Lily", "Sunflower"],
                "correct": "Nasturtium",
                "fact": "Nasturtium flowers are peppery and colorful!",
                "image": "nasturtium.png"
            },
            {
                "question": "Which flower is named after a famous Dutch painter?",
                "options": ["Van Gogh Sunflower", "Monet Tulip", "Rembrandt Rose", "Da Vinci Lily"],
                "correct": "Van Gogh Sunflower",
                "fact": "Van Gogh famously painted sunflowers, inspiring flower names!",
                "image": "sunflower.png"
            },
            {
                "question": "Which flower is shaped like a bell and often used in weddings?",
                "options": ["Lily of the Valley", "Daisy", "Rose", "Tulip"],
                "correct": "Lily of the Valley",
                "fact": "Tiny bell-shaped flowers, symbolizing humility and sweetness!",
                "image": "lilyofthevalley.png"
            },
            {
                "question": "Which desert flower blooms only after rare heavy rain?",
                "options": ["Desert Mariposa Lily", "Sunflower", "Orchid", "Daisy"],
                "correct": "Desert Mariposa Lily",
                "fact": "Desert flowers can wait years for the right rain to bloom!",
                "image": "desertmariposalily.png"
            },
            {
                "question": "Which flower inspired a famous festival in the Netherlands?",
                "options": ["Tulip", "Rose", "Orchid", "Lily"],
                "correct": "Tulip",
                "fact": "The Tulip Festival celebrates millions of blooming tulips!",
                "image": "tulip.png"
            },
            {
                "question": "Which flower is the official flower of March?",
                "options": ["Daffodil", "Rose", "Lily", "Sunflower"],
                "correct": "Daffodil",
                "fact": "Daffodils symbolize rebirth and new beginnings!",
                "image": "daffodil.png"
            },
            {
                "question": "Which flower is often associated with mystery and rare beauty?",
                "options": ["Black Rose", "Orchid", "Tulip", "Lily"],
                "correct": "Black Rose",
                "fact": "Black roses symbolize mystery and uniqueness!",
                "image": "blackrose.png"
            },
            {
                "question": "Which flower blooms in the shape of a heart?",
                "options": ["Bleeding Heart", "Tulip", "Rose", "Daisy"],
                "correct": "Bleeding Heart",
                "fact": "Bleeding Hearts are loved for their delicate heart shape!",
                "image": "bleedingheart.png"
            },
            {
                "question": "Which flower's seeds are roasted to make a popular snack?",
                "options": ["Sunflower", "Poppy", "Lily", "Rose"],
                "correct": "Sunflower",
                "fact": "Sunflower seeds are rich in healthy fats!",
                "image": "sunflower.png"
            },
            {
                "question": "Which flower symbolizes hope and renewal?",
                "options": ["Snowdrop", "Daisy", "Rose", "Orchid"],
                "correct": "Snowdrop",
                "fact": "Snowdrops are among the first to bloom after winter!",
                "image": "snowdrop.png"
            },
            {
                "question": "Which bright flower is used during Dia de los Muertos in Mexico?",
                "options": ["Marigold", "Rose", "Daisy", "Tulip"],
                "correct": "Marigold",
                "fact": "Marigolds are believed to guide spirits with their vibrant color!",
                "image": "marigold.png"
            },
            {
                "question": "Which flower was once a symbol of wealth and power in Europe?",
                "options": ["Tulip", "Rose", "Lily", "Sunflower"],
                "correct": "Tulip",
                "fact": "The 'Tulip Mania' period saw tulips valued like gold!",
                "image": "tulip.png"
            },
            {
                "question": "Which flower has varieties called 'King Alfred'?",
                "options": ["Daffodil", "Tulip", "Rose", "Daisy"],
                "correct": "Daffodil",
                "fact": "King Alfred daffodils are large and golden yellow!",
                "image": "Daffodil.png"
            },
            {
                "question": "Which flower's roots were used as a love potion ingredient?",
                "options": ["Orchid", "Rose", "Sunflower", "Daisy"],
                "correct": "Orchid",
                "fact": "Ancient Greeks believed orchids had love powers!",
                "image": "orchid.png"
            },
            {
                "question": "Which flower’s name means 'rainbow' in Greek?",
                "options": ["Iris", "Rose", "Daisy", "Tulip"],
                "correct": "Iris",
                "fact": "Iris flowers come in almost every color of the rainbow!",
                "image": "iris.png"
            },
            {
                "question": "Which flower is used to make chamomile tea?",
                "options": ["Chamomile", "Daisy", "Rose", "Sunflower"],
                "correct": "Chamomile",
                "fact": "Chamomile tea is famous for its calming effects!",
                "image": "chamomile.png"
            },
            {
                "question": "Which flower has the nickname 'snow-in-summer'?",
                "options": ["Cerastium", "Daisy", "Sunflower", "Rose"],
                "correct": "Cerastium",
                "fact": "Cerastium blooms tiny white flowers that cover fields!",
                "image": "cerastium.png"
            },
            {
                "question": "Which flower was sacred to the ancient Egyptians?",
                "options": ["Lotus", "Rose", "Daisy", "Tulip"],
                "correct": "Lotus",
                "fact": "Lotuses symbolized rebirth and the sun!",
                "image": "lotus.png"
            },
            {
                "question": "Which flower shares its name with a musical instrument?",
                "options": ["Trumpet Flower", "Rose", "Lily", "Sunflower"],
                "correct": "Trumpet Flower",
                "fact": "Trumpet flowers have large, trumpet-shaped blooms!",
                "image": "trumpetflower.png"
            },
            {
                "question": "Which flower is considered lucky in Ireland?",
                "options": ["Shamrock", "Daisy", "Rose", "Tulip"],
                "correct": "Shamrock",
                "fact": "Shamrocks are three-leafed clovers symbolizing good luck!",
                "image": "shamrock.png"
            },
            {
                "question": "Which flower blooms on cacti and survives deserts?",
                "options": ["Cactus Flower", "Rose", "Tulip", "Daisy"],
                "correct": "Cactus Flower",
                "fact": "Cactus flowers are brilliantly colored and short-lived!",
                "image": "cactusflower.png"
            },
            {
                "question": "Which flower is symbolic of eternal love in many cultures?",
                "options": ["Red Rose", "Sunflower", "Orchid", "Daisy"],
                "correct": "Red Rose",
                "fact": "Red roses are universal symbols of true love!",
                "image": "rose.png"
            },
            {
                "question": "Which flower is a symbol of the zodiac sign Virgo?",
                "options": ["Morning Glory", "Sunflower", "Rose", "Daisy"],
                "correct": "Morning Glory",
                "fact": "Morning glories bloom early and fade quickly!",
                "image": "morningglory.png"
            },
            {
                "question": "Which flower grows wild in the Himalayas and is rare?",
                "options": ["Blue Poppy", "Rose", "Sunflower", "Lily"],
                "correct": "Blue Poppy",
                "fact": "The Himalayan Blue Poppy is a rare and prized flower!",
                "image": "bluepoppy.png"
            },
            {
                "question": "Which flower is associated with secret love in Victorian times?",
                "options": ["Carnation", "Rose", "Tulip", "Daisy"],
                "correct": "Carnation",
                "fact": "Different colors of carnations conveyed secret messages!",
                "image": "carnation.png"
            }
        ]        
    
    }

}

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.size = random.randint(2, 5)
        self.color = color
        self.speed = random.uniform(0.5, 2)
        self.angle = random.uniform(0, math.pi * 2)
        
    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.size -= 0.05
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

class Button:
    def __init__(self, x, y, width, height, text, color=BUTTON_COLOR, hover_color=HOVER_COLOR):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.font = pygame.font.SysFont("Bubblegum sans", 28)
        
    def draw(self, screen):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        pygame.draw.rect(screen, BLACK, self.rect, 2, border_radius=10)
        
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered
        
    def is_clicked(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("KIDS LEARNING ADVENTURE!")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.title_font = pygame.font.Font(None, 48)
        
        # Load sounds
        self.load_sounds()
        
        # Game state
        self.current_game = None
        self.level = 1
        self.score = 0
        self.questions_per_level = 10
        self.total_levels = 10
        self.current_questions = 0
        self.paused = False
        self.game_state = "menu"
        
        # Background particles
        self.particles = []
        for _ in range(50):
            self.add_particle()
    
    def add_particle(self):
        x = random.randint(0, WINDOW_WIDTH)
        y = random.randint(0, WINDOW_HEIGHT)
        color = (
            random.randint(100, 200),
            random.randint(100, 200),
            random.randint(100, 200)
        )
        self.particles.append(Particle(x, y, color))
    
    def load_sounds(self):
        try:
            self.correct_sound = pygame.mixer.Sound("match.wav")
            self.wrong_sound = pygame.mixer.Sound("error.wav")
            self.level_up_sound = pygame.mixer.Sound("achievement.wav")
            pygame.mixer.music.load("background.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        except:
            # Create silent sounds if files not found
            self.correct_sound = pygame.mixer.Sound(buffer=bytearray(44))
            self.wrong_sound = pygame.mixer.Sound(buffer=bytearray(44))
            self.level_up_sound = pygame.mixer.Sound(buffer=bytearray(44))
    
    def load_image(self, image_name):
        """Load and scale an image from the assets folder"""
        try:
            if not image_name:
                return None
            path = os.path.join("images", image_name)
            image = pygame.image.load(path).convert_alpha()
            return image
        except Exception as e:
            print(f"Error loading image {image_name} : {str(e)}")
            return None
        
    def update_background(self):
        # Update background particles
        for particle in self.particles[:]:
            particle.move()
            if particle.size <= 0:
                self.particles.remove(particle)
        
        # Add new particles occasionally
        if random.random() < 0.05:
            self.add_particle()
            
    def draw_background(self):
        # Draw gradient background
        for y in range(WINDOW_HEIGHT):
            # Sky blue gradient
            color = (
                int(135 + (200 - 135) * y / WINDOW_HEIGHT),
                int(206 + (230 - 206) * y / WINDOW_HEIGHT),
                int(250 + (255 - 250) * y / WINDOW_HEIGHT)
            )
            pygame.draw.line(self.screen, color, (0, y), (WINDOW_WIDTH, y))
        
        # Draw particles
        for particle in self.particles:
            particle.draw(self.screen)
    
    def show_menu(self):
        
        # Create menu buttons
        animal_btn = Button(WINDOW_WIDTH//2 - 150, 250, 300, 60, "ANIMAL ZONE")
        fruit_btn = Button(WINDOW_WIDTH//2 - 150, 330, 300, 60, "FRUITS WORLD")
        flower_btn = Button(WINDOW_WIDTH//2 - 150, 410, 300, 60, "FLOWER GARDEN")
        quit_btn = Button(WINDOW_WIDTH//2 - 150, 490, 300, 60, "QUIT GAME", RED, (200, 50, 50))
        running = True        
        while running and self.game_state == "menu":
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Check button clicks
                if animal_btn.is_clicked(mouse_pos, event):
                    self.current_game = "animals"
                    self.reset_game()
                    self.game_state = "playing"
                elif fruit_btn.is_clicked(mouse_pos, event):
                    self.current_game = "fruits"
                    self.reset_game()
                    self.game_state = "playing"
                elif flower_btn.is_clicked(mouse_pos, event):
                    self.current_game = "flowers"
                    self.reset_game()
                    self.game_state = "playing"
                elif quit_btn.is_clicked(mouse_pos, event):
                    pygame.quit()
                    sys.exit()
            
            # Update background
            self.update_background()
            
            # Draw everything
            self.draw_background()
            
            # Draw title
            title = self.title_font.render("KIDS LEARNING ADVENTURE!", True, PURPLE)
            shadow = self.title_font.render("KIDS LEARNING ADVENTURE!", True, BLACK)
            self.screen.blit(shadow, (WINDOW_WIDTH//2 - title.get_width()//2 + 3, 103))
            self.screen.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 100))
            
            # Draw buttons and check hover
            animal_btn.check_hover(mouse_pos)
            fruit_btn.check_hover(mouse_pos)
            flower_btn.check_hover(mouse_pos)
            quit_btn.check_hover(mouse_pos)
            
            animal_btn.draw(self.screen)
            fruit_btn.draw(self.screen)
            flower_btn.draw(self.screen)
            quit_btn.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(FPS)
    
    def reset_game(self):
        self.level = 1
        self.score = 0
        self.current_question = 0
        total_questions = len(GAME_DATA[self.current_game]["questions"])
        self.total_levels = total_questions // self.questions_per_level
        if total_questions % self.questions_per_level != 0:
            self.total_levels += 1

    def generate_questions(self):
        """Get questions for the current level"""
        all_questions = GAME_DATA[self.current_game]["questions"]
        questions_per_level = 10
        start_index = (self.level - 1) * questions_per_level
        end_index = start_index + questions_per_level
        if end_index > len(all_questions):
            end_index = len(all_questions)

        return all_questions[start_index:end_index]
    
    def show_pause_menu(self):
        self.paused = True
        
        # Create pause menu buttons
        resume_btn = Button(WINDOW_WIDTH//2 - 150, 300, 300, 60, "RESUME GAME", GREEN, (50, 200, 50))
        menu_btn = Button(WINDOW_WIDTH//2 - 150, 380, 300, 60, "MAIN MENU")
        quit_btn = Button(WINDOW_WIDTH//2 - 150, 460, 300, 60, "QUIT GAME", RED, (200, 50, 50))
        
        while self.paused:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Check button clicks
                if resume_btn.is_clicked(mouse_pos, event):
                    self.paused = False
                elif menu_btn.is_clicked(mouse_pos, event):
                    self.paused = False
                    self.game_state = "menu"
                    return
                elif quit_btn.is_clicked(mouse_pos, event):
                    pygame.quit()
                    sys.exit()
            
            # Create semi-transparent overlay
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            self.screen.blit(overlay, (0, 0))
            
            # Draw pause title
            title = self.title_font.render("GAME PAUSED", True, WHITE)
            self.screen.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 200))
            
            # Draw buttons and check hover
            resume_btn.check_hover(mouse_pos)
            menu_btn.check_hover(mouse_pos)
            quit_btn.check_hover(mouse_pos)
            
            resume_btn.draw(self.screen)
            menu_btn.draw(self.screen)
            quit_btn.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(FPS)
    
    def show_reward_animation(self):
        start_time = time.time()
        reward_particles = []
        
        # Create reward particles
        for _ in range(100):
            x = WINDOW_WIDTH // 2
            y = WINDOW_HEIGHT // 2
            color = (
                random.randint(200, 255),
                random.randint(200, 255),
                random.randint(0, 100)
            )
            reward_particles.append(Particle(x, y, color))
        
        while time.time() - start_time < 3:  # 3 second animation
            self.update_background()
            self.draw_background()
            
            # Update and draw reward particles
            for p in reward_particles[:]:
                p.move()
                if p.size > 0:
                    p.draw(self.screen)
                else:
                    reward_particles.remove(p)
            
            # Draw level complete text
            text = self.title_font.render(f"Level {self.level} Complete!", True, WHITE)
            shadow = self.title_font.render(f"Level {self.level} Complete!", True, BLACK)
            self.screen.blit(shadow, (WINDOW_WIDTH//2 - text.get_width()//2 + 3, WINDOW_HEIGHT//2 + 3))
            self.screen.blit(text, (WINDOW_WIDTH//2 - text.get_width()//2, WINDOW_HEIGHT//2))
            
            pygame.display.flip()
            self.clock.tick(FPS)
    
    def play_game(self):
        while self.game_state == "playing" and self.level <= self.total_levels:
            questions = self.generate_questions()

            if not questions:
                print(f"no more questions in level{self.level}")
                self.level += 1
            
            for q in questions:
                if self.game_state != "playing":
                    break
                    
                result = self.show_question(q)
                if not result:  # User went back to menu
                    return
                
                self.current_question += 1
                
                if self.current_question >= self.questions_per_level:
                    self.level_up_sound.play()
                    self.show_reward_animation()
                    self.level += 1
                    self.current_question = 0
                    break

        # Game completed
        if self.level > self.total_levels:
            self.show_game_complete()
            self.game_state = "menu"
    
    def show_game_complete(self):
        # Create completion screen buttons
        menu_btn = Button(WINDOW_WIDTH//2 - 150, 400, 300, 60, "Main Menu")
        
        waiting = True
        while waiting:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if menu_btn.is_clicked(mouse_pos, event):
                    waiting = False
            
            self.update_background()
            self.draw_background()
            
            # Draw completion messages
            title = self.title_font.render(f"{GAME_DATA[self.current_game]['name']} Completed!", True, WHITE)
            shadow = self.title_font.render(f"{GAME_DATA[self.current_game]['name']} Completed!", True, BLACK)
            self.screen.blit(shadow, (WINDOW_WIDTH//2 - title.get_width()//2 + 3, 203))
            self.screen.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 200))
            
            score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
            score_shadow = self.font.render(f"Final Score: {self.score}", True, BLACK)
            self.screen.blit(score_shadow, (WINDOW_WIDTH//2 - score_text.get_width()//2 + 2, 273))
            self.screen.blit(score_text, (WINDOW_WIDTH//2 - score_text.get_width()//2, 270))
            
            # Draw button and check hover
            menu_btn.check_hover(mouse_pos)
            menu_btn.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(FPS)
    
    def generate_questions(self):
        """Get questions for the current level"""
        all_questions = GAME_DATA[self.current_game]["questions"]
        questions_per_level = 10
        start_index = (self.level - 1) * questions_per_level
        end_index = start_index + questions_per_level
        if end_index > len(all_questions):
            end_index = len(all_questions)
        return all_questions[start_index:end_index]
        
    
    def show_question(self, question):
        running = True
        option_buttons = []
    
    # Load image with error handling
        image = None
        if "image" in question and question["image"]:
            try:
            # Try loading from images folder first, then current directory
                image_path = os.path.join("images", question["image"])
                if not os.path.exists(image_path):
                    image_path = question["image"]  # Fallback to direct path
            
                image = pygame.image.load(image_path).convert_alpha()
                image = pygame.transform.scale(image, (250, 250))  # Standard size
            except Exception as e:
                print(f"Error loading image {question['image']}: {e}")
                image = None

    # Create option buttons - positioned on left side
        for i, option in enumerate(question["options"]):
            btn = Button(100, 250 + i * 70, 300, 60, option)
            option_buttons.append(btn)

    # Create control buttons
        back_btn = Button(20, 20, 100, 40, "Back", GRAY, (180, 180, 180))
        pause_btn = Button(WINDOW_WIDTH - 120, 20, 100, 40, "Pause", GRAY, (180, 180, 180))

        while running and self.game_state == "playing":
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Check back button
                if back_btn.is_clicked(mouse_pos, event):
                    self.game_state = "menu"
                    return False
            
            # Check pause button
                if pause_btn.is_clicked(mouse_pos, event):
                    self.show_pause_menu()
                    if self.game_state != "playing":
                        return False
            
            # Check answer options
                for i, btn in enumerate(option_buttons):
                    if btn.is_clicked(mouse_pos, event):
                        selected = question["options"][i]
                        if selected == question["correct"]:
                            self.correct_sound.play()
                            self.score += 10
                            feedback = "Correct!"
                            color = GREEN
                        else:
                            self.wrong_sound.play()
                            feedback = f"Wrong! Correct answer: {question['correct']}"
                            color = RED
                    
                        self.show_feedback(feedback, question["fact"], color)
                        running = False
                        break

        # Update and draw background
            self.update_background()
            self.draw_background()

        # Draw question box (single instance)
            question_rect = pygame.Rect(50, 100, WINDOW_WIDTH - 100, 120)
            pygame.draw.rect(self.screen, (240, 240, 240), question_rect, border_radius=10)
            pygame.draw.rect(self.screen, BLACK, question_rect, 2, border_radius=10)

        # Draw question text (only once)
            question_lines = self.wrap_text(question["question"], self.font, WINDOW_WIDTH - 150)
            for i, line in enumerate(question_lines):
                text_surface = self.font.render(line, True, BLACK)
                self.screen.blit(text_surface, (70, 120 + i * 30))

        # Draw image right of options if available
            if image:
                image_x = 450  # Right side position
                image_y = 250  # Aligned with first option
                image_rect = pygame.Rect(image_x, image_y, 280, 280)
            
            # Draw frame
                pygame.draw.rect(self.screen, WHITE, image_rect.inflate(20, 20), border_radius=10)
                pygame.draw.rect(self.screen, BLACK, image_rect.inflate(20, 20), 2, border_radius=10)
            
            # Draw image
                self.screen.blit(image, image_rect)

        # Draw buttons
            back_btn.check_hover(mouse_pos)
            pause_btn.check_hover(mouse_pos)
            back_btn.draw(self.screen)
            pause_btn.draw(self.screen)

        # Draw score and level
            score_text = self.font.render(f"Score: {self.score} | Level: {self.level}", True, BLACK)
            self.screen.blit(score_text, (WINDOW_WIDTH//2 - score_text.get_width()//2, 30))

        # Draw option buttons
            for btn in option_buttons:
                btn.check_hover(mouse_pos)
                btn.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

        return True
    
    def show_feedback(self, feedback, fact, color):
        """Show feedback for 2 seconds"""
        start_time = time.time()
        
        while time.time() - start_time < 2:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.update_background()
            self.draw_background()
            
            # Draw feedback box
            feedback_rect = pygame.Rect(WINDOW_WIDTH//2 - 250, WINDOW_HEIGHT//2 - 100, 500, 200)
            pygame.draw.rect(self.screen, WHITE, feedback_rect, border_radius=15)
            pygame.draw.rect(self.screen, BLACK, feedback_rect, 2, border_radius=15)
            
            # Draw feedback text
            feedback_text = self.font.render(feedback, True, color)
            self.screen.blit(feedback_text, (WINDOW_WIDTH//2 - feedback_text.get_width()//2, WINDOW_HEIGHT//2 - 70))
            
            # Draw fact text (with word wrapping)
            fact_text = self.wrap_text(fact, self.small_font, 450)
            for i, line in enumerate(fact_text):
                text_surface = self.small_font.render(line, True, BLACK)
                self.screen.blit(text_surface, (WINDOW_WIDTH//2 - text_surface.get_width()//2, WINDOW_HEIGHT//2 - 30 + i * 25))
            
            pygame.display.flip()
            self.clock.tick(FPS)
    
    def wrap_text(self, text, font, max_width):
        """Wrap text to fit within a specified width"""
        words = text.split(' ')
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_width = font.size(test_line)[0]
            
            if test_width <= max_width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    def run(self):
        while True:
            if self.game_state == "menu":
                self.show_menu()
            elif self.game_state == "playing":
                self.play_game()


if __name__ == "__main__":
    game = Game()
    game.run()