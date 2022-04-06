import pygame;
from pygame.math import Vector2 as vector;
import time;

class GameUI(object):
    def __init__(self):
        self.models = {}
        self.pause = False;

    def addModel(self, model, name):
        self.models[name] = model;

    def startUI(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        running = True;
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quit command received')
                    running = False;
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        model = self.models['testAStar'];
                        model.findShortestPath(model.getStartPoint(), model.getEndPoint());
                    if event.key == pygame.K_SPACE:
                        self.pause = not self.pause;
                        model = self.models['testAStar'];
                        model.setPaused(self.pause);
                    if event.key == pygame.K_ESCAPE:
                        model = self.models['testAStar'];
                        model.setRunning(False);
                        running = False;
                time.sleep(0.05);
            self.update();

    def drawLine(self, x1, y1, x2, y2, r, g, b):
        color = pygame.Color(r, g, b);
        start = vector(x1, y1);
        end = vector(x2, y2);
        pygame.draw.line(self.screen, color, start, end, width =  1);

    def drawRect(self, x, y, w, h, r, g, b):
        color = pygame.Color(r, g, b);
        area = pygame.Rect(x, y, w, h);
        pygame.draw.rect(self.screen, color, area, 1);

    def update(self):
        self.drawGameSurface();
        self.drawPassedNodes(); #Debug
        #self.drawNodesToGoal();
        pygame.display.update();

    
    #def drawNodesToGoal(self):
    #    index = 0;
    #    [width, height] = pygame.display.get_surface().get_size()
    #    bSize = height / len(self.models['testAStar'].getDataPoints()[0]);
    #    nodesToGoal = self.models['testAStar'].getNodesToGoal();
    #    for dataPoint in nodesToGoal:
    #        self.drawRect(bSize*dataPoint[0][0]+1, bSize*dataPoint[0][1]+1, bSize-1, bSize-1, 180, 180, 180);
    #        index = index + 1;
            

    def drawGameSurface(self):
        row = 0;
        column = 0;
        [width, height] = pygame.display.get_surface().get_size()
        bSize = height / len(self.models['testAStar'].getDataPoints()[0]);
        for dataPointRow in self.models['testAStar'].getDataPoints():
            for dataPoint in dataPointRow:
                column = column + 1;
                if(dataPoint == 'X'):
                    self.drawRect(bSize*column, bSize*row, bSize, bSize, 255, 0, 0);
                if(dataPoint == 'S'):
                    self.drawRect(bSize*column, bSize*row, bSize, bSize, 255, 255, 255);
                if(dataPoint == 'G'):
                    self.drawRect(bSize*column, bSize*row, bSize, bSize, 255, 0, 255);
            column = 0;
            row = row + 1;

    def drawPassedNodes(self):
        index = 0;
        [width, height] = pygame.display.get_surface().get_size()
        bSize = height / len(self.models['testAStar'].getDataPoints()[0]);
        passedNodes = self.models['testAStar'].getPassedNodes();
        lastNode = 0;
        greyColorInt = 128;
        whiteColorInt = 255;
        colorInt = whiteColorInt;
        for dataPoint in passedNodes:
            if lastNode != 0: 
                if(lastNode[0][1] < dataPoint[0][1]):
                    colorInt = greyColorInt;
                else:
                    colorInt = whiteColorInt;
            self.drawRect(bSize*dataPoint[0][0]+1, bSize*dataPoint[0][1]+1, bSize, bSize, colorInt, colorInt, colorInt);
                
            lastNode = dataPoint;
            index = index + 1;
            
