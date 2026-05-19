import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

# Константы
m = 5.0
mu_static = 1
mu_kinetic = 0.85
g = 9.8
F_max_static = mu_static * m * g

# Переменные
F_applied = 10.0
x_blue = 2.0
x_red = 0.5
v_blue = 0.0
dt = 0.05

fig, ax = plt.subplots(figsize=(10, 5))
plt.subplots_adjust(bottom=0.3)

# Синий блок (высокий)
blue_block = plt.Rectangle((x_blue, 0.2), 0.6, 0.6, fc='blue')
ax.add_patch(blue_block)

# Красный толкач (низкий, стоит на той же линии y = 0.2)
red_block = plt.Rectangle((x_red, 0.2), 0.6, 0.3, fc='red')
ax.add_patch(red_block)

# Опорная линия (пол)
ax.axhline(y=0.2, color='black', linewidth=2)
ax.set_ylim(0, 1.2)
ax.set_xlim(-1, 10)

status_text = ax.text(0.5, 0.9, "Блок НЕ движется", transform=ax.transAxes,
                      ha='center', fontsize=12, color='red')

# Слайдер
ax_slider = plt.axes([0.2, 0.15, 0.6, 0.03])
slider = Slider(ax_slider, 'Сила толкача (Н)', 0, F_max_static * 2, valinit=F_applied)

# Кнопка сброса
ax_button = plt.axes([0.8, 0.05, 0.1, 0.04])
button = Button(ax_button, 'Сброс')

def reset(event):
    global x_blue, x_red, v_blue
    x_blue = 2.0
    x_red = 0.5
    v_blue = 0.0
    blue_block.set_x(x_blue)
    red_block.set_x(x_red)
    slider.set_val(10.0)

button.on_clicked(reset)

def update(frame):
    global x_blue, x_red, v_blue
    F = slider.val
    F_kinetic = mu_kinetic * m * g

    # Движение красного
    a_red = F / m
    x_red += a_red * dt * 0.5

    # Касание (ширина 0.6 у обоих)
    if x_red + 0.6 >= x_blue:
        x_red = x_blue - 0.6

        if F <= F_max_static and v_blue == 0:
            a_blue = 0
        else:
            a_blue = (F - F_kinetic) / m

        v_blue += a_blue * dt
        x_blue += v_blue * dt
        x_red = x_blue - 0.6

        if v_blue < 0:
            v_blue = 0
        if x_blue < 0:
            x_blue = 0
            v_blue = 0
    else:
        v_blue = 0

    if x_red < 0:
        x_red = 0

    blue_block.set_x(x_blue)
    red_block.set_x(x_red)

    if v_blue > 0.01:
        status_text.set_text("Блок ДВИЖЕТСЯ")
        status_text.set_color('green')
    else:
        status_text.set_text("Блок НЕ движется")
        status_text.set_color('red')

    ax.set_title(f"Сила: {F:.1f} Н | F_тр_макс = {F_max_static:.1f} Н | v = {v_blue:.2f} м/с")
    return blue_block, red_block, status_text

ani = animation.FuncAnimation(fig, update, interval=30)
plt.show()