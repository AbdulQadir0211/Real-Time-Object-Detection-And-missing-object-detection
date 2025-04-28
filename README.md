# Real-Time Object Monitoring System

This project implements a real-time object detection and monitoring system that tracks new object placements and missing objects in a video stream. The system uses **YOLOv8** for object detection and **DeepSORT** for tracking.

## Features

- Real-time detection of objects in a video stream using YOLOv8.
- Tracks objects across frames with unique IDs (DeepSORT).
- Alerts for missing or newly placed objects.
- Displays FPS and relevant information in real-time.
- Modular code for easy customization and optimization.

## Setup Instructions

### Using Docker

1. Clone the repository:
    ```bash
    git clone https://github.com/AbdulQadir0211/Real-Time-Object-Detection-And-missing-object-detection.
    cd RealTime-Object-Monitoring
    ```

2. Build the Docker image:
    ```bash
    docker build -t object-monitor .
    ```

3. Run the Docker container:
    ```bash
    docker run -p 8501:8501 object-monitor
    ```

4. Open the application in your browser:
    ```
    http://localhost:8501
    ```

### Without Docker (using Python environment)

1. Clone the repository:
    ```bash
    git clone https://github.com/AbdulQadir0211/Real-Time-Object-Detection-And-missing-object-detection.
    cd RealTime-Object-Monitoring
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run streamlit_app.py
    ```

4. Open the application in your browser:
    ```
    http://localhost:8501
    ```

## Report

The detailed project report is available in the file [report_Abdul_Qadir_ML_Intern.docx](report_AbdulQadir_ML_Intern.docx).

## Sample Output

Here are some sample output frames from the video stream:

- ![Sample Output](output/sample_output.jpg)

- You can download the output video from [this link](output/output_video.mp4).

## Optimizations

- The object detection pipeline has been optimized for **real-time performance** by:
    - Using **YOLOv8n** (lightweight version of YOLO).
    - Processing frames at a reduced resolution during inference.
    - Skipping video writing during testing to maintain FPS.
- Used **DeepSORT** for efficient object tracking and ID management across frames.

## Hardware Used

- **CPU**: Intel i7 7th Gen
- **GPU**: Integrated Intel UHD Graphics
- **RAM**: 12GB

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
