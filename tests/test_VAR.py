import pandas as pd
import pytest as pytest
import numpy as np

from src.VAR.VAR import get_lags


@pytest.mark.parameteize("test_input, expected", [
    (get_lags(pd.DataFrame(np.arange(0, 100)), pd.DataFrame(np.arange(1, 100))))
])
def test_multi_inputs(test_input, expected):
    assert get_lags()
