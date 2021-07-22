# **AliCoin**
![N|Solid](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)  ![N|Solid](https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png) ![N|Solid](https://upload.wikimedia.org/wikipedia/fr/thumb/6/65/Blockchain-Logo.png/800px-Blockchain-Logo.png)
## **Introduction**
Create a new Blockchains with Python based on [medium article](https://medium.com/@vanflymen/learn-blockchains-by-building-one-117428612f46) writen by **Daniel van Flymen**  :

## Before you get started :
**Python 3.6+**
**Flask** : 

``` $ pip install Flask\==0.12.2 requests==2.18.4  ```

we need an HTTP Client, like  [Postman](https://www.postman.com/)  or cURL

## Step1:  Building a Blockchain :
    ### What does a Block look like ? 
```
    block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
```
Each block has an index, a timestamp (in unix time), a list of transaction, a proof ( digital print ), and the hash of the previous Block.

The idea of a chain is to link each new Block with the previous Block ** this is curcial because it's whats gives blockchains immutability ** ( if an attacker corrupter an earlier Block in th chain then **all** subsequent blocks will contain incorrect hashes)