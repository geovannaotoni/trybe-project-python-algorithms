from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("secret", 2) == "terc_es"

    assert encrypt_message("secret", 3) == "ces_ter"

    assert encrypt_message("secret", 10) == "terces"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("secret", "a")
