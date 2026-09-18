# PROJECT REPORT
## Stereo Vision Based Depth Estimation

**Student:** Nandini Vashistha  
**Program:** B.Tech CSE (AI & ML)  
**Institution:** VIT Bhopal University  
**Project Area:** Computer Vision

---

## 1. Abstract
Stereo vision is a computer-vision technique used to estimate the distance of objects from a camera system using two images captured from slightly different viewpoints. The principle is similar to human binocular vision. This project implements a basic stereo-vision pipeline in Python using OpenCV. A left and right stereo image are processed to calculate disparity using the StereoBM block-matching algorithm. The disparity is then converted into depth using the stereo-camera equation `Z = fB/d`. The final system produces a disparity map and a depth map, demonstrating that objects with larger disparity are estimated to be closer.

## 2. Introduction
A single camera normally records a 3-D scene as a 2-D image, so direct distance information is lost. Stereo vision addresses this limitation by using two cameras separated by a known distance called the baseline. A point in the scene appears at different horizontal positions in the two images. This difference is called disparity.

If the focal length and baseline are known, depth can be calculated from disparity. Therefore, stereo vision is useful in robotics, autonomous systems, 3-D reconstruction, augmented reality and intelligent transportation.

## 3. Problem Statement
Develop a computer-vision system that takes a pair of stereo images, estimates pixel disparity between corresponding regions, and converts disparity into an approximate depth map.

## 4. Objectives
1. Understand the stereo-vision depth-estimation principle.
2. Process a left/right image pair.
3. Calculate a disparity map.
4. Convert disparity into depth.
5. Visualize the estimated depth.
6. Understand the limitations of block-matching stereo.

## 5. Theoretical Background

### 5.1 Stereo Geometry
Consider two cameras separated by baseline `B`. A 3-D point is projected to different horizontal coordinates in the two images.

The disparity is:

`d = x_left - x_right`

For a rectified stereo pair, depth is:

`Z = (f × B) / d`

where:
- `Z` = depth
- `f` = focal length in pixels
- `B` = camera baseline
- `d` = disparity

Thus, depth is inversely proportional to disparity. A larger disparity generally indicates a closer object.

### 5.2 Disparity Estimation
The project uses OpenCV StereoBM. It compares local image blocks between the left and right images and searches for the horizontal displacement that best matches the blocks.

### 5.3 Depth Map
After disparity is calculated, every valid pixel can be assigned an estimated depth. The resulting depth values are visualized as a grayscale image.

## 6. System Architecture

```text
Left Image ─────┐
                ├──> Grayscale ──> StereoBM ──> Disparity Map
Right Image ────┘                         │
                                          ▼
                                  Z = f × B / d
                                          │
                                          ▼
                                     Depth Map
```

## 7. Methodology

### Step 1: Input
The system loads a left and right stereo image.

### Step 2: Pre-processing
Both images are converted from RGB/BGR to grayscale because stereo block matching mainly requires intensity information.

### Step 3: Disparity Calculation
StereoBM is configured with a block size of 15 pixels and 128 possible disparity values. The algorithm finds corresponding regions and estimates their horizontal displacement.

### Step 4: Depth Calculation
For every valid disparity value:

`Depth = (700 × 6) / disparity`

The focal length used in this educational demonstration is 700 pixels and the baseline is 6 cm.

### Step 5: Visualization
The calculated disparity and depth values are normalized for display and saved as PNG images.

## 8. Implementation
The implementation is contained in `main.py`.

Main processing stages:
- Load images using `cv2.imread()`.
- Convert images to grayscale.
- Create a `StereoBM` matcher.
- Compute disparity.
- Convert disparity into depth using the stereo equation.
- Save disparity and depth maps.

## 9. Experimental Setup
Software:
- Python 3.9+
- OpenCV
- NumPy
- VS Code / terminal

Hardware:
- Any normal computer capable of running Python and OpenCV.

Input:
- `data_left.png`
- `data_right.png`

The supplied images are a controlled synthetic stereo pair created for demonstration. The scene contains objects with different simulated disparities.

## 10. Results and Discussion
When the program is executed, two output images are generated:

1. **Disparity Map** — represents the estimated horizontal displacement between corresponding pixels.
2. **Depth Map** — represents depth calculated from disparity.

The synthetic scene contains objects with disparities of approximately 24, 14 and 8 pixels. Since the depth formula is inversely proportional to disparity, the object with the largest disparity is expected to have the smallest estimated depth.

Using `f = 700 px` and `B = 6 cm`, the theoretical depths are approximately:
- `d = 24 px` → `Z = 175 cm`
- `d = 14 px` → `Z = 300 cm`
- `d = 8 px` → `Z = 525 cm`

Actual StereoBM estimates can differ because block matching is an approximation.

## 11. Advantages
- Simple and inexpensive depth-estimation principle.
- Works with ordinary stereo images.
- Produces dense disparity information in textured areas.
- Easy to implement with OpenCV.

## 12. Limitations
- Accuracy depends strongly on camera calibration.
- Textureless areas can produce unreliable disparity.
- Repeated patterns may cause incorrect correspondences.
- Different lighting between cameras can reduce matching quality.
- StereoBM is relatively basic compared with modern stereo algorithms.

## 13. Applications
Stereo depth estimation is used in:
- Robotics
- Autonomous navigation
- 3-D reconstruction
- Object distance estimation
- Augmented reality
- Industrial inspection
- Intelligent transportation systems

## 14. Future Scope
The project can be extended by:
1. Capturing images from a real stereo camera.
2. Performing camera calibration.
3. Applying stereo rectification.
4. Replacing StereoBM with StereoSGBM.
5. Generating a 3-D point cloud.
6. Implementing real-time depth estimation.

## 15. Conclusion
This project demonstrates the fundamental process of estimating depth from stereo images. The system calculates disparity using block matching and applies the stereo depth equation `Z = fB/d` to obtain an approximate distance for image pixels. The experiment illustrates the key relationship between disparity and depth and provides a foundation for more advanced stereo-vision systems involving calibration, rectification, improved matching and 3-D reconstruction.

## 16. References
1. OpenCV documentation — Stereo correspondence and StereoBM.
2. R. Szeliski, *Computer Vision: Algorithms and Applications*, Springer.
3. Standard pinhole-camera stereo geometry and the relation `Z = fB/d`.
