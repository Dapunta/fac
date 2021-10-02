import os,requests,json,time,sys,random
r_get = requests.get
r_pos = requests.post
js_lo = json.loads
url1_ = 'https://graph.facebook.com/'
url2_ = '?access_token='
url3_ = '?fields=feed&access_token='
post_dev = []
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")
def logo():print('   _______  _____\n  / __/ _ |/ ___/  • Facebook\n / _// __ / /__    • Auto\n/_/ /_/ |_\___/    • Comment\n')
def login():
    os.system('rm -rf token.txt');clear();logo()
    tok_dev = input('Masukkan Token : ')
    try:re_gex = r_get("%sme%s%s"%(url1_,url2_,tok_dev));re_jso = js_lo(re_gex.text);re_num = re_jso['name'];with_ = open("token.txt", "w");with_.write(tok_dev);with_.close();main()
    except (KeyError,IOError):print('Token Invalid');os.system('rm -rf token.txt');login()
    except requests.exceptions.ConnectionError:print('Koneksi Bermasalah');exit()
def main():
    clear();logo()
    try:tok_dev = open("token.txt","r").read();re_gex = requests.get("%sme%s%s"%(url1_,url2_,tok_dev));re_jso = json.loads(re_gex.text);re_num = re_jso['name']
    except (KeyError,IOError):print('Token Invalid');os.system('rm -rf token.txt');login()
    except requests.exceptions.ConnectionError:print('Koneksi Bermasalah');exit()
    print('Komentar Post Target Harus Publik');print('Apabila Target Grup');print('Harus Bergabung Ke Dalam Grup');print('\nPisahkan ID Target Dengan \',\'')
    id_dev = input('Masukkan ID : ').split(',')
    print('\nPisahkan Komentar Acak Dengan \',,\'');print('Ganti Baris Komentar Dengan \'===\'');kom_dev = input('Masukkan Komentar : ').replace('===','\n').split(',,');print('');personal(id_dev,kom_dev,tok_dev)
def personal(id_dev,kom_dev,tok_dev):
    try:
        for id in id_dev:
            re_dev  = r_get('%s%s%s%s'%(url1_,id,url3_,tok_dev));js_dev  = js_lo(re_dev.text)
            for post in js_dev['feed']['data']:
                id_post = post['id'];post_dev.append(id_post);time.sleep(10);re_dev_kom = r_pos('%s%s/comments?message=%s&access_token=%s'%(url1_,id_post,random.choice(kom_dev),tok_dev));js_dev_kom = js_lo(re_dev_kom.text)
                if 'id' in js_dev_kom:print('Komentar Ke %s Berhasil'%(len(post_dev)))
                elif 'error' in js_dev_kom:print('Komentar Ke %s Gagal'%(len(post_dev)))
        print('Proses Selesai');exit()
    except (KeyError,IOError):print('Token Invalid / ID Tidak Ditemukan');exit()
    except requests.exceptions.ConnectionError:print('Koneksi/Sinyal Bermasalah');exit() 
if __name__=='__main__':os.system('git pull');main()
