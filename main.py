import cv2
import numpy as np
from pathlib import Path

BASE = Path(__file__).resolve().parent
LEFT_PATH = BASE / "data_left.png"
RIGHT_PATH = BASE / "data_right.png"
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)

# Camera parameters (example calibrated values for this educational demo)
FOCAL_LENGTH_PX = 700.0
BASELINE_CM = 6.0

left = cv2.imread(str(LEFT_PATH))
right = cv2.imread(str(RIGHT_PATH))
if left is None or right is None:
    raise FileNotFoundError("Stereo images not found.")

gray_l = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
gray_r = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)

# StereoBM estimates disparity = horizontal pixel shift between corresponding points.
num_disparities = 16 * 8
block_size = 15
stereo = cv2.StereoBM_create(
    numDisparities=num_disparities,
    blockSize=block_size
)
disparity = stereo.compute(gray_l, gray_r).astype(np.float32) / 16.0

# Keep valid positive disparities.
valid = disparity > 0
disp_vis = np.zeros_like(disparity, dtype=np.uint8)
if np.any(valid):
    dmin, dmax = np.percentile(disparity[valid], [2, 98])
    scaled = np.clip((disparity - dmin) / max(dmax - dmin, 1e-6) * 255, 0, 255)
    disp_vis = scaled.astype(np.uint8)

cv2.imwrite(str(OUT/"disparity_map.png"), disp_vis)

# Depth formula: Z = (f * B) / d
depth_cm = np.zeros_like(disparity, dtype=np.float32)
depth_cm[valid] = (FOCAL_LENGTH_PX * BASELINE_CM) / disparity[valid]

# Convert depth to a displayable map. Very distant/invalid pixels are suppressed.
depth_display = np.zeros_like(depth_cm, dtype=np.uint8)
depth_valid = (depth_cm > 0) & (depth_cm < 1000)
if np.any(depth_valid):
    zmin, zmax = np.percentile(depth_cm[depth_valid], [2, 98])
    normalized = np.clip((depth_cm - zmin) / max(zmax-zmin, 1e-6) * 255, 0, 255)
    depth_display = normalized.astype(np.uint8)
cv2.imwrite(str(OUT/"depth_map.png"), depth_display)

# Report sample median depths around the known object centers.
samples = [
    ("Near object", 155, 195),
    ("Middle object", 355, 185),
    ("Far object", 525, 220),
]
print("Stereo Vision Based Depth Estimation")
print("-------------------------------------")
print(f"Focal length: {FOCAL_LENGTH_PX:.0f} px")
print(f"Baseline:     {BASELINE_CM:.1f} cm")
for name, x, y in samples:
    patch = depth_cm[max(0,y-12):y+12, max(0,x-12):x+12]
    vals = patch[(patch > 0) & (patch < 1000)]
    if len(vals):
        print(f"{name}: estimated depth = {np.median(vals):.2f} cm")
    else:
        print(f"{name}: no valid depth")
print("\nGenerated:")
print("  outputs/disparity_map.png")
print("  outputs/depth_map.png")
