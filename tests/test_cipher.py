from crypto.cipher import encrypt, decrypt, crack
import pytest

def test_encrypt_with_a_single_shift():
    actual = encrypt("BOY", 1)
    expected = "CPZ"
    assert actual == expected

def test_decrypt_prev_encrypted():
    actual = decrypt("CPZ", 1)
    expected = "BOY"
    assert actual == expected


def test_encrypt_hand_upper_lower():
    actual = encrypt("NicE Day", 7)
    expected = "UpjL Khf"
    assert actual == expected


def test_enecrypt_handle_special_chars():
    actual = encrypt("Who? Me?!", 3)
    expected = "Zkr? Ph?!"
    assert actual == expected

def test_decrypt_long_text():
    actual = decrypt("IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APONAN HATTEXCV SDV", 15)
    expected = "THE QUICK BROWN FOX JUMPED OVER THE LAZYLY SLEEPING DOG"
    assert actual == expected

def test_crack_without_knowing_the_key():
    # shifted by 15
    actual = crack("Xi lph iwt qthi du ixbth, xi lph iwt ldghi du ixbth.")
    expected = "It was the best of times, it was the worst of times."
    assert actual == expected