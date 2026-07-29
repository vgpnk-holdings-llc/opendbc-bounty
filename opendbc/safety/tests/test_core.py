#!/usr/bin/env python3
"""Branch-coverage tests for core safety infrastructure (safety.h)."""
import unittest

from opendbc.car.structs import CarParams
from opendbc.safety.tests.libsafety import libsafety_py
from opendbc.safety.tests.common import make_msg


class TestSafetyCore(unittest.TestCase):
  def setUp(self):
    self.safety = libsafety_py.libsafety
    self.safety.set_safety_hooks(CarParams.SafetyModel.body, 0)
    self.safety.init_tests()

  def _rx_body(self, length=8):
    return self.safety.safety_rx_hook(make_msg(0, 0x201, length))

  def test_set_safety_hooks_invalid_mode(self):
    self.assertEqual(-1, self.safety.set_safety_hooks(0xDEAD, 0))

  def test_safety_tick_null_config(self):
    # must be a no-op
    before = self.safety.safety_config_valid()
    self.safety.safety_tick(libsafety_py.ffi.NULL)
    self.assertEqual(before, self.safety.safety_config_valid())

  def test_safety_tick_lagging(self):
    # rx a valid message, then jump the timer past the lag threshold
    self._rx_body()
    self.assertTrue(self.safety.safety_config_valid())
    self.safety.set_controls_allowed(True)
    self.safety.set_timer(int(3e6))
    self.safety.safety_tick_current_safety_config()
    self.assertFalse(self.safety.get_controls_allowed())
    self.assertFalse(self.safety.safety_config_valid())

  def test_safety_tick_healthy(self):
    # rx a valid message and tick immediately: nothing lagging, config stays valid
    self._rx_body()
    self.safety.set_controls_allowed(True)
    self.safety.safety_tick_current_safety_config()
    self.assertTrue(self.safety.get_controls_allowed())
    self.assertTrue(self.safety.safety_config_valid())

  def test_rx_wrong_length_not_whitelisted(self):
    # a registered address with the wrong DLC must not match its rx check
    self._rx_body()
    controls_allowed = self.safety.get_controls_allowed()
    self.safety.safety_rx_hook(make_msg(0, 0x201, 4))
    self.assertEqual(controls_allowed, self.safety.get_controls_allowed())


if __name__ == "__main__":
  unittest.main()
