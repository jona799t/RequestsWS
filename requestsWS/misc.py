import gzip
import zlib

_zlib = zlib.decompressobj()
def decompress(message, encryption):
    if encryption.lower() == "zlib":
        return _zlib.decompress(message).decode("utf-8")
    elif encryption.lower() == "gzip":
        return str(gzip.decompress(message), encoding="utf8")
    elif encryption == None:
        return message
    else:
        exit(f"requestsWS | Error: {encryption} is not supported yet, if you would like for it to be supported please open an issue on Github")