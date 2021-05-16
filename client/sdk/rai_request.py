import ed25519
import base64
import datetime
import hashlib

from urllib import parse

class RAIRequest(object):

    def __init__(
        self,
        rai_config,
        method,
        url,
        query_params=[],
        headers=dict(),
        post_params=None,
        body="{}",
        _preload_content=True,
        _request_timeout=None,
        service:str="transaction"
    ):
        self.config = rai_config
        self.service = service
        self.method = method
        self.url = url
        self.query_params = query_params
        self.headers = headers
        self.post_params = post_params
        self.body = body
        self._preload_content = _preload_content
        self._request_timeout = _request_timeout

    def sign(self, t=datetime.datetime.now(), debug_level:int=0):

        # ISO8601 date/time strings for time of request
        signature_date = t.strftime("%Y%m%dT%H%M%SZ")
        scope_date = t.strftime("%Y%m%d")

        # Authentication scope
        scope = str("{}/{}/{}/rai01_request".format(scope_date, self.config.region, self.service))

        # SHA256 hash of content
        content_hash = hashlib.sha256(str(self.body).encode("utf-8")).hexdigest()

        # Include "x-rai-date" in signed headers
        self.headers["x-rai-date"] = signature_date

        # Sort and lowercare headers to produce a canonical form
        canonical_headers = ["{}:{}".format(k.lower(), v.strip()) for k, v in self.headers.items()]
        canonical_headers.sort()

        h_names = [ k.lower() for k in self.headers ]
        h_names.sort()
        signed_headers = ";".join(h_names)

        # Sort query string
        self.query_params.sort()

        # Create hash of canonical request
        split_result = parse.urlsplit(self.url)
        canonical_form = "{}\n{}\n{}\n{}\n\n{}\n{}".format(
            self.method,
            split_result.path,
            split_result.query,
            "\n".join(canonical_headers),
            signed_headers,
            content_hash
        )

        if debug_level > 0:
            print("canonial form:")
            print(canonical_form)
            print("")

        canonical_hash = hashlib.sha256(canonical_form.encode("utf-8")).hexdigest()
        # Create and sign "String to sign"
        string_to_sign = "RAI01-ED25519-SHA256\n{}\n{}\n{}".format(
            signature_date,
            scope,
            canonical_hash
        )

        seed = base64.b64decode(self.config.creds.private_key)

        signing_key = ed25519.SigningKey(seed)
        sig = signing_key.sign(string_to_sign.encode("utf-8")).hex()

        if debug_level > 0:
            print("string_to_sing:")
            print(string_to_sign)
            print("")
            print("signature:")
            print(sig)
            print("")

        self.headers["authorization"] = "RAI01-ED25519-SHA256 Credential={}/{}, SignedHeaders={}, Signature={}".format(
            self.config.creds.access_key,
            scope,
            signed_headers,
            sig
        )