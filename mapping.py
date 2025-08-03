import json

with open('dis_en.json', 'r', encoding='utf-8') as f_en, open('dis_np.json', 'r', encoding='utf-8') as f_np:
    data_en = json.load(f_en)
    data_np = json.load(f_np)

dis_m = {np['name']: en['name'] for np, en in zip(data_np, data_en) if np['id'] == en['id']}



with open('district_mapping_nep_eng.json', 'w', encoding='utf-8') as f_out:
    json.dump(dis_m, f_out, ensure_ascii=False, indent=4)
    
