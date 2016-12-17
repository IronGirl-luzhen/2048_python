from button import*
import random
import copy
class Box:
    def __init__(self,xVal,yVal,color,n):
        self.x = xVal
        self.y = yVal
        self.c = color
        self.n = n
        self.f =Rectangle(Point(self.x-0.5,self.y-0.5),Point(self.x+0.5,self.y+0.5))
        self.f.setFill(self.c)
        self.t = Text(Point(self.x,self.y),self.n)
        
    def getRectangle(self):
        return self.f
    
    def getText(self):
        return self.t
    
class Game:
    def setBox(self,i,j,color,n):
        self.boxList[i][j].getRectangle().setFill(color)
        if self.b[i][j] == 0:
            self.boxList[i][j].getText().setText("")
        else:
            self.boxList[i][j].getText().setText(self.b[i][j])
            
    def drawBox(self,i,j):
        self.boxList[i][j].getRectangle().draw(self.w)
        self.boxList[i][j].getText().draw(self.w)
        
    def undrawBox(self,i,j):
        self.boxList[i][j].getRectangle().undraw()
        self.boxList[i][j].getText().undraw()
        
    def __init__(self):
        win = GraphWin("Jane`s 2048",700,700)
        win.setCoords(0.0,0.0,7.0,7.0)
        win.setBackground("light blue")
        Text(Point(0.5,5),"Your score:").draw(win)
        Text(Point(0.7,5.5),"The best score:").draw(win)
        self.f_score = Text(Point(2,5.5),"0")
        self.f_score.draw(win)
        Text(Point(0.7,6),"The highest number:").draw(win)
        self.h_num = Text(Point(2,6),"0")
        self.h_num.draw(win)
        score = 0
        a = Text(Point(2,5),"0")
        a.draw(win)
        Text(Point(3,6.5),"Join the numbers and get the 2048 tile!").draw(win)
        self.qButton = Button(win,Point(6,6),1,1,"Quit")
        self.qButton.activate()
        self.up = Button(win,Point(6,3.5),0.5,0.5,"up")
        self.down = Button(win,Point(6,2.5),0.5,0.5,"down")
        self.right = Button(win,Point(6.5,3),0.5,0.5,"right")
        self.left = Button(win,Point(5.5,3),0.5,0.5,"left")
        self.restart = Button(win,Point(6,1),0.5,0.5,"restart")
        self.up.activate()
        self.down.activate()
        self.right.activate()
        self.left.activate()
        tt=0.5
        for i in range(5):
            line1 = Line(Point(0.5,tt),Point(4.5,tt)).draw(win)
            line2 = Line(Point(tt,0.5),Point(tt,4.5)).draw(win)
            tt+=1
        blist=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        clist={0:"lightblue",2:"yellow",4:"orange",8:"grey",16:"light green",32:"light yellow",64:"brown",128:"purple",256:"green",512:"light red",1024:"red",2048:"black"}
        self.w = win
        self.a = a
        self.c = clist
        self.b = blist
        self.s = score
        boxList = []
        for i in range(4):
            tmpList = []
            for j in range(4):
                box = Box(i+1,j+1,self.c[0],"")
                tmpList.append(box)
            boxList.append(tmpList)
        self.boxList = boxList
        
    def step_first(self):
        num=random.choice((2,2,2,2,4))
        color = "lightblue"
        while 1:
            xx=random.randrange(1,5)
            yy=random.randrange(1,5)
            if self.b[xx-1][yy-1]!=0:
                pass
            else:
                x=xx
                y=yy
                break
            if num==2:
                color= self.c[2]
            else:
                color = self.c[4]
        self.setBox(x-1,y-1,color,num)
        self.undrawBox(x-1, y-1)
        self.drawBox(x-1,y-1)
        self.b[x-1][y-1] = num
        
    def up_move(self):
        for k in range(3):
            for i in range(3,-1,-1):
                for j in range(2,-1,-1):
                    if self.b[i][j+1]==0:
                        self.b[i][j],self.b[i][j+1]=0,self.b[i][j]
                    else:
                        continue


    def di_up(self):
        self.up_move()
        for i in range(4):
            lst = []
            for j in range(3,-1,-1):
                lst.append(self.b[i][j])
            pos1 , t= self.merge(lst)
            for k in range(4):
                self.b[i][k] = pos1[3-k]
        
    def down_move(self):
        for t in range(3):
            for i in range(4):
                for j in range(1,4):
                    if self.b[i][j-1]==0:
                        self.b[i][j],self.b[i][j-1]=0,self.b[i][j]
                    else:
                        continue
                    
    def di_down(self):
        self.down_move()
        for i in range(4):
            lst = []
            for j in range(4):
                lst.append(self.b[i][j])
            pos1 , t= self.merge(lst)
            for k in range(4):
                self.b[i][k] = pos1[k]
        
    def merge(self,lst):
        if len(lst) == 2:
            a = 0
            if lst[0] != 0 and lst[0] == lst[1]:
                lst[0], lst[1] = 2*lst[0], 0
                self.s += lst[0]
                a += 1
            else:
                a += 1
            return lst, a
        else:
            tem = lst[len(lst)-1]
            pos, b = self.merge(lst[:len(lst)-1])
            pos.append(tem)
            if pos[b+1] != 0 and pos[b+1] == pos[b]:
                pos[b+1], pos[b] = 0, 2*pos[b]
                self.s += pos[b]
            if pos[b] == 0 :
                pos[b], pos[b+1] = pos[b+1], 0
            b  += 1
            return pos, b
        
    def right_move(self):
        for t in range(3):
            for j in range(4):
                for i in range(2,-1,-1):
                    if self.b[i+1][j]==0:
                        self.b[i][j],self.b[i+1][j]=0,self.b[i][j]
                    else:
                        continue

    def di_right(self):
        self.right_move()
        for i in range(4):
            lst = []
            for j in range(3,-1,-1):
                lst.append(self.b[j][i])
            pos1 , t= self.merge(lst)
            for k in range(4):
                self.b[k][i] = pos1[3-k]
       
    
    def left_move(self):
        for t in range(3):
            for j in range(4):
                for i in range(1,4):
                    if self.b[i-1][j]==0:
                            self.b[i-1][j],self.b[i][j]=self.b[i][j],0
                    else:
                        continue

    def di_left(self):
        self.left_move()
        for i in range(4):
            lst = []
            for j in range(4):
                lst.append(self.b[j][i])
            pos1 , t= self.merge(lst)
            for k in range(4):
                self.b[k][i] = pos1[k]
                        
    def step_third(self):
        for i in range(4):
            for j in range(4):
                self.setBox(i,j,self.c[self.b[i][j]],self.b[i][j])
                self.undrawBox(i, j)
                self.drawBox(i, j)
                        
    def step_score(self):
        self.a.undraw()
        self.a = Text(Point(2,5),str(self.s))
        self.a.draw(self.w)
    def over_step(self):
        count1 = 0
        for i in range(4):
            for j in range(4):
                if self.b[i][j] != 0:
                    count1+=1
        count2 = 0
        for i in range(4):
            for j in range(3):
                if self.b[i][j] == self.b[i][j+1]:
                    count2 += 1
                if self.b[j+1][i] == self.b[j][i]:
                    count2 += 1
        if count1 == 16 and count2 ==0:
            c = Rectangle(Point(2,2),Point(6,6))
            c.setFill("red")
            c.draw(self.w)
            b = Text(Point (4,4),"Game Over!!!")
            b.draw(self.w)
            self.w.getMouse()
            c.undraw()
            b.undraw()
            return 1
        for i in range(4):
            for j in range(4):
                if self.b[i][j] == 2048:
                    r = Rectangle(Point(2,2),Point(6,6))
                    r.setFill("red")
                    r.draw(self.w)
                    tt = Text(Point (4,4),"Congratulation!!!You win !!!")
                    tt.draw(self.w)
                    q = self.w.getMouse()
                    r.undraw()
                    tt.undraw()
                    return 0
        return 2            
                
    def quit_step(self):
        self.w.close()
        
    def step_restart(self):
        for i in range(4):
            for j in range(4):
                self.setBox(i, j, self.c[self.b[i][j]], self.b[i][j])
                self.undrawBox(i, j)
                self.b[i][j] = 0
        pos=[]
        for i in range(2):
            xx=random.randrange(1,5)
            yy=random.randrange(1,5)
            if not((xx,yy) in pos):
                self.b[xx-1][yy-1]=2
                self.setBox(xx-1,yy-1,self.c[2],self.b[xx-1][yy-1])
                self.undrawBox(xx-1, yy-1)
                self.drawBox(xx-1, yy-1)
                self.b[xx-1][yy-1] = 2
                pos.append((xx,yy))
        self.a.undraw()
        self.a = Text(Point(2,5),"0")
        self.a.draw(self.w)

    def best_score(self):
        ff = open("grade.txt", "r")
        bb = ff.readline()
        self.max = eval(bb)
        
    def draw_best_score(self):
        self.f_score.undraw()
        self.f_score = Text(Point(2,5.5),self.max)
        self.f_score.draw(self.w)
        
    def change_best_score(self):
        if self.s >= self.max:
            ff = open("grade.txt", "w")
            ff.write(str(self.s))
            ff.close()

    def change_highest_num(self):
        li = []
        for item in self.b:
            li.append(max(item))
        self.num = max(li)
        if self.num >= self.hst:
            ff = open("highest_number.txt", "w")
            ff.write(str(self.num))
            
    def highest_num(self):
        ff = open("highest_number.txt","r")
        bb = ff.readline()
        self.hst= eval(bb)

    def draw_highest_num(self):
        self.h_num.undraw()
        self.h_num = Text(Point(2,6),self.hst)
        self.h_num.draw(self.w)
                
                
            
        
    def start(self):
        pos=[]
        for i in range(2):
            xx=random.randrange(1,5)
            yy=random.randrange(1,5)
            if not((xx,yy) in pos):
                self.b[xx-1][yy-1]=2
                self.setBox(xx-1,yy-1,self.c[2],self.b[xx-1][yy-1])
                self.undrawBox(xx-1, yy-1)
                self.drawBox(xx-1, yy-1)
                pos.append((xx,yy))
        while True:
            q = self.w.getMouse()
            self.restart.activate()
            lst1 = copy.deepcopy(self.b)
            if self.qButton.clicked(q):
                self.quit_step()
                break
            if self.left.clicked(q):
                self.di_left()
            if self.right.clicked(q):
                self.di_right()
            if self.up.clicked(q):
                self.di_up()
            if self.down.clicked(q):
                self.di_down()
            lst2 = copy.deepcopy(self.b)
            if self.left.clicked(q)or self.right.clicked(q)or self.up.clicked(q)or self.down.clicked(q):
                if lst1 != lst2:
                    self.step_first()
            self.step_score()
            #self.step_second()
            self.step_third()
            if self.restart.clicked(q):
                self.step_restart()
            self.best_score()
            self.change_best_score()
            self.best_score()
            self.draw_best_score()
            self.highest_num()
            self.change_highest_num()
            self.highest_num()
            self.draw_highest_num()
            
            result = self.over_step()
            if result == 2:
                continue
            else:
                self.quit_step()
                break
            
def main():
    Ga = Game()
    Ga.start()
main()


    
    
    
    


        
