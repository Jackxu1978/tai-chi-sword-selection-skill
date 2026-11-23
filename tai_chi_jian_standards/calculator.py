# SPDX-License-Identifier: MIT
"""Pure Python biomechanical sizing, ceiling clearance, and static wrist torque models.

Maintained by Jack Xu (ICNBUYS Equipment Engineering / ChineseTaiChiSword.com Technical Standards Lab).
Documentation and physical constants are additionally available under CC-BY-4.0.
"""

from dataclasses import dataclass
import math
from typing import Optional, Tuple

LBF_IN_TO_NEWTON_METER = 0.1129848290276167
LBS_TO_GRAMS = 453.59237
INCHES_TO_CM = 2.54


@dataclass(frozen=True)
class StatureTierSpec:
    """Master Spec v2.0 physical constants for a stature calibrated solo practice Tai Chi jian."""

    tier_number: int
    sku_code: str
    stature_label_us: str
    min_height_in: float
    max_height_in: float
    blade_length_in: float
    blade_length_cm: float
    handle_length_in: float
    handle_length_cm: float
    overall_length_in: float
    overall_length_cm: float
    approx_bare_weight_lbs: float
    approx_bare_weight_oz: float
    approx_bare_weight_g: int
    approx_pob_past_guard_in: float
    approx_pob_past_guard_cm: float
    scabbard_weight_oz_range: Tuple[float, float] = (3.5, 5.3)
    scabbard_weight_g_range: Tuple[int, int] = (100, 150)
    blade_alloy: str = "Heat treated 2Cr13 martensitic stainless steel (AISI 420 / SUS420J1 class, ~13% Cr)"
    blunt_edge_thickness_in: float = 0.06
    staged_stiffness: str = "Rigid lower two thirds near guard; quiet semi flexible front third"
    fitting_alloy: str = "Corrosion resistant cast alloy guard, throat collar, and pommel counterweight"
    hardwood_janka_lbf: int = 1930
    scabbard_retention: str = "Recessed scabbard throat liner"


STATURE_TIERS_V2: Tuple[StatureTierSpec, ...] = (
    StatureTierSpec(
        tier_number=1,
        sku_code="ICETTCSF01",
        stature_label_us="Up to 5 ft 3 in (160 cm and under)",
        min_height_in=48.0,
        max_height_in=63.0,
        blade_length_in=28.0,
        blade_length_cm=71.0,
        handle_length_in=8.3,
        handle_length_cm=21.0,
        overall_length_in=36.2,
        overall_length_cm=92.0,
        approx_bare_weight_lbs=1.30,
        approx_bare_weight_oz=20.8,
        approx_bare_weight_g=590,
        approx_pob_past_guard_in=2.4,
        approx_pob_past_guard_cm=6.0,
    ),
    StatureTierSpec(
        tier_number=2,
        sku_code="ICETTCSF02",
        stature_label_us="5 ft 3.5 in to 5 ft 8 in (161 to 173 cm)",
        min_height_in=63.5,
        max_height_in=68.0,
        blade_length_in=30.0,
        blade_length_cm=77.0,
        handle_length_in=8.3,
        handle_length_cm=21.0,
        overall_length_in=38.6,
        overall_length_cm=98.0,
        approx_bare_weight_lbs=1.32,
        approx_bare_weight_oz=21.2,
        approx_bare_weight_g=600,
        approx_pob_past_guard_in=3.3,
        approx_pob_past_guard_cm=8.5,
    ),
    StatureTierSpec(
        tier_number=3,
        sku_code="ICETTCSF03",
        stature_label_us="5 ft 8.5 in and taller (174 cm and above)",
        min_height_in=68.5,
        max_height_in=86.0,
        blade_length_in=32.0,
        blade_length_cm=82.0,
        handle_length_in=8.7,
        handle_length_cm=22.0,
        overall_length_in=40.9,
        overall_length_cm=104.0,
        approx_bare_weight_lbs=1.39,
        approx_bare_weight_oz=22.2,
        approx_bare_weight_g=630,
        approx_pob_past_guard_in=3.5,
        approx_pob_past_guard_cm=9.0,
    ),
)


@dataclass(frozen=True)
class StatureSelection:
    """Computed blade tier recommendation with indoor ceiling safety verification."""

    tier: StatureTierSpec
    effective_height_in: float
    overhead_peak_arc_in: float
    ceiling_clearance_margin_in: Optional[float]
    ceiling_safe: bool
    inverted_ear_test_check: str


@dataclass(frozen=True)
class WristTorqueResult:
    """Static cantilever wrist torque around the middle finger living grip (huo ba) fulcrum."""

    effective_lever_arm_in: float
    static_torque_lbf_in: float
    static_torque_n_m: float
    reference_cutter_torque_lbf_in: float
    reference_cutter_torque_n_m: float
    torque_reduction_pct: float


@dataclass(frozen=True)
class LoadBoundaryAssessment:
    """Metallurgical failure boundary evaluation for 2Cr13 martensitic stainless blades."""

    approved_for_2cr13_solo_jian: bool
    mechanical_regime: str
    engineering_rationale: str


def select_stature_tier(
    height_in: float,
    arm_span_in: Optional[float] = None,
    ceiling_height_in: Optional[float] = None,
) -> StatureSelection:
    """Map practitioner height, optional arm span, and room ceiling height to Master Spec v2.0."""
    if height_in < 48.0 or height_in > 86.0:
        raise ValueError("height_in must be between 48.0 and 86.0 inches.")

    effective_h = float(height_in)
    if arm_span_in is not None:
        delta = arm_span_in - height_in
        if abs(delta) >= 2.0:
            effective_h += 0.5 * delta

    if effective_h <= 63.25:
        chosen = STATURE_TIERS_V2[0]
    elif effective_h <= 68.25:
        chosen = STATURE_TIERS_V2[1]
    else:
        chosen = STATURE_TIERS_V2[2]

    overhead_peak = round(0.80 * height_in + chosen.blade_length_in + 4.0, 2)
    margin = None
    is_safe = True
    if ceiling_height_in is not None:
        margin = round(ceiling_height_in - overhead_peak, 2)
        is_safe = margin >= 0.0

    return StatureSelection(
        tier=chosen,
        effective_height_in=round(effective_h, 2),
        overhead_peak_arc_in=overhead_peak,
        ceiling_clearance_margin_in=margin,
        ceiling_safe=is_safe,
        inverted_ear_test_check="Confirm inverted guard in left palm places rounded tip between lower earlobe and ear top.",
    )


def calculate_static_wrist_torque(
    bare_weight_lbs: float,
    pob_past_guard_in: float,
    middle_finger_pivot_offset_in: float = 1.25,
    elevation_angle_deg: float = 0.0,
    ref_cutter_weight_lbs: float = 2.00,
    ref_cutter_pob_past_guard_in: float = 5.50,
) -> WristTorqueResult:
    """Compute radial/ulnar static wrist torque relative to a forward weighted cutting sword."""
    if bare_weight_lbs <= 0 or pob_past_guard_in < 0:
        raise ValueError("Weight must be positive and balance distance non negative.")

    cos_theta = math.cos(math.radians(elevation_angle_deg))
    lever_in = pob_past_guard_in + middle_finger_pivot_offset_in
    torque_lbf_in = bare_weight_lbs * lever_in * cos_theta
    torque_n_m = torque_lbf_in * LBF_IN_TO_NEWTON_METER

    ref_lever_in = ref_cutter_pob_past_guard_in + middle_finger_pivot_offset_in
    ref_torque_lbf_in = ref_cutter_weight_lbs * ref_lever_in * cos_theta
    ref_torque_n_m = ref_torque_lbf_in * LBF_IN_TO_NEWTON_METER

    reduction = 0.0
    if ref_torque_lbf_in > 0:
        reduction = (1.0 - (torque_lbf_in / ref_torque_lbf_in)) * 100.0

    return WristTorqueResult(
        effective_lever_arm_in=round(lever_in, 3),
        static_torque_lbf_in=round(torque_lbf_in, 3),
        static_torque_n_m=round(torque_n_m, 4),
        reference_cutter_torque_lbf_in=round(ref_torque_lbf_in, 3),
        reference_cutter_torque_n_m=round(ref_torque_n_m, 4),
        torque_reduction_pct=round(reduction, 2),
    )


def evaluate_metallurgical_load_boundary(
    impact_cutting: bool = False,
    blade_on_blade_contact: bool = False,
) -> LoadBoundaryAssessment:
    """Enforce metallurgical safety boundary for 2Cr13 martensitic stainless blades."""
    if impact_cutting or blade_on_blade_contact:
        return LoadBoundaryAssessment(
            approved_for_2cr13_solo_jian=False,
            mechanical_regime="High shock impact or contact sparring",
            engineering_rationale=(
                "Prohibited: 2Cr13 martensitic stainless steel (AISI 420 class) has lower Charpy "
                "impact toughness than 9260 or 1095 spring carbon steel and must never strike "
                "tatami mats, bamboo, hard targets, or another weapon."
            ),
        )
    return LoadBoundaryAssessment(
        approved_for_2cr13_solo_jian=True,
        mechanical_regime="Zero collision solo Tai Chi form practice",
        engineering_rationale=(
            "Approved: Under target free solo kinematics, heat treated 2Cr13 provides rigid lower "
            "two thirds alignment, elastic recovery in the distal third, and high sweat corrosion resistance."
        ),
    )
