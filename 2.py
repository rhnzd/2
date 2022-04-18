import os , sys , requests , json , time
from rich import print as cetak
from rich.panel import Panel as nel
from rich.console import Console

ras = Console()

def logo():
	os.system("clear")
	print(""" __    _ .____  .       __   _____       _ .___  
 |\   |  /      /       |   (            | /   ` 
 | \  |  |__.   |       |    `--.  .---' | |    |
 |  \ |  |      |  /\   /       |        | |    |
 |   \|  /----/ |,'  \,'   \___.'        / /---/ 
                                                """)
def cnn():
	try:
		url = requests.get("https://berita-indo-api.vercel.app/v1/cnn-news/").json()
		b = url["data"]
		for rhn in b:
			c = rhn["title"]
			d = rhn["link"]
			e = rhn["contentSnippet"]
			f = rhn["isoDate"]
			print("")
			han = (f" {c}")	
			cetak(nel(han , title="Judul "))
			hann = (f"{d}")
			cetak(nel(nel(hann , title="Link")))
			rhan = (f"{e}")
			cetak(nel(rhan , title="Deskripsi"))
			print(" Terakhir Post = ",f)
			print(" = " * 21)
	except:
		print("Gangguan")
		
def login():
	try:
		url = requests.get("https://classify-web.herokuapp.com/api/keygen").json()
		a = url["key"]
		ras.print(" Akses Key Anda = ",a, " [ DiTerima ] ",style="bold cyan on white")
		print(" Silahkan Jalankan Ulang Sc")
		ddek =open("Raihan.txt","w").write(a)
	except:
			print(" Sistem Error ")

def hanzd():
	print("")
	duh = ("Tulis: https://Url Anda")
	cetak(nel(duh , title="Berguna Buat Scraping:v"))	
	ras.print(" Contoh : https://classify-web.herokuapp.com/api/keygen",style="italic green on white \n")
	han = input(" > ")
	try:
		url = requests.get(han)
		print(" Tunggu......\n")
		time.sleep(3)
		ras.print(" Hasil Responnya Adalah : ",url,style="italic cyan")
		ras.print(" \n Respons 202 Bisa Digunakan Tanpa Header \n Dan Respons 400/401 Dan Yang Lain Harus Menggunakan Headers",style="bold white on red")
	except:
		print(" Terjadi Kesalahn")
	
	
		
def rhnz():
	logo()
	try:
			duh = open("Raihan.txt","r").read()
			print(" Akses Key ",duh)
			print("")
			aku = (" 1.Berita Cnn \t\t\t\t 0.Ganti Key\n 2.Cek Response Url")       
			cetak(nel(aku , title="Daftar List"))  
			dek = input(" > ")    
			if dek in ["1","01"]:
				cnn()
			elif dek in ["0","00"]:
				print(" \n Sedang Mengganti Key")
				time.sleep(4)
				os.system("rm -rf Raihan.txt")
				login()
			elif dek in ["2","02"]:
				hanzd()
			else:
				print(" Tidak Ada Dalam Kategori")
	except:
		print(" Anda Tidak Mempunyai Akses Login ")
		print(" Silahkan Menunggu")
		time.sleep(6)
		login()
		
rhnz()