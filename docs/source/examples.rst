###############
Example Gallery
###############

This gallery contains a collection of manim0.5.0 connected to matplotlib:

.. manim:: ABC

    class ABC(Scene):
        def construct(self):
            abc = Dot().set_color(GREEN)
            self.add(abc)
            self.wait(1)