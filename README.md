# HReview

## SteelHacks Project 2025: HReview

**Team Members:** Sumukh, Utkarsh, Tanishq

### Project Overview

HReview aims to consolidate various reviews into a comprehensive summary that highlights the best and worst aspects of employee performance. 

### Introduction

HReview is designed to collect, summarize, and analyze reviews from employees about their peers. By utilizing the **Gemini API**, this system generates concise summaries of individual reviews, providing valuable insights into employee performance and team dynamics. This tool aids management in making informed decisions regarding promotions and addressing any concerns that may arise.

### Tools Used

- **Flask** – Back-end
- **Python**
- **React** – Front-end
- **JavaScript, HTML, CSS**
- **FastAPI** – Web Framework
- **Bart** – Large Language Model
- **Gemini API** – Summarizes reviews into 3 pros and 3 cons.

### Features

- **Collect Reviews:** Employees can submit reviews for their peers, providing feedback on performance, teamwork, and contributions.
  
- **Summarization:** Using the Gemini API, all collected reviews for a specific employee are summarized into a cohesive overview.

- **Decision Support:** The summarized feedback helps management identify high-performing employees eligible for promotion and pinpoint those who may need additional support or coaching.

### Usage

1. **Submitting Reviews:**  
   Employees can log in to the system and navigate to the review submission form, where they can enter their feedback on colleagues.

2. **Generating Summaries:**  
   Management can view summaries of reviews for any employee by entering the employee's ID in the summary interface. The system will call the Gemini API to fetch and summarize the reviews.

### Interpreting Results

- **Promotion Considerations:**  
  Use the summarized feedback to identify candidates for promotion based on positive contributions and feedback.

- **Addressing Concerns:**  
  Reviews indicating issues can highlight employees who may benefit from discussions or support.

### Applications

HReview can be extended beyond just HR:

- **In a large college class:** Students can provide feedback on their professor, allowing the professor to see the most important feedback summarized.

- **In a restaurant:** HReview can be used to evaluate employee performance based on concise reviews, making it easier to decide on raises.

Since we utilize a large language model (LLM) to summarize the reviews, it maintains anonymity between the reviewers and the reviewees.
