
import numpy as np;
import math, time;
class TestAStar():

	def __init__(self, callback):
		self.points = [[]];
		self.passedNodes = [];
		self.callback = callback;
		self.paused = False;
		self.running = True;

	def setPaused(self, paused):
		self.paused = paused;

	def setRunning(self, running):
		self.running = running;
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
	
	def getPassedNodes(self):
		return self.passedNodes;

	def findNextNode(self, location, passedNodes):
		# This method will route from location to start and pick the
		# next node closest to start out of the startlocations neighbours
		neighBours = self.getNeighbours(passedNodes[len(passedNodes)-1]);
		minStartDistance = 10000000.0;
		minGoalDistance = 10000000.0;
		minTotalDistance = 10000000.0;
		minTotalOfAll = 10000000.0;
		minNeighBour = None;
		for neighBour in neighBours:
			
			neighbourDistanceToStart = self.getStartWeight(neighBour);
			# Checks if this is the node closest to start
			if(neighbourDistanceToStart < minStartDistance):
				minStartDistance = neighbourDistanceToStart;
			
			# Checks if this is the node closest to the goal
			neighBourDistanceToGoal = self.getGoalDistance(neighBour);
			if(neighBourDistanceToGoal < minGoalDistance):
				minGoalDistance = neighBourDistanceToGoal;
			
			# Checks if the total is the lowest total, then it is the preferred choice
			minTotalDistance = minStartDistance + minGoalDistance;
			if(minTotalDistance < minTotalOfAll):
				minTotalOfAll = minTotalDistance;
				minNeighBour = neighBour;
			print('Neighbour ' + str(neighBour) + ' Goal distance=' + str(minTotalDistance));
		print('Selected: ' + str(minNeighBour));
		return minNeighBour;

	def getNeighbours(self, loc):
		neighbours = [];
		distances = [];
		lowN = 0; highN = 3;
		lowK = 0; highK = 3;
		
		if(loc[0][0] == 0):
			#left border
			lowN = 1;
		if(loc[0][0] == self.maxHeight-1):
			#bottom border
			highN = 2;
		if(loc[0][1] == 0):
			#top border
			lowK = 1;
		if(loc[0][1] < self.maxWidth):
			#right border
			highK = 2;
		x = [[1, 1, 1],
			[1, 0, 1],
			[1, 1, 1]];
			
		for n in range(lowN,highN):
			for k in range(lowK,highK):
				a = loc[0][0] + n - 1;
				b = loc[0][1] + k - 1;
				newPoint = [a, b];
				distance = math.sqrt(a**2 + b**2);
				nodeWasPassed = False;
				for node in self.passedNodes:
					if(newPoint == node[0]):
						nodeWasPassed = True;
				if( x[n][k] == 1 and not nodeWasPassed):
					if(self.points[b][a] == '0' or self.points[b][a] == 'G'):
						print('n=' + str(n) + ' k=' + str(k));
						print('b=' + str(b) + ' a=' + str(a));
						print('points[b][a]=' + str(self.points[b][a]));
						print('newPoint=' + str(newPoint));
						neighbours.append([newPoint, distance]);
		return neighbours;

	def getStartWeight(self, location):
		totalWeight = 0;
		for node in self.passedNodes:
			totalWeight = totalWeight + node[1];
		return totalWeight;

	def getGoalDistance(self, location):
		current = [];
		current.append(location[0][0]);
		current.append(location[0][1]);
		
		distance = 0;
		
		while(not current == self.endPoint):
			#print(' current:' + str(current)  + ' endPoint:' + str(self.endPoint))
			
			if(current[0] < self.endPoint[0]):
				current[0] = current[0] + 1;
				if((current[1] > self.endPoint[1])):
					current[1] = current[1] - 1;
					distance = distance + 1/math.sqrt(2);

				elif((current[1] < self.endPoint[1])):
					current[1] = current[1] + 1;
					distance = distance + 1/math.sqrt(2);
				else:
					distance = distance + 1;

			elif(current[0] > self.endPoint[0]):
				current[0] = current[0] - 1;
				if((current[1] > self.endPoint[1])):
					current[1] = current[1] - 1;
					distance = distance + 1/math.sqrt(2);
				elif((current[1] < self.endPoint[1])):
					current[1] = current[1] + 1;
					distance = distance + 1/math.sqrt(2);
				else:
					distance = distance + 1;

			elif(current[0] == self.endPoint[0]):
				if(current[1] < self.endPoint[1]):
					current[1] = current[1] + 1;
					distance = distance + 1;
				if(current[1] > self.endPoint[1]):
					current[1] = current[1] - 1;
					distance = distance + 1;

			elif(current[1] == self.endPoint[1]):
				if(current[0] < self.endPoint[0]):
					current[0] = current[0] + 1;
					distance = distance + 1;
				if(current[0] > self.endPoint[0]):
					current[0] = current[0] - 1;
					distance = distance + 1;
			elif(current == self.endPoint):
				distance = distance;
				time.sleep(1000000);
		return distance;

	def fullPath(self, passedNodes, currentNode):
		# This method will return a list of nodes bet
		pass;

	## Method for calculation of shortest path top
	def findShortestPath(self, startPoint, endPoint):
		print('Shortest ');
		width = len(self.points);
		height = len(self.points[0]);
		if(self.dataLoaded):
			totalLength = len(self.points) * len(self.points[0]);
			x = 0;
			print(totalLength);
			currentNode = [self.startPoint, 0.0];
			testing = 0;
			self.passedNodes.append(currentNode);
			while(len(self.passedNodes) < totalLength and self.running):
				
				currentNode = self.findNextNode(self.endPoint, self.passedNodes);
				self.passedNodes.append(currentNode);
				print('Passed nodes: ' + str(self.passedNodes));
				if(currentNode == self.endPoint):
					#return fullPath(passedNodes, currentNode);
					print('FOUND IT!');
					return;
				else:
					print('Passing: ' + str(currentNode) + ' started at: ' + str(self.startPoint) + ' goal is: ' + str(self.endPoint));
				time.sleep(0.2);
				self.callback.update();
				while(self.paused):
					time.sleep(1);
					pass;
	## Other help mehods
