import argparse
import logging
from typing import Optional

from consts import (
    conversion_factors_mass,
    conversion_functions_temperature,
    conversion_factors_length,
    log_file,
)


def convert_mass(value: float, from_unit: str, to_unit: str) -> Optional[float]:
    """
    Конвертация массы из одной единицы в другую.

    Parameters:
        value (float): Значение массы для конвертации.
        from_unit (str): Исходная единица измерения (граммы, килограммы, фунты, унции).
        to_unit (str): Единица измерения, в которую нужно конвертировать.

    Returns:
        Optional[float]: Конвертированное значение массы или None, если единицы измерения неверны.
    """

    if (
        from_unit not in conversion_factors_mass
        or to_unit not in conversion_factors_mass
    ):
        logging.error(
            f"Ошибка конвертации массы: неверные единицы '{from_unit}' в '{to_unit}'."
        )
        return None

    value_in_grams = value * conversion_factors_mass[from_unit]
    converted_value = value_in_grams / conversion_factors_mass[to_unit]
    logging.info(
        f"Конвертация массы: {value} {from_unit} = {converted_value} {to_unit}."
    )
    return converted_value


def convert_temperature(value: float, from_unit: str, to_unit: str) -> Optional[float]:
    """
    Конвертация температуры из одной единицы в другую.

    Parameters:
        value (float): Значение температуры для конвертации.
        from_unit (str): Исходная единица измерения (Цельсий, Фаренгейт, Кельвин).
        to_unit (str): Единица измерения, в которую нужно конвертировать.

    Returns:
        Optional[float]: Конвертированное значение температуры или None, если единицы измерения неверны.
    """

    if (
        from_unit in conversion_functions_temperature
        and to_unit in conversion_functions_temperature[from_unit]
    ):
        converted_value = conversion_functions_temperature[from_unit][to_unit](value)
        logging.info(
            f"Конвертация температуры: {value} {from_unit} = {converted_value} {to_unit}."
        )
        return converted_value

    logging.error(
        f"Ошибка конвертации температуры: неверные единицы '{from_unit}' в '{to_unit}'."
    )
    return None


def convert_length(value: float, from_unit: str, to_unit: str) -> Optional[float]:
    """
    Конвертация длины из одной единицы в другую.

    Parameters:
        value (float): Значение длины для конвертации.
        from_unit (str): Исходная единица измерения (метры, километры, мили, футы).
        to_unit (str): Единица измерения, в которую нужно конвертировать.

    Returns:
        Optional[float]: Конвертированное значение длины или None, если единицы измерения неверны.
    """
    if from_unit in conversion_factors_length and to_unit in conversion_factors_length:
        converted_value = value * (
            conversion_factors_length[from_unit] / conversion_factors_length[to_unit]
        )
        logging.info(
            f"Конвертация длины: {value} {from_unit} = {converted_value} {to_unit}."
        )
        return converted_value

    logging.error(
        f"Ошибка конвертации длины: неверные единицы '{from_unit}' в '{to_unit}'."
    )
    return None


def main() -> None:
    """
    Основная функция, которая запускает конвертер единиц измерения.
    """
    parser = argparse.ArgumentParser(description="Конвертер единиц измерения.")

    parser.add_argument(
        "-log",
        type=str,
        default=log_file,
        help="Файл для записи логов. Если не указан, используется файл по умолчанию.",
    )

    parser.add_argument(
        "-unit",
        type=str,
        required=True,
        help=(
            "Исходные единицы:\n"
            f"  Масса: {', '.join(conversion_factors_mass.keys())}\n"
            f"  Температура: {', '.join(conversion_functions_temperature.keys())}\n"
            f"  Длина: {', '.join(conversion_factors_length.keys())}."
        ),
    )

    parser.add_argument(
        "-translation",
        type=str,
        required=True,
        help=(
            "Единица для перевода:\n"
            f"  Масса: {', '.join(conversion_factors_mass.keys())}\n"
            f"  Температура: {', '.join(conversion_functions_temperature.keys())}\n"
            f"  Длина: {', '.join(conversion_factors_length.keys())}."
        ),
    )

    parser.add_argument("value", type=float, help="Числовое значение для конвертации.")

    args = parser.parse_args()

    # Настройка логирования в указанный файл
    if args.log is not None:
        logging.basicConfig(
            filename=args.log,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    # Определяем, какую функцию конвертации использовать
    match args.unit:
        case unit if unit in conversion_factors_mass.keys():
            result = convert_mass(args.value, args.unit, args.translation)

        case unit if unit in conversion_functions_temperature.keys():
            result = convert_temperature(args.value, args.unit, args.translation)

        case unit if unit in conversion_factors_length.keys():
            result = convert_length(args.value, args.unit, args.translation)

        case _:
            logging.error("Ошибка: неверные единицы измерения.")
            result = None

    if result is not None:
        print("{} {} = {} {}".format(args.value, args.unit, result, args.translation))
        logging.info("Конвертация выполнена успешно.")
    else:
        print("Ошибка: Неверные единицы измерения.")
        logging.error(f"Ошибка конвертации. Неверно указаны единицы измерения.")


if __name__ == "__main__":
    main()
