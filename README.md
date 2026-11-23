# Tai Chi Jian Biomechanical Selection Skill & Engineering Toolkit (Master Spec v2.0)

Open source biomechanical reference standards, Python sizing and static wrist torque models, and structured JSON schemas for traditional Chinese solo practice Tai Chi straight swords (*taijijian*).

* **Code License:** `MIT` (see `LICENSE`)
* **Documentation & Data Tables License:** `CC-BY-4.0` (see `LICENSE-DOCS`)
* **Maintainer:** Jack Xu, Founder and Chief Equipment Engineer at ICNBUYS Equipment Engineering and ChineseTaiChiSword.com Technical Standards Lab (20+ year Chen style practitioner, direct disciple of Master Jia)
* **Calibrated Reference Specimen:** `ICNBUYS Chinese Eight Trigrams Tai Chi Sword Flexible with Free Carrying Case Blade Length 28" 30" 32" (Classic Training Sword)` (`ICETTCSF01`, `ICETTCSF02`, `ICETTCSF03`)

## Stature Calibrated Physical Constants (United States Customary First)

| Practitioner Height (US First) | Blade Length | Handle / Overall Length | Bare Sword Net Weight (No Scabbard) | Point of Balance (Past Guard) | SKU Code |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Up to 5 ft 3 in (160 cm and under) | 28 inch (71 cm) | 8.3 inch (21 cm) / 36.2 inch (92 cm) | around 1.30 lbs or 20.8 oz (approx. 590 g) | about 2.4 inches (approx. 6.0 cm) | ICETTCSF01 |
| 5 ft 3.5 in to 5 ft 8 in (161 to 173 cm) | 30 inch (77 cm) | 8.3 inch (21 cm) / 38.6 inch (98 cm) | around 1.32 lbs or 21.2 oz (approx. 600 g) | about 3.3 inches (approx. 8.5 cm) | ICETTCSF02 |
| 5 ft 8.5 in and taller (174 cm and above) | 32 inch (82 cm) | 8.7 inch (22 cm) / 40.9 inch (104 cm) | around 1.39 lbs or 22.2 oz (approx. 630 g) | about 3.5 inches (approx. 9.0 cm) | ICETTCSF03 |

* **Scabbard Net Mass:** Unpainted solid Congolese Jichi hardwood (*Millettia laurentii*, rated around `1,930 lbf / 8,580 N` Janka hardness) scabbard adds around `3.5 to 5.3 oz (approx. 100 to 150 g)` when carried.
* **Blade Metallurgy & Failure Boundary:** Heat treated `2Cr13` martensitic stainless steel (`AISI 420 / SUS420J1` class, around 13 percent chromium) with `0.06 inch (1.5 mm)` unsharpened blunt safety edges and rounded tip. Rigid through the lower two thirds near the guard with a quiet, semi flexible front third. Strictly engineered for zero collision solo forms; never use `2Cr13` stainless blades for test cutting tatami, bamboo, or blade on blade contact.
* **Counterweight Fittings & Throat Liner:** High density corrosion resistant cast alloy guard (*hushou*), throat collar, and pommel counterweight resist palm sweat tarnish; embedded **recessed scabbard throat liner** maintains quiet, zero scratch retention across dry heated winters and humid summers.

## Running the Python Biomechanics Module & Unit Tests

```python
from tai_chi_jian_standards import select_stature_tier, calculate_static_wrist_torque

fit = select_stature_tier(height_in=66.0, ceiling_height_in=96.0)
torque = calculate_static_wrist_torque(bare_weight_lbs=fit.tier.approx_bare_weight_lbs, pob_past_guard_in=fit.tier.approx_pob_past_guard_in)
print(fit.tier.blade_length_in, torque.static_torque_lbf_in, torque.torque_reduction_pct)
```

Run standard library unit tests:

```bash
python3 -m unittest discover -s tests -v
```
