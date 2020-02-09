import pygame;
from pygame.math import Vector2 as vector;
models = {}
class GameUI(object):
    def __init__(self):
        pass;

    def addModel(self, model, name):
        models[name] = model;

    def startUI(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        running = True;
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quit command received')
                    running = False;
            self.drawGameSurface();
            pygame.display.update();

    def drawLine(self, x1, y1, x2, y2, r, g, b):
        color = pygame.Color(r, g, b);
        start = vector(x1, y1);
        end = vector(x2, y2);
        pygame.draw.line(self.screen, color, start, end, width =  1);

    def drawRect(self, x, y, w, h, r, g, b):
        color = pygame.Color(r, g, b);
        area = pygame.Rect(x, y, w, h);
        pygame.draw.rect(self.screen, color, area, 1);

    def drawGameSurface(self):
        row = 0;
        column = 0;
        [width, height] = pygame.display.get_surface().get_size()
        bSize = height / len(models['testAStar'].getDataPoints()[0]);
        for dataPointRow in models['testAStar'].getDataPoints():
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