#!/usr/bin/env python

# Recording soundcard output
# https://ubuntuincident.wordpress.com/2011/03/26/recording-soundcard-output/
# Laszlo Szathmary, 2011 (jabba.laci@gmail.com)

from termcolor import colored

def color(text, color, attrs=[]):
    return colored(text, color, attrs=attrs)

##############################################################################

if __name__ == "__main__":
    print color('Everything is going perfectly fine.', 'green')
    print color('Reactor meltdown alert! Leave the building immediately!', 'red')
    print color('[ OK ]', 'cyan')
