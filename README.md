
# Cruise Ships Performance Analysis

This repository contains Python scripts and notebooks for analyzing the performance trends of two cruise ships (Vessel 1 and Vessel 2).
This project aims to analyze various aspects of the ships' operations using Python and SQL, focusing on key performance indicators (KPIs) such as efficiency, propulsion systems, power generation, and more.

## Background
Data given is of two Cruise ships for an year from Januray 1st to Deceber 31, 2023 in 5 minute inteval. The condition or destination in which the ships have travelled is not given.

## Repository Structure

The repository is structured as follows:

- **data/**: Directory containing the dataset files used for analysis.
- **scripts/**
  - **Data Cleaning.ipynb**: Jupyter Notebook for preprocessing and cleaning the dataset.
  - **Vessel1_Analysis.ipynb**: Jupyter Notebook focusing on performance trends of Vessel 1.
  - **Vessel2_Analysis.ipynb**: Jupyter Notebook focusing on performance trends of Vessel 2.
  - **utilities.py**: Python script containing utility functions used across analysis notebooks.(this conatins all the helper functions)
- **documents/**: This folder contains all the documents neccessary for this project.

## How to Run and Navigate

1. Clone this repository to your local machine.
2. Ensure you have Python 3.x and Jupyter Notebook installed.
3. Open `Data_cleaning.ipynb` in Jupyter Notebook from **scripts/**
4. Run the Data_clean_function to get the cleaned data.
5. Run each cell in vessel1_analysis from **scripts/**, where you can observe trends of different KPI and narrative in the begining of each cell.
6. Run each cell in vessel2_analysis from **scripts/**, where you can observe trends of different KPI and narrative in the begining of each cell.
7. As the above two notebooks gives indivual insights of vessel 1 and 2 , for quick look up between both open Analysis of cruise ships performance trends in **documents/**
8. For more understanding ,**Please read the documentaion in **documents/**

## Key Components

- Data Cleaning: Handling missing values and converting data types.
- EDA: Visualizing distributions and exploring correlations.
- KPIs: Calculating efficiency metrics and visualizing trends.
- Narrative Development: Summarizing findings and insights.

### Further Scope

The analysis provided in this repository offers a comprehensive view of the performance metrics for Vessel 1 and Vessel 2 based on the data available for the year 2023. However, there are several avenues for further exploration and enhancement:
- **Detailed Operational Context**: Incorporating additional data on the operational context, such as specific routes, weather conditions, or maintenance schedules, could provide deeper insights into performance variations.
- **Comparative Analysis**: Conducting a comparative analysis with industry benchmarks or similar vessels could benchmark the performance metrics against industry standards.
- **Predictive Modeling**: Developing predictive models to forecast performance indicators based on historical data could assist in proactive decision-making and optimization of operational strategies.
  

### Acknowledgments

This project benefited from collaboration and support from various sources:

- **Data Providers**: tuicruises.com.
  
- **website used**: 1.https://wwwcdn.imo.org/localresources/en/KnowledgeCentre/IndexofIMOResolutions/MEPCDocuments/MEPC.333(76).pdf
                    2.https://www.sustainable-ships.org/stories/2022/sfc
                    3.chatgpt.com




