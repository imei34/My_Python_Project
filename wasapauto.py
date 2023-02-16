import pywhatkit

mystr = ("+62 823-7612-0370")

strrep = mystr.replace(" ","")
strrep = strrep.replace("-","")
strrep = strrep.replace(","," ")
phones = strrep.split()
# print(phones)

# ini buat ngirim teks doang
for phone in phones:
    pywhatkit.sendwhatmsg_instantly(phone,"Pesan ini dikirim menggunakan python | test doang heheheh")

# ini buat ngirim sekalian dengan gambar
# for phone in phones:
#     pywhatkit.sendwhats_image(phone,"images/hello.png","Pesan ini dikirim menggunakan python | test doang heheheh")
    


