# flask_encryption_endpoint
Endpoint that encrypts and decrypts strings using flask.

# A) About:

## A-1) Encryption Algorithm:
**GnuPG**



## A-2) Packages used:
1. **Flask**
2. **pydantic**
3. **Flask-Pydantic**
4. **graphene**
5. **Flask-GraphQL**
6. **python-gnupg**
7. **unittest**



## A-3) Other Technologies used:
1. **Git**
2. **Github**
3. **Shell**
4. **Docker**
5. **Testing**
6. **GraphiQL**





# B) How to run it:


## 1) Using bash:

<b>

```bash
python app.py
```
</b>

## 2) Using Docker:

<b>

```bash
docker-compose up --force-recreate --build -d
```
</b>

And the image will be running.





# C) Testing:


## C-1) Using Bash File:
<b>

```bash
bash run_tests.sh
```
</b>

## C-2) Using Python File:
<b>

```bash
python tests_all.py
```
</b>


## C-3) Specialized Testing:
<b>

```bash
python test_cryp.py
python test_endpoints.py
python test_pydantic_models.py
python test_schema.py
```
</b>






# D) Endpoints:



<table>
<tr>
	<th>number</th>
	<th>path</th>
	<th>methods</th>
	<th>Function</th>
</tr>




<tr>
	<td>1</td>
	<td>"/"</td>
	<td>GET</td>
	<td>Make sure every thing is up and running</td>
</tr>

<tr>
	<td>2</td>
	<td>"/ping"</td>
	<td>GET</td>
	<td>Make sure every thing is up and running</td>
</tr>

<tr>
	<td>3</td>
	<td>"/decryptMessage"</td>
	<td>POST</td>
	<td>Decrypt the message using passphrase</td>
</tr>

<tr>
	<td>4</td>
	<td>"/encryptOriginal"</td>
	<td>POST</td>
	<td>Encrypt original test using passphrase</td>
</tr>

<tr>
	<td>5</td>
	<td>"/graphql"</td>
	<td>GET</td>
	<td>Encrypt and decrypt using the pass phrase</td>
</tr>

</table>



# E) General Errors:

Example: **404**
<b>

```python
{
	'error': 404, 
	'message': 'resource not found', 
	'success': False
}
```
</b>


Example: **405**
<b>

```python
{
	'error': 405, 
	'message': 'method not allowed', 
	'success': False
}
```
</b>









# F) Endpoints Documentation:

## F-1) "/"

### Request Method:
**GET**

### Result:

<b>

```python
{
	"message":"hello, world!"
}
```
</b>

### Reason:
Just to make sure every thing is up and running.

### Expected inputs:
None

### Errors:
None

### Examples:
<b>

```bash
curl --location --request GET 'http://127.0.0.1/'
```
</b>





























## F-2) "/ping"

### Request Method:
**GET**

### Result:

<b>

```python
{
    "message": "ping"
}
```
</b>

### Reason:
Just to make sure every thing is up and running.

### Expected inputs:
None

### Errors:
None

### Examples:
<b>

```bash
curl --location --request GET 'http://127.0.0.1/ping'
```
</b>






























## F-3) "/decryptMessage"

### Request Method:
**POST**


### Reason:
Decrypt the encrypted message using a passphrase.

### Expected inputs:



<table>
	<tr>
		<th>Number</th>
		<th>Name</th>
		<th>Location</th>
		<th>Type</th>
		<th>Function</th>
	</tr>
	<tr>
		<td>1</td>
		<td>message</td>
		<td>Request Body</td>
		<td>String</td>
		<td>The message to be decrypted</td>
	</tr>
	<tr>
		<td>2</td>
		<td>passphrase</td>
		<td>Request Body</td>
		<td>String</td>
		<td>The passphrase that will be used to 
		decrypt the message</td>
	</tr>
</table>




### Examples:
<b>

```bash
curl --location --request GET 'http://127.0.0.1/ping'
```
</b>


### Result:

<b>

```python
{
    "message": "ping"
}
```
</b>





### Errors:
None













## F-3) "/encryptMessage"

### Request Method:
**POST**


### Reason:
Decrypt the encrypted message using a passphrase.

### Expected inputs:



<table>
	<tr>
		<th>Number</th>
		<th>Name</th>
		<th>Location</th>
		<th>Type</th>
		<th>Function</th>
	</tr>
	<tr>
		<td>1</td>
		<td>message</td>
		<td>Request Body</td>
		<td>String</td>
		<td>The message to be decrypted</td>
	</tr>
	<tr>
		<td>2</td>
		<td>passphrase</td>
		<td>Request Body</td>
		<td>String</td>
		<td>The passphrase that will be used to 
		decrypt the message</td>
	</tr>
</table>




### Examples:
<b>

Request:
```bash
curl --location --request POST 'http://127.0.0.1/decryptMessage' \
--header 'Content-Type: application/json' \
--data-raw '{
    "message":"-----BEGIN PGP MESSAGE-----\nVersion: GnuPG v2\njA0ECQMCVady3RUyJw3X0kcBF+zdkfZOMhISoYBRwR3uk3vNv+TEg+rJnp4/yYISpEoI2S82cDiCNBIVAYWB8WKPtH2R2YSussKhpSJ4mFgqyOA01uwroAKvJQ===\n-----END PGP MESSAGE-----",
    "passphrase":"topsecret"
}'
```
Response:

```bash
{
    "DecryptedMessage": "Nice work!\n"
}
```

</b>





### Errors:
1. **No Inputs:**

<b>

Request:
```bash
curl --location --request POST 'http://127.0.0.1/decryptMessage' \
--data-raw ''
```
Response:

```bash
{
    "detail": "Unsupported media type '' in request. 'application/json' is required."
}
```

</b>


2. **Missing Inputs:**

<b>

Request:
```bash
curl --location --request POST 'http://127.0.0.1/decryptMessage' \
--header 'Content-Type: application/json' \
--data-raw '{
    "passphrase":"secret"
}'
```
Response:

```bash
{
    "validation_error": {
        "body_params": [
            {
                "loc": [
                    "message"
                ],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }
}
```
</b>




3. **Failure Of Decryption:**

<b>

Request:
```bash
curl --location --request POST 'http://127.0.0.1/decryptMessage' \
--header 'Content-Type: application/json' \
--data-raw '{
    "passphrase":"secret",
    "message":"123"
}'
```
Response:

```bash
{
    "validation_error": {
        "body_params": [
            {
                "loc": [
                    "message"
                ],
                "msg": "no data was provided",
                "type": "value_error.decryption_failure"
            }
        ]
    }
}
```
</b>












































