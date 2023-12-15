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
### Device Etha
##### Spawn Rate 25
![WhatsApp Image 2023-12-15 at 15 44 25_7d730b64](https://github.com/J0see1/FP-TKA/assets/124648489/1fe22add-dd40-4618-8f2d-a156e45cf5a9)
![WhatsApp Image 2023-12-15 at 15 44 38_d896eff3](https://github.com/J0see1/FP-TKA/assets/124648489/c8791d94-ed51-43fc-9c5d-668b48e7eaf7)


##### Spawn Rate 50 
![WhatsApp Image 2023-12-15 at 15 45 19_2802e040](https://github.com/J0see1/FP-TKA/assets/124648489/51d28a3e-c3a9-4d80-ad53-2dd16208dadd)
![WhatsApp Image 2023-12-15 at 15 46 10_e0223052](https://github.com/J0see1/FP-TKA/assets/124648489/b11ccdd0-c2bc-4b78-ad11-468a2e835fff)

##### Spawn Rate 100
![WhatsApp Image 2023-12-15 at 15 46 44_00f9caae](https://github.com/J0see1/FP-TKA/assets/124648489/252c3d0e-4de7-4f35-8458-9bb6bcf74e2e)
![WhatsApp Image 2023-12-15 at 15 47 39_f6d3c196](https://github.com/J0see1/FP-TKA/assets/124648489/b8d2dee6-7719-4e75-8b21-92869559f4f0)

### Device Rehana
##### Spawn Rate 25
![WhatsApp Image 2023-12-15 at 15 50 55_97650523](https://github.com/J0see1/FP-TKA/assets/124648489/067f844d-c881-499b-b9ce-c01dba7253d8)
![WhatsApp Image 2023-12-15 at 15 51 19_82cb62b3](https://github.com/J0see1/FP-TKA/assets/124648489/77f077ef-828b-4732-b1d5-b995209aee87)

##### Spawn Rate 50 
![WhatsApp Image 2023-12-15 at 15 52 54_3029108e](https://github.com/J0see1/FP-TKA/assets/124648489/df667b6c-74f1-4693-ab38-8f432884d806)
![WhatsApp Image 2023-12-15 at 15 53 10_8a3ea6ba](https://github.com/J0see1/FP-TKA/assets/124648489/bb140fd5-d424-439d-8dfa-971733facc38)

##### Spawn Rate 100
![WhatsApp Image 2023-12-15 at 15 54 49_8b945d67](https://github.com/J0see1/FP-TKA/assets/124648489/4ade26eb-d1b3-4f49-81fc-9dc13f3dc409)
![WhatsApp Image 2023-12-15 at 15 55 05_6dae4171](https://github.com/J0see1/FP-TKA/assets/124648489/ccb4442f-40d0-4db8-ab44-38ba58af2398)


## Kesimpulan

Setelah beberapa kali percobaan, disarankan untuk meningkatkan jumlah node pada load balancer seiring dengan peningkatan jumlah worker. Hal ini dikarenakan pada percobaan menggunakan satu node load balancer dan tiga worker, terjadi penurunan performa pada ketiga worker tersebut.

## Problem

Tidak ada
