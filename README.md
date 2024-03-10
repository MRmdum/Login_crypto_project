# Login for Student Cryptographique project

Just a simple login handling the passwords using hash+salt then aead encryption \n
We used Google tink lib: https://github.com/tink-crypto/tink/blob/master/docs/PYTHON-HOWTO.md \n
and Bcrypt lib: https://github.com/pyca/bcrypt \n

To run just build and run with docker: \n
docker build -t image_name . \n
docker run -it --name container_name image_name \n
