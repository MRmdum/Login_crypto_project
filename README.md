# Login for Student Cryptographique project

Just a simple login handling the passwords using hash+salt then aead encryption __
We used Google tink lib: https://github.com/tink-crypto/tink/blob/master/docs/PYTHON-HOWTO.md __
and Bcrypt lib: https://github.com/pyca/bcrypt __

To run just build and run with docker: __
docker build -t image_name . __
docker run -it --name container_name image_name __
