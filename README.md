<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">


  <h1 align="center">Optical Flow </h1>


</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary><h3>Table of Contents</h3></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#demo">Demo</a></li>
      </ul>
    </li>
    <li>
      <a href="#pipeline">Pipeline</a>
      <ul>
        <li><a href="#results">Results</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#contributors">Contributors</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



This repository presents a program that utilizes Sparse Optical Flow to detect and track a moving vehicle, which could find applications in speed-limit enforcement.

Summary of tasks achieved:
* The program detects the moving vehicle by taking the difference between two consecutive images, contour detection, SIFT feature matching, and pixel displacement.
* The program computes the speed of the vehicle by taking the average of the pixel displacement of various features of the vehicle detected using SIFT.
* The program achieves an accuracy of 99% for various speeds.
* The program can be executed in real-time, allowing for quick and efficient detection and tracking of moving vehicles.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Demo

<div align="center">


  <h4 align="center">Output for vehicle speed of 10mph</h4>


</div>

<img src="https://github.com/KACHAPPILLY2021/optical_flow/blob/main/gif/output_10mph.gif?raw=true"  alt="output">
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!--Pipeline and Results -->
## Pipeline

* The slides with detailed explanation can be found [here](https://github.com/KACHAPPILLY2021/optical_flow/blob/main/presentation.pptx). 
* And flowchart represents the formulated pipeline to detect speed. 
<img src="https://github.com/KACHAPPILLY2021/optical_flow/blob/main/gif/flowchart.png?raw=true"  alt="pipeline">
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Results

More video results with different vehicle speeds can be found [here](https://github.com/KACHAPPILLY2021/optical_flow/tree/main/results).
<div align="center">


  <h4 align="center">Accuracies for different vehicle speeds:</h4>


</div>

<img src=https://github.com/KACHAPPILLY2021/optical_flow/blob/main/results/accuracy/10mph.png width=45% height=45%> <img src=https://github.com/KACHAPPILLY2021/optical_flow/blob/main/results/accuracy/20mph.png width=45% height=45%>
<p align="center">
<img src=https://github.com/KACHAPPILLY2021/optical_flow/blob/main/results/accuracy/25mph.png width=45% height=45%>
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

These are the instructions to get started on the project.
To get a local copy up and running follow these simple steps.

### Prerequisites
* atleast Python 2.0
* OpenCV
* OS - Linux (tested)


### Usage

1. Clone repository
   ```sh
   git clone https://github.com/KACHAPPILLY2021/optical_flow.git
   ```
2. Make a ```data``` folder
   ```sh
   cd ∼ /optical_flow
   mkdir data
   ```
3. Place your video of a moving vehicle recorded from side view inside folder and change input video name inside ```project4.py``` to the test video. 
4. Navigate to ```code``` folder and run program.
   ```sh
   python project4.py
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTORS -->
## Contributors

- [Abhijith Mahalle](https://github.com/abhijitmahalle)
- [Jeffin Johny](https://github.com/KACHAPPILLY2021)
- [Pradip Kathiriya](https://github.com/Pradip-Kathiriya)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jeffin Johny K - [![MAIL](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jeffinjk@umd.edu)
	
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/KACHAPPILLY2021)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](http://www.linkedin.com/in/jeffin-johny-kachappilly-0a8597136)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See [MIT](https://choosealicense.com/licenses/mit/) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
