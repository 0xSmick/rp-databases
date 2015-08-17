# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:15:21 2015

@author: sheldon
"""

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    
    c.execute("UPDATE population SET population = 9000000 WHERE city = 'New York City'")
    c.execute("DELETE FROM population WHERE city = 'Boston'")
    
    print "\nNEW DATA:\n"
    
    c.execute("SELECT * FROM population")
    
    rows = c.fetchall()
    
    for r in rows:
        print r[0], r[1], r[2]