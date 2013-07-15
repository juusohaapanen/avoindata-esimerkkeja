#Hakee avoindata.net APIn kautta kategoriat ja niiden kysymysmäärät
#Äärimmäisen yksinkertainen esimerkki.
#Tekijänoikeus: Ju


library(rjson)
library(RCurl)

#API endpoint
url = "http://api.avoindata.net/categories"

#haetaan API:n sisältö muuttujaan
from <- getURL(url)

#parsitaan JSON R:n listaksi
dat <- fromJSON(from)



