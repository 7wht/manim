from manim import * # type: ignore

class scene1(MovingCameraScene):
    def construct(self):
        text = Text(
            "Hello World!",
            font_size = 100
                    )
        circle = Circle(
            radius = 2,
            color = BLUE,
            stroke_width = 12
        )
        circle.set_fill(color = TEAL, opacity = .6)

        self.play(Write(text), run_time = 2)
        self.play(Transform(text, circle), run_time = 1, Animation = linear)
        self.wait(1)
        self.play(Uncreate(text))

        centre = Dot(radius = .05)
        axes = Axes(
            x_range=[-30, 30, 1],
            x_length=60,
            y_range=[-30, 30, 1],
            y_length=60,
            tips=False
        )
        grid = NumberPlane(
            x_range=[-30, 30, 1],
            y_range=[-30, 30, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 2,
                "stroke_opacity": 0.3
            }
        )

        eqn = Text("y = 0.2x²", font_size = 40, color=BLUE)
        eqn.move_to([5,1,0]) # type: ignore
        g = axes.plot(
            lambda x: (.2)*x**2,
            color = BLUE
        )
        g_slow = axes.plot(
            lambda x: (.2)*x**2,
            color = BLUE,
            x_range=[-5, 5],
        )

        eqn2 = Text("y = 2x + 2", font_size = 40, color=RED)
        eqn2.move_to([-4,-1,0]) # type: ignore
        g2 = axes.plot(
            lambda x: 2*x + 2,
            color = RED
            )
        g2_slow = axes.plot(
            lambda x: 2*x + 2,
            color = RED,
            x_range=[-4, 2],
        )

        
        intersecth = Circle(radius=0.7, stroke_width = 7, color=PURPLE)
        intersecth.move_to([-0.91608, 0.16784, 0]) # type: ignore
        intersect = Dot(color=PURPLE, radius=0.07)
        intersect.move_to([-0.91608, 0.16784, 0]) # type: ignore
        intersect2 = intersect.copy()
        info1 = Text("(x, y) =", font_size=40, color=PURPLE)
        info1.move_to([2, -.9, 0]) # type: ignore
        info2 = Text("(-0.91608, 0.16784)", font_size=40, color=PURPLE)
        info2.move_to([3.4, -1.67, 0]) # type: ignore

        eqn3 = Text("y = 0.2x²", font_size = 40, color=BLUE)
        eqn3.move_to([9, 25, 0]) # type: ignore
        eqn4 = Text("y = 2x + 2", font_size = 40, color=RED)
        eqn4.move_to([15, 26, 0]) # type: ignore

        intersecthb = Circle(radius=0.7, stroke_width = 7, color=PURPLE)
        intersecthb.move_to([10.91608, 23.83216, 0]) # type: ignore
        intersectb = Dot(color=PURPLE, radius=0.07)
        intersectb.move_to([10.91608, 23.83216, 0]) # type: ignore
        intersect2b = intersectb.copy()
        info1b = Text("(x, y) =", font_size=40, color=PURPLE)
        info1b.move_to([13.1, 23.83216, 0]) # type: ignore
        info2b = Text("(10.91608, 23.83216)", font_size=40, color=PURPLE)
        info2b.move_to([14, 23, 0]) # type: ignore


        self.add(centre)
        self.play(Create(axes))
        self.play(Write(eqn))
        self.play(Create(g_slow), run_time = 4)
        self.add(g)
        self.play(Write(eqn2))
        self.play(Create(g2_slow), run_time = 4)
        self.add(g2)

        self.play(FadeIn( grid), run_time=2, Animation=linear)
        self.wait(2)

        self.play(Create(intersecth))
        self.play(Transform(intersecth, intersect))
        self.add(intersect2)
        self.play(intersect2.animate.move_to([.9, -.9, 0])) # type: ignore
        self.play(Write(info1))
        self.play(Write(info2))
        self.wait(2)

        self.add(eqn3)
        self.add(eqn4)
        self.play(self.camera.frame.animate.move_to([10.91608, 23.83216, 0]), run_time=2) # type: ignore

        self.play(Create(intersecthb))
        self.play(Transform(intersecthb, intersectb))
        self.add(intersect2b)
        self.play(intersect2b.animate.move_to([12, 23.83216, 0])) # type: ignore
        self.play(Write(info1b))
        self.play(Write(info2b))
        self.wait(2)
