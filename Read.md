CyberGuard-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── artifacts/
│   ├── email/
│   ├── url/
│   └── chatbot/
│
├── dataset/
│   ├── email/
│   ├── url/
│   └── chatbot/
│
├── notebooks/
│   ├── email/
│   ├── url/
│   └── chatbot/
│
├── templates/
├── static/
│
└── src/
    │
    ├── __init__.py
    ├── logger.py
    ├── exception.py
    ├── utils.py
    │
    ├── email_spam/
    │   ├── __init__.py
    │   ├── data_ingestion.py
    │   ├── data_preprocessing.py
    │   ├── feature_engineering.py
    │   ├── model_trainer.py
    │   ├── model_evaluation.py
    │   └── predict.py
    │
    ├── url_detection/
    │   ├── __init__.py
    │   ├── data_ingestion.py
    │   ├── data_preprocessing.py
    │   ├── feature_engineering.py
    │   ├── model_trainer.py
    │   ├── model_evaluation.py
    │   └── predict.py
    │
    ├── chatbot/
    │   ├── __init__.py
    │   ├── llm_loader.py
    │   ├── prompt_template.py
    │   ├── rag.py
    │   ├── chatbot.py
    │   └── predict.py
    │
    ├── pipeline/
    │   ├── email_pipeline.py
    │   ├── url_pipeline.py
    │   └── chatbot_pipeline.py
    │
    └── config/
        └── config.py