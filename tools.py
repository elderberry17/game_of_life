import pygame as pg
from grid_class import Grid
from const import width, height, extra_height, colors_dict, cell_size
from simulator_class import Simulation

pg.init()

# переменная дисплея и часиков для отслеживания времени
display = pg.display.set_mode((width, height + extra_height))
pg.display.set_caption('The Game of Life')
clock = pg.time.Clock()

# главный класс сетки, содержащий в себе классы ячеек
main_grid = Grid(display, colors_dict, cell_size)
main_grid.make_cells()

# созададим класс, который примет нашу сетку и будет обновлять цвета ее ячеек в зависимости от текущей ситуации
main_simulator = Simulation(main_grid)


# функция для начального окрашивания 10 ячеек
def check_click(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        x_click, y_click = event.pos[0] // cell_size * cell_size, event.pos[1] // cell_size * cell_size
        index = x_click // cell_size * height // cell_size + y_click // cell_size
        if main_grid.cells[index].color != colors_dict["life"]:
            main_grid.cells[index].change_color(colors_dict["life"])
            return True
    return False


# для логирования текста
def logging(gen, population, sim, set_cells):
    display.fill(colors_dict["back"])
    font = pg.font.SysFont("arial", 28)
    color = colors_dict["text"]
    if not sim:
        log_sim = font.render(f'Set {set_cells} more creatures wherever you want', True, color)
        text_rect = log_sim.get_rect(center=(width // 2, height + extra_height // 2))
        display.blit(log_sim, text_rect)
    else:
        log_gen = font.render(f'Generation: {gen}   Population: {population}', True, color)
        text_rect = log_gen.get_rect(center=(width // 2, height + extra_height // 2))
        display.blit(log_gen, text_rect)


def show_end(gens, pops):
    display.fill(colors_dict["back"])
    font = pg.font.SysFont("arial", 28)
    over_log = font.render(f"The game is over. Max population {max(pops)} in {gens[-1]} generations", True,
                           colors_dict["text"])
    over_rect = over_log.get_rect(center=(width // 2, (height + extra_height) // 2 - cell_size // 2))
    display.blit(over_log, over_rect)
    pg.display.update()


# для отрисовки всего на свете и обновления поля
def draw():
    main_grid.draw_cells()
    main_grid.draw_grid()

    pg.display.update()
