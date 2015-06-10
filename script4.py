import os
import sys
import csv

head = """
<!DOCTYPE html>
<html lang="en">
  <head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
	<meta name="description" content="">
	<meta name="author" content="">

	<title>AKB Visualized</title>

	<!-- Bootstrap core CSS -->
	<link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
	<!-- Bootstrap theme -->
	<link href="http://getbootstrap.com/dist/css/bootstrap-theme.min.css" rel="stylesheet">

	<!-- Custom styles for this template -->
	<link href="http://getbootstrap.com/examples/theme/theme.css" rel="stylesheet">
  </head>

  <body role="document">

	<!-- Fixed navbar -->
	<nav class="navbar navbar-inverse navbar-fixed-top">
	  <div class="container">
		<div class="navbar-header">
		  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
			<span class="sr-only">Toggle navigation</span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
		  </button>
		  <a class="navbar-brand" href="http://akb-visualized.hikari-project.com/">AKB Visualized</a>
		</div>
		<div id="navbar" class="navbar-collapse collapse">
		  <ul class="nav navbar-nav">
			<li><a href="http://akb-visualized.hikari-project.com/">Home</a></li>
			<li><a href="http://akb-visualized.hikari-project.com/vis1.html">2D View</a></li>
			<li><a href="http://akb-visualized.hikari-project.com/vis2.html">3D View</a></li>
			<li class="active"><a href="http://akb-visualized.hikari-project.com/table.html">Directory</a></li>
			<li><a href="https://github.com/lfy1030/akb-visualized">GitHub</a></li>
		  </ul>
		</div><!--/.nav-collapse -->
	  </div>
	</nav>

	<div class="container theme-showcase" role="main">

	  <div class="page-header">
		<h1>Song Directory</h1>
		<p>This shows the graph for each song. Click for the interactive version! The title links to the reference used for transcribing the song</p>
	  </div>

		<div class="col-md-6">
		  <table class="table table-striped">
			<thead>
			  <tr>
			  	<th>#</th>
				<th>Title</th>
				<th>Title(Japanese)</th>
				<th>Year</th>
				<th>Graph</th>
			  </tr>
			</thead>
			<tbody>
"""
tail = """

			</tbody>
		  </table>
		</div>
	  </div>

   
	</div> <!-- /container -->


	<!-- Bootstrap core JavaScript
	================================================== -->
	<!-- Placed at the end of the document so the pages load faster -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
	<script src="http://getbootstrap.com/dist/js/bootstrap.min.js"></script>
	<script src="http://getbootstrap.com/assets/js/docs.min.js"></script>
  </body>
</html>


"""

target = open("table.html", "w", encoding='utf-8')
target.write(head)

path = os.path.expanduser("~/Documents/GitHub/akb/songs.csv")
with open(path, 'r', encoding='utf-8') as f:
	reader = csv.reader(f)
	counter = 1 
	for row in reader:
		#start row
		target.write("<tr>\n")
		#number
		target.write("<td>%s</td>\n" % str(counter))
		#title
		target.write("<td><a href=\"%s\" target=\"_blank\">%s</a></td>\n" % (row[3], row[0]))
		#japanese title
		target.write("<td>%s</td>\n" % row[1])
		#year
		target.write("<td>%s</td>\n" % row[2])
		#graph
		target.write("<td><a href=\"%s\" target=\"_blank\"><img src=\"%s.png\" alt=\"Graph\" style=\"width:490px;height:350px;\"></a></td>" % (row[4], row[4]))
		#end row
		target.write("</tr>\n")
		counter += 1

target.write(tail)
target.close()
f.close()
