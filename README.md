# BIg_Data_Analytics
Big Data Analytics Pipeline using Docker Hadoop (HDFS + MapReduce) on Spotify Million Playlist DataSet, With Python ML and Visualizations for popularity-based insights.

# Big Data Analytics Assignment: Spotify MPD (HDFS + MapReduce + ML)

This repository contains my end-to-end Big Data Analytics assignment using a Hadoop cluster deployed with Docker. The project uses the Spotify Million Playlist Dataset (MPD) to demonstrate: HDFS ingestion, distributed processing using MapReduce, and machine learning + visualisation using Python.

## Business Problem
Music streaming platforms need scalable systems to analyse large playlist data and identify:
- which tracks are most popular,
- which tracks are emerging,
- and which tracks behave like outliers (viral/trending).

This project builds a popularity-based analytics pipeline that can support playlist curation and trend monitoring.

## Dataset
- **Spotify Million Playlist Dataset (MPD)**  
- Source: AIcrowd challenge page (downloaded separately by the user)

> Note: The dataset files are not included in this repository due to size and licensing.

## Tech Stack
- Docker + Docker Compose
- Hadoop (HDFS + YARN)
- MapReduce (Hadoop Streaming / Hadoop Examples)
- Python (Pandas, scikit-learn, Matplotlib)
- Google Colab (for ML and visualisation)

## Project Pipeline (High Level)
1. **Ingest data into HDFS** (HDFS blocks + replication)
2. **Process data using MapReduce**
   - Extract/prepare track occurrence data
   - Run MapReduce to aggregate track popularity
3. **Machine Learning + Visualisation**
   - Pre-processing: filtering, log transform, scaling
   - Training: K-Means clustering for popularity segmentation
   - Outlier detection: DBSCAN (or safe alternative if needed)
   - Visualisations and business insights
