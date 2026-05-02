import typer
from typing import Optional
from lab_package import lab4 as lab4_module
from lab_package import lab5 as lab5_module
from lab_package import lab6 as lab6_module

app = typer.Typer(help="Выбор лабораторной работы (№4, №5, №6)")


@app.command()
def lab4(
    list_str: str = typer.Argument(..., help="Список, например: [1,2,[3,4]]")
):
    """Лабораторная работа №4 - Подсчёт элементов"""
    try:
        lst = eval(list_str)
        result = lab4_module.recursive(lst)
        typer.echo(f"Количество элементов: {result}")
    except Exception as e:
        typer.echo(f"Ошибка: {e}")


@app.command()
def lab5(
    operation: str = typer.Argument(..., help="Операция: +, -, mul, /"),
    x: float = typer.Argument(..., help="Число для операции"),
    initial: float = typer.Option(1, "--initial", "-i", help="Начальное значение")
):
    """Лабораторная работа №5 - Замыкание make_calc"""
    try:
        # Заменяем mul на * для вашей функции
        if operation == "mul":
            operation = "*"
        calc_func = lab5_module.make_calc(operation, initial)
        result = calc_func(x)
        typer.echo(f"Результат: {result}")
    except Exception as e:
        typer.echo(f"Ошибка: {e}")


@app.command()
def lab6(
    count: int = typer.Option(1, "--count", "-n", help="Количество чисел"),
    min_val: int = typer.Option(1, "--min", "-a", help="Минимальное значение"),
    max_val: int = typer.Option(67, "--max", "-b", help="Максимальное значение"),
    seed: Optional[int] = typer.Option(None, "--seed", "-s", help="Начальное зерно")
):
    """Лабораторная работа №6 - Генератор случайных чисел"""
    try:
        if seed is not None:
            lab6_module.init_rng(seed)
        results = lab6_module.generate(count, min_val, max_val)
        if count == 1:
            typer.echo(f"Случайное число: {results[0]}")
        else:
            typer.echo(f"Случайные числа: {results}")
    except Exception as e:
        typer.echo(f"Ошибка: {e}")


if __name__ == "__main__":
    app()