ARKADASSSSLARRR MERHABALAR

Projeyi çalıştırmak için Python'u bilgisayarımıza kuruyoruz. Kurulumda **Add PATH** demeniz lazım.

Kontrol için CMD yazın: `python -V` komutu ile beraber versiyon göreceğiz. Versiyon çıkıyorsa tamamız.

Projeyi `git pull` ile çekiyoruz. Sonrasında ise proje klasörüne giriyoruz.

Path `schedulex` olacak ama en dış path'taki `schedulex` olacak. Yani şöyle bir şey görmeyin:
Belgeler\projects\schedulex\schedulex
Tek `schedulex` göreceksiniz bu path’te.

Yapmamız gereken `python -m venv venv` ile sanal makinamızı kuracağız. Ardından aynı path üzerinden VSCode terminalinde `venv\scripts\activate` yazarak sanal makinayı kuracağız.

Bunu PowerShell değil, Command Line üzerinden yapmanızı tavsiye ederim. PowerShell izinleri bazılarında açık olmuyor. Macera yaşamayalım.

Satır başında `(venv)` görmeniz lazım CMD üzerinde.

Sonra ise tamamız. `pip freeze` ile venv içerisindeki yüklü paketleri kontrol edebilirsiniz.

`pip install django` yazıyoruz terminale.
Venv açık olmasına dikkat!
PC’ye kurarsınız yoksa. (Bir şey olmaz ama gerek yok, tek pakette gitsin.)

Şu anlık başka dependencies kurmanıza gerek yok.

Ard arda aşağıdaki adımları izleyin:

cd schedulex
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Tebrikler 🎉
Sunucunuz ayağa kalktı. Terminal üzerinden çıkan linke CTRL + sol click yaparsanız açılır.

Ama şu anda frontend entegre değil. Bu yüzden çalışmalarınızı halihazırdaki URL üzerinden yapabilirsiniz:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Böyle bir şey olacak:
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

Yazarsanız Django’nun admin paneline erişebilirsiniz.

Burada isteyen şifre ve kullanıcı adını ise:
`python manage.py createsuperuser` kodu ile tanımlayabilir
ve sistem üzerindeki modellerinizi ve datalarınızı görüntüleyebilir.

Apps’ler içindeki `admin.py` dosyasından bu sayfada görmek istediklerinizi özelleştirebilirsiniz.

!! GIT PUSH YAPARKEN VENV VE NODEMODULES DOSYALARI GELMEYECEK SQLITE DB DE GELMEYECEK BUNLARI KENDI LOCALINIZDE YAPCAKSINIZ
!! ZTN VENV DOSYASINI VE SQLITE SOYLEDIM NODEMODULESI HALLEDICEGIZ
!! SIZE BOS DB GELCEK SUANLIK ADMIN SAYFASI UZERINDEN MODELINIZE YENI KISILER TANIMLAYABILIRSINIZ 
