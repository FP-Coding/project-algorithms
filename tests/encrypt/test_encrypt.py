import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("certo", "15")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(15, 15)
    result_odd_reversed = encrypt_message("certo", 15)
    result_even_reversed = encrypt_message("certo", 14)
    result_even = encrypt_message("certo", 4)
    result_odd = encrypt_message("certo", 3)

    assert result_odd_reversed == "otrec"
    assert result_even_reversed == "otrec"
    assert result_odd == "rec_ot"
    assert result_even == "o_trec"
