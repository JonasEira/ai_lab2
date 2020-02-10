from TestAStar import TestAStar;
from GameUI import GameUI;
def main():
	print('Starting AI-game');
	var = TestAStar();
	gameUI = GameUI();
	testAStar = TestAStar();
	testAStar.readMap('Map1.txt');
	gameUI.addModel(testAStar, 'testAStar');
	gameUI.startUI();
	testAStar.findShortestPath(testAStar.getStartPoint(), testAStar.getEndPoint());
	#print(testAStar.getDataPoints());

if(__name__ == '__main__'):
	main();
