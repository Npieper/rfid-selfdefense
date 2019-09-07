#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sqlite3


reader = SimpleMFRC522()

try:
        name = input('Name:')
        print("Now place your tag to write")
        reader.write(name)
        print("Written")

        vorname = input('Vorname:')
        bday = input('Geburtsdatum:')
        geburtsort = input('Geburtsort:')
        nationalitaet = input('Nationalitaet:')
        beruf = input('Beruf:')
        strasse = input('Strasse:')
        plz = input('Plz:')
        telefon = input('Telefon:')
        email = input('Email:')

        conn = sqlite3.connect('timetracking.db')
        c  = conn.cursor()

        c.execute("INSERT INTO user VALUES('{}', '{}', '{}', '{}','{}','{}','{}','{}','{}','{}','{}')".format(id, name, vorname, bday, geburtsort,nationalitaet,beruf,strasse,plz,telefon,email))

        conn.commit()
        conn.close()




finally:
        GPIO.cleanup()
