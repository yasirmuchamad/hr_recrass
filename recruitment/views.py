from django.shortcuts import render
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes  import CategoricalNB
from django.conf import settings
from .models import Pelamar, Seleksi, Departemen, Perteker
from .forms import *
import pandas as pd
import json
import os
import joblib

# Create your views here.
def listDepartemen(request):
    departemen = Departemen.objects.all()

    context = {
        'title'     : 'Departemen',
        'subtitle'  : 'HR-Recruitment & Assesment',
        'depts'     : departemen
    }

    return render(request, 'recruitment/departemen/list.html', context)

def createDepartemen(request):
    form = DepartemenForm(request.POST or None)
    if request.method == 'Post':
        if form.is_valid():
            form.save()
        return redirect('departemen:list_departemen')
    context = {
        'title'     : 'Tambah Departemen',
        'subtitle'  : 'HR-Recruitment & Assesment',
        'forms'     : form
    }
    return render(request, 'recruitment/departemen/create.html', context)

# --------------------------------------------------------------------------------------------------------------

def listPelamar(request):
    pelamar = Pelamar.objects.all()
    
    context = {
        'title'     : 'Pelamar',
        'subtitle'  : 'HR-Recruitment & Assesment',
        'pelamars' : pelamar
    }

    return render(request, 'recruitment/pelamar/list.html', context)

def listPerteker(request):
    perteker = Perteker.objects.all()
    
    context = {
        'title'     : 'Permintaan Tenaga Kerja',
        'subtitle'  : 'HR-Recruitment & Assesment',
        'pertekers' : perteker
    }

    return render(request, 'recruitment/perteker/list.html', context)

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
    # load model dan encoder yang sudah dilatih
    model_path = os.path.join(settings.BASE_DIR, 'recruitment/static', 'model_cakar.joblib')
    encoders_path = os.path.join(settings.BASE_DIR, 'recruitment/static', 'encoders_cakar.joblib')
    le_target_path = os.path.join(settings.BASE_DIR, 'recruitment/static', 'le_target_cakar.joblib')

    model = joblib.load(model_path)
    encoders = joblib.load(encoders_path)
    le_target = joblib.load(le_target_path)

    # penampungan data
    all_data = []

    # load data dari database
    for obj in Seleksi.objects.all():
        record = {
            'id'        : obj.id,
            'Nama'      : obj.pelamar.nama,
            'Gender'    : obj.pelamar.gender,
            'Pendidikan': obj.pelamar.pendidikan,
            'Pengalaman': obj.pelamar.pengalaman,
            'Usia'      : obj.pelamar.usia,
            'Psikotest' : obj.nilai_psikotest,
            'Interview' : obj.nilai_interview,
            'Status'    : obj.status,
            'Prediksi'  : 'Belum lengkap'
        }

        if all([obj.pelamar.gender, obj.pelamar.pendidikan, obj.pelamar.pengalaman, obj.pelamar.usia, obj.nilai_psikotest, obj.nilai_interview]):
            # lakukan prediksi untuk data yang sudah lengkap
            # record = normalisasi_nilai(record)
            df_row  = pd.DataFrame([record]).copy()
            # preprocessing data
            df_row  = preprocess_data(df_row)
            fitur   = ['Gender', 'Pendidikan', 'Pengalaman', 'Usia', 'Psikotest', 'Interview']
            for col in fitur:
                df_row[col] = encoders[col].transform(df_row[col])
            X   = df_row[fitur]
            pred = model.predict(X)
            hasil = le_target.inverse_transform(pred)
            record['Prediksi'] = hasil[0]
        
        all_data.append(record)

    context = {
        'title'     : 'Seleksi',
        'subtitle'  : 'HR-Recruitment & Assesment',
        'data'      : all_data,
    }
    return render(request, 'recruitment/seleksi/list.html', context)




    