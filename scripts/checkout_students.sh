#!/bin/sh
[ ! -d ~/output ] && mkdir output
sqlite3 TimeTrack4237.db < scripts/checkout_students.sql > output/checkout_students.out