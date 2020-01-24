#!/bin/sh
[ ! -d ~/output ] && mkdir output
exec > output/checkout_students_$(date +%Y_%m_%d).out                                                                      
exec 2>&1
/usr/bin/sqlite3 TimeTrack4237.db < scripts/checkout_students.sql