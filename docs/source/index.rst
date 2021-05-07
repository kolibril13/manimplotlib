manimplotlib - Example Gallery
========================================

This gallery contains a collection of manim 0.6.0 connected to matplotlib :

.. manim:: ConnectingMatplotlib

    import matplotlib.pyplot as plt

    def my_function(amplitude, x):
        return amplitude * np.sin(x)

    def mpl_image_plt(amplitude, x):
        fig, ax = plt.subplots()
        ax.plot(x, my_function(amplitude, x))
        ax.set_ylim(-1, 1)
        fig.canvas.draw()
        img = ImageMobject(fig.canvas.buffer_rgba()).scale(2)
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
            self.play(tr_amplitude.animate.set_value(amp2), run_time=3)



.. .. toctree::
..    :maxdepth: 2
..
..       examples


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`