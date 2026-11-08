<div align="center">

<img src="assets/hero.svg" width="100%" alt="Pooja Anbalagan — Data Science undergraduate exploring AI, machine learning, MLOps, DevOps and data engineering" />

<p>
  <a href="https://www.linkedin.com/in/pooja-anbalagan/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://github.com/PoojaAnbalagan"><img src="https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" /></a>
  <img src="https://img.shields.io/badge/Focus-AI%20%26%20Data%20Engineering-6366F1?style=flat-square" alt="AI and Data Engineering" />
</p>

### Building data-driven applications — from experimentation to deployment.

<a href="https://github.com/PoojaAnbalagan">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=18&duration=2800&pause=900&color=60A5FA&center=true&vCenter=true&width=700&lines=Data+Science+Undergraduate;AI%2FML+%26+NLP+Enthusiast;Exploring+MLOps+and+Cloud-Native+Systems;Interested+in+DevOps+%26+Data+Engineering" alt="Typing introduction: Data Science, AI/ML, NLP, MLOps, DevOps and Data Engineering" />
</a>

</div>

---

## About

I’m a **BSc (Hons) Data Science undergraduate at Sabaragamuwa University of Sri Lanka**, interested in applying data science and intelligent technologies to practical problems.

I enjoy working across the lifecycle of data-driven applications: exploring and preparing data, building and evaluating machine learning models, developing APIs, and learning how to package, deploy, automate, and monitor software systems.

My project work spans **machine learning, natural language processing, cloud-based analytics, graph theory, and full-stack application development**. I’m particularly interested in connecting model development with reliable engineering practices through MLOps, DevOps, and cloud infrastructure.

**Currently focused on**
- Building and evaluating practical machine learning and NLP solutions.
- Understanding model deployment, containerization, CI/CD, and observability.
- Exploring AWS services, cloud workflows, and data engineering concepts.
- Strengthening software engineering and reproducible experimentation practices.

## Technical ecosystem

The technologies below reflect a combination of hands-on project use and ongoing learning.

### Programming
<p>
  <img src="https://skillicons.dev/icons?i=python,java,js,r,mysql&perline=8" alt="Python, Java, JavaScript, R and SQL technology icons" />
</p>

### Data science, analytics & AI
<p>
  <img src="https://skillicons.dev/icons?i=pytorch,tensorflow,sklearn,opencv&perline=8" alt="PyTorch, TensorFlow, scikit-learn and OpenCV technology icons" />
</p>

`Pandas` · `NumPy` · `NLTK` · `Transformers` · `Hugging Face` · `Matplotlib` · `Seaborn` · `Plotly` · `Power BI` · `ONNX`

### Backend & application development
<p>
  <img src="https://skillicons.dev/icons?i=fastapi,django,react,nodejs&perline=8" alt="FastAPI, Django, React and Node.js technology icons" />
</p>

`REST APIs` · `Uvicorn` · `Tailwind CSS` · `Prisma`

### MLOps, DevOps & cloud
<p>
  <img src="https://skillicons.dev/icons?i=docker,kubernetes,githubactions,git,aws,linux,prometheus&perline=8" alt="Docker, Kubernetes, GitHub Actions, Git, AWS, Linux and Prometheus technology icons" />
</p>

`Docker Compose` · `CI/CD` · `Helm` · `Amazon S3` · `AWS Lambda` · `AWS Glue` · `Amazon Athena` · `CloudWatch`

### Data platforms & engineering concepts

`PostgreSQL` · `ETL / ELT` · `Data preprocessing` · `Data validation` · `Data pipelines` · `SQL analytics`

---

## Featured projects

A selection of projects demonstrating applied machine learning, cloud workflows, research experimentation, and collaborative application development.

### 1. Customer Review Sentiment Intelligence Platform
**[SENTIMENTAL-ANALYSIS](https://github.com/PoojaAnbalagan/SENTIMENTAL-ANALYSIS)**

An end-to-end platform for analysing customer review sentiment beyond star ratings. The project combines NLP research and model benchmarking with a web application and deployment-oriented engineering.

- Processes customer review text into **Negative, Neutral, and Positive** sentiment classes.
- Compares TF-IDF classical models, VADER, and a fine-tuned DistilBERT model.
- Includes a FastAPI backend and React application for prediction, review exploration, analytics, and reporting.
- Repository documents Docker, Kubernetes/Helm manifests, GitHub Actions CI/CD, and Prometheus metrics.
- Uses a stratified train/validation/test methodology and macro-F1 to account for class imbalance.

**Reported evaluation:** DistilBERT achieved **90.93% accuracy** and **0.8906 macro-F1**, compared with the VADER baseline at **0.6171 accuracy** and **0.5539 macro-F1** in the repository's recorded results.

`Python` `NLP` `DistilBERT` `Scikit-learn` `FastAPI` `React` `Docker` `Kubernetes` `GitHub Actions` `Prometheus`

### 2. AWS-Based Customer Churn Prediction System
**[ChurnPredictionAWS](https://github.com/PoojaAnbalagan/ChurnPredictionAWS)**

A team-based cloud machine learning and business analytics data lake using the telecom Cell2Cell dataset (approximately 71,000 records).

- Documents a cloud workflow from raw data ingestion and validation to preprocessing, model training, batch inference, and SQL analytics.
- Uses Amazon S3, Lambda, CloudWatch, Glue, and Athena across the documented pipeline.
- Trains a `HistGradientBoostingClassifier` and scores a 20,000-record holdout dataset.
- Organizes predictions into customer risk tiers to support retention analysis.

**Reported evaluation:** the repository reports a champion cross-validation ROC-AUC of **0.6720+**. The README also documents business risk segmentation and revenue-at-risk analysis.

`Python` `Scikit-learn` `AWS S3` `AWS Lambda` `AWS Glue` `Amazon Athena` `CloudWatch` `SQL`

### 3. Urban Drainage Resilience — Graph Theory Simulation
**[Urban_Drainage_Problem_Solved_Graph_Theory](https://github.com/PoojaAnbalagan/Urban_Drainage_Problem_Solved_Graph_Theory)**

A simulation study exploring how graph structure and risk-based prioritization can influence reinforcement decisions in a synthetic drainage network.

- Models a directed acyclic network and cascading pipe failures.
- Compares risk-only reinforcement with a blended risk-plus-betweenness strategy.
- Evaluates failure rates, unmet demand, residual capacity, and cascade behaviour.
- Uses repeated experiments, paired statistical tests, and stress tests to examine strategy performance.

**Selected reported result:** at a 10% reinforcement budget and baseline rainfall setting, the graph-based strategy reduced mean unmet demand from **0.1687 to 0.1460** in the repository's experiment results.

*Scope note: this is a simulation on synthetic networks, not a hydraulically validated model of a real drainage system.*

`Python` `NetworkX` `Graph Theory` `Simulation` `Statistical Analysis` `Matplotlib` `SciPy`

### 4. Relaunch Her — Return-to-Tech Platform
**[relaunch_her](https://github.com/PoojaAnbalagan/relaunch_her)**

A collaborative MVP concept designed to support Sri Lankan women returning to the technology industry after career breaks.

- Provides separate experiences for returners and employers.
- Includes skills assessment, learning pathways, job listings, applications, and employer-facing workflows.
- Uses a Next.js frontend and Express/TypeScript backend.
- Documents a mock JSON data client, with a path to PostgreSQL/Prisma integration.

The project focuses on using technology to support career re-entry and access to opportunities.

`Next.js` `React` `TypeScript` `Express` `Prisma` `PostgreSQL`

### 5. Barking Shelter — Pet Adoption Platform
**[Barking-Shelter](https://github.com/PoojaAnbalagan/Barking-Shelter)**

A web application concept connecting people with rescued dogs and supporting responsible pet adoption.

- Supports browsing dog profiles with images, breed, and age.
- Includes adopter/seller authentication and a seller listing workflow.
- Documents pet-care guides and a veterinary directory.

`React` `Django` `Python`

---

## Engineering interests

| Area | What I’m interested in building |
|---|---|
| **Data Science** | Data exploration, statistical reasoning, and predictive insights |
| **AI / ML** | Models and intelligent applications that address practical problems |
| **MLOps** | Reproducible experiments, model packaging, evaluation, and deployment |
| **DevOps** | Automated testing, CI/CD, containers, orchestration, and observability |
| **Data Engineering** | Reliable ingestion, transformation, validation, and analytics pipelines |

## Achievements & community

- **First Place — AURELIA 2.0, IEEE WIE Day 2026:** team project, RelaunchHer.
- **Finalist — J'puraXtreme:** Predictra team.
- **Finalist — CodeRally.**
- **Finalist — CryptX.**
- **HackElite 3.0:** Phase 2 participant with Team WeCodeX, working on AgroGuard AI.
- **CodeArena '26:** participant.
- **Community involvement:** Rotaract content and communications activities, IEEE Computer Society activities, and technical event hosting/organizing.

*Awards, finalist placements, and participation are listed separately to distinguish the type of involvement.*

## Currently exploring

- Deep learning and computer vision.
- Applied NLP and large language model workflows.
- Model lifecycle management and MLOps.
- Kubernetes, container orchestration, and cloud infrastructure.
- Data engineering patterns and scalable pipelines.

## GitHub activity

<div align="center">

<a href="https://github.com/PoojaAnbalagan">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=PoojaAnbalagan&show_icons=true&hide_border=true&rank_icon=github&theme=transparent" alt="GitHub profile statistics" />
</a>
<a href="https://github.com/PoojaAnbalagan">
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=PoojaAnbalagan&layout=compact&hide_border=true&theme=transparent&langs_count=6" alt="Most used programming languages on GitHub" />
</a>

</div>

<sub>These cards are provided by an external service and may occasionally be unavailable. Visit the GitHub profile for the source activity and repositories.</sub>

---

## Connect

<p>
  <a href="https://github.com/PoojaAnbalagan"><img src="https://img.shields.io/badge/GitHub-PoojaAnbalagan-181717?style=for-the-badge&logo=github" alt="GitHub profile" /></a>
  <a href="https://www.linkedin.com/in/pooja-anbalagan/"><img src="https://img.shields.io/badge/LinkedIn-Pooja%20Anbalagan-0A66C2?style=for-the-badge&logo=linkedin" alt="LinkedIn profile" /></a>
</p>

---

<div align="center">
  <sub>Learning continuously. Building thoughtfully. Turning data into useful systems.</sub>
</div>
