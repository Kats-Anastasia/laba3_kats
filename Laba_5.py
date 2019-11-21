from random import randrange as rnd, choice
import tkinter
import math
import time

# print (dir(math))


class ball():
    def __init__(self, n, x=40, y=450, r=15, color=0):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.time = 0
        self.timer = 0
        self.n = n
        if color == 0:
            self.color = choice(['blue', 'green', 'red', 'brown'])
        else:
            self.color = color
        if n == 0:
            self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
            )
        else:
            d_alfa = math.pi * 2 / n
            alfa = 0
            side = 2 * self.r * math.sin(math.pi / n)
            self.points = []
            x1 = self.x - side / 2
            y1 = self.y - math.sqrt(self.r ** 2 - (side / 2) ** 2)
            self.points += (x1, y1)
            for i in range(n):
                x1 += side * math.sin(alfa)
                y1 += side * math.cos(alfa)
                alfa += d_alfa
                self.points += (x1, y1)
            self.id = canv.create_polygon(self.points, outline="black")
            canv.itemconfig(self.id, fill=self.color)
        self.live = 30

    def set_coords(self):
        if self.n == 0:
            canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
            )
        else:
            for i in range(len(self.points) // 2):
                self.points[2 * i + 1] -= self.vy
                self.points[2 * i] += self.vx
                canv.coords(
                    self.id,
                    self.points
                )

    def move(self):
        """
        Переместить мяч по прошествии единицы времени
        Метод описывает перемещение мяча за один кадр перерисовки. То есть,
        обновляет значения self.x и self.y с учетом скоростей
        self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        friction = 0.96
        if -6 < self.vy < 6 and self.y > 549:
            g = 0
            friction *= 0.75
        else:
            g = 1
        self.vx *= friction
        self.vy = self.vy * friction - g
        if self.y >= 550:
            self.vy *= -1
            friction = friction ** 2
        if self.x >= 785:
            self.vx *= -1
            self.x += self.vx
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()
        self.timer += 0.03
        if abs(self.vy) < 0.001:
            self.time += 0.03

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью,
        описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном
            случае возвращает False.
        """
        if math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y)
                     ** 2) >= self.r + obj.r:
            return False
        else:
            return True


class gun():
    def __init__(self, game):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.y = 450
        # FIXME: don't know how to set it...
        self.id = canv.create_line(20, 450, 50, 420, width=7)
        self.vy = 0.5
        self.game = game

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy
        зависят от положения мыши.
        """
        self.game.bullet += 1
        numbers = [0, 3, 4, 5, 6, 7]
        n1 = choice(numbers)
        new_ball = ball(y=self.y, n=n1)
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)

        self.game.balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan2((event.y - self.y), (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, self.y,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def move(self):
        if self.y - 20 < 0:
            self.vy *= -1
        if self.y + 20 > 540:
            self.vy *= -1
        self.y += self.vy
        canv.coords(self.id, 20, self.y,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )


class target():
    def __init__(self):
        self.point = 0
        self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
        self.id_points = canv.create_text(30, 30, text=self.point, font='28')
        self.vy = 1
        self.id = 0

    def new_target(self, n):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        self.n = n
        if n == 0:
            self.id = canv.create_oval(0, 0, 0, 0)
            canv.coords(self.id, x - r, y - r, x + r, y + r)
        else:
            d_alfa = math.pi * 2 / n
            alfa = 0
            side = 2 * self.r * math.sin(math.pi / n)
            self.points = []
            x1 = self.x - side / 2
            y1 = self.y - math.sqrt(self.r ** 2 - (side / 2) ** 2)
            self.points += (x1, y1)
            for i in range(n):
                x1 += side * math.sin(alfa)
                y1 += side * math.cos(alfa)
                alfa += d_alfa
                self.points += (x1, y1)
            self.id = canv.create_polygon(self.points, outline="black")
        canv.itemconfig(self.id, fill=color)

    def set_coords(self):
        if self.n == 0:
            canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
            )
        else:
            for i in range(len(self.points) // 2):
                self.points[2 * i + 1] += self.vy
                canv.coords(
                    self.id,
                    self.points
                )

    def move(self):
        if self.y - self.r < 0:
            self.vy *= -1
        if self.y + self.r > 600:
            self.vy *= -1
        self.y += self.vy
        self.set_coords()

    def hit(self, point=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.point += point


class Game():
    def __init__(self):
        g1 = gun(self)
        numbers = [0, 3, 4, 5, 6, 7]
        n = choice(numbers)
        t2.new_target(n)
        n = choice(numbers)
        t1.new_target(n)
        self.bullet = 0
        self.balls = []
        canv.bind('<Button-1>', g1.fire2_start)
        canv.bind('<ButtonRelease-1>', g1.fire2_end)

        canv.bind('<Motion>', g1.targetting)
        t1.live = 1
        t2.live = 1
        while t1.live or t2.live or self.balls:
            g1.move()
            if t1.live:
                t1.move()
            if t2.live:
                t2.move()
            for b in self.balls:
                b.move()
                if 0.5 <= b.timer <= 1 and abs(b.vy) > 3:
                    n1 = choice(numbers)

                    new_ball_1 = ball(
                        y=b.y, x=b.x, n=n1, r=15 / math.sqrt(2), color=b.color)
                    new_ball_1.vx = b.vx + 5
                    new_ball_1.vy = b.vy + 5
                    self.balls += [new_ball_1]
                    n1 = choice(numbers)
                    new_ball_2 = ball(
                        y=b.y, x=b.x, n=n1, r=15 / math.sqrt(2), color=b.color)
                    new_ball_2.vx = b.vx - 5
                    new_ball_2.vy = b.vy - 5
                    self.balls += [new_ball_2]
                    b.timer = 2
                    canv.delete(b.id)
                    new_ball_1.timer = 2
                    new_ball_2.timer = 2
                if b.time >= 1:
                    canv.delete(b.id)
                if b.hittest(t1) and t1.live:
                    t1.live = 0
                    t1.hit()
                if b.hittest(t2) and t2.live:
                    t2.live = 0
                    t2.hit()
                if t1.live == 0 and t2.live == 0:
                    canv.delete(g1.id)
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
                    canv.itemconfig(
                        screen1,
                        text='Вы уничтожили цели за ' +
                        str(self.bullet) +
                        ' выстрелов')
                    canv.itemconfig(t1.id_points, text=t1.point)
                    canv.itemconfig(t2.id_points, text=t2.point)
                    for bb in self.balls:
                        canv.delete(bb.id)
                    self.balls = []
            canv.update()
            time.sleep(0.03)
            g1.targetting()
            g1.power_up()
        time.sleep(3)
        canv.itemconfig(screen1, text='')
        Game()


root = tkinter.Tk()
fr = tkinter.Frame(root)
root.geometry('800x600')
canv = tkinter.Canvas(root, bg='white')
canv.pack(fill=tkinter.BOTH, expand=1)
t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
Game()
