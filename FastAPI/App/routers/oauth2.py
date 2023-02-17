# from jose import JWTError,jwt
# from datetime import datetime, timedelta

# # there are three components required for a token
# # SECRET_KEY
# # Algorithm
# # Expiration date of the token


# # Now we can name the secret key anything but usually we use a string character
# # to generate a random string character we use "openssl rand -hex 32"
# # the random character generated are e72bb4797e400c574388d1b53eef1a0c6946d250c28bd0b76c63ee9ebf4c5423

# SECRET_KEY = "e72bb4797e400c574388d1b53eef1a0c6946d250c28bd0b76c63ee9ebf4c5423"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES= 30

# def create_access_token(data: dict):
#     to_encode = data.copy() #Creating a copy of the data
#     expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) #adding the epiration minutes
#     # adding the expiration minutes to the copy
#     to_encode.update({"exp": expire})

#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)
#     return encoded_jwt
    