# SPDX-License-Identifier: MIT
import unittest

from tai_chi_jian_standards import (
    calculate_static_wrist_torque,
    evaluate_metallurgical_load_boundary,
    select_stature_tier,
)


class TestTaiChiJianStandards(unittest.TestCase):
    def test_three_us_stature_tiers(self):
        t1 = select_stature_tier(62.0)
        self.assertEqual(t1.tier.blade_length_in, 28.0)
        self.assertEqual(t1.tier.sku_code, "ICETTCSF01")
        self.assertAlmostEqual(t1.tier.approx_bare_weight_lbs, 1.30)
        self.assertAlmostEqual(t1.tier.approx_pob_past_guard_in, 2.4)

        t2 = select_stature_tier(66.0)
        self.assertEqual(t2.tier.blade_length_in, 30.0)
        self.assertEqual(t2.tier.sku_code, "ICETTCSF02")
        self.assertAlmostEqual(t2.tier.approx_bare_weight_lbs, 1.32)
        self.assertAlmostEqual(t2.tier.approx_pob_past_guard_in, 3.3)

        t3 = select_stature_tier(70.0, ceiling_height_in=96.0)
        self.assertEqual(t3.tier.blade_length_in, 32.0)
        self.assertEqual(t3.tier.sku_code, "ICETTCSF03")
        self.assertAlmostEqual(t3.tier.approx_bare_weight_lbs, 1.39)
        self.assertAlmostEqual(t3.tier.approx_pob_past_guard_in, 3.5)
        self.assertTrue(t3.ceiling_safe)

    def test_low_indoor_ceiling_flag(self):
        low_room = select_stature_tier(70.0, ceiling_height_in=86.0)
        self.assertFalse(low_room.ceiling_safe)
        self.assertLess(low_room.ceiling_clearance_margin_in, 0.0)

    def test_static_wrist_torque_reduction(self):
        res = calculate_static_wrist_torque(bare_weight_lbs=1.32, pob_past_guard_in=3.3)
        self.assertAlmostEqual(res.static_torque_lbf_in, 6.006, places=2)
        self.assertGreater(res.torque_reduction_pct, 50.0)

    def test_metallurgical_boundary(self):
        cut_res = evaluate_metallurgical_load_boundary(impact_cutting=True)
        self.assertFalse(cut_res.approved_for_2cr13_solo_jian)
        solo_res = evaluate_metallurgical_load_boundary(impact_cutting=False, blade_on_blade_contact=False)
        self.assertTrue(solo_res.approved_for_2cr13_solo_jian)


if __name__ == "__main__":
    unittest.main()
