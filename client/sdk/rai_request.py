import ed25519
import base64
import datetime
import hashlib

from urllib import parse

class RAIRequest(object):

    def __init__(self, rai_creds, service:str="transaction"):
        self.creds = rai_creds
        self.region = rai_creds.region
        self.service = service

    def sign(self, body, method, url, headers, query_params, t=datetime.datetime.now(), debug_level:int=0):

        # ISO8601 date/time strings for time of request
        signature_date = t.strftime("%Y%m%dT%H%M%SZ")
        scope_date = t.strftime("%Y%m%d")

        # Authentication scope
        scope = str("{}/{}/{}/rai01_request".format(scope_date, self.region, self.service))

        # SHA256 hash of content
        content_hash = hashlib.sha256(body.encode("utf-8")).hexdigest()

        # Include "x-rai-date" in signed headers
        headers["x-rai-date"] = signature_date

        # Sort and lowercare headers to produce a canonical form
        canonical_headers = ["{}:{}".format(k.lower(), v.strip()) for k, v in headers.items()]
        canonical_headers.sort()

        h_names = [ k.lower() for k in headers ]
        h_names.sort()
        signed_headers = ";".join(h_names)

        # Sort query string
        query_params.sort()

        # Create hash of canonical request
        split_result = parse.urlsplit(url)
        canonical_form = "{}\n{}\n{}\n{}\n\n{}\n{}".format(method,split_result.path,split_result.query,"\n".join(canonical_headers),signed_headers,content_hash)

        if debug_level > 0:
            print("canonial form:")
            print(canonical_form)
            print("")

        canonical_hash = hashlib.sha256(canonical_form.encode("utf-8")).hexdigest()
        # Create and sign "String to sign"
        string_to_sign = "RAI01-ED25519-SHA256\n{}\n{}\n{}".format(signature_date, scope, canonical_hash)
        seed = base64.b64decode(self.creds.private_key)

        signing_key = ed25519.SigningKey(seed)
        sig = signing_key.sign(string_to_sign.encode("utf-8")).hex()

        if debug_level > 0:
            print("string_to_sing:")
            print(string_to_sign)
            print("")
            print("signature:")
            print(sig)
            print("")

        headers["authorization"] = "RAI01-ED25519-SHA256 Credential={}/{}, SignedHeaders={}, Signature={}".format(self.creds.access_key, scope, signed_headers, sig)