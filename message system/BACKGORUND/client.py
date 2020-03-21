import socket
import sys
 
HOST = '192.168.2.129'   # Sembolik şimdilik 
PORT = 8888 # dinlenecek port numarası
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Soket oluşturuldu'
 
try:
    s.bind(('', PORT)) # soket bind işlemi yapıldı
except socket.error , msg:
    print 'Bind hatası . Hata Kodu : ' + str(msg[0]) + ' Mesaj ' + msg[1]
    sys.exit()
 
 
s.listen(10) # belli aralıklarla portu dinliyoruz 
print 'Soket dinleniyor...'
 
#bağlantı kabul ediyoruz 
conn, addr = s.accept()
 
#client bilgisini ekranda gösteriyoruz 
print 'Bağlandı ' + addr[0] + ':' + str(addr[1])
#client ile konuşma 
data = conn.recv(1024) # clienttan gelen veri alınması ve ekrana yazılması 
print data
#conn.sendall(data) burada karşı cevap vermek için kullanılan bir metod var karşıdan client recv ile #yollan veriyi alabiliriz
  
conn.close()
s.close()