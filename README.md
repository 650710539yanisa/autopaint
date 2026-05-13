# 🎨 Heartopia Auto Painter

An automation tool that paints images in the game **Heartopia** on a **114×150 canvas** using simulated mouse clicks, color matching, and smart palette navigation.


[![Heartopia Auto Painter Demo](https://img.youtube.com/vi/GN28BOSm8ik/0.jpg)](https://www.youtube.com/watch?v=GN28BOSm8ik)


## ✨ Features

### 🖱️ Auto Mouse Click
- Simulates `mouseDown` + `mouseUp` for natural clicking.
- Press `Q` anytime for an emergency stop.

### 🎨 Color Matching
- Resizes the input image to fit the game grid.
- Finds the closest palette color using **RGB Euclidean Distance**.

### 🧩 Grid Coordinate System
- Loads real pixel coordinates from `grid_coords.json`.
- Maps every image pixel to the correct canvas cell automatically.
