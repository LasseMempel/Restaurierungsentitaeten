@echo off
echo Setting up Restaurierungsentitaeten backend environment...

conda env create -f environment.yml
call conda activate restaurierungsentitaeten

python -m spacy download en_core_web_sm

python -c "from app.database import engine; from app import models; models.Base.metadata.create_all(bind=engine)"

echo Setup complete! Activate with: conda activate restaurierungsentitaeten
pause