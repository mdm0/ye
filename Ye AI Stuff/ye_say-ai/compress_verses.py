import csv
import random
import re

redact_words = ['slave', 'nigga']

verses = open("Kanye West Lyrics.txt", "r")

def remove_brackets(file, output):
    read_lines = file.readlines()
    write_file = open(output, "w")
    for lines in read_lines:
        if "[" not in lines and "]" not in lines:
            if lines != "\n":
                    write_file.write(lines)
    write_file.close()

remove_brackets(verses, "KW_VerseOnly.txt")

verses = open("KW_VerseOnly.txt", "r")

def compress_file(file, output):
    read_lines = file.readlines()
    write_file = open(output, "w")
    all_lines = []
    count = 0 
    for lines in read_lines:
        if lines not in all_lines:
            if "(" not in lines and ")" not in lines:
                    all_lines.append(lines)
                    count += 1
        if count >= 1:
            pass
    for lines in all_lines:
        lines=str(lines)
        write_file.write(lines)
    
compress_file(verses, "verses_compressed.txt")
verses = open("verses_compressed.txt", "r")

def convert_csv(file, output):
    output = open(output, "w")
    file = file.readlines()
    header = ['name', 'line']
    csv_writer = csv.writer(output, delimiter=",")
    csv_writer.writerow(header)
    for lines in file:
        row = ['Kanye', lines]
        csv_writer.writerow(row)
                
convert_csv(verses, "verses.csv")
