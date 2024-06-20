# EPIC Campus Server Room Thermometer 

This project displays the current temperature reading of  a DHT11 sensor connected to a Raspberry Pi in the EPIC Campus server room. It cycles through a random view using the `pygame` library every 30 seconds. 

## How to Run
Download the directory and install `pygame`, `opencv`, and Adafruit's [DHT library for CircuitPython](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup). Run the programm with `python therm_variants.py`. 

## Displays
This is a list of all possible temperature display windows. 

### Classic Display
![classic](https://github.com/gormes-EPIC/thermometer/assets/134316348/8bd66990-c26e-4dab-9f7e-413e9628564f)

### Comic Display
![comicsans](https://github.com/gormes-EPIC/thermometer/assets/134316348/a5dd3210-a879-4644-abab-ec9ae0913a78)

### Console Display
![console](https://github.com/gormes-EPIC/thermometer/assets/134316348/9c2769e0-fe94-4246-9c07-cec7184d931c)

### Digital Display
![digital](https://github.com/gormes-EPIC/thermometer/assets/134316348/5b1b3a18-8f41-451a-8aa1-98fe3309f9cd)

### Galaga Display - E.Y. 2024
![galaga](https://github.com/gormes-EPIC/thermometer/assets/134316348/ff984fe7-0cd5-4890-bf7f-ececb522be7e)

### Lovelace Display
![lovelace](https://github.com/gormes-EPIC/thermometer/assets/134316348/10513ec9-518c-4032-abbb-582bb3d588b2)

### Medieval Display
![medieval](https://github.com/gormes-EPIC/thermometer/assets/134316348/b48049de-7f6c-4d62-8a13-8b5a10593499)

### Oregon Display
![oregon](https://github.com/gormes-EPIC/thermometer/assets/134316348/7adc48ed-71e9-4eea-bf3f-66d545dd93e1)

### Pacman Display
![pacman](https://github.com/gormes-EPIC/thermometer/assets/134316348/fcbf15d4-d685-422b-bba7-86d95e6a056a)

### Seventies Display
![seventies](https://github.com/gormes-EPIC/thermometer/assets/134316348/97528186-27d4-4790-8d4f-97fc9f7e99f1)

### Star Wars Display
![starwars](https://github.com/gormes-EPIC/thermometer/assets/134316348/6e82e1ef-7cec-49ed-9b0f-6d6585a66f09)

### Tetris Display - J.P. 2024
![tetris](https://github.com/gormes-EPIC/thermometer/assets/134316348/f63df171-59a2-40c8-9422-d3767e209f4b)

## Add a Display

Want to add a display? Create a Python function using pygame for a 1024 by 600 pixel screen. Your function should accept at least one argument `temp`, which is the current temperature in the room. Once your design is complete, create a new branch on the project and upload your code and assets for review!

## List of Contributors
Gwyneth Ormes
J.P. - 2024
E.Y. - 2024

These are the font available by default. You must include an addition `.ttf` file if you want to use another font: `'dejavuserif', 'urwbookman', 'dejavusansmono', 'pibotocondensed', 'liberationmono', 'nimbusmonops', 'notosansmono', 'freesans', 'p052', 'dejavusans', 'nimbussans', 'liberationsans', 'nimbussansnarrow', 'freeserif', 'c059', 'quicksandlight', 'freemono', 'pibotolt', 'z003', 'urwgothic', 'd050000l', 'liberationserif', 'piboto', 'nimbusroman', 'cantarell', 'droidsansfallback', 'quicksand', 'yaheiconsolashybrid', 'quicksandmedium', 'standardsymbolsps', 'notomono'`
