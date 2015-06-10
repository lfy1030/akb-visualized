import os
import sys
import bs4
import re

import plotly.plotly as py
from plotly.graph_objs import *

mapping = {
	"C":12,
	"D":14,
	"E":16,
	"F":17,
	"G":19,
	"A":21,
	"B":23
}

#change file name
fn = "14 Iiwake_Maybe"
path = os.path.expanduser("~/Documents/GitHub/akb38/data/" + fn + ".xml")
soup = bs4.BeautifulSoup(open(path, "r", encoding='utf-8'))
notes = soup.findAll("note")
print(len(notes))

round1 = []
counter = 0
pos = 0
for n in notes:
	#checking if start of phrase and add position of note 
	rest = n.findAll("rest")
	if(len(rest)<=0):
		single = []
		marker = n.findAll("up-bow")
		if(len(marker)>0):
			counter += 1
			pos = 0
		else:
			pos += 1
		single.append(pos)
		single.append(counter)
		#get the pitch
		p1 = str(n.select("step")) 
		p2 = str(n.select("octave"))
		srch1 = re.search( r'<step>(.*?)</step>', p1, re.M|re.I)
		srch2 = re.search( r'<octave>(.*?)</octave>', p2, re.M|re.I)
		p_a = 0
		p_b = 0
		if(srch1):
			p_a = int(mapping[str(srch1.group(1))])
		if(srch2):
			p_b = (int(srch2.group(1))-1)*12
		single.append(p_a + p_b)
		#get the rhythm
		d = str(n.select("duration"))
		srch3 = re.search( r'<duration>(.*?)</duration>', d, re.M|re.I)
		single.append(int(srch3.group(1)))
		#add to song
		round1.append(single)

print(round1)
#put the notes into phrases then into song
song = []
phrase = []
for i, v in enumerate(round1):
	if(i == 0):
		phrase.append(v)
	else:
		if(round1[i-1][1] == v[1]): 
			phrase.append(v)
		else:
			song.append(phrase)
			phrase = []
			phrase.append(v)

song.append(phrase)
print(song)
#do the calculations

#for the traces
dataset = []

for i, phrase in enumerate(song):
	data_x = []
	data_y = []
	midi_offset = phrase[0][2]
	notes_total = sum(i[3] for i in phrase)
	notes_buffer = 0
	for note in phrase:
		data_y.append(note[2]-midi_offset)
		notes_buffer = notes_buffer+note[3]
		data_x.append(notes_buffer)

	trace = Scatter(
		x=data_x,
	  	y=data_y,
	   	mode='lines+markers',
	    name=str(i),
	    line=Line(
	        shape='spline'
	    )
	)

	dataset.append(trace)

data = Data(dataset)
layout = Layout(
    legend=Legend(
        y=0.5,
        font=Font(
            size=16
        ),
        yref='paper'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename= fn)