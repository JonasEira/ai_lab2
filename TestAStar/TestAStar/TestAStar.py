
import numpy as np;
import math;
class TestAStar():

	def __init__(self):
		self.points = [[]];

	## This method will read the mapinformation
	##
	def readMap(self, mapLocation):
		self.maxWidth = 0;
		self.maxHeight = 0;
		f=open(mapLocation, "r");
		try:
			data = f.read();
		except FileNotFoundError as fnfe:
			print('File not found');
			return;
		except Exception as e:
			print('Everything else went wrong');
			return;

		column = 0;
		row = 0;
		for character in data:
			if(character == '\n'):
				row = row + 1;
				self.points.append([]);
				column = 0;
				if(self.maxWidth < column):
					self.maxWidth = column;
			else:
				self.points[row].append(character);
				column = column + 1;
				if(character == 'S'):
					self.startPoint = [row, column];
				if(character == 'G'):
					self.endPoint = [row, column];

		self.maxHeight = row;
		self.dataLoaded = True;
	
	##	This method will return the map datapoints

	def getStartPoint(self):
		return self.startPoint;

	def getEndPoint(self):
		return self.endPoint;

	def getDataPoints(self):
		return self.points;
	
	def getRoute(self):
		return self.passedNodes;

	def findNextNode(self, location, passedNodes):
		# This method will route from location to start and pick the
		# next node closest to start out of the startlocations neighbours
		neighBours = self.getNeighbours(passedNodes[len(passedNodes)-1]);
		minDistance = 10000000.0;
		for neighBour in neighBours:
			neighbourDistanceToStart = self.getStartWeight(neighBour, self.passedNodes);
			neighBourDistanceToGoal = self.getGoalWeight(neighbour);
			if(minDistance >= neighbourDistanceToStart):
				minDistance = neighbourDistanceToStart;
				minNeighBour = neighBour;
		return minNeighBour;

	def getNeighbours(self, loc):
		neighbours = [];
		lowN = 0; highN = 3;
		lowK = 0; highK = 3;
		
		if(loc[0] == 0):
			#left border
			lowN = 1;
		if(loc[0] == self.maxHeight-1):
			#bottom border
			highN = 2;
		if(loc[1] == 0):
			#top border
			lowK = 1;
		if(loc[1] < self.maxWidth):
			#right border
			highK = 2;
		x = [[1, 1, 1],
			[1, 0, 1],
			[1, 1, 1]];
			
		for n in range(lowN,highN):
			for k in range(lowK,highK):
				newPoint = [loc[0] + n - 1, loc[1] + k - 1];
				if( x[n][k] == 1 and (newPoint not in self.passedNodes)):
					print('n=' + str(n) + ' k=' + str(k));
					neighbours.append(newPoint);
		return neighbours;

	def getStartWeight(self, location, passedNodes):
		return len(passedNodes);

	def getGoalWeight(self, location):


	def fullPath(self, passedNodes, currentNode):
		# This method will return a list of nodes bet
		pass;

	## Method for calculation of shortest path top
	def findShortestPath(self, startPoint, endPoint):
		print('Shortest ');
		width = len(self.points);
		height = len(self.points[0]);
		wPoints = np.zeros((width, height));
		wPoints[self.startPoint[0],self.startPoint[1]] = 1.0;
		self.passedNodes = [];
		print(wPoints);
		if(self.dataLoaded):
			totalLength = len(self.points) * len(self.points[0]);
			x = 0;
			print(totalLength);
			currentNode = self.startPoint;
			testing = 0;
			self.passedNodes.append(currentNode);
			while(len(self.passedNodes) < totalLength):
				currentNode = self.findNextNode(self.endPoint, self.passedNodes);
				self.passedNodes.append(currentNode);
				if(currentNode == self.endPoint):
					#return fullPath(passedNodes, currentNode);
					print('FOUND IT!');
				else:
					print('Passing: ' + str(currentNode) + ' started at: ' + str(self.startPoint));
	## Other help mehods
