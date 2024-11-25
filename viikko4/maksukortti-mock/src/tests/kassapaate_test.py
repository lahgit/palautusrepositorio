import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo.return_value = 10
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo.return_value = 4
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()


    def testi_yksi(self):
        maksukortti1_mock = Mock()

        self.kassa.lataa(maksukortti1_mock, 900)
        maksukortti1_mock.lataa.assert_called_with(900)


    
    def testi_kaksi(self):
        maksukortti2_mock = Mock()

        self.kassa.lataa(maksukortti2_mock, -900)
        maksukortti2_mock.lataa.assert_not_called()

