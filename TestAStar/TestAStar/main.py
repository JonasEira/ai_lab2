from TestAStar import TestAStar;
from GameUI import GameUI;
def main():
	print('Starting AI-game');
	gameUI = GameUI();
	testAStar = TestAStar(gameUI);
	testAStar.readMap('Map3.txt');
	gameUI.addModel(testAStar, 'testAStar');
	gameUI.startUI();
	#print(testAStar.getDataPoints());

if(__name__ == '__main__'):
	main();
