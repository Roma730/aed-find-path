from time import sleep

import big_o

from challenges.find_path import (
    find_path,
)

from tests.complexities import (
    NOTATIONS,
    ComplexityInferenceData,
    infer_complexity,
    measure_execution_times,
)

from tests.generators import (
    generate_city_map,
)


def test_evaluate_time_find_path():

    highest_acceptable_complexity = (
        big_o.complexities.Linearithmic
    )

    for _ in range(3):

        data = ComplexityInferenceData(
            analyzed_function=find_path,
            generation_function=generate_city_map,
            order_of_magnitude=5,
            initial_order=3,
            base_of_magnitude=4,
            execution_quantity=3,
            times_to_repeat=3,
        )

        results = measure_execution_times(
            data
        )

        observed_complexity = (
            infer_complexity(
                results.registered_sizes,
                results.registered_times,
            )
        )

        if (
            observed_complexity
            <= highest_acceptable_complexity
        ):
            break

        sleep(2)

    else:

        assert False, (
            "Seu algoritmo parece ser "
            f"{NOTATIONS[observed_complexity.__class__]}"
            ", mas deveria ser no máximo "
            f"{NOTATIONS[highest_acceptable_complexity]}"
        )
