

# Seeing the Words 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14674002.svg)](https://doi.org/10.5281/zenodo.14674002)

## Table of Contents

- Introduction
- Methodology
- Repository Organization
- Requirements
- Accessing Data
- Usage Instructions
- Related Resources 
- License
- Archiving
- Contact


### Introduction
This repository contains the code corresponding to the *Seeing the Words* project conducted jointly at the Eep Talstra Centre for Bible and Computer (ETCBC) and the Computer Science department, Vrije Universiteit Amsterdam. The aim of the project was to generate images by using biblical text as prompts. The generated images were analyzed using different tools with the results stored in a CSV file. The corresponding dataset is called the Visio Divina Dataset (VVD) and it is made available on the DANS SSH Data Station. 

The canonical citation for this project is below:

- bibtex: TODO.
- APA: TODO. 

### Methodology

Here, we provide a summary of the methodology of this project. 
The following biblical texts were used. 
- Adam and Eve's Expulsion of Paradise (Genesis 4:23-24)
- The Tower of Babel (Genesis 11:1-9)
- Binding of Isaac (Genesis 22:9-14)
- The Last Supper (Mark 14:12-25)
- Moses Found (Exodus 2:5-9).



The following Text2Image (T2I) generators were used. 
- DALL E 
- Midjourney 
- Stable Diffusion (various versions)

There are in total 7,116 images generated. 

We then performed different means to evaluate the generated images. 
Details are provided in the paper. 

### Repository Organization
The repository is organized as follows:


    .
    ├── data/
    │   ├──prompts/
    │   │   └── <prompt text files>
    │   ├──data_csv/
    │   └── <data_csv_files>
    │   ├── images/ 
    │   │   └── <image files links>
    ├── src/
    │   └──
    │
    ├── models/
    │
    └── README.md


* The folder data/data_csv/ contains the CSV file with relevant analytical and evaluation results.
* The folder data/images/ contains image links to the generated images that are hosted on ImageKit.
* The folder data/prompts/ contains the (pre-processed) biblical text used to generate images. 
* All the code are in the folder ./src/.
* The models used to evaluate generated images are available upon request. 

The mathematical formulas for computing the metrics are included in the thesis (Appendix D).
 
### Requirements
To access and work with this data, you will need the following:

* Python 3.6+
* Pandas (for CSV file handling)
* PIL or OpenCV (for image handling)
* analyzeppl for analysis
* import the imagekit before image processing as follows:
```python 
    from imagekitio import ImageKit
```
Install the dependencies with:
```python 
    pip install pandas 
    pip install imagekitio
```
### Accessing Data
The set of images is named Visio Divina Dataset (VVD). There are multiple ways one can access the data. 

#### 1. Download the entire dataset.
The dataset can be downloaded directly from the DANS SSH Data station  To make sure the script runs correctly, you need to unzip the images and put them under the directory ./data/images/ folder. 

#### 2. Browsing the dataset on the ImageKit online
The images are hosted on ImageKit and can be viewed directly on ImageKit by following the [link](https://imagekit.io/public/share/seeingthewords/17368c1b7d6a64ee236504ab0640570889752289e8b62dea37c6af47760bbea9defe396aa562589a45decb498b7e19800eb928a6a5c41b02aa59ac87b2c6f2b3963916aa15fd66d9b5fe0e6f46a31916/media-library/L2RhdGE).

#### 3. Checking the data analysis result
The data.csv file can be found in the ./data/data_csv/ folder. It contains the analysis result. 

Example to load the CSV in Python:
```python
    import pandas as pd

    data = pd.read_csv('data/data_csv/prompt_0/data.csv')
```
Make sure to check the CSV headers for proper column names and data types.

#### 4. Display Some Images

To load and display images hosted on ImageKit in Python:
```python
    from imagekitio import ImageKit
```
Example image path
```python
    magekit = ImageKit(
        private_key='your private_key',
        public_key='public_kRnwmhVYMoavSB9Eqsc0gEc8rKw=',
        url_endpoint = "https://ik.imagekit.io/seeingthewords/'
    )


    image_url = imagekit.url({
                "path": "/default-image.jpg"
            }
    )


Load and display the image:    

    image = Image.open(image_path)
    image.show()
```    

### Usage Instructions
- Clone the repository to your local machine.
- Install the necessary packages (see the instructions above).
- Use the examples above to load the CSV data and images as needed.
- Run any analysis or scripts provided in the project.
- Specify the license under which the project is shared.

### Related Resources
- The VR Exhibition: [link](https://shuai.ai/art/seeing/).

- The code generates the Visio Divina Dataset. It has been made available on the DANS SSH Data Station. 

- Please check the webpage of ETCBC for other related resources: [webpage](https://etcbc.nl/data/).


### Archiving 
The code and data have been archived at the Vrije Universiteit by Shuai Wang. 
You can download the code, data, intermediate results, selected samples for manual process and analysis, and the paper on YODA: [link ](https://google.com) to be added.

### License 

The code and results included in this repository can be used for free to generate images and perform further analysis. All that has been included in this repository is released under the GNU GPL v3 license. 

### Contact 
- Prof. Willem van Peursen: [e-mail](mailto:w.t.van.peursen@vu.nl), [VU Research portal](https://research.vu.nl/en/persons/willem-van-peursen) (the main researcher).
- Hidde Makimei: [e-mail](mailto:h.n.g.makimei@student.vu.nl), [Linkedin](https://www.linkedin.com/in/hidde-makimei-406744210/), [GitHub](https://github.com/ChiefGitau) (the main developer).
- Shuai Wang: [e-mail](mailto:shuai.wang.vu@gmail.com), [website](https://shuai.ai/research), [LinkedIn](https://www.linkedin.com/in/shuai-wang-02a820216/), [Github](https://github.com/shuaiwangvu) (data steward). 

To follow the latest development of the project, please check the following pages:
- The GitHub page of ETCBC: [GitHub](https://github.com/ETCBC).
- The official website of the ETCBC webpage: [homepage](https://etcbc.nl/).
