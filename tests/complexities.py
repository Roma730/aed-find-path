import json
from dataclasses import dataclass, field
from itertools import zip_longest
from statistics import mean, median, stdev
from timeit import repeat
from typing import Any, Callable, List, Optional, Union

import big_o
import matplotlib.pyplot as plt
import numpy as np

Times = List[Union[float, int]]
Sizes = List[int]

NOTATIONS = {
    big_o.complexities.Constant: "O(1)",
    big_o.complexities.Logarithmic: "O(log n)",
    big_o.complexities.Linear: "O(n)",
    big_o.complexities.Linearithmic: "O(n log n)",
    big_o.complexities.Quadratic: "O(n²)",
    big_o.complexities.Cubic: "O(n³)",
    big_o.complexities.Polynomial: "O(nˣ)",
    big_o.complexities.Exponential: "O(2ⁿ)",
}


@dataclass
class ComplexityInferenceData:
    analyzed_function: Callable
    generation_function: Callable[[int], Any]
    order_of_magnitude: int = 4
    base_of_magnitude: int = 10
    execution_quantity: int = 1000
    times_to_repeat: int = 5
    initial_order: int = 2


@dataclass
class MeasurementResults:
    registered_sizes: Sizes
    registered_times: Times
    registered_means: List[float] = field(default_factory=list)
    registered_deviations: List[float] = field(default_factory=list)


def _execute_function(function: Callable, inputs: Any):
    if isinstance(inputs, tuple):
        return function(*inputs)

    return function(inputs)


def measure_execution_times(
        data: ComplexityInferenceData
        ) -> MeasurementResults:
    medians = []
    means = []
    standard_deviations = []

    input_sizes = [
        data.base_of_magnitude**order
        for order in range(
            data.initial_order,
            data.initial_order + data.order_of_magnitude,
        )
    ]

    for input_size in input_sizes:
        inputs = data.generation_function(input_size)

        timer_result = repeat(
            lambda: _execute_function(
                data.analyzed_function,
                inputs,
            ),
            number=data.execution_quantity,
            repeat=data.times_to_repeat,
        )

        medians.append(median(timer_result))
        means.append(mean(timer_result))
        standard_deviations.append(
            stdev(timer_result)
            if len(timer_result) > 1
            else 0
        )

    return MeasurementResults(
        registered_sizes=input_sizes,
        registered_times=medians,
        registered_means=means,
        registered_deviations=standard_deviations,
    )


def infer_complexity(
    input_sizes: Sizes,
    measured_times: Times,
) -> big_o.complexities.ComplexityClass:
    likely_complexity, _ = big_o.infer_big_o_class(
        ns=np.array(input_sizes),
        time=measured_times,
    )

    if (
        likely_complexity is None
        or not isinstance(
            likely_complexity,
            big_o.complexities.ComplexityClass,
        )
    ):
        raise ValueError(
            "Complexidade inferida inválida."
        )

    return likely_complexity


def register_data(
    data: ComplexityInferenceData,
    results: MeasurementResults,
    likely_complexity: big_o.complexities.ComplexityClass,
    id_: int = 1,
) -> str:
    result_data = {
        "funcao_analisada": data.analyzed_function.__name__,
        "funcao_de_geracao": data.generation_function.__name__,
        "ordens_de_grandeza": data.order_of_magnitude,
        "base_de_grandeza": data.base_of_magnitude,
        "quantidade_de_execucoes": data.execution_quantity,
        "vezes_a_repetir": data.times_to_repeat,
        "pontos_medidos": list(
            zip_longest(
                results.registered_sizes,
                results.registered_times,
                results.registered_means,
                results.registered_deviations,
            )
        ),
        "provavel_complexidade": str(likely_complexity),
    }

    complete_path = _generate_file_path(
        data.analyzed_function,
        id_,
    )

    with open(
        f"{complete_path}.json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            result_data,
            file,
            ensure_ascii=False,
            indent=4,
        )

    return str(id_).zfill(3)


def plot_chart(
    data: ComplexityInferenceData,
    results: MeasurementResults,
    likely_complexity: Optional[
        big_o.complexities.ComplexityClass
    ] = None,
    id_: int = 1,
):
    complete_path = _generate_file_path(
        data.analyzed_function,
        id_,
    )

    plt.plot(
        results.registered_sizes,
        results.registered_times,
        "bo-",
    )

    plt.plot(
        results.registered_sizes,
        results.registered_means,
        "ro:",
    )

    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo de execução")

    plt.title(
        f"{data.analyzed_function.__name__}\n"
        f"{likely_complexity or 'Não inferida'}"
    )

    plt.savefig(f"{complete_path}.png")
    plt.close()


def _generate_file_path(
    analyzed_function: Callable,
    id_: int,
):
    path = "tests/results"

    file_name = (
        f"{analyzed_function.__name__}"
        f" - {str(id_).zfill(3)}"
    )

    return f"{path}/{file_name}"
