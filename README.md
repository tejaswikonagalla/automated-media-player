# Project Overview

In today's fast-paced world, everyone seeks instant and efficient ways to interact with technology. This project provides touch-free and remote-free control over video playback, offering an innovative advancement in human-computer interaction. By leveraging this technology, users can enjoy a more intuitive and natural way to interact with media, potentially transforming media consumption experiences.

This system allows users to control media playback using hand gestures, powered by machine learning algorithms and computer vision techniques. It interprets user gestures and responds accordingly, making life easier and more comfortable by enabling device control from a distance.

## Libraries Used

1. **OpenCV**: An open-source computer vision and machine learning library used for identifying, detecting, and matching features from images captured by a camera.

2. **MediaPipe**: Utilized for identifying hand landmarks and processing time-series data such as video and audio.

3. **PyAutoGUI**: Allows Python scripts to control the mouse and keyboard, automating interactions with applications without any external devices.

4. **Time**: Used to manage pauses and delays during execution.

## Gesture Controls

- **1 Finger Raised**: Moves the video forward.
- **2 Fingers Raised**: Moves the video backward.
- **3 Fingers Raised**: Increases the volume.
- **4 Fingers Raised**: Decreases the volume.
- **5 Fingers Raised**: Plays or pauses the video.

## Advantages

- Provides an innovative and convenient way to interact with multimedia content.
- Enhances user experience by enabling hands-free operation.
- Increases accessibility for individuals with different needs.
- Easy to perform, fast, efficient, and ensures an immediate response.

## Getting Started

To get started with the project, follow these steps:

1. **Clone the Repository**: Clone the project repository to your local machine using:

   ```bash
   git clone <repository-url>
   ```

2. **Install Dependencies**: Navigate to the project directory and install the required libraries using:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**: Execute the main script to start the gesture control application:

   ```bash
   python main.py
   ```

4. **Calibrate**: Follow the on-screen instructions to calibrate the system for your environment.

5. **Enjoy**: Use the specified gestures to control your media playback.

## Contributing

We welcome contributions to enhance the functionality and performance of this project. Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.