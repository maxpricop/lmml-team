import math

SENSORS = ["temperature_c", "humidity_pct", "vibration_g", "acoustic_db", "air_pressure_kpa", "co2_ppm"]
PRIOR_MEAN = {"temperature_c": 13.0, "humidity_pct": 72.0, "vibration_g": 0.12,
              "acoustic_db": 32.0, "air_pressure_kpa": 101.5, "co2_ppm": 510.0}
PRIOR_SD = {"temperature_c": 0.37, "humidity_pct": 0.58, "vibration_g": 0.01,
            "acoustic_db": 0.5, "air_pressure_kpa": 0.1, "co2_ppm": 10.5}
COLLECTIVE = ["vibration_g", "acoustic_db", "co2_ppm"]

BASE_ALPHA = 0.01
DRIFT_ALPHA = 0.1
POINT_Z = 6.0
COLL_Z = 7.0
DRIFT_Z = 2.5
WARMUP = 50

def _num(v):
    try:
        x = float(v)
    except (TypeError, ValueError):
        return None
    return x if math.isfinite(x) else None


class _Zone:
    def __init__(self):
        self.mean = dict(PRIOR_MEAN)
        self.var = {s: PRIOR_SD[s] ** 2 for s in SENSORS}
        self.ewz = {s: 0.0 for s in SENSORS}
        self.n = 0


class Detector:
    def __init__(self):
        self.zones = {}

    def update(self, reading: dict) -> float:
        zone = self.zones.setdefault(reading.get("bunker_zone", "default"), _Zone())
        zone.n += 1
        vals = {s: _num(reading.get(s)) for s in SENSORS}
        if zone.n == 1:
            for s, x in vals.items():
                if x is not None:
                    zone.mean[s] = x

        z = {s: 0.0 if x is None else (x - zone.mean[s]) / math.sqrt(zone.var[s]) for s, x in vals.items()}
        for s in SENSORS:
            zone.ewz[s] += DRIFT_ALPHA * (max(-10.0, min(10.0, z[s])) - zone.ewz[s])

        point = max(abs(v) for v in z.values()) / POINT_Z
        coll = sum(z[s] for s in COLLECTIVE) / COLL_Z
        drift = max(min(abs(zone.ewz[s]), abs(z[s]) * 1.5) if zone.ewz[s] * z[s] > 0 else 0.0
                    for s in SENSORS) / DRIFT_Z
        ratio = max(point, coll, drift)
        score = ratio / (1.0 + ratio)


        a = BASE_ALPHA if ratio < 0.6 else BASE_ALPHA * 0.05
        if zone.n <= WARMUP:
            a = max(a, 1.0 / zone.n)
        for s, x in vals.items():
            if x is None or abs(z[s]) > POINT_Z:
                continue
            d = x - zone.mean[s]
            zone.mean[s] += a * d
            v = (1 - a) * zone.var[s] + a * d * d
            zone.var[s] = min(max(v, (0.7 * PRIOR_SD[s]) ** 2), (1.5 * PRIOR_SD[s]) ** 2)

        return float(max(0.0, min(1.0, score))) if math.isfinite(score) else 0.0