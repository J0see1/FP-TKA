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
  ![WhatsApp Image 2023-12-15 at 16 02 47_891acdab](https://github.com/J0see1/FP-TKA/assets/124648489/9bc12ce9-1582-4911-96d3-acc6788953f7)



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
![getall](https://github.com/J0see1/FP-TKA/assets/134209563/4ad87ea7-8f3f-4995-a1b5-aaf305882407)

3. Get specific order berdasarkan ID
![getbyid](https://github.com/J0see1/FP-TKA/assets/134209563/58f57b9e-a3ff-4134-8c83-2bc90f00576b)

4. Buat order baru
![post](https://github.com/J0see1/FP-TKA/assets/134209563/78a5c850-9e70-4e58-b31a-2884ec8b3f9e)

5. Update order berdasarkan ID nya
![update](https://github.com/J0see1/FP-TKA/assets/134209563/068e0008-dd0a-465e-a20d-de069a68a0ec)

6. Hapus order berdasarkan ID nya
![delete](https://github.com/J0see1/FP-TKA/assets/134209563/dcef5cf9-862a-4340-92dc-54b490d34180)

## Hasil Pengujian Loadtesting Locust
### Device Etha
##### Spawn Rate 25
![WhatsApp Image 2023-12-15 at 16 20 18_c5e6773b](https://github.com/J0see1/FP-TKA/assets/124648489/ab65ff90-dc37-457d-8c17-610ee4ec35d2)
![WhatsApp Image 2023-12-15 at 16 20 31_e4ed6c1f](https://github.com/J0see1/FP-TKA/assets/124648489/cff63b44-9841-4ddd-b928-b50f82bdd204)

##### Spawn Rate 50 
![WhatsApp Image 2023-12-15 at 16 17 02_a1bb8a9e](https://github.com/J0see1/FP-TKA/assets/124648489/6d9b11b1-9418-4314-82ee-9e4351d89bcb)
![WhatsApp Image 2023-12-15 at 16 17 15_8baa75ea](https://github.com/J0see1/FP-TKA/assets/124648489/d001120d-ba54-4933-ab84-4440a8d4aba4)


##### Spawn Rate 100
![WhatsApp Image 2023-12-15 at 16 22 51_525472b9](https://github.com/J0see1/FP-TKA/assets/124648489/f4e02170-6b1e-49b3-807b-1b705e2a2bce)
![WhatsApp Image 2023-12-15 at 16 23 05_ad9ef182](https://github.com/J0see1/FP-TKA/assets/124648489/684dcfa8-0876-418d-8e43-bc26ba794f1c)


### Device Rehana
##### Spawn Rate 25
![WhatsApp Image 2023-12-15 at 16 24 33_5bddf6bd](https://github.com/J0see1/FP-TKA/assets/124648489/29cf45c9-a700-43ea-8189-ff7a73d1e181)
![WhatsApp Image 2023-12-15 at 16 25 16_d917e880](https://github.com/J0see1/FP-TKA/assets/124648489/b6ac69c3-267a-4b77-afb4-235b2f2dfaa6)

##### Spawn Rate 50 
![WhatsApp Image 2023-12-15 at 16 26 58_9197dd2e](https://github.com/J0see1/FP-TKA/assets/124648489/ecaf9e1d-e454-4824-ba6f-58ef15c09f7f)
![WhatsApp Image 2023-12-15 at 16 27 14_12a457ae](https://github.com/J0see1/FP-TKA/assets/124648489/36d50ffa-eccc-486c-b5aa-583bd5bb3c13)

##### Spawn Rate 100
![WhatsApp Image 2023-12-15 at 16 28 43_ed9bc967](https://github.com/J0see1/FP-TKA/assets/124648489/3b575857-6463-4def-92af-67c0130ab056)
![WhatsApp Image 2023-12-15 at 16 28 57_818d6c91](https://github.com/J0see1/FP-TKA/assets/124648489/fe944b34-11e4-42de-93f0-d5e5b6752e37)

## Kesimpulan

Setelah beberapa kali percobaan, disarankan untuk meningkatkan jumlah node pada load balancer seiring dengan peningkatan jumlah worker. Hal ini dikarenakan pada percobaan menggunakan satu node load balancer dan tiga worker, terjadi penurunan performa pada ketiga worker tersebut.

## Problem

Tidak ada
