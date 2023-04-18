import webbrowser 
from tkinter import*
from tkinter import messagebox 
import requests 
from bs4 import BeautifulSoup 
from tkinter.font import Font
import feedparser
import datetime



FinStock = { #Luodaan sanakirja, jossa on osakkeen nimi ja sitä vastaava
    #kaupankäyntitunnus. Haku tehdään nettisivulta kaupankäyntitunnuksella, käyttäjän
    #tarvitsee kirjoittaa vain osakkeen nimi.
    
    'afarak' : 'afagr',
    'ahlstrom-Munksjö' : 'am1',
    'aktia' : 'aktia',
    'alma-Media' : 'alma',
    'altia' : 'altia',
    'apetit' : 'apetit',
    'asiakastieto' : 'atg1v',
    'aspo' : 'aspo',
    'aspocomp' : 'acg1v',
    'atria' : 'atrav',
    'basware' : 'bas1v',
    'biohit' : 'biobv',
    'bittium' : 'bitti',
    'capman' : 'capman',
    'cargotec' : 'cgcbv',
    'caverion' : 'cav1v',
    'citycon' :  'cty1s',
    'componenta' : 'cth1v',
    'consti' : 'consti',
    'cramo' : 'cra1v',
    'digia' : 'digia',
    'digitalist' : 'digigr',
    'dna' : 'dna',
    'dovre' : 'dov1v',
    'eab' : 'eab',
    'efore' : 'efo1v',
    'elecster' : 'eleav',
    'elisa' : 'elisa',
    'endomines' : 'endom',
    'eq' : 'eqv1v',
    'ericsson' : 'eribr',
    'etteplan' : 'ette',
    'evli' : 'evli',
    'exel' : 'exl1v',
    'f-secure' : 'fsc1v',
    'finnair' : 'fia1s',
    'fiskars' : 'fskrs',
    'fortum' : 'fortum',
    'glaston' : 'gla1v',
    'harvia' : 'harvia',
    'hkscan' : 'hksav',
    'hoivatilat' : 'hoiva',
    'honkarakenne' : 'honbs',
    'huhtamäki' : 'huh1v',
    'ilkka-Yhtymä 1' : 'ilk1s',
    'ilkka-Yhtymä 2' : 'ilk2s',
    'incap' : 'icp1v',
    'innofactor' : 'ifa1v',
    'investors' : 'invest',
    'kamux' : 'kamux',
    'kemira' : 'kemira',
    'keskisuomalainen' : 'kslav',
    'kesko a' : 'keskoa',
    'kesko b' : 'keskob',
    'kesla' : 'kelas',
    'kojamo' : 'kojamo',
    'kone' : 'knebv',
    'konecranes' : 'kcr',
    'lassila & tikanoja' : 'lat1v',
    'lehto' : 'lehto',
    'marimekko' : 'mmo1v',
    'martela' : 'maras',
    'metso' : 'metso',
    'metsä board a' : 'metsa',
    'metsä board b' : 'metsb',
    'neo' : 'neo1v',
    'neste' : 'neste',
    'nixu' : 'nixu',
    'noho' : 'noho',
    'nokia' : 'nokia',
    'nokian renkaat' : 'tyres',
    'nordea' : 'nda%20fi',
    'nurminen' : 'nlg1v',
    'olvi' : 'olvas',
    'oma säästöpanki' : 'omasp',
    'oriola a' : 'okdav',
    'oriola b' : 'okdbv',
    'orion a' : 'ornav',
    'orion b' : 'ornbv',
    'outokumpu' : 'out1v',
    'outotec' : 'ote1v',
    'ovaro' : 'ovaro',
    'panostaja' : 'pna1v',
    'pihlajalinna' : 'pihlis',
    'ponsse' : 'pon1v',
    'punamusta' : 'pumu',
    'qpr' : 'qpr1v',
    'qt' : 'qtcom',
    'raisio k' : 'raikv',
    'raisio v' : 'raivv',
    'ramirent' : 'rami',
    'rapala' : 'rap1v',
    'raute' : 'raute',
    'revenio' : 'reg1v',
    'robit' : 'robit',
    'rovio' : 'rovio',
    'saga' : 'sagcv',
    'sampo' : 'sampo',
    'sanoma' : 'saa1v',
    'scanfil' : 'scanfl',
    'sievi' : 'sievi',
    'siili solutions' : 'siili',
    'silmäasema' : 'silma',
    'solteq' : 'solteq',
    'soprano' : 'sopra',
    'sotkamo silver' : 'sosi1',
    'srv' : 'srv1v',
    'ssab a' : 'ssabah',
    'ssab b' : 'ssabbh',
    'ssh' : 'ssh1v',
    'stockmann a' : 'stcas',
    'stockmann b' : 'stcbv',
    'stora enso a' : 'steav',
    'stora enso r' : 'sterv',
    'suominen' : 'suy1v',
    'taaleri' : 'taala',
    'talenom' : 'tnom', 
    'tallink' : 'tallink',
    'tecnotree' : 'tem1v',
    'teleste' : 'tlt1v',
    'telia' : 'telia1',
    'terveystalo' : 'ttalo',
    'tieto' : 'tieto',
    'tikkurila' : 'tik1v',
    'tokmanni' : 'tokman',
    'trainers house' : 'trh1v',
    'tulikivi' : 'tulav',
    'upm-Kymmene' : 'upm',
    'uponor' : 'uponor',
    'uutechnic' : 'uutec',
    'vaisala' : 'vaias',
    'valmet' : 'valmt',
    'valoe' : 'valoe',
    'viking line' : 'vik1v',
    'wulff' : 'wuf1v',
    'wärtsilä' : 'wrt1v',
    'yit' : 'yit',
    'yleiselektroniikka' : 'yeint',
    'ålandsbanken a' : 'albav',
    'ålandsbanken b' : 'albbv'
    
    }

def saveIndex():
    #jos tekstilaatikko on tyhjä, näytetään siitä ilmoitus
    if len(textbox.get('1.0','end-1c')) == 0:
        messagebox.showinfo('info',' Textbox is empty, Load index values first!')
    else:

        currentdate = datetime.datetime.now()
        txtdate =  currentdate.strftime('%d%m%y')
        file = open('indexValues'+txtdate+'.txt','a')
        mySave = textbox.get('1.0','end-1c')
        file.write(mySave)
        file.close

def getStock():#funktio kurssi- ja osinkohakuihin.
    stock = (Entry.get(enterName))#muuttujaan stock tallennetaan enterName-syötekenttään
                                  #kirjoitettu haettavan osakkeen nimi.
    
    stock = stock.lower()#muutetaan syötetty merkkijono pieniksi kirjaimiksi, koska ne ovat myös
                        #sanakirjaan tallennettu pieninä kirjaimina. Näin ne saadaan vastaamaan toisiaan,
                        #eikä käyttäjän tarvitse miettiä minkälaista kirjoitusasua käyttää.
    
    stock = FinStock.get(stock)#haetaan osaketta vastaava kaupankäyntitunnus sanakirjasta.
    enterName.delete(0,END) #tyhjennnetään syötekenttä.
    Entry.insert(enterName,0,stock)#lisätään osakkeen nimen tilalle sen kaupankäyntitunnus.
    
    if priceinfo.get() == 1 and dividendinfo.get() == 0: #jos valittuna on price
        #info valintaruutu, avataan selain allaolevaan osoitteeseen. stock-muutuja
        #linkin lopussa on haetun osakkeen kaupankäyntitunnus.
        webbrowser.open('https://www.kauppalehti.fi/porssi/porssikurssit/osake/'+stock)
        
    elif priceinfo.get() == 0 and dividendinfo.get() == 1: #jos valittuna on
        #osinkotieto valintaruutu, avataan selain allaolevaan osoitteeseen.
          webbrowser.open('https://www.is.fi/taloussanomat/osinkokalenteri/'+stock)
          
    elif priceinfo.get () == 1 and dividendinfo.get() == 1: # jos valittuna on
        #molemmat valintaruudut, avataan selain kahteen allaolevaan osoitteeseen.
        webbrowser.open('https://www.kauppalehti.fi/porssi/porssikurssit/osake/'+stock)
        webbrowser.open('https://www.is.fi/taloussanomat/osinkokalenteri/'+stock)

def getCrypto(): #funktio kryptovaluuttojen hakemiseen.
    crypto = (Entry.get(kryptoSearch))
    crypto = crypto.lower() #muunnetaan käyttäjän syöttämä merkkijono pieniksi kirjaimiksi.
    webbrowser.open('https://fi.investing.com/crypto/'+crypto)

def question(): #funktio, joka suoritetaan kysymysmerkkiä painettaessa.
                #funkto avaa ohjetekstin erilliseen ikkunaan.
    messagebox.showinfo('?','Write stock name here. Example: If you want to look Nokia company stock price or dividend,'
                        'write in the field just Nokia. Do not use oy,ab etc.')
    
#funktio toiselle kysymysmerkkipainikkeelle.
def indexquestion():
    messagebox.showinfo('Indexs', 'See OMXHPI, OMXH25, OMX30, DAX30, SXXP, NDX, INX, HSI indexs and EUR-USD & JPY-USD currency rates')

#funktio indeksitietojen kaavintaan.    
def getIndex():
    currentdate = datetime.datetime.now()
    #tehdään pyyntö nettisivulle, joka on annettu parametrina
    page = requests.get('https://www.investing.com/indices/major-indices')
    soup = BeautifulSoup(page.text, 'html.parser')
    #etsitään parametrina oleva div-luokka nettisivulta
    result = soup.find(class_='datatable_body__3EPFZ')
    #haetaan kaikki divin sisältä tieto
    result2 = result.find_all('tr')

    #käydään tieto for-silmukassa läpi ja tulostetaan ne tekstilaatikkoon.
    textbox.insert(INSERT,currentdate.strftime('%d.%m.%y'),END)
    for result in result2:
        textbox.insert(INSERT,'\n',END)
        textbox.insert(INSERT,'\n',END)
        finalresult = result.text
        textbox.insert(INSERT,finalresult,END)
        textbox.insert(INSERT,'\n',END)

#funktio, joka tyhjentää syötekentät ja tekstilaatikon.
def clearAll():
    textbox.delete(1.0,END)
    enterName.delete(0,END)
    kryptoSearch.delete(0,END)

#avataan rss syötteet uuteen ikkunaan

def openWindow():
        currentdate = datetime.datetime.now()
        RssWindow = Toplevel(root)
        titlelbl = Label(RssWindow,text = 'Financial RSS news').pack()
        RssScrollbar = Scrollbar(RssWindow)
        text = Text(RssWindow,yscrollcommand = RssScrollbar.set)
        RssScrollbar.config(command = text.yview)
        RssScrollbar.pack(side = RIGHT, fill = Y)
      
        news = feedparser.parse('https://www.arvopaperi.fi/api/feed/v2/rss/ap')
        text.insert(INSERT,currentdate.strftime('%d.%m.%y'),END)
        text.insert(INSERT,' Arvopaperi.fi RSS',END)
        text.insert(INSERT,'\n',END)

        for post in news.entries:
            post.title + ' : ' + post.description 
            text.insert(INSERT,'\n',END)
            text.insert(INSERT,post.title,END)
            text.insert(INSERT,post.description,END)
            text.insert(INSERT,'\n',END)
        text.pack()
    
       
    
    

root = Tk()#luodaan pohjakomponetti.
root.configure(background = 'azure4')#asetetaan pohjakomponentin taustaväri.

#tallennetaan muuttujiin ohjelmassa käytettävät fontit.
titlefont = Font (family = 'Segoe Print')
labelfont = Font (family = 'High Tower Text')



#tuodaan ohjelmaan png-kuvat, joita käytetään painikkeissa kuvakkeinna.
dollar = PhotoImage(file = 'KurssihakuDollari.png')
finaldollar = dollar.subsample(3,3)

krypto = PhotoImage(file = 'KurssihakuKrypto.png')
finalkrypto = krypto.subsample(3,3)

root.title('Finance App')

menubar = Menu(root)
root.config(menu=menubar)
savemenu = Menu(menubar)
menubar.add_cascade(label="Save", menu = savemenu )
savemenu.add_command(label='Save index values', command = saveIndex)

#luodaan frame-komponentit, joiden avulla asemoidaan muita komponentteja.
frame1 = Frame(root, background = 'azure4')
frame2 = Frame(root, background = 'azure4')
frame3 = Frame(root, background = 'azure4')
frame4 = Frame(root, background = 'azure4')
frame5 = Frame(root, background = 'azure4')
frame6 = Frame(root, background = 'azure4')

scrollbar = Scrollbar(frame4)
scrollbar.pack(side = RIGHT, fill = Y)

#luodaan tekstikomponentit label-komennolla, text-komennolla annetaan näytettävä teksti, backgound-komennolla
#taustaväri ja fg-komennolla fontin väri.
appname = Label(root, text = 'Finance App', background = 'azure4', fg = 'white', font = titlefont)
nameLabel = Label (root, text = 'Enter the stock name in the field', background = 'azure3', font = labelfont)
cryptoName = Label(frame2, text = 'Currency name: ', background = 'azure3')
krypto = Label(root, text='Crypto currencies', background='azure3', font = labelfont)

#luodaan syötekentät entry-komennolla.
enterName = Entry(frame1, width = 15, relief = 'solid', background = 'gray94')
kryptoSearch = Entry(frame2, background = 'gray94', relief = 'solid')

#luodaan painikkeet button-komennolla, command-komennolla annetaan painikkeelle funktio joka suoritetaan, kun
#painiketta on painettu. image-komennolla liitetään aiemmin tuotu png-kuva painikkeeseen
#compound-komennolla asemoidaan kuva painikkeen oikeaan reunaan.

pricebtn = Button(root, text = 'Check price/dividend', command = getStock, image = finaldollar, compound = RIGHT)
questionbtn = Button (frame1, text = '?', command = question)
indexQuestion = Button (frame5, text = '?', command = indexquestion)

kryptobtn = Button(root, text = 'Check value', command = getCrypto, image = finalkrypto, compound = RIGHT)
indexbtn = Button(frame5, text = 'Check stock indexes', command = getIndex)
clearbtn = Button(frame5, text = 'Clear textbox & entry fields', command = clearAll)

rssbtn = Button(frame5, text = 'Rss feeds (open in new window)', command = openWindow)

#luodaan valintaikkunat.
priceinfo = IntVar()
pricechoice = Checkbutton(frame3, text = 'Price', variable = priceinfo, background = 'azure4')
dividendinfo = IntVar()
dividendchoice = Checkbutton(frame3, text = 'Dividend', variable = dividendinfo, background = 'azure4')

textbox = Text(frame4, width = 40, height = 8, yscrollcommand = scrollbar.set)
scrollbar.config(command = textbox.yview)

                    
#pakataan komponentit, jolloin ne näkyvät ohjelmassa, side komennoilla komponentteja voidaan
#asemoida. pady komennolla lisätään tyhjää tilaa komponenttien väliin.
appname.pack()
nameLabel.pack()
frame1.pack()
enterName.pack(side=LEFT, pady = 4,padx=4)
questionbtn.pack(side=RIGHT, pady = 2,padx=2)
clearbtn.pack(side=BOTTOM,pady=4)


frame3.pack()
pricechoice.pack(side=LEFT)
dividendchoice.pack(side=RIGHT)
pricebtn.pack(pady = 10)
krypto.pack(pady = 8)

frame2.pack()
cryptoName.pack()                   
kryptoSearch.pack(pady = 4)
kryptobtn.pack()
frame4.pack()

textbox.pack()
frame5.pack()
frame6.pack()
rssbtn.pack(side=BOTTOM)
indexbtn.pack(side = LEFT, pady = 4, padx = 4)
indexQuestion.pack(side=RIGHT)



mainloop()







