import graph


def ellipse(x, y, x1, y1, a):
    points_list = list()
    for i in range(int(min(x1, x)) - int(a), int(max(x1, x)) + int(a), ++ 1):
        for j in range(int(min(y1, y)) - int(a),
                       int(max(y1, y)) + int(a), ++ 1):
            if ((x - i) ** 2 + (y - j) ** 2) ** 0.5 + \
                    ((x1 - i) ** 2 + (y1 - j) ** 2) ** 0.5 <= a:
                points_list.append(graph.point(i, j))
    return points_list


def ellipse1(x, y, a, b, x1, y1):  # функция для элипсов, наклоненных в правую сторону
    ellipse(131 * a + x1 + x, 33 * b + y1 + y, 121 * a + x1 + x, 56 * b +
            y1 + y, ((131 * a - 121 * a) ** 2 + (56 * b - 33 * b) ** 2) ** 0.5 + 0.5)


def ellipse2(x, y, a, b, x1, y1):  # Функция для элипсов, наклоненных в левую сторону
    ellipse(321 * a + x1 + x, 20 * b + y1 + y, 331 * a + x1 + x, 43 * b +
            y1 + y, ((321 * a - 331 * a) ** 2 + (43 * b - 20 * b) ** 2) ** 0.5 + 0.5)


def plant(a, x, b, y):
    graph.brushColor(0, 102, 53)
    graph.penColor(0, 102, 53)
    graph.penSize(2)
    # Далее ветки
    graph.polyline([(119 *
                     a +
                     x, 27 *
                     b +
                     y), (152 *
                          a +
                          x, 30 *
                          b +
                          y), (174 *
                               a +
                               x, 37 *
                               b +
                               y), (199 *
                                    a +
                                    x, 49 *
                                    b +
                                    y), (213 *
                                         a +
                                         x, 58 *
                                         b +
                                         y), (229 *
                                              a +
                                              x, 71 *
                                              b +
                                              y)])
    graph.polyline([(274 *
                     a +
                     x, 57 *
                     b +
                     y), (286 *
                          a +
                          x, 41 *
                          b +
                          y), (304 *
                               a +
                               x, 26 *
                               b +
                               y), (326 *
                                    a +
                                    x, 14 *
                                    b +
                                    y), (342 *
                                         a +
                                         x, 7 *
                                         b +
                                         y), (362 *
                                              a +
                                              x, 4 *
                                              b +
                                              y), (376 *
                                                   a +
                                                   x, 2 *
                                                   b +
                                                   y)])
    graph.polyline([(270 *
                     a +
                     x, 113 *
                     b +
                     y), (274 *
                          a +
                          x, 103 *
                          b +
                          y), (280 *
                               a +
                               x, 96 *
                               b +
                               y), (287 *
                                    a +
                                    x, 88 *
                                    b +
                                    y), (297 *
                                         a +
                                         x, 80 *
                                         b +
                                         y), (305 *
                                              a +
                                              x, 76 *
                                              b +
                                              y), (314 *
                                                   a +
                                                   x, 76 *
                                                   b +
                                                   y), (321 *
                                                        a +
                                                        x, 75 *
                                                        b +
                                                        y), (329 *
                                                             a +
                                                             x, 78 *
                                                             b +
                                                             y), (333 *
                                                                  a +
                                                                  x, 79 *
                                                                  b +
                                                                  y)])
    graph.polyline([(170 *
                     a +
                     x, 105 *
                     b +
                     y), (178 *
                          a +
                          x, 102 *
                          b +
                          y), (187 *
                               a +
                               x, 100 *
                               b +
                               y), (194 *
                                    a +
                                    x, 100 *
                                    b +
                                    y), (203 *
                                         a +
                                         x, 102 *
                                         b +
                                         y), (210 *
                                              a +
                                              x, 105 *
                                              b +
                                              y), (220 *
                                                   a +
                                                   x, 110 *
                                                   b +
                                                   y), (228 *
                                                        a +
                                                        x, 117 *
                                                        b +
                                                        y), (234 *
                                                             a +
                                                             x, 123 *
                                                             b +
                                                             y), (245 *
                                                                  a +
                                                                  x, 139 *
                                                                  b +
                                                                  y)])
    # Далее ствол
    graph.polygon([(254 * a + x, 53 * b + y), (269 * a + x, 4 * b + y),
                   (275 * a + x, 7 * b + y), (260 * a + x, 56 * b + y)])
    graph.polygon([(244 * a + x, 94 * b + y), (256 * a + x, 60 * b + y),
                   (266 * a + x, 64 * b + y), (254 * a + x, 98 * b + y)])
    graph.rectangle(247 * a + x, 105 * b + y, 263 * a + x, 165 * b + y)
    graph.rectangle(247 * a + x, 225 * b + y, 263 * a + x, 173 * b + y)
    # Далее листья накл. вправо
    ellipse1(0, -3 * b, a, b, x, y)
    ellipse1(11 * a, -2 * b, a, b, x, y)
    ellipse1(21 * a, 0, a, b, x, y)
    ellipse1(33 * a, 5 * b, a, b, x, y)
    ellipse1(51 * a, 11 * b, a, b, x, y)
    ellipse1(50 * a, 71 * b, a, b, x, y)
    ellipse1(65 * a, 71 * b, a, b, x, y)
    ellipse1(81 * a, 78 * b, a, b, x, y)
    # Далее листья накл. влево
    ellipse2(0, 0, a, b, x, y)
    ellipse2(15 * a, -10 * b, a, b, x, y)
    ellipse2(24 * a, -13 * b, a, b, x, y)
    ellipse2(34 * a, -15 * b, a, b, x, y)
    ellipse2(44 * a, -16 * b, a, b, x, y)
    ellipse2(1 * a, 56 * b, a, b, x, y)
    ellipse2(-13 * a, 56 * b, a, b, x, y)
    ellipse2(-26 * a, 64 * b, a, b, x, y)


def panda(x, y, a):
    panda_list = list()
    graph.brushColor("white")
    graph.penColor("White")
    panda_list.append(graph.polygon([(318 *
                                      a +
                                      x, 122 *
                                      a +
                                      y), (328 *
                                           a +
                                           x, 125 *
                                           a +
                                           y), (339 *
                                                a +
                                                x, 133 *
                                                a +
                                                y), (358 *
                                                     a +
                                                     x, 171 *
                                                     a +
                                                     y), (358 *
                                                          a +
                                                          x, 196 *
                                                          a +
                                                          y), (356 *
                                                               a +
                                                               x, 200 *
                                                               a +
                                                               y), (332 *
                                                                    a +
                                                                    x, 220 *
                                                                    a +
                                                                    y), (301 *
                                                                         a +
                                                                         x, 220 *
                                                                         a +
                                                                         y), (285 *
                                                                              a +
                                                                              x, 209 *
                                                                              a +
                                                                              y), (281 *
                                                                                   a +
                                                                                   x, 201 *
                                                                                   a +
                                                                                   y), (280 *
                                                                                        a +
                                                                                        x, 195 *
                                                                                        a +
                                                                                        y), (278 *
                                                                                             a +
                                                                                             x, 157 *
                                                                                             a +
                                                                                             y), (304 *
                                                                                                  a +
                                                                                                  x, 128 *
                                                                                                  a +
                                                                                                  y), (316 *
                                                                                                       a +
                                                                                                       x, 122 *
                                                                                                       a +
                                                                                                       y), (318 *
                                                                                                            a +
                                                                                                            x, 122 *
                                                                                                            a +
                                                                                                            y)]))
    panda_list.extend(
        ellipse(
            402 * a + x,
            184 * a + y,
            296 * a + x,
            184 * a + y,
            130 * a))
    graph.brushColor("black")
    graph.penColor("black")
    panda_list.append(graph.polygon([(276 *
                                      a +
                                      x, 158 *
                                      a +
                                      y), (271 *
                                           a +
                                           x, 154 *
                                           a +
                                           y), (270 *
                                                a +
                                                x, 148 *
                                                a +
                                                y), (272 *
                                                     a +
                                                     x, 138 *
                                                     a +
                                                     y), (278 *
                                                          a +
                                                          x, 130 *
                                                          a +
                                                          y), (291 *
                                                               a +
                                                               x, 121 *
                                                               a +
                                                               y), (300 *
                                                                    a +
                                                                    x, 123 *
                                                                    a +
                                                                    y), (304 *
                                                                         a +
                                                                         x, 127 *
                                                                         a +
                                                                         y), (303 *
                                                                              a +
                                                                              x, 131 *
                                                                              a +
                                                                              y), (276 *
                                                                                   a +
                                                                                   x, 158 *
                                                                                   a +
                                                                                   y)]))
    panda_list.append(graph.polygon([(340 *
                                      a +
                                      x, 133 *
                                      a +
                                      y), (346 *
                                           a +
                                           x, 131 *
                                           a +
                                           y), (353 *
                                                a +
                                                x, 133 *
                                                a +
                                                y), (361 *
                                                     a +
                                                     x, 142 *
                                                     a +
                                                     y), (363 *
                                                          a +
                                                          x, 146 *
                                                          a +
                                                          y), (364 *
                                                               a +
                                                               x, 149 *
                                                               a +
                                                               y), (364 *
                                                                    a +
                                                                    x, 225 *
                                                                    a +
                                                                    y), (358 *
                                                                         a +
                                                                         x, 266 *
                                                                         a +
                                                                         y), (335 *
                                                                              a +
                                                                              x, 288 *
                                                                              a +
                                                                              y), (327 *
                                                                                   a +
                                                                                   x, 290 *
                                                                                   a +
                                                                                   y), (312 *
                                                                                        a +
                                                                                        x, 286 *
                                                                                        a +
                                                                                        y), (304 *
                                                                                             a +
                                                                                             x, 277 *
                                                                                             a +
                                                                                             y), (304 *
                                                                                                  a +
                                                                                                  x, 269 *
                                                                                                  a +
                                                                                                  y), (312 *
                                                                                                       a +
                                                                                                       x, 258 *
                                                                                                       a +
                                                                                                       y), (322 *
                                                                                                            a +
                                                                                                            x, 249 *
                                                                                                            a +
                                                                                                            y), (336 *
                                                                                                                 a +
                                                                                                                 x, 214 *
                                                                                                                 a +
                                                                                                                 y), (351 *
                                                                                                                      a +
                                                                                                                      x, 206 *
                                                                                                                      a +
                                                                                                                      y), (359 *
                                                                                                                           a +
                                                                                                                           x, 198 *
                                                                                                                           a +
                                                                                                                           y), (359 *
                                                                                                                                a +
                                                                                                                                x, 169 *
                                                                                                                                a +
                                                                                                                                y), (354 *
                                                                                                                                     a +
                                                                                                                                     x, 172 *
                                                                                                                                     a +
                                                                                                                                     y), (350 *
                                                                                                                                          a +
                                                                                                                                          x, 168 *
                                                                                                                                          a +
                                                                                                                                          y), (340 *
                                                                                                                                               a +
                                                                                                                                               x, 133 *
                                                                                                                                               a +
                                                                                                                                               y)]))
    panda_list.extend(
        ellipse(
            318 * a + x,
            192 * a + y,
            318 * a + x,
            192 * a + y,
            25 * a))
    panda_list.append(graph.polygon([(286 *
                                      a +
                                      x, 173 *
                                      a +
                                      y), (291 *
                                           a +
                                           x, 175 *
                                           a +
                                           y), (293 *
                                                a +
                                                x, 178 *
                                                a +
                                                y), (294 *
                                                     a +
                                                     x, 185 *
                                                     a +
                                                     y), (292 *
                                                          a +
                                                          x, 194 *
                                                          a +
                                                          y), (290 *
                                                               a +
                                                               x, 197 *
                                                               a +
                                                               y), (286 *
                                                                    a +
                                                                    x, 197 *
                                                                    a +
                                                                    y), (282 *
                                                                         a +
                                                                         x, 196 *
                                                                         a +
                                                                         y), (279 *
                                                                              a +
                                                                              x, 192 *
                                                                              a +
                                                                              y), (278 *
                                                                                   a +
                                                                                   x, 187 *
                                                                                   a +
                                                                                   y), (278 *
                                                                                        a +
                                                                                        x, 183 *
                                                                                        a +
                                                                                        y), (281 *
                                                                                             a +
                                                                                             x, 175 *
                                                                                             a +
                                                                                             y), (286 *
                                                                                                  a +
                                                                                                  x, 173 *
                                                                                                  a +
                                                                                                  y)]))
    panda_list.append(graph.polygon([(278 *
                                      a +
                                      x, 191 *
                                      a +
                                      y), (272 *
                                           a +
                                           x, 230 *
                                           a +
                                           y), (274 *
                                                a +
                                                x, 244 *
                                                a +
                                                y), (276 *
                                                     a +
                                                     x, 256 *
                                                     a +
                                                     y), (299 *
                                                          a +
                                                          x, 271 *
                                                          a +
                                                          y), (319 *
                                                               a +
                                                               x, 243 *
                                                               a +
                                                               y), (318 *
                                                                    a +
                                                                    x, 220 *
                                                                    a +
                                                                    y), (300 *
                                                                         a +
                                                                         x, 221 *
                                                                         a +
                                                                         y), (299 *
                                                                              a +
                                                                              x, 219 *
                                                                              a +
                                                                              y), (301 *
                                                                                   a +
                                                                                   x, 216 *
                                                                                   a +
                                                                                   y), (301 *
                                                                                        a +
                                                                                        x, 213 *
                                                                                        a +
                                                                                        y), (297 *
                                                                                             a +
                                                                                             x, 209 *
                                                                                             a +
                                                                                             y), (291 *
                                                                                                  a +
                                                                                                  x, 208 *
                                                                                                  a +
                                                                                                  y), (285 *
                                                                                                       a +
                                                                                                       x, 209 *
                                                                                                       a +
                                                                                                       y), (281 *
                                                                                                            a +
                                                                                                            x, 202 *
                                                                                                            a +
                                                                                                            y), (278 *
                                                                                                                 a +
                                                                                                                 x, 191 *
                                                                                                                 a +
                                                                                                                 y)]))
    panda_list.append(graph.polygon([(404 *
                                      a +
                                      x, 187 *
                                      a +
                                      y), (409 *
                                           a +
                                           x, 191 *
                                           a +
                                           y), (411 *
                                                a +
                                                x, 201 *
                                                a +
                                                y), (411 *
                                                     a +
                                                     x, 219 *
                                                     a +
                                                     y), (407 *
                                                          a +
                                                          x, 239 *
                                                          a +
                                                          y), (398 *
                                                               a +
                                                               x, 256 *
                                                               a +
                                                               y), (379 *
                                                                    a +
                                                                    x, 275 *
                                                                    a +
                                                                    y), (368 *
                                                                         a +
                                                                         x, 273 *
                                                                         a +
                                                                         y), (353 *
                                                                              a +
                                                                              x, 263 *
                                                                              a +
                                                                              y), (362 *
                                                                                   a +
                                                                                   x, 235 *
                                                                                   a +
                                                                                   y), (382 *
                                                                                        a +
                                                                                        x, 206 *
                                                                                        a +
                                                                                        y), (397 *
                                                                                             a +
                                                                                             x, 190 *
                                                                                             a +
                                                                                             y), (404 *
                                                                                                  a +
                                                                                                  x, 187 *
                                                                                                  a +
                                                                                                  y)]))
    return panda_list


def keyPressed(event):
    global x, y
    if event.keycode == graph.VK_LEFT:
        x = -5
        y = 0
    if event.keycode == graph.VK_UP:
        x = 0
        y = -5
    if event.keycode == graph.VK_RIGHT:  # Right
        x = 5
        y = 0
    if event.keycode == graph.VK_DOWN:  # Down
        x = 0
        y = 5


def update():
    global x, y
    for i in list1:
        graph.moveObjectBy(i, x, y)


x = 0
y = 0
graph.brushColor(255, 175, 128)  # Фон
graph.rectangle(0, 0, 500, 333)
plant(1, 0, 1, 0)
plant(0.322, 89.7, 0.707, 71)
list1 = panda(0, 0, 1)
graph.onKey(keyPressed)
graph.onTimer(update, 1)
graph.run()