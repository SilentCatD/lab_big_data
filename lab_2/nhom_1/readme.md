  

<div style="text-align: center">

    <span style="font-size: 3em; font-weight: 700; font-family: Consolas">

        Lab 02 <br>

		Building a Sentiment Analysis Benchmark

    </span>

    <br><br>

    <span style="">

        A assignment for <code>CSC14114</code>  Big Data Application @ 19KHMT

    </span>

</div>

  
  

## Collaborators (nhom 1)

- `19127519` **Nguyễn Ngọc Phước** ([Nguyễn Ngọc Phước](https://github.com/SilentCatD))

- `19127523` **Đặng Nguyễn Minh Quân** ([Đặng Nguyễn Minh Quân](https://github.com/quainhan1110))

## Instructors

- `HCMUS` **Đoàn Đình Toàn** ([@ddtoan](ddtoan18@clc.fitus.edu.vn))

- `HCMUS` **Nguyễn Ngọc Thảo** ([@nnthao](nnthao@fit.hcmus.edu.vn))

---

<div style="page-break-after: always"></div>
## Link to notebooks and data:

https://drive.google.com/drive/folders/1aAn4DKlNm2xuQMFEQdUw8zCAFk3WU9en?usp=sharing

We present folders with the following structure:

- Data crawler: Python crawler for data collection, run the `main.py` file to collect data and save it to files: 
	- `bottom_movie_reviews.csv`: Reviews from the bottom up, more likely to get bad reviews
	- `top_movie_reviews.csv`: Reviews from the top down, more likely to get good review
- `Labeling - Preprocess Notebook.ipynb`: Labeling process we proceed on the data, this notebook need the above 2 `csv` data files and output `labeled_data.csv`
- `Classification Notebook.ipynb`: Feature extraction and models process, take input `labeled_data.csv`  and perform analysis.