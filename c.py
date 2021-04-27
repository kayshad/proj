from manim import *


from manim import *
class MaScene(Scene):
    def construct(self):
        l = NumberLine(include_numbers=True)
        l1 = NumberLine(include_numbers=True, unit_size=2)
        self.add(l)
        self.wait()
        dot = Dot([-1, 0, 0]).shift(2*UP)
        dot2 = Dot([1, 0, 0]).shift(2*UP)
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")
        self.add(line, dot, dot2, b1, b2, b1text, b2text)
        self.play(Transform(l, l1),run_time=3)
        self.wait(10)
