# Stereo Vision Based Depth Estimation

## 1. Project Overview
This project demonstrates **depth estimation from a pair of stereo images** using OpenCV. A stereo camera setup captures a left and a right image of the same scene. The horizontal shift between corresponding points is called **disparity**. Once disparity is obtained, depth can be estimated using:

**Z = (f × B) / d**

where:
- `Z` = depth/distance from the camera
- `f` = camera focal length in pixels
- `B` = distance between the two cameras (baseline)
- `d` = disparity in pixels

The project uses OpenCV's **StereoBM** block-matching algorithm to create a disparity map and then converts disparity into a depth map.

## 2. Objectives
- Understand the basic principle of stereo vision.
- Generate disparity from a left/right image pair.
- Apply the stereo depth equation.
- Visualize disparity and estimated depth.
- Demonstrate how larger disparity corresponds to a nearer object.

## 3. Technologies
- Python 3.9+
- OpenCV
- NumPy

## 4. Project Structure
```text
stereo_vision_depth_estimation/
├── main.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
├── data_left.png
├── data_right.png
└── outputs/
    ├── disparity_map.png
    └── depth_map.png   # generated after running
```

## 5. How to Run

### Step 1: Install Python
Install Python 3.9 or newer.

### Step 2: Open the project folder
Open the folder in VS Code or a terminal.

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run
```bash
python main.py
```

The program prints estimated depths and creates:
- `outputs/disparity_map.png`
- `outputs/depth_map.png`

## 6. Methodology
1. Read the left and right stereo images.
2. Convert both images to grayscale.
3. Use StereoBM to calculate disparity.
4. Remove invalid/negative disparity values.
5. Apply `Z = fB/d` to estimate depth.
6. Save visual disparity and depth maps.

## 7. Important Parameters
The demo uses:
- Focal length = 700 pixels
- Baseline = 6 cm
- StereoBM block size = 15
- Number of disparities = 128

For a real stereo camera, focal length and baseline should come from camera calibration rather than being guessed.

## 8. Expected Result
The disparity map highlights pixels according to their horizontal displacement. Objects with larger disparity are closer to the cameras. The depth map converts these disparity values into estimated distances.

## 9. Limitations
- This educational demo uses synthetic stereo images.
- The camera parameters are example values.
- StereoBM can be affected by textureless regions, repeated patterns and illumination differences.
- A real-world implementation should include stereo camera calibration and image rectification.

## 10. Future Scope
- Use real stereo-camera images.
- Add camera calibration and rectification.
- Compare StereoBM with StereoSGBM.
- Add point-cloud generation.
- Build a real-time stereo-camera application.

## 11. References
- OpenCV documentation: StereoBM / stereo correspondence concepts.
- Standard stereo-vision formulation: depth is inversely proportional to disparity, `Z = fB/d`.
