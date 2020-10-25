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


import os
import sys
from pathlib import Path

if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(
        f"manim  -l --custom_folders  --disable_caching -i -m -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' "
        + script_name
    )
