#Particle motion
#David Lovitz

import math, random, time, Tkinter as tk
from ptvec import *
from PIL import ImageTk

deltaT = .005

class Particle(object):
    def __init__(self,canvas,x,y,dx,dy):
        self.canvas = canvas
        self.velocity = Vector(dx, dy)
        self.acceleration = Vector(0, 0)
        self.location = Point(x, y)
        self.radius = 7
        self.id = self.canvas.create_oval(150*self.location.x-self.radius/2,150*self.location.y-self.radius/2, 150*self.location.x+self.radius/2,150*self.location.y+self.radius/2,fill="#000000")
        self.distanceTo = 0

    def aPotential(self,x,y):#-p'(r)
        return Vector(-1*x,-1*y)

    def aPotential2(self,x,y):
        a = .4
        #xcomp = (-1.0/4.0)*(4*(x**3)-(4*x)*(a**2))
        xcomp = 0.35*((-1 + 0.7*x)**2)*(1 + 0.7*x) + 0.35*((-1 + 0.7*x))*(1 + 0.7*x)**2;
        return Vector(-xcomp,-0.2*y)
    
    def update(self, particles,iterations):
        self.location.move(self.velocity.multiply(deltaT))
        if(iterations%1 == 0):
            self.canvas.move(self.id, 150*self.velocity.multiply(deltaT).horizontal, 150*self.velocity.multiply(deltaT).vertical)
        self.velocity = self.velocity.add(self.acceleration.multiply(deltaT))
        anew1 = self.aPotential2(self.location.x,self.location.y)
        anew2 = self.separation(particles)
        self.acceleration = anew1.add(anew2)
        
    def separation(self, particles):
        alpha = 0.03
        asep = Vector(0.0, 0.0)
        for pt in particles:
            if (pt.id != self.id):
                dist = self.location.distance(pt.location)
                vToThem = self.location.makeVectorTo(pt.location)
                vToThem = vToThem.normalize()
                vToThem = vToThem.multiply(-alpha/(dist**2))
                asep = asep.add(vToThem)
        return asep


class runGraphics(object):
    def __init__(self, master, **kwargs):
        #graphics stuff
        self.master = master
        self.canvas = tk.Canvas(self.master,width=600,height=600,bg = "white")
        self.canvas.pack()
        self.canvas.configure(scrollregion=(-300,-300,300,300))

        self.image = ImageTk.PhotoImage(file = "contour2.png");
        self.canvas.create_image(0,0,image = self.image)
        
        #draw axes
        #self.canvas.create_line(0, 300, 0, -300,dash=(3,2),fill="#a3a3a3")
        #self.canvas.create_line(-300, 0, 300, 0,dash=(3,2),fill="#a3a3a3")

        self.iterations = 0
        #generate the particles
        self.particles = []
        i=0
        while i<10:
            xpos = random.uniform(-2.0, 2.0)
            ypos = random.uniform(-2.0, 2.0)
            #self.particles.append(Particle(self.canvas,((-1)**i)*100,10*(-1)**i,0,0))
            self.particles.append(Particle(self.canvas,xpos,ypos,0,0))
            i=i+1
        self.master.after(1,self.updateState)
        
    #loop for updating all particles
    def updateState(self):
        for particle in self.particles:
            particle.update(self.particles,self.iterations)
        #calls updateState again after #milliseconds
        self.iterations += 1
        self.master.after(3, self.updateState)

root = tk.Tk()
app = runGraphics(root)
root.mainloop()
