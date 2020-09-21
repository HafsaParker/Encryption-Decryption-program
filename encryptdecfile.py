class code:
    def __init__(self):
        self.codes={'a':'z','b':'x','c':'y','d':'s','e':'u','f':'a','g':'e','h':'c','i':'k','j':'r','k':'n','l':'g','m':'d','n':'l','o':'m','p':'t','q':'f','r':'i','s':'h','t':'o','u':'j','v':'p','w':'v','x':'b','y':'w','z':'q'}
        self.first=[]
        self.enc=[]
        self.en=[]
        self.dec1=[]
        self.dec2=[]
    def option(self):
        q=str(input("encrypt or decrypt:"))
        if q == "encrypt":
            text=str(input("enter text:"))
            self.encrypt(text)
        else:
            text=str(input("enter text:"))
            self.decrypt(text)
    def encrypt(self,text):
        x=text.split(" ")
        y=x[::-1]
        z=""
        for i in range(0,len(y)):
            string = "".join(reversed(y[i]))
            z+=string
            z+=" "
        for i in z:
            self.en.append(i)

        
        for i in range(0,len(self.en)):
            for j in self.en[i]:
                if j !=' ':
                    
                    for key in self.codes.keys():
                        if key in j:
                            self.enc.append(self.codes.get(key))
                else:
                    self.enc.append("/s")
        encrypt=" "
        for i in range(0,len(self.enc)):
            if self.enc[i]=="/s":
                encrypt+=" "
            else:
                encrypt+=self.enc[i]
        print("your encrypted text:",encrypt)


    def decrypt(self,text):
        z=[]
        for i in text:
            z.append(i)
        
        for i in range(0,len(z)):
            for j in z[i]:
                if j!=" ":
                    if j in self.codes.values():
                        self.dec1.append(list(self.codes.keys())[list(self.codes.values()).index(z[i])])
                            
                            
                else:
                    self.dec1.append("/s")
        z=""
        for i in range(0,len(self.dec1)):
            if self.dec1[i]=="/s":
                z+=" "
            else:
                
                z+=self.dec1[i]
        y=z.split(" ")
        for i in y:
            self.dec2.append(i)
        rev=self.dec2[::-1]
        rever=""
        for i in range(0,len(rev)):
            string = "".join(reversed(rev[i]))
            rever+=string
            rever+=" "
        print("decrypted text:",rever)
           
           
                    
                
                   
       
            

            

                
                    
       

        
            

        

        

            
                

                
       
                    





ob=code()
ob.option()
