from p5 import *


def setup():
  createCanvas(400,400)

  global ball
  ball={'x':width/2,'y':height/2,'size':20,'sx':1,'speedSize':0.5}

  '''
               global ballX
               global ballY
               global ballSize
               ballX = 100
               ballY = 100
               ballSize = 20
  '''

def draw():
  global ball
  background('black')
  drawTickAxes()
  fill("cyan")
  circle(ball['x'],ball['y'],ball['size'])
  ball['x'] +=ball['sx']
  ball['size'] +=ball['speedSize']
  cond1=ball['x']+ball['size']/2
  cond2=ball['x']+ball['size']/2
  
  if cond1 > 400 or cond2<0:
    ball['sx']=-ball['sx']
    ball['speedSize'] = - ball['speedSize']

  
  '''
  global ballX
  global ballY
  global ballSize
  fill("cyan")
  circle(ballX, ballY, ballSize)

  ballX = ballX + 1
  ballSize = ballSize + 1

  
  '''
  