#!/bin/bash

# set -e

source encry_decry_util.sh

list_Openssl_opts () {
    clear
    echo -ne "
What Openssl Operation you want to do?
1) Start Encryption
2) Start Decryption
3) Exit
    Choose an option:  "
    read -r ans
    case $ans in
        1)
            OPERATION=$ECRY
            list_encrypt_opts
            # get_user_input
        ;;
        2)
            OPERATION=$DCRY
            list_encrypt_opts
        ;;
        3)
            echo 'Exiting...'
        exit 0;;
        *)
            echo 'Wrong option'
        exit 0;;
    esac
}

list_encrypt_opts () {
    clear
    echo -ne "
What Encryption you want to use?
1) aes-128-cbc
2) aes-256-cbc
3) base64
4) Exit
    Choose an option:  "
    read -r ans
    case $ans in
        1)
        ENCRYPT_TYPE=aes-128-cbc;;
        2)
        ENCRYPT_TYPE=aes-256-cbc;;
        3)
        ENCRYPT_TYPE=base64;;
        4)
            echo 'Exiting...'
        exit 0;;
        *)
            echo 'Wrong option'
        exit 0;;
    esac
}

list_Openssl_opts

# Calling Encryption
if [[ $OPERATION == $ECRY  ]]; then
    get_user_name
    get_user_pass
    
    FILE_NAME=${user_name}
    
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
        sleep 3
        list_Openssl_opts
    fi
    
fi

# Calling Decryption
if [[ $OPERATION == $DCRY  ]]; then
    get_user_name
    get_user_pass
    echo
    
    FILE_NAME=${user_name}
    #     openssl_decrypt $ENCRYPT_TYPE $SHA $ITER $FILE_NAME $user_pwd
    openssl_get_decrypt $ENCRYPT_TYPE $SHA $ITER $FILE_NAME $user_pwd
    
    echo "Encrypted password is: $PASSKEY"
fi