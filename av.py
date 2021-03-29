import requests
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QScrollArea
import sys
class SCLAB(QScrollArea):
  
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
  
        self.setWidgetResizable(True)
  
        content = QWidget(self)
        self.setWidget(content)
  
        lay = QVBoxLayout(content)
  
        self.label = QLabel(content)
  
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
  
        self.label.setWordWrap(True)
  
        lay.addWidget(self.label)
  
    def setText(self, text):
        self.label.setText(text)
class Birimler(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Birimler")
        self.setWindowIcon(QtGui.QIcon('birimler.jpg'))
        self.setGeometry(100, 100, 100, 400)
        self.yaraaa=QLabel()
        self.yaraaa.setText("""
         Para Birimleri:
         AED
         AFN
         ALL
         AMD
         ANG
         AOA
         ARS
         AUD
         AWG
         AZN
         BAM
         BBD
         BDT
         BGN
         BHD
         BIF
         BMD
         BND
         BOB
         BRL
         BSD
         BTC
         BTN
         BWP
         BYN
         BYR
         BZD
         CAD
         CDF
         CHF
         CLF
         CLP
         CNY
         COP
         CRC
         CUC
         CUP
         CVE
         CZK
         DJF
         DKK
         DOP
         DZD
         EGP
         ERN
         ETB
         EUR
         FJD
         FKP
         GBP
         GEL
         GGP
         GHS
         GIP
         GMD
         GNF
         GTQ
         GYD
         HKD
         HNL
         HRK
         HTG
         HUF
         IDR
         ILS
         IMP
         INR
         IQD
         IRR
         ISK
         JEP
         JMD
         JOD
         JPY
         KES
         KGS
         KHR
         KMF
         KPW
         KRW
         KWD
         KYD
         KZT
         LAK
         LBP
         LKR
         LRD
         LSL
         LTL
         LVL
         LYD
         MAD
         MDL
         MGA
         MKD
         MMK
         MNT
         MOP
         MRO
         MUR
         MVR
         MWK
         MXN
         MYR
         MZN
         NAD
         NGN
         NIO
         NOK
         NPR
         NZD
         OMR
         PAB
         PEN
         PGK
         PHP
         PKR
         PLN
         PYG
         QAR
         RON
         RSD
         RUB
         RWF
         SAR
         SBD
         SCR
         SDG
         SEK
         SGD
         SHP
         SLL
         SOS
         SRD
         STD
         SVC
         SYP
         SZL
         THB
         TJS
         TMT
         TND
         TOP
         TRY
         TTD
         TWD
         TZS
         UAH
         UGX
         USD
         UYU
         UZS
         VEF
         VND
         VUV
         WST
         XAF
         XAG
         XAU
         XCD
         XDR
         XOF
         XPF
         YER
         ZAR
         ZMK
         ZMW
         ZWL
        
        """)
        label = SCLAB(self)
        label.setText(self.yaraaa.text())
        self.show()
class window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Borsa Aracı")
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))
        self.w=None
        self.mikbel=QLabel()
        self.mikbel.setText("Miktar:")
        self.equal=QLabel()
        self.equal.setText("==")
        self.checkbox=QLabel()
        self.checkbox.setText("TO")
        self.mik =  QLineEdit()
        self.bir1bel=QLabel()
        self.bir1bel.setText("Para Birimi:")
        self.bir1 = QLineEdit()
        self.bir2bel=QLabel()
        self.bir2bel.setText("Para Birimi:")
        self.bir2 = QLineEdit()
        self.ans =  QLabel()
        self.ans.setText("")
        self.birs = QPushButton("Birimler")
        self.cevir = QPushButton("Çevir")
        h_box = QHBoxLayout()
        h_box.addWidget(self.mikbel)
        h_box.addWidget(self.mik)
        h_box.addWidget(self.bir1bel)
        h_box.addWidget(self.bir1)
        h_box.addWidget(self.checkbox)
        h_box.addWidget(self.bir2bel)
        h_box.addWidget(self.bir2)
        h_box.addWidget(self.equal)
        h_box.addWidget(self.ans)
        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()
        v_box.addWidget(self.birs)
        v_box.addWidget(self.cevir)
        self.setLayout(v_box)
        self.birs.clicked.connect(self.OtherWindowOpen)
        self.cevir.clicked.connect(self.trans)
        self.show()
    def OtherWindowOpen(self,check):
        if self.w is None:
            self.w = Birimler()
            self.w.show()
        else:
            self.w.close() 
            self.w = None
    def trans(self):
        url = ""#Your's API url
        j=self.mik.text()
        j=float(j)
        response = requests.get(url)
        veri =  response.json()
        ver1=float(veri["rates"][self.bir1.text()])
        ver2=float(veri["rates"][self.bir2.text()])
        try:
            a=(ver2/ver1)*j
            a=str(a)
            return self.ans.setText(a)
        except KeyError:
            return self.ans.setText("Lütfen para birimlerini kontrol edin")
app = QApplication(sys.argv)
pencere =window1()
sys.exit(app.exec_())