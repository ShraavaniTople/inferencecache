from nacl.signing import SigningKey

_signing_key = SigningKey.generate()
_verify_key = _signing_key.verify_key

def sign_output(data: bytes) -> bytes:
    return _signing_key.sign(data).signature

def get_verify_key() -> bytes:
    return _verify_key.encode()
