#!/bin/bash

# set -e

# Define Variables
ITER=310000
SHA=sha256
FILE_NAME=''
ENCRYPT_TYPE=aes-128-cbc
# OPERATION='Encrypt'
ECRY="Encrypt"
DCRY="Decrypt"
PASSKEY=''
USER_EXISTS=0
user_name=$1
user_pwd=$2
OPERATION=$3

# Check the user exists
is_user_exists() {
    
    shopt -s nocasematch
    userid="$1".enc
    
    if [ -f "$userid" ]; then
        USER_EXISTS=1
        clear
        echo "$1 user already exists"
    else
        USER_EXISTS=0
    fi
}
# Create Passsord file
create_pwd_file() {
cat << EOF > $1
$2
EOF
}

# Define Error Handlers
error_handler() {
    clear
    if [[ ! "$1" == "0" ]]; then
        echo "Exit Code: $1 " $2 $3
        exit 200
    fi
}

# encrypt password
openssl_encrypt() {
    openssl enc -$1 -pbkdf2 -md $2 -iter $3 -salt -in $4 -out $4.enc -e -pass pass:$5
}

# Decrypt password
openssl_decrypt() {
    openssl enc -$1 -pbkdf2 -md $2 -iter $3 -salt -in $4.enc -out $4.txt -d -pass pass:$5
    error_handler "Exception Occurred: " "Decryption key is not valid"
}

# Return Decrypted content
openssl_get_decrypt() {
    passkey=$(openssl enc -$1 -pbkdf2 -md $2 -iter $3 -salt -in $4.enc -d -pass pass:$5)
    status_code=$?
    
    error_handler "$status_code" "Exception occurred: " "Entered Paaskey key is in-valid"
    PASSKEY=$passkey
}

# Removing password file
remove_file() {
    if [ -f "$1" ]; then
        # echo "Removing file..."
        rm -f $1
        # else
        #     echo "File not exist..."
    fi
}

# *************************************************************

FILE_NAME=${user_name}

# Calling Encryption
if [[ $OPERATION == $ECRY  ]]; then

    # Check if the user already exists
    is_user_exists $FILE_NAME
   
    # echo $USER_EXISTS
    if [ $USER_EXISTS -eq 0 ]; then
        # Create a password file
        create_pwd_file $FILE_NAME $user_pwd
        
        # Encrypt password file
        openssl_encrypt $ENCRYPT_TYPE $SHA $ITER $FILE_NAME $user_pwd
        
        # Removing original password file
        remove_file $FILE_NAME
        clear
        echo "User Passkey generated successfully..."
    else
        # openssl_decrypt $ENCRYPT_TYPE $SHA $ITER $FILE_NAME $user_pwd
        openssl_get_decrypt $ENCRYPT_TYPE $SHA $ITER $FILE_NAME $user_pwd
        echo "Encrypted password is: $PASSKEY"
    fi
else
    # Check if the user already exists
    is_user_exists $FILE_NAME

    # echo $USER_EXISTS
    if [ $USER_EXISTS -eq 1 ]; then
        # openssl_decrypt $ENCRYPT_TYPE $SHA $ITER $FILE_NAME $user_pwd
        openssl_get_decrypt $ENCRYPT_TYPE $SHA $ITER $FILE_NAME $user_pwd
        echo "Encrypted password is: $PASSKEY"
    else
        echo "User $PASSKEY"
    fi    
fi
