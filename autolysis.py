import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openai

# Set up OpenAI API
openai.api_base = "https://aiproxy.sanand.workers.dev/openai/v1"
openai.api_key = os.getenv("AIPROXY_TOKEN")

def load_dataset(file_path):
    """Load a CSV file into a pandas DataFrame with encoding fallback."""
    encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            print(f"Dataset loaded successfully with encoding '{encoding}': {file_path}")
            return df
        except UnicodeDecodeError:
            continue  # Try the next encoding
    print(f"Failed to load file {file_path} with tested encodings: {encodings}")
    sys.exit(1)


def perform_analysis(df):
    """Perform a general analysis on the DataFrame."""
    numeric_cols = df.select_dtypes(include=[np.number])
    categorical_cols = df.select_dtypes(include=["object", "category"])
    
    analysis = {
        "shape": df.shape,
        "columns": df.dtypes.to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "summary_statistics": numeric_cols.describe().to_dict(),
        "correlations": numeric_cols.corr().to_dict() if not numeric_cols.empty else {},
        "top_categories": {
            col: df[col].value_counts().head(5).to_dict()
            for col in categorical_cols
        },
    }
    return analysis

def generate_visualizations(df, output_dir):
    """Generate and save visualizations."""
    os.makedirs(output_dir, exist_ok=True)
    plots = []
    
    # Correlation heatmap
    numeric_df = df.select_dtypes(include=[np.number])
    if not numeric_df.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap")
        heatmap_path = os.path.join(output_dir, "correlation_heatmap.png")
        plt.savefig(heatmap_path)
        plt.close()
        plots.append(heatmap_path)
    
    # Distribution plots
    for col in numeric_df.columns:
        plt.figure()
        sns.histplot(df[col].dropna(), kde=True, bins=30, color="blue")
        plt.title(f"Distribution of {col}")
        dist_path = os.path.join(output_dir, f"{col}_distribution.png")
        plt.savefig(dist_path)
        plt.close()
        plots.append(dist_path)

    return plots

def ask_llm_for_insights(analysis, visualizations):
    """Use the LLM to provide insights and narratives based on the analysis."""
    prompt = (
        f"Here is a dataset analysis:\n"
        f"- Shape: {analysis['shape']}\n"
        f"- Columns and Types: {analysis['columns']}\n"
        f"- Missing Values: {analysis['missing_values']}\n"
        f"- Summary Statistics: {analysis['summary_statistics']}\n"
        f"- Correlations: {analysis['correlations']}\n"
        f"- Top Categories: {analysis['top_categories']}\n\n"
        "Please provide a narrative summary of the dataset, insights from the analysis, "
        "and suggestions for further investigation."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print(f"Error interacting with LLM: {e}")
        return "No insights could be generated due to an error."

def write_readme(output_dir, analysis, insights, visualizations):
    """Generate the README.md file."""
    readme_path = os.path.join(output_dir, "README.md")
    with open(readme_path, "w") as f:
        f.write("# Automated Data Analysis Report\n\n")
        f.write("## Dataset Overview\n")
        f.write(f"**Shape:** {analysis['shape']}\n\n")
        f.write("**Columns:**\n")
        for col, dtype in analysis["columns"].items():
            f.write(f"- {col}: {dtype}\n")
        f.write("\n**Missing Values:**\n")
        for col, count in analysis["missing_values"].items():
            f.write(f"- {col}: {count}\n")
        f.write("\n## Summary Statistics\n")
        f.write(f"{pd.DataFrame(analysis['summary_statistics']).to_markdown()}\n\n")
        f.write("## Insights\n")
        f.write(insights + "\n\n")
        if visualizations:
            f.write("## Visualizations\n")
            for plot in visualizations:
                f.write(f"![{os.path.basename(plot)}]({plot})\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python autolysis.py <dataset.csv>")
        sys.exit(1)

    dataset_path = sys.argv[1]
    output_dir = os.path.splitext(dataset_path)[0]
    
    # Load data
    df = load_dataset(dataset_path)
    
    # Perform analysis
    analysis = perform_analysis(df)
    
    # Generate visualizations
    visualizations = generate_visualizations(df, output_dir)
    
    # Ask LLM for insights
    insights = ask_llm_for_insights(analysis, visualizations)
    
    # Write README.md
    write_readme(output_dir, analysis, insights, visualizations)
    
    print(f"Analysis completed. Results saved in {output_dir}")

if __name__ == "__main__":
    main()
