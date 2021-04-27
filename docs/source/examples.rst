###############
Example Gallery
###############

This gallery contains a collection of manim0.5.0 connected to matplotlib:

.. manim:: ManimCELogo
    :save_last_frame:
    :ref_classes: MathTex Circle Square Triangle

    class ManimCELogo(Scene):
        def construct(self):
            self.camera.background_color = "#ece6e2"
            logo_green = "#87c2a5"
            logo_blue = "#525893"
            logo_red = "#e07a5f"
            logo_black = "#343434"
            ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
            ds_m.shift(2.25 * LEFT + 1.5 * UP)
            circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
            square = Square(color=logo_blue, fill_opacity=1).shift(UP)
            triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
            logo = VGroup(triangle, square, circle, ds_m)  # order matters
            logo.move_to(ORIGIN)
            self.add(logo)

.. code-block:: python

    from manim import *

    import matplotlib.pyplot as plt


    def my_function(amplitude, x):
        return amplitude * np.sin(x)


    def mpl_image_plt(amplitude, x):
        fig, ax = plt.subplots()
        ax.plot(x, my_function(amplitude, x))
        ax.set_ylim(-1, 1)
        fig.canvas.draw()
        img = ImageMobject(fig.canvas.buffer_rgba()).scale(4.5)
        plt.close(fig)
        return img


    class ConnectingMatplotlib(Scene):
        def construct(self):
            x_values = np.linspace(0, 30, 400)
            amp1 = 0.5
            amp2 = 1
            tr_amplitude = ValueTracker(amp1)
            image = mpl_image_plt(amp1, x_values)
            self.add(image)

            def update_image(mob):
                new_mob = mpl_image_plt(tr_amplitude.get_value(), x_values)
                mob.become(new_mob)

            image.add_updater(update_image)

            self.play(tr_amplitude.set_value, amp2, run_time=3)


.. image:: _static/ConnectingMatplotlib.gif
