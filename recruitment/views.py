from django.shortcuts import render
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes  import CategoricalNB
from django.conf import settings
from .models import Pelamar, Seleksi
import pandas as pd
import json
import os
import joblib

# Create your views here.
def preprocess_data(df):
    # Kategorisasi Pendidikan
    def kategori_pendidikan(p):
        if p in ['SD/MI', 'SMP/MTS', 'SMA/SMK/MA']:
            return 'Umum'
        else:
            return 'Tinggi'
    
    # Kategorisasi Usia
    def kategori_usia(u):
        return 'Muda' if u < 35 else 'Dewasa'
    
    df['Pendidikan'] = df['Pendidikan'].apply(kategori_pendidikan)
    df['Usia'] = df['Usia'].apply(kategori_usia)

    return df

    
def listSeleksi(request):
    pass