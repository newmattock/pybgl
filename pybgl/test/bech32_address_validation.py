import unittest

from pybgl import functions
from pybgl.functions import script as tools


class Bech32AddressValidationTests(unittest.TestCase):
    def test_accepts_uppercase_bech32_address(self):
        public_key = "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
        address_hash = tools.hash160(public_key)
        address = functions.hash_to_address(address_hash)

        self.assertTrue(functions.is_address_valid(address))
        self.assertTrue(functions.is_address_valid(address.upper()))

    def test_rejects_mixed_case_bech32_payload(self):
        public_key = "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
        address_hash = tools.hash160(public_key)
        address = functions.hash_to_address(address_hash)
        mixed_case_payload = address[:4] + address[4].upper() + address[5:]

        self.assertTrue(functions.is_address_valid(address))
        self.assertFalse(functions.is_address_valid(mixed_case_payload))
