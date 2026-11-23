# SPDX-License-Identifier: MIT
"""Biomechanical stature sizing and static wrist torque models for solo practice Tai Chi jian."""

from .calculator import (
    STATURE_TIERS_V2,
    StatureTierSpec,
    StatureSelection,
    WristTorqueResult,
    LoadBoundaryAssessment,
    select_stature_tier,
    calculate_static_wrist_torque,
    evaluate_metallurgical_load_boundary,
)

__all__ = [
    "STATURE_TIERS_V2",
    "StatureTierSpec",
    "StatureSelection",
    "WristTorqueResult",
    "LoadBoundaryAssessment",
    "select_stature_tier",
    "calculate_static_wrist_torque",
    "evaluate_metallurgical_load_boundary",
]
__version__ = "2.0.0"
