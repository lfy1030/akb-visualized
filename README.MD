# AKB Visualized

## Overview

This project aims to programmatically identify melodic patterns and/or rhythmic patterns in the singles by top-selling female pop music group AKB48. Using the data, visualizations and computational compositions can then be developed.

## Stage 1: Transcription

The choruses of selected AKB48 singles were transcribed by ear using MuseScore and output into both MuseScore and MusicXML formats. The choruses have all been transposed to either A minor or C major to avoid unecessary workaround related to keys since in this case what matters is the relative intervals between notes and not the absolute values of the notes. 

## Stage 2: Data Crunching

The MusicXML is parsed in python with [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Stage 3: Graphing

The music data is visualized with [plot.ly](https://plot.ly/) in python

## Stage 4: Presentation

Python is used to generate some of the html files used in the final project website