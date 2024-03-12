import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import numpy as np
from src import mapper_values
from src.mapper_values import get_cardiac_arrest_constants


path=['data/nemsis.db',"figs/missing/aed_prior_ems-bar.png","figs/missing/cpr_prior_ems-bar.png"]

def map_aed(aed):
    aed = str(aed)
    for enum in mapper_values.CARDIAC_ARREST_AED_PRIOR_EMS:
        if aed == '7701001':
            return None
        if enum.value == aed:
            return enum.name


def map_cpr(cpr):
    cpr = str(cpr)
    for enum in mapper_values.CARDIAC_ARREST_CPR_PRIOR_TO_EMS:
        if cpr == '7701001':
            return None
        if enum.value == cpr:
            return enum.name


def map_cpr_before_after(cpr):
    cpr = str(cpr)
    for enum in mapper_values.CARDIAC_ARREST_CPR:
        if cpr == '7701001':
            return None
        if enum.value == cpr:
            return enum.name

def map_date_time(date_time: str):
    try:
        format = "%d%b%Y:%H:%M:%S"
        return pd.to_datetime(date_time, format=format)
    except:
        return None

# 数据库连接
con = sqlite3.connect(path[0])


# 数据可视化函数定义
def generate_heat_map(df: pd.DataFrame, file):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isna().transpose(), cbar=False)
    plt.title("Missing Values", fontsize=12)
    plt.xlabel("Records", fontsize=10)
    plt.ylabel("Features", fontsize=10)
    plt.tight_layout()
    plt.savefig(file)


def nullity_correlation_map(df: pd.DataFrame, file):
    plt.figure(figsize=(11, 9))
    sns.set_theme(style="white")
    corr = df.isna().corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap=cmap, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.tight_layout()
    plt.savefig(file)


def generate_missing_value_bar_chart(df: pd.DataFrame, variable_name: str, file_path: str):
    # 计算非缺失值的数量
    non_missing_count = df[variable_name].notna().sum()
    # 计算总观测数
    total_count = len(df)
    # 计算缺失值的数量
    missing_count = total_count - non_missing_count

    counts_df = pd.DataFrame({
        'Status': ['Missing', 'Non-Missing'],
        'Count': [missing_count, non_missing_count]
    })

    plt.figure(figsize=(8, 4))
    sns.barplot(x='Status', y='Count', data=counts_df)
    plt.title(f'Missing Value Counts for {variable_name}')
    plt.tight_layout()

    plt.savefig(file_path)
    plt.close()


# 查询并处理数据
constants = mapper_values.get_cardiac_arrest_constants()

aed_prior_ems_field = constants['CARDIAC_ARREST']['AED_PRIOR_EMS']
cpr_prior_to_ems_field = constants['CARDIAC_ARREST']['CPR_PRIOR_TO_EMS']

query = f"""
SELECT
TRIM({aed_prior_ems_field}) as aed_prior_ems, 
TRIM({cpr_prior_to_ems_field}) as cpr_prior_ems
FROM Pub_PCRevents_CA
"""
df = pd.read_sql(query, con)
df['aed_prior_ems'] = df['aed_prior_ems'].map(map_aed)
df['cpr_prior_ems'] = df['cpr_prior_ems'].map(map_cpr)

# AED
aed_prior_ems_field = constants['CARDIAC_ARREST']['AED_PRIOR_EMS']
query = f"SELECT TRIM({aed_prior_ems_field}) as aed_prior_ems FROM Pub_PCRevents_CA;"
df = pd.read_sql(query, con)
df['aed_prior_ems'] = df['aed_prior_ems'].apply(map_aed)
print("Generating bar chart for AED Prior EMS missing data")
generate_missing_value_bar_chart(df, 'aed_prior_ems', path[1])

# CPR
cpr_prior_to_ems_field = constants['CARDIAC_ARREST']['CPR_PRIOR_TO_EMS']
query = f"SELECT TRIM({cpr_prior_to_ems_field}) as cpr_prior_ems FROM Pub_PCRevents_CA;"
df = pd.read_sql(query, con)
df['cpr_prior_ems'] = df['cpr_prior_ems'].apply(map_cpr)
print("Generating bar chart for CPR Prior EMS missing data")
generate_missing_value_bar_chart(df, 'cpr_prior_ems', path[2])

con.close()
