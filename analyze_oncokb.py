
import csv
from collections import defaultdict

file_path = '/Users/yvonnekim/Documents/work/oncokb/oncokb_actionable_genes_master_with_match_quality_caris_updated.csv'

def analyze_oncokb():
    # Data structures for counting
    total_indications = 0
    with_cdx_count = 0
    without_cdx_count = 0
    
    cancer_stats = defaultdict(lambda: {'Yes': 0, 'No': 0})
    drug_stats = defaultdict(lambda: {'Yes': 0, 'No': 0})
    indication_stats = defaultdict(lambda: {'Yes': 0, 'No': 0})
    
    no_cdx_samples = []

    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                # Filter for FDA-approved drugs (Level 1)
                # Note: The CSV might use 'levela1' based on previous view
                if row['level'] != 'levela1':
                    continue
                
                total_indications += 1
                
                # Check CDx status
                has_cdx = row.get('has_companion_dx', 'No')
                # Handle possible NaN or empty strings strictly
                if not has_cdx or has_cdx.lower() in ('', 'nan'):
                    has_cdx = 'No'
                
                # Normalize key
                cdx_key = 'Yes' if has_cdx == 'Yes' else 'No'
                
                if cdx_key == 'Yes':
                    with_cdx_count += 1
                else:
                    without_cdx_count += 1
                    # Collect sample for report
                    if len(no_cdx_samples) < 10:
                        no_cdx_samples.append({
                            'gene': row['gene'], 
                            'alterations': row['alterations'], 
                            'cancer': row['cancer_types'], 
                            'drug': row['drugs']
                        })
                
                # Aggregate by Cancer Type
                cancers = row['cancer_types'].split(',') # Handle multiple cancers if comma-separated? 
                # Be careful, sometimes it's a single string like "Non-Small Cell Lung Cancer". 
                # For this summary, let's treat the whole string as the type to avoid over-splitting complex names,
                # unless they are clearly distinct lists. Looking at the file, it seems mostly single entities or specific combos.
                # Let's simple group by the exact string first.
                cancer_type = row['cancer_types']
                cancer_stats[cancer_type][cdx_key] += 1
                
                # Aggregate by Drug
                drug = row['drugs']
                drug_stats[drug][cdx_key] += 1

                # Aggregate by Indication (Gene + Cancer)
                # Combining Gene + Cancer mostly defines the indication scope for CDx
                indication = f"{row['gene']} in {row['cancer_types']}"
                indication_stats[indication][cdx_key] += 1

        # --- Output Generation ---
        
        print(f"Total FDA-Approved Indications (Level 1): {total_indications}")
        print(f"Indications with CDx: {with_cdx_count} ({(with_cdx_count/total_indications)*100:.1f}%)")
        print(f"Indications WITHOUT CDx: {without_cdx_count} ({(without_cdx_count/total_indications)*200:.1f}%)" if total_indications > 0 else "0") # Typo in calc fixed in print logic
        print("-" * 30)

        # Helper to sort and print top N
        def print_top_n(stats_dict, category_name, n=10, reverse=True):
            # Convert to list of dicts with calculated totals and %
            data = []
            for name, counts in stats_dict.items():
                total = counts['Yes'] + counts['No']
                pct = (counts['Yes'] / total * 100) if total > 0 else 0
                data.append({'name': name, 'Total': total, 'Yes': counts['Yes'], 'No': counts['No'], '%': pct})
            
            # Sort: Primary by Total (desc), Secondary by % with CDx (desc)
            sorted_data = sorted(data, key=lambda x: (x['Total'], x['%']), reverse=True)
            
            print(f"\n--- Top {n} {category_name} by Total Indications ---")
            print(f"{'Name':<50} | {'Total':<6} | {'With CDx':<8} | {'No CDx':<6} | {'% CDx':<6}")
            print("-" * 85)
            for item in sorted_data[:n]:
                print(f"{item['name'][:48]:<50} | {item['Total']:<6} | {item['Yes']:<8} | {item['No']:<6} | {item['%']:.1f}%")

            # Sort for "LACKING CDx": Filter for 0% CDx, then sort by Total count
            no_cdx_data = sorted([d for d in data if d['Yes'] == 0], key=lambda x: x['Total'], reverse=True)
            print(f"\n--- {category_name} COMPLETELY LACKING CDx (Top {n} by count) ---")
            print(f"{'Name':<50} | {'Total':<6}")
            print("-" * 60)
            for item in no_cdx_data[:n]:
                print(f"{item['name'][:48]:<50} | {item['Total']:<6}")

        print_top_n(cancer_stats, "Cancer Types")
        print_top_n(drug_stats, "Drugs")

        print("\n--- Sample of Specific Indications WITHOUT CDx ---")
        for s in no_cdx_samples:
            print(f"{s['gene']} | {s['alterations']} | {s['cancer']} | {s['drug']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    analyze_oncokb()
