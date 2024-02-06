#!/usr/bin/env python3
import sqlite3

CONN = sqlite3.connect('hatch-match.db')
CURSOR = CONN.cursor()