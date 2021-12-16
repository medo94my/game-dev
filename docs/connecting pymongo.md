# Connecting PyMongo with Flask

---

#### Starting with installing the PyMongo to Flask

```pip
pip install pymongo
```

#### Then import it to flask app.py file

```python
from flask_pymongo import PyMongo
```

## Connecting DB

- ##### Go to your account in mongo atles ;_Which is a cloud based mongoDB_, and in the defualt cluster will find a connect button press it

![video](img/connect.png)

##### Same as above figure

- #### window will showup with three choices Choose the second choice that state _connect your application_ and press on it.
  ![connection](img/connnect2.png)

* #### Another window will showup to give the connection String

  ![connect2](img/connnect3.png)

      * press copy to copy the Connection String
      * Replace <password> with the password for your app user
      * Go to your flask app

and paste the connection string inside app.config

```python

app.config["MONGO_URI"] = "mongodb+srv://db username:your password@<cluster_name>.mongodb.net/test?retryWrites=true&w=majority"
app= PyMongo(app) #to set the config
```

> ## Add records in Mongo DB
>
> To add a record in DB

- Establish connection
  ```python
  var = mongo.db.collectionName
  ```
- for inserting data have for example using insert\*one to insert one record at a time:
  - `python var.insert_one({ 'title':'put String value here' })`
    \_ `python var.insert_one({ 'title': the variableName })`
    > ## View Record :

```python
    var = mongo.db.collectionName
    var.find()
```

- by using find() we ask Database to view all records in the chosen collection

```python
    var = mongo.db.collectionName
    var.find_one({})
```

- by using find_one({}) DB will return one record according to what put inside {}
  > ## Deleting Record

```python
    var = mongo.db.collectionName
    var.Delete_one({})
```

- Delete_one used to delete one record or Dictionary from DB if we but something inside {'\_id':"1"} means delete record where id equals = 1

```python
    var = mongo.db.collectionName
    var.Delete_many({})
```

- Delete_one used to delete all record or Dictionary from DB
  > ## Update Record

```python
    var = mongo.db.collectionName
    var.update_one({{criteria},{'$set'{
        title:'changed title goes here'
    }}})
```

- update_one() takes two parameters one is the criteria and the other is update the wanted to be updated

> ### Helpful Links

- [Mongo DB](https://www.mongodb.com)
- [Connecting DB](https://www.youtube.com/watch?v=3ZS7LEH_XBg&t=50s)
- [Tutorials](https://www.youtube.com/watch?v=-56x56UppqQ&t=101s)
- Used Material
  - [CollectionMethods](https://docs.mongodb.com/manual/reference/method/js-collection/)
