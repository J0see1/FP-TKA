# Final Project Teknologi Komputasi Awan

## Anggota Kelompok B-2

| Nama                            | NRP          |
| ------------------------------- | ------------ |
| Mutiara Nurhaliza               | `5027221010` |
| Monica Damelia Hutapea          | `5027221011` |
| Marcelinus Alvinanda Chrisantya | `5027221012` |
| Rehana Putri Salsabila          | `5027221015` |
| Etha Felisya Br Purba           | `5027221017` |


## Permasalahan

Anda adalah seorang lulusan Teknologi Informasi, sebagai ahli IT, salah satu kemampuan yang harus dimiliki adalah Keampuan merancang, membangun, mengelola aplikasi berbasis komputer menggunakan layanan awan untuk memenuhi kebutuhan organisasi.(menurut kurikulum IT ITS 2023 😙)
Pada suatu saat teman anda ingin mengajak anda memulai bisnis di bidang digital marketing, anda diberikan sebuah aplikasi berbasis API File: app.py dengan spesifikasi sebagai berikut

## Rancangan Arsitektur dan Tabel Harga Spesifikasi VM

## Langkah Implementasi dan Konfigurasi VM

Untuk setup database:

![image](https://github.com/J0see1/FP-TKA/assets/134209563/5372d41b-48b9-4ea9-b856-24f6799564b5)

![image](https://github.com/J0see1/FP-TKA/assets/134209563/921689e6-b804-408c-ae0b-ed3a6491a8cf)

Untuk setup worker:

1. buka powershell / cmd, etc dan masukkan command di bawah
   ```
   ssh root@[ipaddress]
   ```
   sesuaikan dengan ip address masing-masing worker. Command ini untuk masuk pada vm melalui ssh.
2. setelah itu lakukan instalasi dependencies yang ada di bawah ini di tiap worker:
   ```
   sudo apt update
   sudo apt install python3
   sudo apt install python3-pip -y

   pip install flask
   pip install gunicorn
   pip install flask_pymongo
   pip install gevent
   ```
3. setelah instalasi masukkan command berikut:
   ```
   gunicorn --bind 0.0.0.0:8000 -w 8 -k gevent app:app
   ```
   command ini untuk menjalankan app.py

untuk setup load balancer:

![image](https://github.com/J0see1/FP-TKA/assets/134209563/f3e66a0e-fc01-45a4-a18a-46a6e72018dd)


## Hasil Pengujian Endpoint-Endpoint

![image](https://github.com/J0see1/FP-TKA/assets/134209563/38ec8262-e131-4933-88ef-af351cdcc864)

![image](https://github.com/J0see1/FP-TKA/assets/134209563/6fa11cba-7dd2-4479-854a-ae2a53027785)

![image](https://github.com/J0see1/FP-TKA/assets/134209563/57da4b7e-3268-4202-acd0-b42ca775b851)

![image](https://github.com/J0see1/FP-TKA/assets/134209563/2791de0b-220e-40c1-a99b-644b9c615e89)

![image](https://github.com/J0see1/FP-TKA/assets/134209563/a3110ef1-7da6-4388-8d10-f5628264e021)

![image](https://github.com/J0see1/FP-TKA/assets/134209563/182222fc-3dcb-4a8d-8a7e-f024b3e15e4d)

## Hasil Pengujian Loadtesting Locust

## Kesimpulan

## Problem
