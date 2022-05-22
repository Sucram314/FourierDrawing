import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import cmath,math
import keyboard as k
import pygame

def maprange(v,a,b,c,d):
    return ((v-a)/(b-a))*(d-c)+c

class Equation:
    def __init__(self,func,start=0,end=1):
        self.func = func
        self.start = start
        self.end = end

    def maprange(self,v,a,b):
        return ((v-a)/(b-a))*(self.end-self.start)+self.start


#paste bezier curves here
equations = [
Equation(lambda t:complex(46.34*(1-t)**3+139.03*t*(1-t)**2+129.62*t**2*(1-t)+39.31*t**3,-134.22*(1-t)**3-391.29*t*(1-t)**2-382.02*t**2*(1-t)-127.34*t**3)),
Equation(lambda t:complex(39.31*(1-t)**3+111.51*t*(1-t)**2+105.79*t**2*(1-t)+33.97*t**3,-127.34*(1-t)**3-382.02*t*(1-t)**2-384.84*t**2*(1-t)-129.75*t**3)),
Equation(lambda t:complex(33.97*(1-t)**3+101.82*t*(1-t)**2+101.71*t**2*(1-t)+33.87*t**3,-129.75*(1-t)**3-389.34*t*(1-t)**2-389.43*t**2*(1-t)-129.84*t**3)),
Equation(lambda t:complex(33.87*(1-t)**3+100.75*t*(1-t)**2+100.01*t**2*(1-t)+33.09*t**3,-129.84*(1-t)**3-390.45*t*(1-t)**2-391.56*t**2*(1-t)-130.94*t**3)),
Equation(lambda t:complex(33.09*(1-t)**3+96.89*t*(1-t)**2+95.33*t**2*(1-t)+31.75*t**3,-130.94*(1-t)**3-396.87*t*(1-t)**2-402.69*t**2*(1-t)-137*t**3)),
Equation(lambda t:complex(31.75*(1-t)**3+95.25*t*(1-t)**2+181.87*t**2*(1-t)+60.62*t**3,-137*(1-t)**3-445.26*t*(1-t)**2-467.31*t**2*(1-t)-133.25*t**3)),
Equation(lambda t:complex(60.62*(1-t)**3+182.01*t*(1-t)**2+178.1*t**2*(1-t)+57.47*t**3,-133.25*(1-t)**3-390.66*t*(1-t)**2-367.59*t**2*(1-t)-112.84*t**3)),
Equation(lambda t:complex(57*(1-t)**3+166.03*t*(1-t)**2+160.01*t**2*(1-t)+51.34*t**3,-110.5*(1-t)**3-306.54*t*(1-t)**2-277.92*t**2*(1-t)-83.12*t**3)),
Equation(lambda t:complex(49.69*(1-t)**3+145.82*t*(1-t)**2+142.7*t**2*(1-t)+46.66*t**3,-75.19*(1-t)**3-209.97*t*(1-t)**2-194.84*t**2*(1-t)-60.31*t**3)),
Equation(lambda t:complex(44.34*(1-t)**3+130.97*t*(1-t)**2+129.62*t**2*(1-t)+43.16*t**3,-47.75*(1-t)**3-130.81*t*(1-t)**2-120.73*t**2*(1-t)-38.25*t**3)),
Equation(lambda t:complex(43.16*(1-t)**3+130.08*t*(1-t)**2+146.62*t**2*(1-t)+52.97*t**3,-38.25*(1-t)**3-74.35*t*(1-t)**2-52.09*t**2*(1-t)-16.97*t**3)),
Equation(lambda t:complex(52.97*(1-t)**3+166.28*t*(1-t)**2+172.12*t**2*(1-t)+57.38*t**3,-16.97*(1-t)**3-50.2*t*(1-t)**2-57.04*t**2*(1-t)-24.03*t**3)),
Equation(lambda t:complex(57.38*(1-t)**3+172.72*t*(1-t)**2+154.6*t**2*(1-t)+44.34*t**3,-24.03*(1-t)**3-97.95*t*(1-t)**2-120.54*t**2*(1-t)-47.75*t**3)),
Equation(lambda t:complex(42.91*(1-t)**3+98.05*t*(1-t)**2+62.44*t**2*(1-t)+20.81*t**3,-49.25*(1-t)**3-179.49*t*(1-t)**2-212.07*t**2*(1-t)-84.94*t**3)),
Equation(lambda t:complex(20.81*(1-t)**3+61.95*t*(1-t)**2+85.89*t**2*(1-t)+47.56*t**3,-84.94*(1-t)**3-293.99*t*(1-t)**2-343.89*t**2*(1-t)-114.47*t**3)),
Equation(lambda t:complex(47.56*(1-t)**3+151.4*t*(1-t)**2+159.25*t**2*(1-t)+55.41*t**3,-114.47*(1-t)**3-343.35*t*(1-t)**2-342.27*t**2*(1-t)-113.47*t**3)),
Equation(lambda t:complex(57.47*(1-t)**3+234.22*t*(1-t)**2+218.69*t**2*(1-t)+53.94*t**3,-112.84*(1-t)**3-316.17*t*(1-t)**2-224.4*t**2*(1-t)-74.66*t**3)),
Equation(lambda t:complex(53.94*(1-t)**3+157.4*t*(1-t)**2+153.15*t**2*(1-t)+49.69*t**3,-74.66*(1-t)**3-224.01*t*(1-t)**2-224.53*t**2*(1-t)-75.19*t**3)),
Equation(lambda t:complex(48.03*(1-t)**3+106.45*t*(1-t)**2+88.38*t**2*(1-t)+47.25*t**3,-75.72*(1-t)**3-240.55*t*(1-t)**2-293.02*t**2*(1-t)-105.5*t**3)),
Equation(lambda t:complex(47.25*(1-t)**3+109.22*t*(1-t)**2+125.23*t**2*(1-t)+49.56*t**3,-105.5*(1-t)**3-288.81*t*(1-t)**2-256.03*t**2*(1-t)-83.44*t**3)),
Equation(lambda t:complex(51.34*(1-t)**3+154.97*t*(1-t)**2+155.99*t**2*(1-t)+52.31*t**3,-83.12*(1-t)**3-249.32*t*(1-t)**2-249.34*t**2*(1-t)-83.12*t**3)),
Equation(lambda t:complex(52.31*(1-t)**3+196.12*t*(1-t)**2+210.91*t**2*(1-t)+57*t**3,-83.12*(1-t)**3-249.38*t*(1-t)**2-311.61*t**2*(1-t)-110.5*t**3)),
Equation(lambda t:complex(55*(1-t)**3+158.68*t*(1-t)**2+151.3*t**2*(1-t)+47.56*t**3,-111.31*(1-t)**3-336.15*t*(1-t)**2-337.44*t**2*(1-t)-112.5*t**3)),
Equation(lambda t:complex(47.56*(1-t)**3+121.14*t*(1-t)**2+78.09*t**2*(1-t)+26.03*t**3,-112.5*(1-t)**3-337.5*t*(1-t)**2-323.79*t**2*(1-t)-90.62*t**3)),
Equation(lambda t:complex(26.03*(1-t)**3+78.09*t*(1-t)**2+108.23*t**2*(1-t)+45.25*t**3,-90.62*(1-t)**3-228.39*t*(1-t)**2-210.72*t**2*(1-t)-61.66*t**3)),
Equation(lambda t:complex(46.66*(1-t)**3+161.56*t*(1-t)**2+180.42*t**2*(1-t)+60*t**3,-60.31*(1-t)**3-159.72*t*(1-t)**2-132.26*t**2*(1-t)-27.22*t**3)),
Equation(lambda t:complex(60*(1-t)**3+180.07*t*(1-t)**2+167.96*t**2*(1-t)+51.69*t**3,-27.22*(1-t)**3-45.31*t*(1-t)**2-16.17*t**2*(1-t)-5.25*t**3)),
Equation(lambda t:complex(51.69*(1-t)**3+138.78*t*(1-t)**2+119.74*t**2*(1-t)+40.12*t**3,-5.25*(1-t)**3-15.33*t*(1-t)**2-54.2*t**2*(1-t)-29.62*t**3)),
Equation(lambda t:complex(40.12*(1-t)**3+120.52*t*(1-t)**2+123.85*t**2*(1-t)+42.91*t**3,-29.62*(1-t)**3-99.44*t*(1-t)**2-120.85*t**2*(1-t)-49.25*t**3)),
Equation(lambda t:complex(45.25*(1-t)**3+138.38*t*(1-t)**2+141.22*t**2*(1-t)+48.03*t**3,-61.66*(1-t)**3-198.51*t*(1-t)**2-212.78*t**2*(1-t)-75.72*t**3)),
Equation(lambda t:complex(49.56*(1-t)**3+154.58*t*(1-t)**2+160.34*t**2*(1-t)+55*t**3,-83.44*(1-t)**3-279.76*t*(1-t)**2-308.82*t**2*(1-t)-111.31*t**3)),
Equation(lambda t:complex(55.41*(1-t)**3+171.41*t*(1-t)**2+174.86*t**2*(1-t)+58.28*t**3,-113.47*(1-t)**3-368.88*t*(1-t)**2-391.35*t**2*(1-t)-133.91*t**3)),
Equation(lambda t:complex(58.28*(1-t)**3+175.03*t*(1-t)**2+121.26*t**2*(1-t)+39.56*t**3,-133.91*(1-t)**3-442.65*t*(1-t)**2-446.7*t**2*(1-t)-141.06*t**3)),
Equation(lambda t:complex(39.56*(1-t)**3+130.02*t*(1-t)**2+139.03*t**2*(1-t)+46.34*t**3,-141.06*(1-t)**3-422.79*t*(1-t)**2-413.79*t**2*(1-t)-134.22*t**3)),
]

def f(t):
    eq = min(len(equations)-1,math.floor(t*len(equations)))
    equation = equations[eq]
    return equation.func(equation.maprange(t,eq/len(equations),(eq+1)/len(equations)))

c = 125
step = 0.0001
twopiistep = complex(0,2*cmath.pi*step)
twopii = complex(0,2*cmath.pi)
total = int(1/step)

coefficients = [sum(f(t*step)*cmath.exp(-n*twopiistep*t) for t in range(0,total+1))/total for n in range(-c,c+1,1)]
coefficients[c] = complex(0,0)

a = pygame.image.load("C:\\Users\\marcu\\OneDrive\\Pictures\\Saved Pictures\\Untitled_ico32.ico")
pygame.display.set_icon(a)

pygame.init()
resolution = pygame.display.Info()
width = resolution.current_w
height = resolution.current_h
hwidth = (width/2)
hheight = (height/2)

myFont = pygame.font.SysFont("couriernew",32)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width,height),pygame.NOFRAME)

magnification = 3

colours = 0
col = (255,0,0)

def rainbow(i):
    return (max(min((abs(i-3*255)-255),255),0),max(min((-abs(i-2*255)+255*2),255),0),max(min((-abs(i-4*255)+255*2),255),0))

def camera(x,y):
    return ((x+campos[0])*magnification+hwidth,(-y+campos[1])*magnification+hheight)

def dist(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

_45 = math.radians(45)
cut = 1-math.sqrt(2)/10

def drawArrow(p1,p2):
    d = dist(p1,p2)
    angle = math.atan2(p2[1]-p1[1],p2[0]-p1[0])
    pygame.draw.aaline(screen,(255,255,255),p1,(math.cos(angle)*d*cut+p1[0],math.sin(angle)*d*cut+p1[1]))
    p3 = (math.cos(angle)*d+math.cos(angle+_45+math.pi)*d/5+p1[0],math.sin(angle)*d+math.sin(angle+_45+math.pi)*d/5+p1[1])
    p4 = (math.cos(angle)*d+math.cos(angle-_45+math.pi)*d/5+p1[0],math.sin(angle)*d+math.sin(angle-_45+math.pi)*d/5+p1[1])
    pygame.draw.aalines(screen,(255,255,255),1,[p2,p3,p4])

def draw():
    global points,campos
    oldpos = complex(0,0)
    pos = coefficients[c]
    arrowsToDraw = [(camera(0,0),camera(pos.real,pos.imag))]
    for i in range(1,c+1):
        oldpos = pos
        pos += coefficients[c+i]*cmath.exp((i)*twopii*t)
        arrowsToDraw.append(((oldpos.real,oldpos.imag),(pos.real,pos.imag)))
        oldpos = pos
        pos += coefficients[c-i]*cmath.exp((-i)*twopii*t)
        arrowsToDraw.append(((oldpos.real,oldpos.imag),(pos.real,pos.imag)))

    points.append(pos)
    if follow: campos = [-pos.real,pos.imag]

    for arrow in arrowsToDraw: drawArrow(camera(*arrow[0]),camera(*arrow[1]))

def trace():
    try: pygame.draw.aalines(screen,col,0,[camera(point.real,point.imag) for point in points])
    except: pass

queue = []

def ui():
    global followfade,followmessage,speedmessage,speedfade,queue
    blitqueue = {}
    if followmessage:
        c = min(followfade,255)
        label = myFont.render("follow = "+str(bool(follow)),1,(c,c,c))
        followfade -= 5
        if followfade < 0:
            followmessage = 0
            queue.remove(0)
        blitqueue[0] = label
    if speedmessage:
        c = min(speedfade,255)
        label = myFont.render("speed = "+str(speed/basespeed)+"x",1,(c,c,c))
        speedfade -= 5
        if speedfade < 0:
            speedmessage = 0
            queue.remove(1)
        else: blitqueue[1] = label

    for i in range(len(queue)-1,-1,-1):
        screen.blit(blitqueue[queue[i]],(0,i*32))

points = []

t = 0

campos = [0,0]
dragging = 0

speed = 0.0005
basespeed = 0.0005
changing = 0
speedmessage = 0
speedfade = 0

follow = 0
followmessage = 0
followfade = 0

while 1:
    dt = clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                magnification *= 1.1
            elif event.button == 5:
                magnification /= 1.1
            if event.button == 2:
                if 0 not in queue: queue.append(0)
                followmessage = 1
                followfade = 500
                follow = 1-follow

    left,middle,right = pygame.mouse.get_pressed()
    if right:
        speedmessage = 1
        speedfade = 1000
        if 1 not in queue: queue.append(1)
        if not changing:
            og_ = pygame.mouse.get_pos()
            ogspeed = speed
            changing = 1
    else:
        changing = 0
        
    if left and not follow:
        if not dragging:
            og = pygame.mouse.get_pos()
            ogcampos = [*campos]
            dragging = 1
    else:
        dragging = 0

    if changing:
        cur_ = pygame.mouse.get_pos()
        speed = ogspeed * maprange(cur_[0]-og_[0],-width,width,0.1,1.9)

    if dragging:
        cur = pygame.mouse.get_pos()
        campos[0] = ogcampos[0]+(cur[0]-og[0])/magnification
        campos[1] = ogcampos[1]+(cur[1]-og[1])/magnification
    
    if k.is_pressed("esc"): break

    screen.fill((0,0,0))
    draw()
    trace()
    ui()
    pygame.display.update()

    t += speed
    if t>1:
        points = []
        t = 0
        colours += 236.398
        col = rainbow(colours)
        if colours > 1530: colours -= 1530

pygame.quit()


