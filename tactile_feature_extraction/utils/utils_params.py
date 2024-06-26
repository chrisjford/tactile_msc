# tolerances for accuracy metrics
POS_TOL = 0.25  # mm
ROT_TOL = 1.0  # deg
FORCE_TOL = 0.2  # newton
TORQUE_TOL = 0.2  # newton-meter

# label names
POS_LABEL_NAMES = ["x", "y", "z"]
ROT_LABEL_NAMES = ["Rx", "Ry", "Rz"]
FORCE_LABEL_NAMES = ["Fx", "Fy", "Fz"]
TORQUE_LABEL_NAMES = ["Tx", "Ty", "Tz"]
POSE_LABEL_NAMES = [*POS_LABEL_NAMES, *ROT_LABEL_NAMES]
FT_LABEL_NAMES = [*FORCE_LABEL_NAMES, *TORQUE_LABEL_NAMES]
FULL_LABEL_NAMES = [*POS_LABEL_NAMES, *ROT_LABEL_NAMES, *FORCE_LABEL_NAMES, *TORQUE_LABEL_NAMES]