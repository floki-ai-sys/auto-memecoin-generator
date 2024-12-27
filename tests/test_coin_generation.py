import pytest
from ai.coin_name_generator import generate_memecoin_name

def test_generate_memecoin_name():
    name = generate_memecoin_name()
    assert isinstance(name, str)
    assert len(name) > 0
    assert "Coin" in name or "Token" in name
