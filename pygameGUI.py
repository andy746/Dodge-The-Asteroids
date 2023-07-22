import pygame as pyg
from random import randint as R

class Button:
    def border(self,r):
        sr = self.rect
        pyg.draw.lines(self.surf, self.bc,True,[(r.left,r.top),(r.right,r.top),(r.right,r.bottom),(r.left,r.bottom)],self.bd)
    def draw(self):
        if self.relpos != None:
            x,y = self.w.get_size()
            self.pos = int(x*self.relpos[0]),int(y*self.relpos[1])

        if type(self.pos) == str:
            if self.pos.lower() == 'center':
                c = self.w.get_rect().center
                self.pos = c[0]-self.size[0]//2,c[1]-self.size[1]//2
       
        self.w.blit(self.surf,(self.pos[0]-self.rect.size[0]//2,self.pos[1]-self.rect.size[1]//2))
        click = self.click()
        if not click:
            self.hover()
        return click
    def create_surface(self):
        r = self.rect
        if self.text != None:
            font = pyg.font.SysFont(self.fonts[self.font],self.fs,self.bold,self.italic)
            txt = font.render(str(self.text),0,self.fc)
            ts = txt.get_size()
            r = pyg.Rect(self.bd,self.bd,max(self.size[0],ts[0]+self.pad*2),max(self.size[1],ts[1]+self.pad*2))
            self.surf = pyg.Surface((r.width+self.bd*2,r.height+self.bd*2), pyg.SRCALPHA) 
        pyg.draw.rect(self.surf,self.bg,r)
        self.rect = self.surf.get_rect()
        if self.text != None:
            self.surf.blit(txt,(r.center[0]-ts[0]//2+1,r.center[1]-ts[1]//2+1))
        if self.bc != self.bg and self.bd > 0:
            self.border(r)
    def click(self):
        mpr = pyg.mouse.get_pressed()
        if not mpr[0]:
            self.click_once = 0
        elif self.click_once == 0:
            clicked = False
            mp = pyg.mouse.get_pos()
            r = pyg.Rect(self.pos[0]-self.rect.size[0]//2,self.pos[1]-self.rect.size[1]//2,self.rect.width,self.rect.height)
            s = pyg.Surface((r.width,r.height),pyg.SRCALPHA)
            if r.collidepoint(mp):
                if mpr[0]:
                    self.click_once = 1
                    clicked = True
                    pyg.draw.rect(s,(0,0,0,50),self.rect)
            self.w.blit(s,(self.pos[0]-self.rect.size[0]//2,self.pos[1]-self.rect.size[1]//2))
            return clicked
    def hover(self):
        hover = False
        mp = pyg.mouse.get_pos()
        mpr = pyg.mouse.get_pressed()
        r = pyg.Rect(self.pos[0]-self.rect.size[0]//2,self.pos[1]-self.rect.size[1]//2,self.rect.width,self.rect.height)
        s = pyg.Surface((r.width,r.height),pyg.SRCALPHA)
        if r.collidepoint(mp):
            hover = True
            pyg.draw.rect(s,(0,0,0,25),self.rect)
        self.w.blit(s,(self.pos[0]-self.rect.size[0]//2,self.pos[1]-self.rect.size[1]//2))
        #return hover        
        
    def __init__(self,w,bg='grey',text=None,fs=20,font=0,fc='black',size=(30,20),relpos=None,pos=(30,20),bold=False,italic=False,pad=2,bc='darkgrey',bd=2):
        self.click_once = 0
        self.w = w
        self.bg = bg
        self.text = text
        self.font = font
        self.fs = fs
        self.fc = fc
        self.size = size
        self.bold = bold
        self.italic = italic
        self.pos = pos
        self.relpos = relpos
        if relpos != None:
            x,y = w.get_size()
            self.pos = int(x*relpos[0]),int(y*relpos[1])
        self.pad = pad
        self.bc = bc
        self.bd = bd
        self.fonts = pyg.font.get_fonts()
        self.surf = pyg.Surface((size[0],size[1]), pyg.SRCALPHA)
        self.rect = pyg.Rect(0,0,self.size[0],self.size[1])
        self.create_surface()
        #self.draw()
        
########################################################################################################################################################################
        
class Slider:

    def __init__(self, w, pos=(0,0), size=(150,50), relpos=None, slider_size=None, x_rng=(1,100), bd=5, sbd=5, bc='black', sbc='black', bg='lightgrey', sc='darkgrey'):

        self.w = w
        x,y = w.get_size()
        self.pos = pos = pos if relpos == None else (x*relpos[0]-size[0]//2,y*relpos[1]-size[1]//2)
        self.size = size
        self.x_rng = x_rng
        self.sbc = sbc
        self.sc = sc
        self.sbd = sbd
        self.bd = bd
        self.bg = bg
        self.bc = bc
        self.value = x_rng[0]
        
        self.slider_size = slider_size = slider_size if slider_size != None else (size[0]//5, size[1]//2)
        self.slide_surf = pyg.Surface(slider_size, pyg.SRCALPHA)
        self.surf = pyg.Surface(self.size,pyg.SRCALPHA)
        self.rect = pyg.Rect(pos[0],pos[1],size[0],size[1])
        self.slider = pyg.Rect(pos[0],pos[1]+self.size[1]//2-slider_size[1]//2, slider_size[0],slider_size[1])
        self.slider_g = pyg.Rect(0,0,slider_size[0],slider_size[1])
        pyg.draw.rect(self.surf, bc, self.rect.move(-pos[0],-pos[1]))
        pyg.draw.rect(self.surf, bg, pyg.Rect(bd, bd, size[0]-bd*2, size[1]-bd*2))

        self.max_dist = self.size[0] - self.slider_size[0]
        self.inc = (x_rng[1]-x_rng[0])/self.max_dist

    def update(self,mp=None,mpr=None):

        mp = pyg.mouse.get_pos() if mp == None else mp
        mpr = pyg.mouse.get_pressed() if mpr == None else mpr

        if mpr[0] or mpr[2]:
            if self.rect.collidepoint(mp):
                ss = self.slider_size
                self.slider.update(min(max(mp[0]-ss[0]//2, self.rect.left),self.rect.right-ss[0]), self.rect.center[1]-ss[1]//2, ss[0], ss[1])
                
        self.w.blit(self.surf, self.pos)
        pyg.draw.rect(self.slide_surf, self.sc, self.slider_g)
        r = self.slider_g
        d = self.sbd
        pyg.draw.lines(self.slide_surf, self.sbc, True, [(r.left+d//2-1,r.top+d//2-1),(r.right-d//2,r.top+d//2-1),(r.right-d//2,r.bottom-d//2),(r.left+d//2-1,r.bottom-d//2)], d)
        self.w.blit(self.slide_surf,self.slider)
        self.slider_value()



    def slider_value(self):
        
        self.value = self.inc*( self.slider.left-self.rect.left )+self.x_rng[0]
        

    def get_slider_value(self):
        return self.value




