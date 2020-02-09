
class TestAStar():

	def __init__(self):
		self.points = [[]];

	## This method will read the mapinformation
	##
	def readMap(self, mapLocation):
		f=open(mapLocation, "r");
		try:
			data = f.read();
		except FileNotFoundError as fnfe:
			print('File not found');
		except Exception as e:
			print('Everything else went wrong');

		column = 0;
		row = 0;
		for character in data:
			if(character == '\n'):
				row = row + 1;
				self.points.append([]);
				column = 0;
			else:
				self.points[row].append(character);
				column = column + 1;
				if(character == 'S'):
					self.startPoint = [row, column];
		
	
	##	This method will return the map datapoints

	def getDataPoints(self):
		return self.points;
	
	## Method for calculation of shortest path top

	## Other help methods
