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
- Berikut rancangan arsitektur _cloud_ dan tabel harga spesifikasi VM final project kami
![WhatsApp Image 2023-12-15 at 04 58 49_ec338030](https://github.com/J0see1/FP-TKA/assets/124648489/580a3f3b-e728-41e7-b9f5-621b235d2303)


## Langkah Implementasi dan Konfigurasi VM

- Untuk setup database :
   
1. _create_ database dan _copy connection string_

![image](https://github.com/J0see1/FP-TKA/assets/134209563/5372d41b-48b9-4ea9-b856-24f6799564b5)

2. _Create new connection_ menggunakan string database yang sebelumnya sudah di-copy

![image](https://github.com/J0see1/FP-TKA/assets/134209563/921689e6-b804-408c-ae0b-ed3a6491a8cf)

- Untuk setup worker

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

1. Import data
![image](https://github.com/J0see1/FP-TKA/assets/134209563/38ec8262-e131-4933-88ef-af351cdcc864)

2. Get orders
![image](https://github.com/J0see1/FP-TKA/assets/134209563/6fa11cba-7dd2-4479-854a-ae2a53027785)

3. Get specific order berdasarkan ID
![image](https://github.com/J0see1/FP-TKA/assets/134209563/57da4b7e-3268-4202-acd0-b42ca775b851)

4. Buat order baru
![image](https://github.com/J0see1/FP-TKA/assets/134209563/2791de0b-220e-40c1-a99b-644b9c615e89)

5. Update order berdasarkan ID nya
![image](https://github.com/J0see1/FP-TKA/assets/134209563/a3110ef1-7da6-4388-8d10-f5628264e021)

6. Hapus order berdasarkan ID nya
![image](https://github.com/J0see1/FP-TKA/assets/134209563/182222fc-3dcb-4a8d-8a7e-f024b3e15e4d)

## Hasil Pengujian Loadtesting Locust
##### Spawn Rate 25 GET
![image](https://github.com/J0see1/FP-TKA/assets/135596748/8fce3336-3ee7-4c37-a15f-896640ea3e6a)
![image](https://github.com/J0see1/FP-TKA/assets/135596748/cee53bf6-6030-416a-bd53-98f8b095b829)

##### Spawn Rate 25 POST
![image](https://github.com/J0see1/FP-TKA/assets/135596748/cd096903-9af0-4d86-aab5-3e059af3c1c4)
![image](https://github.com/J0see1/FP-TKA/assets/135596748/306521c0-fc99-4706-8d8b-23ae764cab93)

##### Spawn Rate 50 GET 
![image](https://github.com/J0see1/FP-TKA/assets/135596748/c5c9a7df-a2b6-49b4-8c88-232c36419467)
![image](https://github.com/J0see1/FP-TKA/assets/135596748/bbc28033-1558-4c22-a6dc-d51766f6d991)

##### Spawn Rate 50 POST
![image](https://github.com/J0see1/FP-TKA/assets/135596748/d41b9e5c-1492-4d14-8774-1ee1a427ffe2)
![image](https://github.com/J0see1/FP-TKA/assets/135596748/6af91767-c78f-49d8-952d-5d6ccb15ba18)

##### Spawn Rate 100 GET
![image](https://github.com/J0see1/FP-TKA/assets/135596748/7c858ecb-a9c6-429a-a12d-48f70c92991f)
![image](https://github.com/J0see1/FP-TKA/assets/135596748/85303d93-977a-4240-b206-81be905c49b8)

##### Spawn Rate 100 POST
![image](https://github.com/J0see1/FP-TKA/assets/135596748/d1071f2f-8d4a-4f56-aa10-b9788cfb2d5a)
![image](https://github.com/J0see1/FP-TKA/assets/135596748/f6c5d44f-ed05-4a91-b625-ab432820758d)


## Kesimpulan

Setelah beberapa kali percobaan, disarankan untuk meningkatkan jumlah node pada load balancer seiring dengan peningkatan jumlah worker. Hal ini dikarenakan pada percobaan menggunakan satu node load balancer dan tiga worker, terjadi penurunan performa pada ketiga worker tersebut.

## Problem

Tidak ada
