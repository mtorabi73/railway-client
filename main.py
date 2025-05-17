from gradio_client import Client

# اتصال به Space در Hugging Face
client = Client("https://mohammadreza73-ag-predictor.hf.space/")

# ارسال SMILES تستی و چاپ نتیجه
result = client.predict("CC(=O)OC1=CC=CC=C1C(=O)O")
print("Prediction Result:", result)
