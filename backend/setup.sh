#!/bin/bash
# Setup script for conda environment

echo "Setting up Restaurierungsentitaeten backend environment..."

# Create and activate conda environment
conda env create -f environment.yml
conda activate restaurierungsentitaeten

# Download spaCy model
python -m spacy download de_dep_news_trf

# Initialize database
python -c "from app.database import engine; from app import models; models.Base.metadata.create_all(bind=engine)"

echo "Setup complete! Activate with: conda activate restaurierungsentitaeten"