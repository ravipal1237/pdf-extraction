import os
import pandas as pd
import json

def save_to_excel(invoice_data, output_dir, file_name):
    try:
        data = json.loads(invoice_data)
    except:
        data = {"raw_output": invoice_data}

    df = pd.json_normalize(data)
    output_path = os.path.join(output_dir, file_name.replace(".pdf", ".xlsx"))
    df.to_excel(output_path, index=False)
    return output_path
